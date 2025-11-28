import streamlit as st
import joblib
import numpy as np


model = joblib.load("models/best_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


st.title("Bienvenue dans HamOrSpamAI - Le Meilleur Système Anti-Spam Intelligent")
st.text("Renseigner les champs suivants pour vérifier si votre email est Spam ou Non")

sujet = st.text_input("Sujet")
corps = st.text_area("Corps", height=300)

if st.button("Prédire") :
    if sujet.strip() == "" or corps.strip() == "":
        st.warning("Veuillez Saisir un Sujet ou un Contenu d'Email !")
    else:
        email = sujet.strip() + " " + corps.strip()
        
        X = vectorizer.transform([email])
        
        pred = model.predict(X)[0]
        
        if pred == 1:
            st.error("Résultat : **SPAM détecté !**")
        else:
            st.success("Résultat : **Email légitime (HAM)**")
            
        st.markdown("---")
        st.subheader("Métriques de prédiction")
        
        proba = model.predict_proba(X)[0]

        st.write("#### Probabilités par classe")
        st.write(f"- HAM (0) : {float(proba[0])}")
        st.write(f"- SPAM (1) : {float(proba[1])}")

        confiance = float(np.max(proba))
        st.write(f"#### Score de confiance : **{confiance:.4f}**")