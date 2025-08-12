# Настройка для Ubuntu:
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

если миграции уже в репозитории(по умолчанию есть):
alembic upgrade head

uvicorn app.main:app --reload

# Настройка для Ubuntu:
python -m venv .venv
venv\Scripts\activate
pip install -r requirements.txt

если миграции уже в репозитории(по умолчанию есть):
alembic upgrade head

uvicorn app.main:app --reload


# Примеры curl запросов и их ответы
## request
curl -sS -X POST "http://127.0.0.1:8000/reviews" \
  -H "Content-Type: application/json" \
  -d '{"text":"Люблю этот сервис"}'

## response
{
  "id": 1,
  "text": "Люблю этот сервис",
  "sentiment": "positive",
  "created_at": "2025-08-12T07:15:21.123456+00:00"
}

## request
curl -sS "http://127.0.0.1:8000/reviews?sentiment=positive"

## response
[
  {
    "id": 1,
    "text": "Люблю этот сервис",
    "sentiment": "positive",
    "created_at": "2025-08-12T07:15:21.123456+00:00"
  }
]

## request
curl -sS "http://127.0.0.1:8000/reviews?sentiment=positive"

## response
{
  "detail": [
    {
      "type": "enum",
      "loc": ["query", "sentiment"],
      "msg": "Input should be 'positive', 'negative' or 'neutral'",
      "input": "bad"
    }
  ]
}



## response
[
  {
    "id": 1,
    "text": "Люблю этот сервис",
    "sentiment": "positive",
    "created_at": "2025-08-12T07:15:21.123456+00:00"
  }
]
