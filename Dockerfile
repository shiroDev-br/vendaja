# Imagem base oficial do Python
FROM python:3.11-slim

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync

COPY . .

EXPOSE 8000

CMD ["uvicorn", "vendaja.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
