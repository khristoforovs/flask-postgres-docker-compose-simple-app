FROM python:3.10

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt

COPY . .