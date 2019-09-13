# Docker & Docker Compose: Starter Pack
Below you will find some of the most commonly used commands.

## Docker commands:
---
  
List running docker services/containers:   
`docker ps`

List docker images on system:   
`docker <TYPE> ls`
```
Example:
docker volume ls
docker container ls
```

Delete/remove:  
`docker volume rm <TYPE> <ID or NAME>`
```
Example:
docker rm volume b7720dd5688d5
docker rm container 847b2561f824
```

Logs:  
`docker logs <ID or NAME>`
```
Example:
docker logs backend
docker logs -f backend // Show log for backend with the follow-flag
```

Open bash inside container:  
`docker exec -it <ID or NAME> /bin/bash`
```
Example:
docker exec -it nodeserver /bin/bash
```

## Docker-compose commands
Start services:  
`docker-compose up`
```
Example:
docker-compose up -d // daemon mode
docker-compose up -d --build
docker-compose up -d --no-cache
```
  
Stop services:  
`docker-compose down`

Stop a single service:
`docker-compose stop <ID or NAME>`
```
Example:
docker-compose stop api
```

Start a single service:  
`docker-compose up <ID or NAME>`
```
Example:
docker-compose up -d api
```
