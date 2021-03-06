# House Price Estimator: Project Overview
* This is my first project to learn data science. Model predict house prices(RMSE - 0.0348) to help people who want to buy house.
* Got data by particepating in ongoing competition on Kaggle [House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques).
* Cleaned data by handling missing values of both categorical and numerical features.
* Perform Exploratory Data Analysis to get know about data.
* Perform feature engineering (feature selection with Pearson correlation and wrapper method).
* Optimized ensemble and linear techniques to get best model.
* Tried deep learning Artificial Neural Network.
* Built client facing API using flask.
* Deployed flask API to Heroku. [Click here](https://predict-your-house-price.herokuapp.com/) to check deployed API.
* Deployed flask API to Microsoft Azure. [click here](https://housepricepredictions.azurewebsites.net/) to check deployed API.
## Code and Resources Used
**Python version:** 3.7<br>
**Packages:** numpy, pandas, seaborn, matplotlib, sklearn, boruta_py, lightgbm, xgboost, pickle, flask, keras. <br>
**Feature Selection Article:** https://medium.com/analytics-vidhya/feature-selection-techniques-2614b3b7efcd <br>
**Flask API Production:** https://www.youtube.com/watch?v=3mwFC4SHY-Y&t=43s <br>
**XGBoost & LGBM Algorithms:** https://www.analyticsvidhya.com/blog/2017/06/which-algorithm-takes-the-crown-light-gbm-vs-xgboost/ <br>
**Decision Tree:** https://www.analyticsvidhya.com/blog/2015/01/decision-tree-simplified/2/ <br>
**Random Forest:** https://www.youtube.com/watch?v=nxFG5xdpDto&t=172s <br>
## Data Cleaning
The first thing i did after getting data from Kaggle competition is clean it up so that I can perform EDA and later useable for model. I did following changes in data.
* Impute missing categorical values with None (according to data description) and by grouping and taking mode.
* Handled numerical null values.
## Exploratory Data Analysis
I compared some features and their effects on each other. I checked how some important features effecting the prices of houses.<br>
**Some visualizations:**<br>
![deleted or not found](https://github.com/zeeshan-akram/House-Price-Predictions-Project/blob/master/garag-vs-prices.png)
![deleted or not found](https://github.com/zeeshan-akram/House-Price-Predictions-Project/blob/master/house-quality.png)
![deleted or not found](https://github.com/zeeshan-akram/House-Price-Predictions-Project/blob/master/sales-per-year.png)
![deleted or not found](https://github.com/zeeshan-akram/House-Price-Predictions-Project/blob/master/number-of-houses-in-neighbours.png)
![deleted or not found](https://github.com/zeeshan-akram/House-Price-Predictions-Project/blob/master/sold-house-vs-prices.png)
![deleted or not found](https://github.com/zeeshan-akram/House-Price-Predictions-Project/blob/master/old-house-vs-prices.png)
![deleted or not found](https://github.com/zeeshan-akram/House-Price-Predictions-Project/blob/master/yearly-sold-houses-on-the-basis-of-house-condition.png)
<br>**Find answers of following questions:**
1. How LotFrontage effecting prices.
2. Having large LotArea will increase prices.
3. How prices vary of Houses on the basis of how old it is?
4. Which year have Highest sales.
5. How Garage Area effecting prices.
6. What are the efects of ground living area.
7. What is correlationship between features.
8. How prices vary on HouseStyle.
9. What is effect of Zoning on Prices.
10. How the differents types of dwelling involved in the sale.
11. Which location have highest sales within Ames city.
12. What is the quality percentage of houses.
13. Are the sales increasing over year or not.
14. Yearly Sold houses condition.
15. House prices wrt garage condition.<br>
## Feature Engineering
After EDA I needed to perform feature engineering so that model get clean data. Incorrect or inconsistent data leads to false conclusions. And so, how well we clean and understand the data has a high impact on the quality of the results.<br>
I perform following operations
* Check Pearson correlation.
  * Removed correlated predictors to reduce multicolinearity.
  * Removed features with very low correlation with target variable.
* Also prepare data for neural networks.
* Used wrapper method for selecting features which are only important to model.
* Removed Outliers.
* Perform label and One hot encoding.
* Scale down data with Min Max Scaler.
## Model Building
I tried ensemble technique (bagging and boosting) and linear model with K-Fold validation and evaluated them with RMSE. I choose RMSE because of competition demand and also I performed hyperparameter tuning of ensemble models.<br>
Boosting techniques performing better than all other techniques. So I selected all three boosting models and stacked them to get overall average predictions.<br>
* **Bagging Models:** Because of training a bunch of individual models in a parallel way. Each model is trained by a random subset of the data 
* **Boosting Models:** Because of training a bunch of individual models in a sequential way. Each individual model learns from mistakes made by the previous model.
* **Linear Regression:** Baseline Model.
## Model Performance
Gradient Boost and XGBoost models outperformed the other models.
* **Gradient Boost:** RMSE = 0.0329
* **XGBoost:** RMSE = 0.0329
* **LGBM :** RMSE = 0.0340
* **Random Forest:** RMSE = 0.0362
* **Linear Regression:** RMSE = 0.0395
* **ANN Result:** Validate RMSE = 0.0538
## Productionization
In this step I built a flask API endpoint. The API endpoint takes list of values of different house features and return estimated price of house.<br>
Finaly I deployed flask API to **Heroku** and **Microsoft Azure**.<br>
**Heroku:** https://predict-your-house-price.herokuapp.com/ <br>
**MS Azure:** https://housepricepredictions.azurewebsites.net/ <br>
