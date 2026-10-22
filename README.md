# MMA3001 Project

## Prediction of Indoor CO₂ Concentration Using Environmental Sensor Data

This repository contains the individual project completed for MMA3001.

The project investigates whether indoor carbon dioxide (CO₂) concentration can be predicted using environmental sensor measurements including:

- Temperature
- Humidity
- Pressure
- Volatile Organic Compounds (VOC)
- PM2.5

## Project Overview

Environmental sensor data were cleaned and processed before developing regression models to predict CO₂ concentration.

The analysis includes:

- JSON sensor data parsing
- Removal of duplicate sensor measurements
- Exploratory data analysis
- Chronological training and testing split
- Baseline prediction model
- Linear Regression
- Decision Tree Regression
- Decision Tree depth sensitivity analysis
- Model performance comparison
- Residual analysis
- Decision Tree feature importance

## Models

Two regression techniques covered in MMA3001 were investigated:

1. Linear Regression
2. Decision Tree Regression

A simple baseline model using the mean training CO₂ concentration was also included for comparison.

## Final Results

| Model | MAE (ppm) | RMSE (ppm) | R² |
|---|---:|---:|---:|
| Baseline | 29.862 | 34.001 | -1.369 |
| Linear Regression | 27.024 | 33.606 | -1.314 |
| Initial Decision Tree | 35.395 | 45.044 | -3.157 |
| Optimised Decision Tree | 31.595 | 39.419 | -2.184 |

Linear Regression achieved the best predictive performance of the tested models. However, its negative R² value and residual patterns indicate limited generalisation to the later testing period.

## Data

The environmental sensor dataset is stored in:

`data/raw/5EnvSensor_MayToDec2024_180kRows.zip`

Sensor location information is stored in:

`data/raw/Sensor ID and Locations.xlsx`

The raw environmental dataset contains repeated database records. Duplicate physical measurements were removed using sensor ID and measurement timestamp before modelling.

## Software

The project was developed in Python using Google Colab.

Main Python packages used:

- pandas
- numpy
- matplotlib
- scikit-learn

## Reproducibility

The notebook is designed to run sequentially from top to bottom.

The dataset is loaded directly from the repository, parsed, cleaned, analysed and used to train and evaluate the regression models.

## Author

MMA3001 Individual Project
