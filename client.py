import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Configuration de la page
st.set_page_config(
    page_title="Prédiction Diabète",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Prédiction du risque de diabète")

st.write("""
Cette application prédit le risque de diabète basé sur vos données cliniques.
Remplissez les informations ci-dessous pour obtenir une évaluation.
""")

# ------------------------------------------------ Chargement du modèle sauvegardé ------------------------------------------------
@st.cache_resource
def load_model():
    with open("model_diabete.pkl", "rb") as file:
        model = pickle.load(file)
    return model

@st.cache_resource
def load_scaler():
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    return scaler

try:
    model = load_model()
    scaler = load_scaler()
    st.success("✅ Modèle et scaler chargés avec succès")
except Exception as e:
    st.error(f"❌ Erreur lors du chargement: {str(e)}")
    st.stop()

# ------------------------------------------------ Interface utilisateur ------------------------------------------------
st.subheader("📋 Informations du Patient")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Nombre de grossesses (Pregnancies)", min_value=0, max_value=20, value=1)
    glucose = st.number_input("Glycémie (mg/dL) (Glucose)", min_value=0, max_value=300, value=90)
    blood_pressure = st.number_input("Pression artérielle (mmHg) (BloodPressure)", min_value=0, max_value=200, value=70)
    skin_thickness = st.number_input("Épaisseur du pli cutané (mm) (SkinThickness)", min_value=0, max_value=100, value=20)

with col2:
    insulin = st.number_input("Insuline (mu U/ml) (Insulin)", min_value=0.0, max_value=900.0, value=80.0, step=1.0)
    bmi = st.number_input("IMC (kg/m²) (BMI)", min_value=0.0, max_value=70.0, value=22.0, step=0.1)
    diabetes_pedigree = st.number_input("Prédisposition génétique (DiabetesPedigreeFunction)", min_value=0.0, max_value=2.5, value=0.5, step=0.01)
    age = st.number_input("Âge (Age)", min_value=0, max_value=120, value=25)

# ------------------------------------------------ Bouton de prédiction ------------------------------------------------
if st.button("🔍 Évaluer le risque", type="primary"):

    try:
        insulin_transformed = np.log1p(insulin)
        diabetes_pedigree_transformed = np.log1p(diabetes_pedigree)
        
        input_data = pd.DataFrame({
            "Pregnancies": [pregnancies],
            "Glucose": [glucose],
            "BloodPressure": [blood_pressure],
            "SkinThickness": [skin_thickness],
            "Insulin": [insulin_transformed],
            "BMI": [bmi],
            "DiabetesPedigreeFunction": [diabetes_pedigree_transformed],
            "Age": [age]
        })

        st.write("### Données entrées (après transformation):")
        st.dataframe(input_data)
        
        # Vérification des valeurs
        st.write("### Vérification des valeurs:")
        st.write(f"- Glucose: {glucose} (doit être >126 pour risque)")
        st.write(f"- BMI: {bmi} (doit être >30 pour risque)")
        st.write(f"- Insulin (transformé): {insulin_transformed:.2f}")
        
        # Standardisation
        input_scaled = scaler.transform(input_data)
        
        st.write("### Données après standardisation:")
        st.write(input_scaled)
        
        # Prédiction
        probabilities = model.predict_proba(input_scaled)[0]
        prediction = model.predict(input_scaled)[0]
        risk_score = probabilities[1]  # Probabilité de classe 1 (risque élevé)
        
        st.write("### Résultats de prédiction:")
        st.write(f"Probabilités brutes: {probabilities}")
        st.write(f"Classe prédite: {prediction}")
        
        # ------------------------------------------------ Affichage des résultats ------------------------------------------------
        st.subheader("📊 Résultats")

        st.progress(float(risk_score))

        st.write(f"**Score de risque : {risk_score*100:.1f}%**")

        custom_threshold = 0.5
        
        # Message de risque
        if risk_score >= custom_threshold:
            st.error("🚨 **RISQUE ÉLEVÉ** - Consultation médicale recommandée")
            
        else:
            st.success("✅ **RISQUE FAIBLE** - Maintenir un mode de vie sain")

    except Exception as e:
        st.error(f"Erreur lors de la prédiction: {str(e)}")
        st.info("Vérifiez que toutes les valeurs sont correctement remplies")

