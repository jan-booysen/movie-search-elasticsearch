# 🎬 Elasticsearch-powered movie search engine with FastAPI and Docker

A full-stack movie search engine built with:
- Elasticsearch
- FastAPI
- Docker
- MovieLens dataset

---

## 🚀 Run the project

```bash
docker compose up
````

---

## 🌐 Access

* Frontend: [http://localhost:8080](http://localhost:8080)
* API docs: [http://localhost:8000/docs](http://localhost:8000/docs)
* Kibana: [http://localhost:5601](http://localhost:5601)

---

## 🔍 Features

* Fuzzy movie search
* Tag-based recommendations
* Genre filtering
* Analytics (Kibana)

---

## 📦 Dataset

MovieLens small dataset

---

## 📦 Dataset Setup

Download the MovieLens dataset:

https://grouplens.org/datasets/movielens/latest/

Extract it into:

data/ml-latest-small/

---

Then run:

```bash
python ingest/merge_movies_tags.py
````

## 🧠 Tech Stack

* Elasticsearch
* FastAPI
* Docker
* Nginx

---

# 🚀 5. Run everything

```bash
docker compose up --build
````

---

# ⚠️ First run checklist

1. Wait for Elasticsearch to fully start (~30 sec)
2. Run your ingestion script (once)

👉 You can still run locally:

```bash
python ingest/merge_movies_tags.py
```

Then load data:

```bash
curl -X POST localhost:9200/_bulk --data-binary "@data/movies_final.json"
```

---