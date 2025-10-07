import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import StandardScaler
from sklearn.impute import KNNImputer


def knn_imputation(data):
    data_knn = data.copy()
    null_columns = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'Insulin'] 
    
    for col in null_columns:
        data_knn[col] = data_knn[col].replace(0, np.nan)
        
    # Normalisation 
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data_knn)
    data_scaled =pd.DataFrame(scaled_data, columns=data_knn.columns)
    
    # Imputation KNN
    knn_imputer = KNNImputer(n_neighbors=5)
    imputed_data = knn_imputer.fit_transform(data_scaled)
    data_imputed = pd.DataFrame(imputed_data, columns=data_knn.columns)
    
    data_final_knn = pd.DataFrame(scaler.inverse_transform(data_imputed), columns=data_knn.columns)
    
    return data_final_knn


# ! ***************************************************************
def knn_imputation_without_standarisation(data):
    data_knn = data.copy()
    null_columns = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'Insulin'] 
    
    for col in null_columns:
        data_knn[col] = data_knn[col].replace(0, np.nan)
    # Imputation KNN
    knn_imputer = KNNImputer(n_neighbors=5)
    imputed_data = knn_imputer.fit_transform(data_knn)
    data_imputed = pd.DataFrame(imputed_data, columns=data_knn.columns)
        
    return data_imputed