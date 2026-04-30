# 🎬 Movie Search Engine (Elasticsearch + FastAPI + Docker)

A full-stack movie search engine powered by Elasticsearch.

Features fuzzy search, tag-based recommendations, and real-time analytics.

---

## Run the project

```bash
docker compose up --build
````

---

## Access

* Frontend → [http://localhost:8080](http://localhost:8080)
* API Docs → [http://localhost:8000/docs](http://localhost:8000/docs)
* Kibana → [http://localhost:5601](http://localhost:5601)

---

## eatures

* Fuzzy movie search (handles typos)
* Tag-based recommendations
* Genre filtering
* Analytics with Kibana

---

## Dataset Setup

Download the MovieLens dataset:

[https://grouplens.org/datasets/movielens/latest/](https://grouplens.org/datasets/movielens/latest/)

Extract into:

```
data/ml-latest-small/
```

---

### Generate merged dataset

```bash
python ingest/merge_movies_tags.py
```

---

### Load data into Elasticsearch

```bash
curl -X POST localhost:9200/_bulk --data-binary "@data/movies_final.json"
```

---

## Run without Docker (optional)

Install dependencies:

```bash
pip install -r requirements.txt
```

Run API:

```bash
uvicorn api.main:app --reload
```

---

## Tech Stack

* Elasticsearch
* FastAPI
* Docker
* Nginx

---

## Notes

* First startup may take ~30 seconds (Elasticsearch warmup)
* Dataset is not included to keep repo lightweight
