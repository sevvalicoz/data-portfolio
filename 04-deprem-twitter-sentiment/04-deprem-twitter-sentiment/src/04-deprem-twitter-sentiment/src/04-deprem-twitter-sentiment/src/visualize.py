import os, pandas as pd
import matplotlib.pyplot as plt

ROOT = os.path.dirname(__file__)
DATA_IN = os.path.join(ROOT, "..", "data", "tweets_scored.csv")
OUT_DIR = os.path.join(ROOT, "..", "outputs")
os.makedirs(OUT_DIR, exist_ok=True)

def plot_counts(df):
    ax = df["sentiment"].value_counts().sort_index().plot(kind="bar")
    ax.set_title("Sentiment Dağılımı (deprem)")
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Adet")
    fig = ax.get_figure()
    p = os.path.join(OUT_DIR, "sentiment_counts.png")
    fig.savefig(p, bbox_inches="tight", dpi=150)
    plt.close(fig)

def plot_timeseries(df):
    d = df.copy()
    d["date"] = pd.to_datetime(d["date"])
    d["sentiment_score"] = d["sentiment"].map({"negative": -1, "neutral": 0, "positive": 1})
    ts = d.set_index("date").resample("D")["sentiment_score"].mean()
    ax = ts.plot()
    ax.set_title("Günlük Ortalama Sentiment (deprem)")
    ax.set_xlabel("Tarih")
    ax.set_ylabel("Ortalama Sentiment (-1..1)")
    fig = ax.get_figure()
    p = os.path.join(OUT_DIR, "sentiment_timeseries.png")
    fig.savefig(p, bbox_inches="tight", dpi=150)
    plt.close(fig)

def main():
    df = pd.read_csv(DATA_IN)
    plot_counts(df)
    plot_timeseries(df)
    print(f"Görseller {OUT_DIR} içine kaydedildi.")

if __name__ == "__main__":
    main()
