import time
from math import sqrt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

def run_sequential(X_train_filled, y_train, X_val_filled, y_val):
    """Runs the sequential parameter search."""
    start_time = time.time()

    # Define the parameter ranges
    n_estimators_range = [10, 25, 50, 100, 200, 300, 400]
    max_features_range = ['sqrt', 'log2', None]
    max_depth_range = [1, 2, 5, 10, 20, None]

    best_rmse = float('inf')
    best_mape = float('inf')
    best_parameters = {}

    for n_estimators in n_estimators_range:
        for max_features in max_features_range:
            for max_depth in max_depth_range:
                rf_model = RandomForestRegressor(
                    n_estimators=n_estimators,
                    max_features=max_features,
                    max_depth=max_depth,
                    random_state=42
                )
                rf_model.fit(X_train_filled, y_train)
                y_val_pred = rf_model.predict(X_val_filled)
                rmse = sqrt(mean_squared_error(y_val, y_val_pred))
                mape = mean_absolute_percentage_error(y_val, y_val_pred) * 100

                if rmse < best_rmse:
                    best_rmse = rmse
                    best_mape = mape
                    best_parameters = {
                        'n_estimators': n_estimators,
                        'max_features': max_features,
                        'max_depth': max_depth
                    }

    end_time = time.time()
    sequential_time = end_time - start_time
    print(f"Sequential Execution Time: {sequential_time}s")
    print(f"Best Parameters: {best_parameters}, RMSE: {best_rmse}, MAPE: {best_mape}%")
    return sequential_time
