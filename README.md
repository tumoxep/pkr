# pkr

## Setup
1. Populate `PKR_LETSENCRYPT_DIR` ([this tutorial](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04#step-4-%E2%80%94-obtaining-an-ssl-certificate) helped me)
1. Populate `PKR_PGCONF_DIR` (afaik at least set listen_addresses param)
1. `docker-compose up -d pkr-postgres`
1. `docker-compose up -d pkr-redis`
1. `docker-compose up pkr-makemigrations-game`
1. `docker-compose up pkr-migrate`
1. `docker-compose run --rm pkr-createsuperuser`
1. `docker-compose up -d pkr-backend-api pkr-backend-ws`
1. `docker-compose up -d pkr-front`

## Credits
* checkbox.scss by Stephanie Eckles https://moderncss.dev/pure-css-custom-checkbox-style/
* django .gitignore by Santosh Purbey https://gist.github.com/santoshpurbey/6f982faf1eacdac153ffd86a3a694239
* CustomUserCreationForm by overiq https://overiq.com/django-1-10/django-creating-users-using-usercreationform/
 