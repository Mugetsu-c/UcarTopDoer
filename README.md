python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# только если миграции уже в репозитории:
alembic upgrade head

uvicorn app.main:app --reload