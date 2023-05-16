# wsi-api

An API for word sense induction using ChatGPT API and FastAPI

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