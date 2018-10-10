## Simple web app for repo control on an raspberrypi

Set `LOCAL_REPO_PATH` in `docker-compose.yml` for where the repos will live locally and build and run with:
```
docker-compose up --build
```

Repos can be easily registered through the admin panel at `/admin`

Upon submitting a repo it will be automatically cloned.

Any POST request at `/` will update all repos.

A GET request to '/' will list the current repos in a simple html templat.
