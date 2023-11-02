FROM python:3.11.6-slim

WORKDIR /app

COPY ["requirements-live.txt", "predict.py", "model_cli.bin", "./"]

RUN pip install -r requirements-live.txt

EXPOSE 9911

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9911", "predict:app"]
