# Heart Failure Prediction

The project is intended to predict cardiovascular disease based on patient measurements and medical data. It could assist patients who avoid medical prescriptions to change their minds.

The dataset is taken from Kaggle: [Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)

It contains the following attributes:
* Age: age of the patient (years)
* Sex: sex of the patient (M: Male, F: Female)
* ChestPainType: chest pain type (TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic)
* RestingBP: resting blood pressure (mm Hg)
* Cholesterol: serum cholesterol (mm/dl)
* FastingBS: fasting blood sugar (1: if FastingBS > 120 mg/dl, 0: otherwise)
* RestingECG: resting electrocardiogram results (Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria)
* MaxHR: maximum heart rate achieved (Numeric value between 60 and 202)
* ExerciseAngina: exercise-induced angina (Y: Yes, N: No)
* Oldpeak: oldpeak = ST (Numeric value measured in depression)
* ST_Slope: the slope of the peak exercise ST segment (Up: upsloping, Flat: flat, Down: downsloping)
* HeartDisease: output class (1: heart disease, 0: Normal) 

# How to run the project locally

## Install

1. Create [virtualenv](https://docs.python.org/3/library/venv.html). I recommend [pyenv](https://github.com/pyenv/pyenv) + [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
2. Run `pip install -r requirements-live.txt`

## (Re)train model

```
$ ./train.py
```

In Windows systems, you might need to run `python train.py`


## Run locally (options)

Flask internal server

```
$ flask --app predict run
```

gunicorn

```
$ gunicorn --bind=127.0.0.1:9911 predict:app
```

## Docker

```
docker build -t zoomcamp-midterm .
docker run -d -t zoomcamp-midterm -p 9911:9911
```

## Test

Local server
```
$ ./test_http.py
```

Remote server
```
$ ./test_http.py --base-url=https://your-server-url
```

## Notes

1. `model_cli.bin` is posted to the repository to simplify deployment in Digital Ocean App Cloud. You may use my [referral link below to register](https://m.do.co/c/ab9eac81b0cf).
2. In my subjective non-medical opinion, the dataset is imperfect because the model reacts strangely to the Cholesterol value.

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%201.svg)](https://www.digitalocean.com/?refcode=ab9eac81b0cf&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)