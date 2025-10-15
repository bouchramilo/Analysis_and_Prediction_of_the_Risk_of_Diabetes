# 🏥 Projet IA – Prédiction du Risque de Diabète

## 📌 Contexte du projet
Ce projet a été réalisé dans le cadre d’un laboratoire biomédical souhaitant développer un **système intelligent** capable de **prédire le risque de diabète** chez un patient à partir de ses données cliniques.

L’objectif principal est double :
1. **Classifier** les patients selon leur risque de diabète (à risque / non à risque).
2. **Regrouper** les individus en profils similaires à l’aide de techniques de **clustering**.

Les variables principales étudiées sont :
- `Glucose` : Taux de glycémie
- `Blood Pressure` : Pression artérielle
- `Skin Thickness` : Épaisseur du pli cutané
- `Insulin` : Taux d’insuline
- `BMI` : Indice de Masse Corporelle
- `Diabetes Pedigree Function` : Fonction de prédisposition génétique
- `Age` : Âge du patient

---

## 🎯 Objectifs du projet
- Effectuer une **analyse exploratoire** des données (EDA).
- Nettoyer et **prétraiter** les données (gestion des valeurs manquantes et aberrantes).
- Appliquer un **clustering (K-Means)** pour identifier des groupes homogènes.
- Construire et comparer plusieurs **modèles de classification supervisée**.
- Évaluer les modèles à l’aide de métriques adaptées (Accuracy, Précision, Rappel, F1-score).
- Sauvegarder le **meilleur modèle** et assurer la **reproductibilité** du projet.
- Développer une **application Streamlit** pour la prédiction du risque de diabète.

---


---

## 🚀 Étapes principales (User Stories)

### **1️⃣ Analyse exploratoire des données (EDA)**
- Chargement du dataset avec `pandas`.
- Analyse de la structure, des types et des valeurs manquantes.
- Visualisations des distributions et corrélations (`seaborn`, `matplotlib`).

### **2️⃣ Prétraitement des données**
- Traitement des valeurs manquantes et aberrantes (IQR, z-score, boxplot).
- Sélection et normalisation des variables pertinentes.
- Visualisation des relations entre variables (`pairplot`).

### **3️⃣ Clustering avec K-Means**
- Détermination du nombre optimal de clusters (`méthode du coude`, `silhouette`).
- Entraînement du modèle K-Means.
- Ajout de la colonne `Cluster` au dataset et interprétation des résultats.

### **4️⃣ Analyse des clusters**
- Calcul des moyennes des variables dans chaque cluster.
- Identification du **cluster à haut risque** :
  - `Glucose > 126`
  - `BMI > 30`
  - `Diabetes Pedigree Function > 0.5`
- Création d’une colonne `risk_category` (1 = risque élevé, 0 = faible).

### **5️⃣ Classification supervisée**
- Définition de `X` (variables) et `y` (cible : cluster ou catégorie de risque).
- Division du dataset (train/test).
- Gestion du déséquilibre des classes (`RandomOverSampler`, `SMOTE`).
- Entraînement de plusieurs modèles :
  - `Random Forest`
  - `SVM`
  - `Gradient Boosting`
  - `Decision Tree`
  - `Régression Logistique`
  - `XGBoost`
- Évaluation avec :
  - Matrice de confusion
  - Précision
  - Rappel
  - F1-score
  - Accuracy
- Optimisation des hyperparamètres avec `GridSearchCV`.

---

## 🛠️ Technologies utilisées

| Catégorie | Outils |
|------------|--------|
| Langage | Python |
| Analyse et EDA | Pandas, Numpy, Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost, Imbalanced-learn |
| Optimisation | GridSearchCV |
| Interface  | Streamlit |
| Gestion de projet | Git, Jira |

---

## ⚙️ Installation et exécution

### 1. Cloner le dépôt
```bash
git clone https://github.com/bouchramilo/Analysis_and_Prediction_of_the_Risk_of_Diabetes
cd Analysis_and_Prediction_of_the_Risk_of_Diabetes
```


## ⚙️ Lancer l’application Streamlit
```bash
streamlit run client.py
```
***
Tankt you 😊



