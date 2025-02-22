import multiprocessing
import time
import itertools
from math import sqrt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

def evaluate_chunk(chunk, X_train_filled, y_train, X_val_filled, y_val):
    """Processes a chunk of parameter combinations and finds the best model."""
    chunk_best_rmse = float('inf')
    chunk_best_mape = float('inf')
    chunk_best_params = {}

    for params in chunk:
        n_estimators, max_features, max_depth = params
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

        if rmse < chunk_best_rmse:
            chunk_best_rmse = rmse
            chunk_best_mape = mape
            chunk_best_params = {
                'n_estimators': n_estimators,
                'max_features': max_features,
                'max_depth': max_depth
            }
    
    return (chunk_best_rmse, chunk_best_mape, chunk_best_params)

def run_multiprocess(X_train_filled, y_train, X_val_filled, y_val):
    """Runs multiprocessing parameter search."""
    start_time = time.time()
    num_processes = min(4, multiprocessing.cpu_count())
    
    n_estimators_range = [10, 25, 50, 100, 200, 300, 400]
    max_features_range = ['sqrt', 'log2', None]
    max_depth_range = [1, 2, 5, 10, 20, None]
    param_combinations = list(itertools.product(n_estimators_range, max_features_range, max_depth_range))

    chunk_size = max(1, len(param_combinations) // num_processes)
    chunks = [param_combinations[i * chunk_size:(i + 1) * chunk_size] for i in range(num_processes)]
    remainder = len(param_combinations) % num_processes
    for i in range(remainder):
        chunks[i].append(param_combinations[chunk_size * num_processes + i])

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(evaluate_chunk, [(chunk, X_train_filled, y_train, X_val_filled, y_val) for chunk in chunks])

    best_rmse = float('inf')
    best_mape = float('inf')
    best_parameters = {}

    for rmse, mape, params in results:
        if rmse < best_rmse:
            best_rmse = rmse
            best_mape = mape
            best_parameters = params

    end_time = time.time()
    multiprocessing_time = end_time - start_time
    print(f"Multiprocessing Execution Time: {multiprocessing_time}s")
    print(f"Best Parameters: {best_parameters}, RMSE: {best_rmse}, MAPE: {best_mape}%")
    return multiprocessing_time
