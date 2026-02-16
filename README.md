[![Python application test with Github Actions](https://github.com/human-ak/python-functions/actions/workflows/main.yml/badge.svg)](https://github.com/human-ak/python-functions/actions/workflows/main.yml)

# python-functions
live training


### To cal Microservice
'''bash
curl -X 'POST' \
  'https://fictional-waffle-xvj5vvr5pq6f6v4w-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "tiger"
}'
'''

### Build container

'docker build .'
'docker image ls'

### Kill previous proces
'ps -ef | grep python'
'kill -9 <id>'


### Run Container

'docker run -p 127.0.0.1:8080:8080 <IMAGE ID>'

### Invoke Post request

'run invoke.sh'

