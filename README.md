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

I ran four different Linear Regression model types: 
1. *Linear Regression:* default
2. *Ridge Regression:* penalizes wrong guesses, but will not zero out coefficients.
3. *Lasso Regression:* penalizes wrong guesses, but *may* drop coefficients.
4. *Elastic Net:* Balance between *Ridge* and *Lasso*.

<a id='evaluate_model'></a>
### Evaluate Model.

*Scores for all models*

 **Model** | **R^2 Score (Train)** | **R^2 Score (Test)** 
 --- |	--- | --- 
 Linear Regression 	|	0.726	| 0.675 
 Ridge Regression		|	0.773	| 0.700 
 Lasso Regression 		|	0.775	| 0.698 
 Elastic Net 			|	0.774	| 0.697 

These R^2 scores are not ideal. While being able to explain nearly 80% of the variance in house price seems good, it can likely be improved. This mainly seems to be in part due to a large outlier in the predictions:

<img src="https://i.imgur.com/7irAXIT.png">

In exploring the data further, it seems that this was likely due to a single outlier data point in one of the strongest features: `GrLivArea` - or above ground living area.
<img src="https://i.imgur.com/7wVnQJe.png">

The next iterations of models should perhaps account for outliers in some way to generate better predictions.

<a id='answer_question'></a>
### Answer Question.

**Q: Were we able to predict home prices?** 

**A:** Somewhat. The R^2 scores  were fairly low (70-80% range) compared to what I think is possible to achieve. That said, I *did* achieve the objective of following the data science workflow, improving EDA, plotting and modeling skills, and was able to predict prices within the expected range. I just wouldn't make an investment strategy out of it :)

**Next steps**
1. More feature selection and engineering work.
    - Involve more categorical variables
    - Have separate models for outliers
    - Try polynomial features on more data
    - Use `itertools.combinations` to try more variations of feature combos
2. Use `GridSearchCV` to more exhaustively tune hyper-parameters
3. Try different models!

[Jupyter notebook with full code available here](https://github.com/jquella/DSI_Project_Ames/blob/master/project-2_JQ_take2.ipynb)