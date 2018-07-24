<img src="https://i.imgur.com/PyHuuqq.png">

# Predicting Housing Prices in Ames, IA

_Jamie Quella - 5/17/18_

**Goal:** The goal of this project was to reinforce basic EDA and regression model techniques, with emphasis on  cross-validation, feature selection and  engineering and refining models over time. This was done by using the [Ames, IA Housing Data set](https://www.kaggle.com/c/house-prices-advanced-regression-techniques "Ames Kaggle Competition") and submitting to the Kaggle competition to be scored on unseen data.

**Process:** 
1. [Define Question.](#define_question)
2. [Gather Data.](#gather_data)
3. [Explore Data.](#explore_data)
4. [Model Data.](#model_data)
5. [Evaluate Model.](#evaluate_model)
6. [Answer Question.](#answer_question)

<a id='define_question'></a>
### Define the Question.
**Can we predict housing prices in Ames, IA to make sure I'm not underselling my home given its features?**
- We will be 

<a id='gather_data'></a>
### Gather Data.
All data collected from [Kaggle competition page](https://www.kaggle.com/c/house-prices-advanced-regression-techniques "Ames Kaggle Competition").

In addition, I wrote some handy functions for EDA/cleaning and plotting to use.

<a id='explore_data'></a>
### Explore Data.
First I took a look at all of the columns to check out the null values in the dataset, specifically trying to find columns which were:
	- Overwhelmingly null, and should be dropped, or
	- Partially null, and might have values imputed

<img src="https://i.imgur.com/tALOGHd.png">