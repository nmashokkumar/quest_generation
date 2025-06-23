from fastapi import FastAPI, Query
from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline

# Initialize FastAPI app
app = FastAPI()

# Load fine-tuned model and tokenizer
model_path = "./quest_model"
model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)

# Create generation pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Health check route
@app.get("/status")
def status():
    return {"model": "QuestGPT", "status": "Running", "version": "v1.0"}

# Text generation route
@app.get("/generate")
def generate(prompt: str = Query(..., description="Prompt to generate quest text")):
    raw_text = generator(prompt, max_length=200, num_return_sequences=1, temperature=0.9)[0]["generated_text"]

    # Extract and clean individual quests
    quests = [q.strip() for q in raw_text.split("### Quest:") if q.strip()]
    unique_quests = list(dict.fromkeys(quests))  # Removes duplicates but keeps order

    # Rebuild as a nice list
    clean_output = "\n".join([f"### Quest: {q}" for q in unique_quests])

    return {
        "prompt": prompt,
        "quest_count": len(unique_quests),
        "quests": clean_output
    }



