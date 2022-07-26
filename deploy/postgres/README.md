## Get the default config

```
docker run -i --rm postgres cat /usr/share/postgresql/postgresql.conf.sample > postgres.conf
```

*you must set* `listen_addresses = '*'` *so that other containers will be able to access postgres.* (https://hub.docker.com/_/postgres?tab=description)