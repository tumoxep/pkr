# pkr

## Deploy
1. set env vars on host. Populate directories
2. `docker-compose up -d pkr-postgres`
3. `docker-compose up -d pkr-redis`
4. `docker-compose up pkr-makemigrations-game`
5. `docker-compose up pkr-migrate`
6. `docker-compose run --rm pkr-createsuperuser`
7. `docker-compose up -d pkr-backend`
8. `docker-compose up -d pkr-front`

## Credits
* checkbox.scss by Stephanie Eckles https://moderncss.dev/pure-css-custom-checkbox-style/
* django .gitignore by Santosh Purbey https://gist.github.com/santoshpurbey/6f982faf1eacdac153ffd86a3a694239
* CustomUserCreationForm by overiq https://overiq.com/django-1-10/django-creating-users-using-usercreationform/
