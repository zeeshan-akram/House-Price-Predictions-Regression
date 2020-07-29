# House Price Estimator: Project Overview
* This is my first project to learn data science. Model predict house prices(RMSE - 0.0348) to help people who want to buy house.
* Got data by particepating in ongoing competition on Kaggle [House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques).
* Cleaned data by handling missing values of both categorical and numerical features.
* Perform Exploratory Data Analysis to get know about data.
* Perform feature engineering (feature selection with Pearson correlation and wrapper method).
* Optimized boosting, tree and linear techniques to get best model.
* Built client facing API using flask
* Deployed flask API to Heroku. [Click here](https://predict-your-house-price.herokuapp.com/) to check deployed api.
## Code and Resources Used
**Python version:** 3.7<br>
**Packages:** numpy, pandas, seaborn, matplotlib, sklearn, boruta_py, lightgbm, xgboost, pickle, flask <br>
**Feature Selection Article:**[link text itself]: https://medium.com/analytics-vidhya/feature-selection-techniques-2614b3b7efcd <br>
**Flask API Production:**[link text itself]: https://www.youtube.com/watch?v=3mwFC4SHY-Y&t=43s <br>
**XGBoost & LGBM Algorithms:**[link text itself]: https://www.analyticsvidhya.com/blog/2017/06/which-algorithm-takes-the-crown-light-gbm-vs-xgboost/ <br>
**Decision Tree:**[link text itself]: https://www.analyticsvidhya.com/blog/2015/01/decision-tree-simplified/2/ <br>
**Random Forest:**[link text itself]: https://www.youtube.com/watch?v=nxFG5xdpDto&t=172s <br>
## Data Cleaning
The first step after getting data from Kaggle competition. I needed to clean it up so that it can be useable for model. I did following changes in data.
* Impute missing categorical values with None (according to data description) and by grouping and taking mode.
* Handled numerical null values.
## Exploratory Data Analysis
I compared some features and their effects on each other. I checked how some important features effecting the prices of houses. 
**Some visualizations are:**<br>
![alt text](https://github.com/zeeshan-akram/House-Price-Predictions-Project/garag-vs-prices.png)
<br>I answered to questions given below.
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
