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

model = load_model()


with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# ------------------------------------------------ Interface utilisateur ------------------------------------------------
st.subheader("📋 Informations du Patient")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Nombre de grossesses (Pregnancies)", min_value=0, max_value=20, value=0)
    glucose = st.number_input("Glycémie (mg/dL) (Glucose)", min_value=0, max_value=300, value=90)
    blood_pressure = st.number_input("Pression artérielle (mmHg) (BloodPressure)", min_value=0, max_value=200, value=70)
    skin_thickness = st.number_input("Épaisseur du pli cutané (mm)", min_value=0, max_value=100, value=20)

with col2:
    insulin = st.number_input("Insuline (mu U/ml)", min_value=0, max_value=300, value=80)
    bmi = st.number_input("IMC (kg/m²)", min_value=0.0, max_value=50.0, value=22.0, step=0.1)
    diabetes_pedigree = st.number_input("Prédisposition génétique", min_value=0.0, max_value=2.5, value=0.2, step=0.01)
    age = st.number_input("Âge", min_value=0, max_value=120, value=25)

# ------------------------------------------------ Bouton de prédiction ------------------------------------------------
if st.button("🔍 Évaluer le risque", type="primary"):

    # Données du patient
    input_data = pd.DataFrame({
        "Pregnancies": [pregnancies],
        "Glucose": [glucose],
        "BloodPressure": [blood_pressure],
        "SkinThickness": [skin_thickness],
        "Insulin": [insulin],
        "BMI": [bmi],
        "DiabetesPedigreeFunction": [diabetes_pedigree],
        "Age": [age]
    })

    # Prédiction
    input_scaled = scaler.transform(input_data)
    risk_score = model.predict_proba(input_scaled)[0][1]  # <-- probabilité de la classe 1 (diabète)
    prediction = model.predict(input_scaled)[0]

    # ------------------------------------------------ Affichage des résultats ------------------------------------------------
    st.subheader("📊 Résultats")

    # Barre de progression du risque
    st.progress(float(risk_score))

    st.write(f"**Score de risque : {risk_score*100:.1f}%**")

    # Message de risque
    if prediction == 1:
        st.error("🚨 **RISQUE ÉLEVÉ** - Consultation médicale recommandée")
    else:
        st.success("✅ **RISQUE FAIBLE** - Maintenir un mode de vie sain")
