FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["flask_app_02.py", "./"]

EXPOSE 1234

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:1234", "flask_app_02:app"]
