from flask import Flask, render_template, request, redirect
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import MinMaxScaler
import pickle

app = Flask(__name__)

def get_categories(data):
    c_f = {
        'Neighborhood':	['Blueste', 'BrDale', 'BrkSide', 'ClearCr',	'CollgCr', 'Crawfor', 'Edwards', 'Gilbert',	
                        'IDOTRR', 'MeadowV', 'Mitchel', 'NAmes', 'NPkVill', 'NWAmes', 'NoRidge', 'NridgHt', 
                        'OldTown', 'SWISU', 'Sawyer', 'SawyerW', 'Somerst', 'StoneBr', 'Timber','Veenker'],
        'HouseStyle': ['1.5Unf', '1Story', '2.5Fin', '2.5Unf', '2Story', 'SFoyer', 'SLvl'],
        'RoofStyle': ['Gable', 'Gambrel', 'Hip', 'Mansard', 'Shed']
    }

    cate_df = pd.DataFrame()
    for col in c_f.keys():
        category = data[col].values
        if category in c_f[col]:
            for cat in c_f[col]:
                if cat == category:
                    cate_df[col + f'_{cat}'] = [1]
                else:
                    cate_df[col + f'_{cat}'] = [0]
        else:
            for cat in c_f[col]:
                cate_df[col + f'_{cat}'] = [0]
    return cate_df

def transform_data(data):
    num_fea = ['LotFrontage','LotArea','OverallQual','YearBuilt','YearRemodAdd',
                'ExterQual','BsmtQual','BsmtFinSF1','TotalBsmtSF','GrLivArea','FullBath',
                'KitchenQual','Fireplaces','GarageCars','GarageQual']
    num_data = data[num_fea]
    for col in num_data.columns:
        num_data[col] = num_data[col].astype('int64')
    min_scale = pickle.load(open('min_max_predictor_variables.pkl', 'rb'))
    num_data = pd.DataFrame(min_scale.transform(num_data), columns=num_fea)
    cate_data = get_categories(data)
    final_data = pd.concat([num_data, cate_data], axis=1)
    return final_data

def make_predictions(data):

    xgb, lgbm, gb = pickle.load(open("House_price_predict_models.pkl", "rb"))
    prediction = xgb.predict(data)
    trans_output = pickle.load(open("min_max_sales_price_target.pkl",'rb'))
    prediction = np.mean([xgb.predict(data), lgbm.predict(data), gb.predict(data)])
    prediction = trans_output.inverse_transform(pd.Series(prediction).values.reshape(-1,1))
    return round(prediction.tolist()[0][0])



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = pd.DataFrame()
    features = ['LotFrontage', 'LotArea', 'YearBuilt', 'YearRemodAdd', 'BsmtFinSF1', 
    'TotalBsmtSF', 'GrLivArea', 'FullBath', 'Fireplaces', 'GarageCars', 'Neighborhood', 
    'HouseStyle', 'OverallQual', 'RoofStyle', 'ExterQual', 'BsmtQual', 'KitchenQual', 'GarageQual']
    for index in range(len(features)):
        value = request.form[features[index]]
        data[features[index]] = [value]
    final_data = transform_data(data)
    print(final_data)
    return render_template('predict.html', predictions = make_predictions(final_data))


if __name__ == "__main__":
    app.run(debug=True)