FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV TELEGRAM_BOT_TOKEN="7629046804:AAEofEIUFWpWKF3-wG4RNb3dra68ViYbrnE"

CMD ["python3", "main.py"]