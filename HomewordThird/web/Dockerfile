FROM python:3.10
#
WORKDIR /app

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install pipenv
    # libpq-dev libpq содержит набор функций, используя которые клиентские программы могут передавать запросы серверу PostgreSQL и принимать результаты этих запросов
    # gcc компилятор


COPY Pipfile.lock Pipfile.lock

RUN pipenv sync

EXPOSE 8000

COPY . /app

CMD pipenv run uvicorn web:app --reload --host 0.0.0.0
#--host 0.0.0.0 делает приложение доступным по локалке

#uvicorn web:app --reload запускаем так чтобы при каждом изменении кода приложение перезапускалось
#docker build . делаем образ -t (тото-тото) называем контейнер
#docker ps показывает запущенные контейнеры
#docker run -p 8080:8000 distributed1  запускаем контейнер слева порт местный справа контейнера