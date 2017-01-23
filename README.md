[![Build Status](https://travis-ci.org/claudiazanetel/kid_activities_manager.svg?branch=master)](https://travis-ci.org/claudiazanetel/kid_activities_manager) 
[![Coverage Status](https://coveralls.io/repos/github/claudiazanetel/kid_activities_manager/badge.svg?branch=master)](https://coveralls.io/github/claudiazanetel/kid_activities_manager?branch=master)

# Kid Activities Manager

## Development

### Docker

###### Build image
`docker build -t kam -f kam_dockerfile .`

###### Run container
`docker run -d -v ${PWD}:/usr/share/app -p 8080:8080 -p 8000:8000 --name=kam kam`

### Vagrant
`vagrant up`
