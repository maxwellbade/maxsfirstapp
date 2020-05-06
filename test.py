import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "3hc4vCBywi9lnDrzRV4Xg", "isbns": "9781632168146"})
print(res.json())
