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
    "S1_Temp", "S2_Temp", "S3_Temp", "S4_Temp",
    "S1_Light", "S2_Light", "S3_Light", "S4_Light",
    "S1_Sound", "S2_Sound", "S3_Sound", "S4_Sound",
    "S5_CO2", "S5_CO2_Slope",
    "S6_PIR", "S7_PIR",
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
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]
    return X, y


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
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model, X_test, y_test


def evaluate_model(model, X_test, y_test) -> float:
    """
    Predict on the test set and compute accuracy.

    Returns:
        Accuracy as a float between 0 and 1.
    """
    # TODO: implement. Hint: model.predict(X_test), then accuracy_score().
    predictions = model.predict(X_test)
    return accuracy_score(y_test, predictions)


if __name__ == "__main__":
    # TODO:
    #   1. Import and call Person C's load_sensor_data() + cleaning functions
    #      from sensor_cleaning.py to get a clean DataFrame.
    #   2. split_features_and_target()
    #   3. train_baseline_model()
    #   4. evaluate_model() and print the accuracy.
    # The deliverable is a printed accuracy number -- doesn't need to be
    # high, just needs to run end to end.
    from sensor_cleaning import load_sensor_data, add_datetime_column

    df = load_sensor_data()
    df = add_datetime_column(df)

    X, y = split_features_and_target(df)
    model, X_test, y_test = train_baseline_model(X, y)
    accuracy = evaluate_model(model, X_test, y_test)
    print(f"Baseline model accuracy: {accuracy:.3f}")