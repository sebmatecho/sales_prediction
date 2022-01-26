# Rossmann stores - 6 weeks sales forecast

This project contains data shared in the competition "Rossmann Store Sales" hosted by Kaggle, available [here](https://www.kaggle.com/c/rossmann-store-sales).

## Problem to be solved 

Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. With thousands of individual managers predicting sales based on their unique circumstances, the accuracy of results can be quite varied. Thus, a unified solution proposing a general method to predict sales for the next six weeks; is required. 

## Used Approach

The CRoss-Industry Standard Process for data mining (CRISP) methodology was used. This is, the life cycle of the project is given by the following figure. 

<img src="img/IBM.jpg" width="400" height="400" />

## Data General Overview
Several stages were considered for this project in terms of data preparation: 

1. To collect and understand the data
2. Cleaning the database
3. Handling  missing values

Some highlighted elements: 
1. 1017209 sales records 
2. 1115 different stores
3. Some variables: "date", "store_type", "customers", "assortment", "school_holiday", "open", "promo2", "sales", among others. 

As the main aim of the project is to provide forecasted values, not available features at the time of the forecast were not considered. 

## EDA and Insights Finding

Once some basic understanding of the data and the business problem were gained (see figure below), an Exploratory Data Analysis (EDA) was performed. To provide a path for such EDA, some hypothesis were proposed, and listed below. 

<img src="img/DAILY_SOTORE_SALES.png" width="400" height="400" />

1. Stores with a larger assortment should sell more
2. Stores with closer competitors should sell less
3. Stores with longer-standing competitors should sell more
4. Stores where products cost less for longer (active promotions) should sell more
5. Stores with more promotion days should sell more
6. Stores with more extended promotions should sell more
7. Stores open during Christmas holiday should sell more
8. Stores should sell more over the years
9. Stores should sell more in the second half of the year
10. Stores should sell more after the 10th day of each month
11. Stores should sell less on weekends
12. Stores should sell less during school holidays
13. Stores that open on Sundays should sell more

## Data preparation (standardization and feature selection)

## Machine learning modeling

## Hyperparameter tuning

## Business performance

## Model in production

<img src="bot.gif" width="300" height="550" />
