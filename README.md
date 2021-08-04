## Negative image

Инвертировать цвета изображения (сделать негатив)

Для начала убедитесь, что у вас установлен Docker и Docker Compose:

```
$ docker -v
Docker version 20.10.6, build 370c289

$ docker-compose -v
docker-compose version 1.29.1, build c34c88b2
```

Для запуска проекта нужно скопировать код из репозитория и
выполнить следующие действия:

1. `git clone git@github.com:netmin/negative-image.git`
2. `cd negative-image`
3. `chmod +x entrypoint.sh`
4. `export REACT_APP_USERS_SERVICE_URL=http://localhost:5001`
5. `docker-compose up -d`
6. `docker-compose exec app  python manage.py recreate_db `

Запуск тестов

`docker-compose exec app pytest project/tests`

Пересоздать базу данных

`docker-compose exec app python manage.py recreate_db`

Swagger http://localhost:5001/doc
