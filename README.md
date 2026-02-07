# 🌍 Travel Guide Assistant

A lightweight AI-powered travel recommendation system that delivers fast, personalized destination suggestions using keyword-based summaries,
text-similarity matching, and Retrieval-Augmented Generation (RAG) concepts.
---

## 🚀 Features

* 📦 Compressed destination summaries (keyword guides)
* 🔍 Personalized recommendations from user input
* 📊 Similarity score ranking
* 🖼️ Destination image display
* ⚡ Fast response using TF-IDF + cosine similarity
* 🌐 Clean web interface using Streamlit
* 🧠 No heavy ML models or databases required

---

## 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit

---

## 📁 Project Structure

```
travel-guide-assistant/
│
├── data/
│   └── destinations.csv
│
├── travel_recommender.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone repository:

```
git clone https://github.com/PrasadKadam-10/travel-guide-assistant.git
cd travel-guide-assistant
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Run Application

```
streamlit run travel_recommender.py
```

Open browser:

```
http://localhost:8501
```

---
## ✍️ Usage

As a user, you can enter your travel preferences in simple keywords, for example:

```
beach calm budget
```

After submitting your input, you will receive:

* Suggested destinations that best match your preferences
* Relevant images to help you visualize the locations
* A quick overview to assist in choosing suitable travel options

---

## 🧠 How It Works (Simple)

1️⃣ Destination keywords stored in CSV
2️⃣ TF-IDF converts text → vectors
3️⃣ User query vectorized
4️⃣ Cosine similarity calculated
5️⃣ Top matches shown instantly

---

## 🎯 Use Cases

* AI/ML mini project
* Academic submission
* Demo of text-based recommendation
* Hackathon prototype

---

## 🔮 Future Improvements

* Budget filters
* Travel category selection
* User profiles
* Cloud deployment
* Larger dataset

