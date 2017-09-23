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

## Docker User Guide

### Build Flask App

`docker build -t <image-name> .`

### Run Flask App Test With Coverage

* `docker run -ti --rm -v $PWD:/opt/webapp <image-name> coverage run --source=app tests.py`
* `docker run -ti --rm -v $PWD:/opt/webapp <image-name> coverage report`
* `docker run -ti --rm -v $PWD:/opt/webapp <image-name> coverage html`

### Start Flask App Container

`docker run -d --name <container-name> --env PORT=5000 -p 5000:5000 <image-name>`

### Check Flask App Container Log

`docker logs -f <container-name>`

### Remove Flask App Container

`docker rm -f <container-name>`

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

## Pipenv User Guide

### Install Depedencies

`pipenv install --dev`

### Run Flask App

`pipenv run gunicorn --bind 0.0.0.0:5000 wsgi --access-logfile - --log-file -`

###  Run Flask App Test With Coverage

`pipenv run coverage run --source=app tests.py`
`pipenv run coverage report`
`pipenv run coverage html`

### Deploy Flask App To Heroku

* `heroku login`
* `heroku apps --all`
* `heroku git:remote -a <heroku-app-name>`
* `git push -f heroku setup:master`
* `heroku open -a <heroku-app-name>`

## Contributing

[Pull Requests](https://github.com/wgx731/jackal-flask/pulls) are most welcome!

## Thanks

**jackal-flask** © 2017+, [@wgx731]. Released under the [MIT](https://github.com/wgx731/jackal-flask/blob/master/LICENSE) License.

Authored and maintained by [@wgx731] with help from contributors ([list][contributors]).

> GitHub [@wgx731]

[@wgx731]: https://github.com/wgx731
[contributors]: https://github.com/wgx731/jackal-flask/contributors

