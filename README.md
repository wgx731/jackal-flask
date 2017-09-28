Jackal Flask - Setup
========================

## Idea Source

[Jackal](https://en.wikipedia.org/wiki/Jackal_(video_game)) as [Python Flask](http://flask.pocoo.org) tutorial :video_game:

![Image Of Jackal](https://upload.wikimedia.org/wikipedia/zh/7/70/Jackal.png)

## Prerequisite

### Docker (Optional)

* [Download Docker](https://www.docker.com/community-edition#/download)
* [Docker Get Started](https://docs.docker.com/get-started)
* [Docker Documentation](https://docs.docker.com)

### Pipenv

* [Python Installation Guide](http://docs.python-guide.org/en/latest/starting/installation)
* [Pipenv Documentation](https://pipenv.readthedocs.io/en/latest)
* [Pipenv Install Guide](https://pipenv.readthedocs.io/en/latest/basics.html#installing-pipenv)

### Heroku

* [Sign Up](https://www.heroku.com)
* [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
* [Heroku Container Registry](https://devcenter.heroku.com/articles/container-registry-and-runtime)

###### NOTE: heroku app used in docker user guide and pipenv user guide should be different app!

## Docker User Guide

### Build Flask App

`docker build -t jackal-flask -f Dockerfile.local .`

### Database Utils

##### Create Flask App Local Sqlite Database (One Time Setup)

`docker run -ti --rm -v $PWD/db:/opt/webapp/db jackal-flask python create_db.py`

##### Drop Flask App Local Sqlite Database (One Time Clean Up)

`docker run -ti --rm -v $PWD/db:/opt/webapp/db jackal-flask python drop_db.py`

### Run Flask App Test With Coverage

* `docker run -ti --rm -v $PWD:/opt/webapp -v $PWD/db:/opt/webapp/db jackal-flask coverage run --source=app tests.py`
* `docker run -ti --rm -v $PWD:/opt/webapp jackal-flask coverage report`
* `docker run -ti --rm -v $PWD:/opt/webapp jackal-flask coverage html`

### Start Flask App Container

`docker run -ti --rm -v $PWD/db:/opt/webapp/db --env PORT=5000 -p 5000:5000 jackal-flask`

_NOTE:_ the container will be removed once you quit app using `Ctrl+C`

### Create Heroku Postgresql Addon (One Time Setup)

* `heroku login`
* `heroku addons:create heroku-postgresql:hobby-dev -a <heroku-docker-app-name>` or `heroku addons:attach <heroku-app-with-db>::DATABASE -a <heroku-docker-app-name>`
* `heroku pg:promote <heroku-database> -a <heroku-docker-app-name>`

### Create Heroku Postgresql Database (One Time Setup)

* `heroku run python create_db.py`

### Drop Heroku Postgresql Database (One Time Clean up)

* `heroku run python drop_db.py`

### Deploy Flask App To Heroku

* `heroku login`
* `heroku container:login`
* `heroku apps --all`
* `heroku container:push web -a <heroku-docker-app-name>`
* `heroku open -a <heroku-docker-app-name>`

### Destory Flask App On Heroku

* `heroku container:rm web -a <heroku-docker-app-name>`

### Clean Up Docker Images

`docker rmi -f $(docker images --filter "dangling=true" -q --no-trunc)`
`docker rmi -f jackal-flask`
`docker rmi -f registry.heroku.com/<heroku-docker-app-name>/web`

## Pipenv User Guide

### Install Depedencies

`pipenv install --dev`

### Database Utils

##### Create Flask App Local Sqlite Database (One Time Setup)

`pipenv run python create_db.py`

##### Drop Flask App Local Sqlite Database (One Time Clean Up)

`pipenv run python drop_db.py`

### Run Flask App

##### Setup Environment Variable

* Mac / Linux: `export FLASK_APP=app_local.py`
* Windows: `set FLASK_APP=app_local.py`

##### Start Flask App

`pipenv run flask run`

###  Run Flask App Test With Coverage

`pipenv run coverage run --source=app tests.py`
`pipenv run coverage report`
`pipenv run coverage html`

### Create Heroku Postgresql Addon (One Time Setup)

* `heroku login`
* `heroku addons:create heroku-postgresql:hobby-dev -a <heroku-normal-app-name>` or `heroku addons:attach <heroku-app-with-db>::DATABASE -a <heroku-normal-app-name>`
* `heroku pg:promote <heroku-database> -a <heroku-normal-app-name>`

### Create Heroku Postgresql Database (One Time Setup)

* `heroku run python create_db.py`

### Drop Heroku Postgresql Database (One Time Clean up)

* `heroku run python drop_db.py`

### Deploy Flask App To Heroku

* `heroku login`
* `heroku apps --all`
* `heroku git:remote -a <heroku-normal-app-name>`
* `git push -f heroku persistent:master`
* `heroku open -a <heroku-normal-app-name>`
* `heroku logs -a <heroku-normal-app-name>`

## Contributing

[Pull Requests](https://github.com/wgx731/jackal-flask/pulls) are most welcome!

## Thanks

**jackal-flask** © 2017+, [@wgx731]. Released under the [MIT](https://github.com/wgx731/jackal-flask/blob/master/LICENSE) License.

Authored and maintained by [@wgx731] with help from contributors ([list][contributors]).

> GitHub [@wgx731]

[@wgx731]: https://github.com/wgx731
[contributors]: https://github.com/wgx731/jackal-flask/contributors

