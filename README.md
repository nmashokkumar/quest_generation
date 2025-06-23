
# 🐉 Quest Text Generator - Red Panda Assignment

This project builds an **NLP-based quest text generator** for fantasy games using a fine-tuned GPT-2 model and FastAPI.  

It was created for Red Panda Games Studio as part of their open assignment.

---

## 🚀 Features

- Trained on 550+ fantasy quests (prompt → output)
- Can generate new quests like “Rescue a dragon in Frozen Reach”
- Simple API with FastAPI (`/generate`, `/status`)
- Runs on CPU locally or Colab (no GPU required)

---

## 📽️ Demo Video

▶️ [Click to Watch My Project Walkthrough](https://youtu.be/4c5HXUof2Yw)

---

## 💡 Sample Output

**Prompt:**
```
Write a quest about a dragon
```

**Generated:**
```
### Quest:
Rescue a dragon hidden in Frozen Reach.
Protect a dragon hidden in Shattered Isles.
Banish a cursed dragon hidden in Obsidian Tower.
```

---

## 🧪 Try It on Colab

▶️ [Click to Open in Colab](https://colab.research.google.com/drive/1w94xtcs_NXc5unigmvvKKU4Sct8D7zlx?usp=sharing)

---

## 🛠️ How to Run Locally

```bash
# Clone repo
git clone https://github.com/nmashokkumar/quest_generation
cd quest_generation

# Create and activate virtual env
python -m venv venv
venv\Scripts\activate

# Install packages
pip install -r requirements.txt

# Run FastAPI server
uvicorn app:app --reload
```

Then go to:  
🔗 http://127.0.0.1:8000/generate?prompt=Write+a+quest+about+a+dragon

---

## 📁 Folder Structure

```
├── app.py
├── quest_model/
├── data/fantasy_quests.jsonl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 👨‍💻 What I’d Improve with More Time

- Add UI to input prompt + show quest
- Use a bigger model like Mistral or LLaMA
- Clean up grammar in quest output

---

## 🧠 Created By

Ashok Kumar for Red Panda Games  
Built with ❤️ using HuggingFace, Colab & FastAPI
