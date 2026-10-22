import sys
from pathlib import Path

import numpy as np
import pandas as pd


# Allow pytest to import functions from the src folder
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(
    0,
    str(PROJECT_ROOT / "src")
)

from project_utils import (
    remove_duplicate_measurements,
    evaluate_regression,
    chronological_split
)


def test_remove_duplicate_measurements():
    """
    Confirm that repeated SensorID-Time combinations are removed.
    """

    data = pd.DataFrame({
        "SensorID": [1, 1, 1],
        "Time": pd.to_datetime([
            "2024-01-01 10:00",
            "2024-01-01 10:00",
            "2024-01-01 10:10"
        ]),
        "CO2": [450, 450, 470]
    })

    result = remove_duplicate_measurements(data)

    assert len(result) == 2

    assert result["CO2"].tolist() == [
        450,
        470
    ]


def test_evaluate_regression_perfect_prediction():
    """
    Confirm that perfect predictions produce zero error
    and an R-squared value of one.
    """

    y_true = np.array([
        400,
        450,
        500
    ])

    y_pred = np.array([
        400,
        450,
        500
    ])

    result = evaluate_regression(
        y_true,
        y_pred
    )

    assert result["MAE"] == 0
    assert result["RMSE"] == 0
    assert result["R2"] == 1


def test_chronological_split():
    """
    Confirm that the chronological split preserves data order.
    """

    data = pd.DataFrame({
        "Time": pd.date_range(
            "2024-01-01",
            periods=10,
            freq="h"
        ),
        "CO2": range(10)
    })

    train_data, test_data = chronological_split(
        data,
        train_fraction=0.80
    )

    assert len(train_data) == 8
    assert len(test_data) == 2

    assert train_data["CO2"].tolist() == list(
        range(8)
    )

    assert test_data["CO2"].tolist() == [
        8,
        9
    ]
