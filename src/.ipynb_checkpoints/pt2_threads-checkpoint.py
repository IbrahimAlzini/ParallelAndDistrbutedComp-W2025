import threading
import time
import itertools
from math import sqrt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

def run_threaded(X_train_filled, y_train, X_val_filled, y_val):
    """Runs a threaded parameter search."""
    start_time = time.time()

    n_estimators_range = [10, 25, 50, 100, 200, 300, 400]
    max_features_range = ['sqrt', 'log2', None]
    max_depth_range = [1, 2, 5, 10, 20, None]
    param_combinations = list(itertools.product(n_estimators_range, max_features_range, max_depth_range))

    num_threads = 4
    chunk_size = len(param_combinations) // num_threads
    chunks = [param_combinations[i*chunk_size:(i+1)*chunk_size] for i in range(num_threads)]
    remainder = len(param_combinations) % num_threads
    for i in range(remainder):
        chunks[i].append(param_combinations[chunk_size * num_threads + i])

    best_rmse = float('inf')
    best_mape = float('inf')
    best_parameters = {}
    lock = threading.Lock()

    def process_chunk(chunk):
        nonlocal best_rmse, best_mape, best_parameters
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
            
            with lock:
                if rmse < best_rmse:
                    best_rmse = rmse
                    best_mape = mape
                    best_parameters = {
                        'n_estimators': n_estimators,
                        'max_features': max_features,
                        'max_depth': max_depth
                    }

    threads = []
    for chunk in chunks:
        thread = threading.Thread(target=process_chunk, args=(chunk,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    threading_time = end_time - start_time
    print(f"Threaded Execution Time: {threading_time}s")
    print(f"Best Parameters: {best_parameters}, RMSE: {best_rmse}, MAPE: {best_mape}%")
    return threading_time
