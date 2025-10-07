
from viz import visualization
# ! ============================================================================================================
def detecte_outliers_with_iqr(data, column):
    
    df_analyser = data.copy()
    Q1 = df_analyser[column].quantile(0.25)
    Q3 = df_analyser[column].quantile(0.75)
    IQR = Q3 - Q1
    
    print("Shape : ", data.shape)
    print("Q1 (25%) : ", Q1)
    print("Q3 (75%) : ", Q3)
    print("IQR : ", IQR)
    
    bande_inf = Q1 - 1.5 * IQR
    bande_sup = Q1 + 1.5 * IQR
    
    mask_outliers = (df_analyser[column] < bande_inf) | (df_analyser[column] > bande_sup)
    outliers = df_analyser[mask_outliers]
    n_outliers = mask_outliers.sum()
    df_analyser = df_analyser[~mask_outliers]
    

    print(f"Nombre des outliers détectés : {n_outliers}")
    print(f"Pourcentage f'outliers: {(n_outliers/len(df_analyser))*100:.2f}%")
    print(f"Limites: [{bande_inf:.2f}, {bande_sup:.2f}]]")
    # print(f"Dataset.head() =  {df_analyser.head()}")
    
    print(f"La distribution des {column} avec les bornes sup/inf :")
        
    visualization(data, column, bande_inf, bande_sup) 

    return outliers, bande_inf, bande_sup, IQR


# ! ============================================================================================================

def detecte_remote_outliers_with_iqr(data, column):
    df_analyser = data.copy()
    Q1 = df_analyser[column].quantile(0.25)
    Q3 = df_analyser[column].quantile(0.75)
    IQR = Q3 - Q1
    
    print("Shape : ", data.shape)
    print("Q1 (25%) : ", Q1)
    print("Q3 (75%) : ", Q3)
    print("IQR : ", IQR)
    
    bande_inf = Q1 - 1.5 * IQR
    bande_sup = Q1 + 1.5 * IQR
    
    mask_outliers = (df_analyser[column] < bande_inf) | (df_analyser[column] > bande_sup)
    outliers = df_analyser[mask_outliers]
    n_outliers = mask_outliers.sum()
    df_analyser = df_analyser[~mask_outliers]
    

    print(f"Nombre des outliers détectés : {n_outliers}")
    print(f"Pourcentage f'outliers: {(n_outliers/len(df_analyser))*100:.2f}%")
    print(f"Limites: [{bande_inf:.2f}, {bande_sup:.2f}]]")
    # print(f"Dataset.head() =  {df_analyser.head()}")
    
    print(f"La distribution des {column} avec les bornes sup/inf :")
      
    visualization(df_analyser, column, bande_inf, bande_sup) 
    
    return df_analyser, outliers, bande_inf, bande_sup, IQR

# ! ============================================================================================================