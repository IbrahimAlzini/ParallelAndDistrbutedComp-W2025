
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import src.pt2_seq as sequential
import src.pt2_threads as thread
import src.pt2_processes as process

def run_part2():
    """Function to generate necessary data and compute speedup metrics."""
    # Load the dataset
    file_path = 'data/train.csv'  # Update this path as needed
    train_data = pd.read_csv(file_path, index_col="Id")

    # Drop unnecessary columns
    columns_to_delete = ['MoSold', 'YrSold', 'SaleType', 'SaleCondition', 'Alley', 'FireplaceQu', 'PoolQC', 'Fence', 'MiscFeature']
    train_data_cleaned = train_data.drop(columns=columns_to_delete, axis=1)

    # Define input features (X) and output (y)
    X = train_data_cleaned.drop('SalePrice', axis=1)
    y = train_data_cleaned['SalePrice']

    # Identify categorical columns
    categorical_columns = X.select_dtypes(include=['object']).columns

    # Apply Label Encoding
    label_encoders = {column: LabelEncoder() for column in categorical_columns}
    for column in categorical_columns:
        X[column] = label_encoders[column].fit_transform(X[column])


    # Split the first dataset (X, y) into train and test sets with a 70% - 30% split
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.30, random_state=42)
    
    # Fill NaN values in X_train and X_val with the median of the respective columns
    X_train_filled = X_train.fillna(X_train.median())
    X_val_filled = X_val.fillna(X_val.median())

    # Call the other scripts to get execution times
    sequential_time = sequential.run_sequential(X_train_filled, y_train,X_val_filled, y_val)
    threading_time = thread.run_threaded(X_train_filled, y_train,X_val_filled, y_val)
    multiprocessing_time = process.run_multiprocess(X_train_filled, y_train,X_val_filled, y_val)


    # Compute speedup and efficiency
    np = 6
    speedup_threads = sequential_time / threading_time
    speedup_processes = sequential_time / multiprocessing_time
    
    efficiency_threads = speedup_threads / np
    efficiency_processes = speedup_processes / np
    
    p = 0.90  # Assuming 90% of program is parallelizable
    speedup_amdahl_threads = 1 / ((1 - p) + (p / np))
    speedup_amdahl_processes = 1 / ((1 - p) + (p / np))
    
    speedup_gustafson_threads = np - (1 - p) * np
    speedup_gustafson_processes = np - (1 - p) * np
    
    print("Performance Analysis:")
    print(f"Speedup (Threads): {speedup_threads}")
    print(f"Speedup (Processes): {speedup_processes}")
    print(f"Efficiency (Threads): {efficiency_threads}")
    print(f"Efficiency (Processes): {efficiency_processes}")
    print(f"Amdahl's Law Speedup (Threads): {speedup_amdahl_threads}")
    print(f"Amdahl's Law Speedup (Processes): {speedup_amdahl_processes}")
    print(f"Gustafson's Law Speedup (Threads): {speedup_gustafson_threads}")
    print(f"Gustafson's Law Speedup (Processes): {speedup_gustafson_processes}")


