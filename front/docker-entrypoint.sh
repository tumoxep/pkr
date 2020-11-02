#!/usr/bin/env sh
set -eu
envsubst '${PKR_DOMAIN}' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf
exec "$@"
