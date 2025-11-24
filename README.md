# 📧 **Système Anti-Spam Intelligent — BMSecurity**

Classification automatique des emails (Spam vs Ham) avec NLP + Machine Learning

## 🚀 **Description du projet**

Le Système Anti-Spam Intelligent est une solution développée pour BMSecurity afin de classifier automatiquement les emails en spam ou non spam (ham).
Le projet utilise des techniques avancées de traitement du langage naturel (NLP) et d’apprentissage supervisé pour analyser le contenu des emails et identifier les messages potentiellement malveillants.

Il s'agit d’un composant clé destiné à être intégré aux futures plateformes de messagerie sécurisée des clients de l’entreprise.


## 🎯 **Objectifs**

- Nettoyer et prétraiter un dataset d’emails.

- Extraire des features textuelles via TF-IDF.

- Entraîner plusieurs modèles ML pour trouver le plus performant.

- Comparer leurs résultats et optimiser le meilleur modèle.

- Développer une interface Streamlit permettant d’évaluer manuellement des emails.


## 🛠️ **Étapes du projet**

### 1️⃣ **Analyse des données :**

- Exploration de la structure du dataset.

- Recherche des valeurs manquantes et doublons.

- Analyse de la distribution des classes (spam vs ham).

- Génération de WordClouds pour les deux catégories.

### 2️⃣ **Prétraitement NLP :**

- Conversion en minuscules.

- Nettoyage des mails vides ou dupliqués.

- Tokenisation (NLTK).

- Suppression des stopwords.

- Suppression ponctuation + caractères spéciaux.

- Stemming avec PorterStemmer.

- Vectorisation avec TfidfVectorizer ou CountVectorizer.

### 3️⃣ **Entraînement et optimisation des modèles :**

- **Modèles testés :** Logistic Regression, Naive Bayes, SVM, Random Forest, Gradient Boosting.

- **Évaluation avec :** Accuracy, Precision, Recall, F1-score.

- **Sauvegarde** du meilleur modèle.

### 4️⃣ **Déploiement avec Streamlit :**

L'application permet :

- De saisir un email et obtenir une prédiction spam/ham.

- D’afficher des métriques du modèle.

- De visualiser les WordClouds.


## 👨‍💻 **Technologies utilisées :**

- Python

- NLTK

- Scikit-learn

- Pandas / NumPy

- Matplotlib / Seaborn

- Streamlit

- WordCloud


## 📜 **Licence :**

Projet interne BMSecurity — Tous droits réservés.