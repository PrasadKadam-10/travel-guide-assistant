✈️ Travel Guide Assistant (RAG-Powered)

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-ACTIVE-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/PROJECT-AI_WEB_APP-purple?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/LEVEL-INTERMEDIATE-orange?style=for-the-badge"/>
</p>---

🌍 Overview

Travel Guide Assistant is a lightweight AI-powered travel recommendation system that delivers fast and personalized destination suggestions using keyword summarization, text similarity matching, and Retrieval-Augmented Generation (RAG) concepts.

The application combines intelligent search techniques, natural language processing, and an interactive web interface to assist users in discovering suitable travel options based on their preferences — without relying on heavy deep-learning models or large-scale databases.

---

🚀 Key Features

- 📦 Compressed destination keyword summaries
- 🔍 Personalized recommendations from user input
- 📊 Similarity score ranking
- 🖼️ Destination image display
- ⚡ Fast response using TF-IDF + cosine similarity
- 🌐 Clean web interface using Streamlit
- 🧠 Lightweight RAG-inspired pipeline

---

🛠️ Tech Stack

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" height="50"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Streamlit-logo-primary-colormark-darktext.png" height="50"/>
  <img src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" height="50"/>
</p>---

📁 Project Structure

travel-guide-assistant/
│
├── data/
│   └── destinations.csv
│
├── travel_recommender.py
├── requirements.txt
└── README.md

---

⚙️ Installation

git clone https://github.com/PrasadKadam-10/travel-guide-assistant.git
cd travel-guide-assistant
pip install -r requirements.txt

---

▶️ Run Application

streamlit run travel_recommender.py

Open browser:

http://localhost:8501

---

✍️ Usage

Enter travel preference keywords such as:

beach calm budget

You will receive:

- Suggested destinations
- Visual references
- Quick summaries

---

🧠 Working Pipeline

1️⃣ Dataset stores destination keywords
2️⃣ TF-IDF converts text to vectors
3️⃣ User query vectorized
4️⃣ Cosine similarity calculated
5️⃣ Top matches displayed instantly

---

🎯 Use Cases

- AI/ML academic project
- Hackathon prototype
- Recommendation system demo
- RAG concept showcase

---

🔮 Future Improvements

- Budget filters
- Category selection
- User profiles
- Cloud deployment
- Larger dataset

---

👨‍💻 Author

Prasad Dilip Kadam
Aspiring IT / Software Engineer focusing on AI & ML

---

<p align="center">
⭐ If you found this useful, consider starring the repository!
</p>