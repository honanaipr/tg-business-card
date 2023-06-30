FROM python:3.11

RUN apt update && apt upgrade -y

RUN pip install -U pip && pip install poetry

WORKDIR /tg_business_card

COPY pyproject.toml .

RUN poetry install --no-root

COPY . .

CMD poetry run python -m business_card
