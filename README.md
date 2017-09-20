Jackal Flask - Setup
========================

## Idea Source

[Jackal](https://en.wikipedia.org/wiki/Jackal_(video_game)) as [Python Flask](http://flask.pocoo.org) tutorial :video_game:

![Image Of Jackal](https://upload.wikimedia.org/wikipedia/zh/7/70/Jackal.png)

## Prerequisite

### Docker

* [Download Docker](https://www.docker.com/community-edition#/download)
* [Docker Get Started](https://docs.docker.com/get-started)
* [Docker Documentation](https://docs.docker.com)

### Heroku

* [Sign Up](https://www.heroku.com)
* [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
* [Heroku Container Registry](https://devcenter.heroku.com/articles/container-registry-and-runtime)

## User Guide

### Build Flask App

`docker build -t <image-name> -f Dockerfile.local .`

### Database Utils

##### Create Flask App Local Sqlite Database (One Time Setup)

`docker run -ti --rm -v $PWD/db:/opt/webapp/db <image-name> python create_db.py`

##### Drop Flask App Local Sqlite Database (One Time Clean Up)

`docker run -ti --rm -v $PWD/db:/opt/webapp/db <image-name> python drop_db.py`

### Run Flask App Test With Coverage

* `docker run -ti -v $PWD:/opt/webapp -v $PWD/db:/opt/webapp/db --rm <image-name> coverage run --source=app tests.py`
* `docker run -ti -v $PWD:/opt/webapp --rm <image-name> coverage report`
* `docker run -ti -v $PWD:/opt/webapp --rm <image-name> coverage html`

### Start Flask App Container

`docker run -d --name <container-name> -v $PWD/db:/opt/webapp/db --env PORT=5000 -p 5000:5000 <image-name>`

### Check Flask App Container Log

`docker logs -f <container-name>`

### Remove Flask App Container

`docker rm -f <container-name>`

### Create Heroku Postgresql Addon (One Time Setup)

* `heroku login`
* `heroku addons:create heroku-postgresql:hobby-dev -a <heroku-app-name>`

### Deploy Flask App To Heroku

* `heroku login`
* `heroku container:login`
* `heroku apps --all`
* `heroku container:push web -a <heroku-app-name>`
* `heroku open -a <heroku-app-name>`

### Destory Flask App On Heroku

* `heroku container:rm web -a <heroku-app-name>`

### Clean Up Docker Images

`docker rmi -f $(docker images --filter "dangling=true" -q --no-trunc)`

## Contributing

[Pull Requests](https://github.com/wgx731/jackal-flask/pulls) are most welcome!

## Thanks

**jackal-flask** © 2017+, [@wgx731]. Released under the [MIT](https://github.com/wgx731/jackal-flask/blob/master/LICENSE) License.

Authored and maintained by [@wgx731] with help from contributors ([list][contributors]).

> GitHub [@wgx731]

[@wgx731]: https://github.com/wgx731
[contributors]: https://github.com/wgx731/jackal-flask/contributors

