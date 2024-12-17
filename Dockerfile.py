# 1. Використовуємо базовий образ Python (версія 3.12)
FROM python:3.12

# 2. Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# 3. Копіюємо файли застосунку у контейнер
COPY bott.py /app/bott.py
COPY pyproject.toml /app/pyproject.toml

# 4. Встановлюємо залежності (через Poetry або pip)
RUN pip install --no-cache-dir poetry
RUN poetry install --no-root || pip install requests flask

# 5. Вказуємо основну команду для запуску застосунку
ENTRYPOINT ["python", "bott.py"]
