import os, re, pandas as pd
from datetime import datetime
from tqdm import tqdm
import snscrape.modules.twitter as sntwitter

SAVE_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(SAVE_DIR, exist_ok=True)
OUT_PATH = os.path.join(SAVE_DIR, "tweets_raw.csv")

SINCE = "2025-01-01"
UNTIL = datetime.now().strftime("%Y-%m-%d")
QUERY = f'(deprem OR #deprem) lang:tr since:{SINCE} until:{UNTIL} -filter:replies'
MAX_TWEETS = 1000

def clean_text(txt: str) -> str:
    txt = re.sub(r"http\\S+", "", txt)
    txt = re.sub(r"RT\\s+", "", txt)
    txt = re.sub(r"[@#]\\S+", "", txt)
    txt = txt.replace("\\n", " ").strip()
    return txt

def main():
    rows = []
    for i, tweet in enumerate(tqdm(sntwitter.TwitterSearchScraper(QUERY).get_items(), total=MAX_TWEETS)):
        if i >= MAX_TWEETS:
            break
        rows.append({
            "id": tweet.id,
            "date": tweet.date,
            "username": tweet.user.username if tweet.user else None,
            "content": clean_text(tweet.content),
            "likeCount": getattr(tweet, "likeCount", None),
            "retweetCount": getattr(tweet, "retweetCount", None),
            "replyCount": getattr(tweet, "replyCount", None),
            "url": tweet.url,
            "lang": getattr(tweet, "lang", None),
        })
    pd.DataFrame(rows).to_csv(OUT_PATH, index=False, encoding="utf-8")
    print(f"Saved: {OUT_PATH} ({len(rows)} rows)")

if __name__ == "__main__":
    main()
