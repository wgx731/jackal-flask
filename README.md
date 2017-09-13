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

`docker build -t <image-name> .`

### Run Flask App Test

`docker run -ti --rm <image-name> python app_tests.py`

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

## Contributing

[Pull Requests](https://github.com/wgx731/jackal-flask/pulls) are most welcome!

## Thanks

**jackal-flask** © 2017+, [@wgx731]. Released under the [MIT](https://github.com/wgx731/jackal-flask/blob/master/LICENSE) License.

Authored and maintained by [@wgx731] with help from contributors ([list][contributors]).

> GitHub [@wgx731]

[@wgx731]: https://github.com/wgx731
[contributors]: https://github.com/wgx731/jackal-flask/contributors

