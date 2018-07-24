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

<a id='gather_data'></a>
### Gather Data.
All data collected from [Kaggle competition page](https://www.kaggle.com/c/house-prices-advanced-regression-techniques "Ames Kaggle Competition").

In addition, I wrote some handy functions for EDA/cleaning and plotting to use later, found in the `notebook_starter.py` and `plotter.py` files.

<a id='explore_data'></a>
### Explore Data.
First I took a look at all of the columns to check out the null values in the dataset, specifically trying to find columns which were:
	- Overwhelmingly null, and should be dropped, or
	- Partially null, and might have values imputed

<img src="https://i.imgur.com/fB0IXZZ.png">

I did a check of % of null values per column and decided to eliminate some columns that have too many nulls to be worthwhile: `['Pool QC', 'Misc Feature', 'Alley', 'Fence', 'Fireplace Qu']`.

For this exercise, I also decided to drop all categorical variables to be able to more easily run different linear regression types. Some features appeared numerical, but were in fact categorical (e.g. `Year Built`).

The next step was to explore *feature correlations*. I did this by making a heatmap of the correlation matrix of the remaining features:

<img src="https://i.imgur.com/3MP09gR.png">

While a couple of features look highly correlated, we will be using some regularization techniques to drop those later.

Lastly, I needed to find out if there were still *null values* sticking around, which there were. The most important feature, `Lot Frontage`, we imputed by `Lot Shape`, which seemed intuitive.

<img src="https://i.imgur.com/WgNTP4a.png">

<a id='model_data'></a>
### Model Data.


 **Model** | **R^2 Score (Train)** | **R^2 Score (Test)** 
 --- |	--- | --- 
 Linear Regression 	|	0.726	| 0.675 
 Ridge Regression		|	0.773	| 0.700 
 Lasso Regression 		|	0.773	| 0.700 
