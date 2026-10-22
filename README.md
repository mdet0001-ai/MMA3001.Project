# MMA3001 Project

## Prediction of Indoor CO₂ Concentration Using Environmental Sensor Data

This repository contains my individual MMA3001 Numerical Methods and Machine Learning project.

The project investigates whether indoor CO₂ concentration can be predicted from other environmental sensor measurements.

## Engineering Problem

Indoor CO₂ concentration is an important indicator of indoor environmental conditions and ventilation performance.

This project investigates whether CO₂ concentration can be estimated using other environmental sensor measurements, potentially supporting indoor environmental monitoring where direct CO₂ prediction or estimation is useful.

## Inputs and Output

### Input variables

The regression models use:

- Temperature
- Humidity
- Pressure
- Volatile Organic Compounds (VOC)
- PM2.5

### Output variable

- CO₂ concentration in ppm

## Dataset

Environmental sensor data are located in:

`data/raw/5EnvSensor_MayToDec2024_180kRows.zip`

Sensor location information is located in:

`data/raw/Sensor ID and Locations.xlsx`

The raw environmental dataset contains repeated database records. Measurements were parsed from JSON data and duplicates were removed using the combination of Sensor ID and measurement timestamp.

## Computational Approach

The following approaches were evaluated:

1. Baseline mean prediction
2. Linear Regression
3. Decision Tree Regression

The environmental data are time ordered, so a chronological 80/20 training and testing split was used rather than a random split.

Decision Tree maximum depth was evaluated using a separate chronological validation period.

## Final Results

| Model | MAE (ppm) | RMSE (ppm) | R² |
|---|---:|---:|---:|
| Baseline | 29.862 | 34.001 | -1.369 |
| Linear Regression | 27.024 | 33.606 | -1.314 |
| Initial Decision Tree | 35.395 | 45.044 | -3.157 |
| Optimised Decision Tree | 31.595 | 39.419 | -2.184 |

Linear Regression achieved the lowest MAE and RMSE of the tested models.

However, the negative R² and residual analysis indicate limited generalisation to the later testing period.

## Decision Tree Optimisation

Decision Tree depths from 1 to 15 were evaluated using validation data.

A maximum depth of 4 produced the lowest validation MAE and was selected as the optimised configuration.

The optimised tree improved compared with the initial depth-5 tree, although it did not outperform Linear Regression.

## Repository Structure

MMA3001.Project/

- MMA3001_Project.ipynb
- README.md
- LICENSE
- requirements.txt
- test_report.txt
- data/raw/
- src/project_utils.py
- tests/test_project_utils.py
- docs/

## Source Code

Reusable functions are contained in:

`src/project_utils.py`

These functions include:

- duplicate sensor measurement removal
- regression metric evaluation
- chronological train/test splitting

Functions contain docstrings describing their inputs, outputs and purpose.

## Testing

Automated testing is implemented using pytest.

Tests are located in:

`tests/test_project_utils.py`

The tests verify:

- removal of duplicate sensor measurements
- regression metric calculations using a known perfect prediction
- chronological data splitting and preservation of data order

The latest automated test run produced:

`3 passed`

The complete output is stored in:

`test_report.txt`

## HTML Documentation

HTML source-code documentation was generated using pdoc.

Open:

`docs/index.html`

to browse the generated documentation.

## Reproducing the Analysis

1. Clone this repository.
2. Install the Python dependencies using `pip install -r requirements.txt`.
3. Open `MMA3001_Project.ipynb`.
4. Run the notebook sequentially from top to bottom.

The notebook loads the raw dataset from the repository and performs the complete cleaning, exploratory analysis, modelling, validation and evaluation workflow.

## Software

The project was developed in Python using Google Colab.

Main packages include:

- pandas
- numpy
- matplotlib
- scikit-learn
- pytest
- pdoc

## Limitations

The models showed limited ability to generalise from the earlier training period to the later testing period.

Important limitations include:

- environmental conditions changed between the training and testing periods
- only one primary sensor was used for the final modelling analysis
- the available variables do not capture all factors influencing indoor CO₂
- short-term CO₂ fluctuations were not captured accurately
- the models identify predictive relationships rather than causal relationships

## Author

MMA3001 Individual Project
