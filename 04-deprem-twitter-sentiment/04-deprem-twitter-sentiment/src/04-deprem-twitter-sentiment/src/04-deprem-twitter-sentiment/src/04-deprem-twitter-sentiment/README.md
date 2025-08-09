# Deprem — Twitter Duygu Analizi (TR)

Bu çalışma, “deprem” anahtar kelimesi içeren Türkçe tweet'lerin duygu dağılımını incelemek için hazırlanmıştır.  
**Teknikler:** snscrape (API'siz veri çekme), Transformers (çok dilli sentiment), Pandas, Matplotlib.

## Nasıl Çalışır?
1) Tweet çekme:
```bash
python src/fetch_tweets.py
2)duygu analizi
python src/analyze_sentiment.py
3)görselleştirme
python src/visualize.py


