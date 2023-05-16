# wsi-api

Topic extractor (using ChatGPT API) and recommender (FastAPI)

## Preparation

- Activate the API key of openAI.
- Set your own API key in `.env`.

## Environment

You need to install `poetry`.

```sh
$ poetry install --no-dev
```

## Run

```sh
$ uvicorn main:app --reload --port 8080
```