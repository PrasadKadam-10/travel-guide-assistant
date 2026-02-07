# travel_recommender.py
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------- Page Config ----------
st.set_page_config(page_title="🌍 Travel Guide Assistant", layout="wide")

# ---------- Sidebar ----------
st.sidebar.title("Travel Guide Assistant")
st.sidebar.markdown("""
**Tech Stack:**  
- Python, Pandas, Scikit-learn, Streamlit  
**Model Used:**  
- Simple RAG-like approach:  
  - Compressed travel guides (short keywords)  
  - TF-IDF + cosine similarity for recommendations  
**How it works:**  
- User enters travel preference  
- System matches keywords in destinations  
- Top matches shown with images & scores
""")

# ---------- Load Data ----------
data = pd.read_csv("data/destinations.csv")

# ---------- Vectorization ----------
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data["summary"])

# ---------- Recommendation Function ----------
def recommend(user_query, top_n=3):
    query_vec = vectorizer.transform([user_query])
    similarity = cosine_similarity(query_vec, tfidf_matrix)[0]

    results = data.copy()
    results["Similarity Score"] = similarity
    results = results.sort_values(by="Similarity Score", ascending=False)

    return results.head(top_n)

# ---------- Main App ----------
st.title("🌍 Travel Guide Assistant")
st.write("Get **fast personalized travel recommendations** using compressed travel guides.")

user_input = st.text_input("✍️ Enter your travel preference:", placeholder="beach calm budget adventure")

if user_input:
    recommendations = recommend(user_input)
    
    for idx, row in recommendations.iterrows():
        st.markdown("---")  # separator
        col1, col2 = st.columns([2, 3])
        
        with col1:
            st.subheader(f"🏖️ {row['destination']}")
            st.write(f"**Keywords:** {row['summary']}")
            st.write(f"**Similarity Score:** {row['Similarity Score']:.2f}")
        
        with col2:
            st.image(row['image'], width=400)
