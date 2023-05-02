# Wine Quality Classification

## Abstract
This machine learning project focused on predicting the quality of red wines based on their
chemical properties. To achieve this, several preprocessing techniques were applied, including
scaling using different methods and applying log and boxcox transformations. Exploratory data
analysis was also performed to better understand the relationships between the features and the
target variable.

Several popular machine learning algorithms were then trained and compared, including logistic
regression, SVM, random forest, decision trees, and boosting algorithms. Performance metrics
such as accuracy, precision, recall, and F1 score were used to identify the best algorithm and
preprocessing technique. The random forest model with id = 1 was found to be the most effective,
with a micro F1 score of 0.73.


## Data Source
- [Wine Quality Classification](https://archive.ics.uci.edu/ml/datasets/wine+quality)

## Reports and Slides
- [Proposal](https://github.com/NirajanBekoju/Wine-Quality-Classification/blob/master/Proposal/main.pdf)
- [Final Report](https://github.com/NirajanBekoju/Wine-Quality-Classification/blob/master/Report/main.pdf)
- [Proposal Presentation](https://github.com/NirajanBekoju/Wine-Quality-Classification/blob/master/proposal_presentation.pdf)
- [Final Defense Presentation](https://github.com/NirajanBekoju/Wine-Quality-Classification/blob/master/prabhat_29_wineQualityClassification.pdf)
## Steps to run in your local machine
**Clone the repository**

```
git clone https://github.com/NirajanBekoju/Wine-Quality-Classification
```

**Setup conda environment**

```
conda env create -f environment.yml
```

## Steps to run django app (Backend)
The backend is developed using django and django rest framework.

**Activate the conda environment**
```
conda activate aifellowship
```

**Run django server**
```
python3 manage.py runserver
```

## Steps to run react frontend
The frontend is developed using React. Node version : 19.9.0 and npm version : 9.6.3
**Install npm packages**
```
npm install 
```

**Run the server**
```
npm run start
```



