# Kid Activities Manager

## Development

### Docker

###### Build image
`docker build -t kam -f kam_dockerfile .`

###### Run container
`docker run -d -v ${PWD}:/usr/share/app -p 8080:8080 -p 8000:8000 --name=kam kam`

### Vagrant
`vagrant up`
