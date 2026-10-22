import numpy as np
import pandas as pd
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


def remove_duplicate_measurements(data):
    """
    Remove duplicate environmental sensor measurements.

    Duplicate measurements are identified using the combination
    of SensorID and Time.

    Parameters
    ----------
    data : pandas.DataFrame
        Environmental sensor dataset containing SensorID and Time.

    Returns
    -------
    pandas.DataFrame
        Dataset containing only unique physical measurements.
    """

    cleaned_data = (
        data
        .drop_duplicates(
            subset=["SensorID", "Time"]
        )
        .sort_values(
            ["SensorID", "Time"]
        )
        .reset_index(drop=True)
    )

    return cleaned_data


def evaluate_regression(y_true, y_pred):
    """
    Calculate common regression performance metrics.

    Parameters
    ----------
    y_true : array-like
        Measured target values.

    y_pred : array-like
        Predicted target values.

    Returns
    -------
    dict
        Dictionary containing MAE, RMSE and R-squared.
    """

    mae = mean_absolute_error(
        y_true,
        y_pred
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_true,
            y_pred
        )
    )

    r2 = r2_score(
        y_true,
        y_pred
    )

    return {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }


def chronological_split(data, train_fraction=0.80):
    """
    Split time-ordered data chronologically into training
    and testing datasets.

    Parameters
    ----------
    data : pandas.DataFrame
        Dataset ordered by measurement time.

    train_fraction : float, optional
        Fraction of data assigned to training.
        Default is 0.80.

    Returns
    -------
    tuple
        Training DataFrame and testing DataFrame.
    """

    split_index = int(
        len(data) * train_fraction
    )

    train_data = (
        data
        .iloc[:split_index]
        .copy()
    )

    test_data = (
        data
        .iloc[split_index:]
        .copy()
    )

    return train_data, test_data
