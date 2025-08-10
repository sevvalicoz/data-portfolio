import os, pandas as pd
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

ROOT = os.path.dirname(__file__)
DATA_IN = os.path.join(ROOT, "..", "data", "tweets_raw.csv")
DATA_OUT = os.path.join(ROOT, "..", "data", "tweets_scored.csv")

MODEL_ID = "cardiffnlp/twitter-xlm-roberta-base-sentiment"  # TR destekli çok dilli

def main():
    df = pd.read_csv(DATA_IN)
    df = df.dropna(subset=["content"])

    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID)
    pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, truncation=True)

    labels_map = {0: "negative", 1: "neutral", 2: "positive"}
    sentiments, confidences = [], []

    for text in tqdm(df["content"].tolist()):
        out = pipe(text, top_k=None)[0]  # [{'label':'positive','score':0.9}, ...]
        best = max(out, key=lambda x: x["score"])
        label = best["label"]
        if label.startswith("LABEL_"):
            label = labels_map.get(int(label.split("_")[-1]), label)
        sentiments.append(label)
        confidences.append(float(best["score"]))

    df["sentiment"] = sentiments
    df["confidence"] = confidences
    os.makedirs(os.path.dirname(DATA_OUT), exist_ok=True)
    df.to_csv(DATA_OUT, index=False, encoding="utf-8")
    print(f"Saved: {DATA_OUT} (n={len(df)})")

if __name__ == "__main__":
    main()
