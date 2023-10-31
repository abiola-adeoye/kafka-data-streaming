FROM 3.10.13-alpine3.17

WORKDIR . /app

COPY requirements.txt .

RUN pip install -r requirements.txt

