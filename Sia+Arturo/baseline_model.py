import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

"""
This file trains a model and evaluates the accuracy based on the 
data from Occupancy_Estimation.csv
"""

FEATURE_COLUMNS = [
    # TODO: fill in with the sensor column names we want to use as model
    # inputs, e.g. "S1_Temp", "S1_Light", "S1_Sound", "S5_CO2", "S6_PIR", ...
    # Look at the actual column names in the cleaned DataFrame and decide
    # which ones make sense to include. You don't need all of them for a
    # first pass -- start with a handful of obviously-relevant ones.
]

TARGET_COLUMN = "Room_Occupancy_Count"


def split_features_and_target(df: pd.DataFrame):
    """
    Split the cleaned DataFrame into X (features) and y (target).

    Args:
        df: cleaned sensor DataFrame (from sensor_cleaning.py).

    Returns:
        (X, y) tuple -- X is a DataFrame of just FEATURE_COLUMNS,
        y is the Room_Occupancy_Count column.
    """
    # TODO: implement.


def train_baseline_model(X, y):
    """
    Split into train/test sets and fit a simple classifier.

    Returns:
        (model, X_test, y_test) -- the trained model plus the held-out
        test set, so we can evaluate it in the next function.
    """
    # TODO: implement.
    # Use train_test_split() to hold out ~20% of the data for testing,
    # then fit a DecisionTreeClassifier() (already imported above) on the
    # training data. Keep it simple for this first pass.


def evaluate_model(model, X_test, y_test) -> float:
    """
    Predict on the test set and compute accuracy.

    Returns:
        Accuracy as a float between 0 and 1.
    """
    # TODO: implement. Hint: model.predict(X_test), then accuracy_score().


if __name__ == "__main__":
    # TODO:
    #   1. Import and call Person C's load_sensor_data() + cleaning functions
    #      from sensor_cleaning.py to get a clean DataFrame.
    #   2. split_features_and_target()
    #   3. train_baseline_model()
    #   4. evaluate_model() and print the accuracy.
    # The deliverable is a printed accuracy number -- doesn't need to be
    # high, just needs to run end to end.
    pass