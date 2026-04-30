from fastapi import FastAPI, Query
from elasticsearch import Elasticsearch
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# es = Elasticsearch("http://elasticsearch:9200")
es = Elasticsearch("http://localhost:9200")

INDEX = "movies"


@app.get("/")
def root():
    return {"message": "Movie Search API is running 🚀"}


# 🔍 Search endpoint
@app.get("/search")
def search_movies(q: str = Query(...)):
    query = {
        "query": {
            "match": {
                "title": {
                    "query": q,
                    "fuzziness": "AUTO"
                }
            }
        }
    }

    res = es.search(index=INDEX, body=query)

    return [hit["_source"] for hit in res["hits"]["hits"]]


# 🏷️ Recommendation endpoint
@app.get("/recommend")
def recommend_movies(tags: str):
    tag_list = tags.split(",")

    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"tags": tag}} for tag in tag_list
                ]
            }
        },
        "sort": [
            {"tag_count": "desc"}
        ]
    }

    res = es.search(index=INDEX, body=query)

    return [hit["_source"] for hit in res["hits"]["hits"]]


# 📊 Top genres endpoint
@app.get("/top-genres")
def top_genres():
    query = {
        "size": 0,
        "aggs": {
            "genres": {
                "terms": {
                    "field": "genres"
                }
            }
        }
    }

    res = es.search(index=INDEX, body=query)

    return res["aggregations"]["genres"]["buckets"]