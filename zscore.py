from viz import visualization
import numpy as np

# ! ============================================================================================================
def detect_outliers_z_score(data, column, seuil=3):
    df_analyser = data.copy()
    
    mean_val = df_analyser[column].mean()
    std_val = df_analyser[column].std()
    
    sup_limit = mean_val + seuil * std_val
    inf_limit = mean_val - seuil * std_val
    
    outliers_mask = (df_analyser[column] < inf_limit) | (df_analyser[column] > sup_limit) 
    n_outliers = outliers_mask.sum()
    outliers = df_analyser[outliers_mask].copy()
    df_analyser = df_analyser[~outliers_mask]
    
    print(f"Moyenne: {mean_val:.2f}")
    print(f"Ecart-type: {std_val:.2f}")
    print(f"Seuil Z-SCORE: {seuil}")
     
    
    print(f"Nombre des outliers détectés : {n_outliers}")
    print(f"Pourcentage f'outliers: {(n_outliers/len(df_analyser))*100:.2f}%")
    print(f"Limites: [{inf_limit:.2f}, {sup_limit:.2f}]")
    # print(f"Dataset.head() =  {df_analyser.head()}")
    
    print(f"La distribution des {column} avec les bornes sup/inf :")
    
    visualization(data, column, inf_limit, sup_limit)
    
    return outliers, mean_val, std_val

# ! ============================================================================================================

def detect_remote_outliers_z_score(data, column, seuil=3):
    df_analyser = data.copy()
    
    mean_val = df_analyser[column].mean()
    std_val = df_analyser[column].std()
    
    sup_limit = mean_val + seuil * std_val
    inf_limit = mean_val - seuil * std_val
    
    outliers_mask = (df_analyser[column] < inf_limit) | (df_analyser[column] > sup_limit) 
    n_outliers = outliers_mask.sum()
    outliers = df_analyser[outliers_mask].copy()
    df_analyser = df_analyser[~outliers_mask]
    
    print(f"Moyenne: {mean_val:.2f}")
    print(f"Ecart-type: {std_val:.2f}")
    print(f"Seuil Z-SCORE: {seuil}")
     
    
    print(f"Nombre des outliers détectés : {n_outliers}")
    print(f"Pourcentage f'outliers: {(n_outliers/len(df_analyser))*100:.2f}%")
    print(f"Limites: [{inf_limit:.2f}, {sup_limit:.2f}]")
    # print(f"Dataset.head() =  {df_analyser.head()}")
    
    print(f"La distribution des {column} avec les bornes sup/inf :")
    visualization(df_analyser, column, inf_limit, sup_limit) 
    
    return df_analyser, outliers, inf_limit, sup_limit 
    
    