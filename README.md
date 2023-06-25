# My business card for Telegram bots selling

## Features
* Users database (first user become admin)


## Configuration
```sh
mv .env.example .env
```
replace **<BOT_TOKEN>** with your bot token in **.env**

## Install dependences
```sh
poetry install
```

## Run
```sh
poetry run python -m business_card
```

## Build and run with Docker
```sh
docker build -t business_card .
docker run -d business_card
```

## Misc
### Install docker
```sh
apt install -y wget
wget -qO- https://get.docker.com/ | sh
```

### Update pip
```sh
pip install -U pip
```

### Insall poetry
```sh
pip install poetry
```