# Nginx reverse proxy for local development
---
This package will make it a bit easier to proxy the dev URL's you want, while still having full control over Nginx .conf-fies.  
  
**Example:**  
A web app running locally on `http://localhost:3000` can be proxied to `http://your-app.local` or `http://your-app.random`.

## Prerequisites
---
* Docker - [[download](https://docs.docker.com/install/)]
* Docker-compose - [[download](https://docs.docker.com/compose/install/)]
* (optional) Python3 for add hosts-script - [[download](https://www.python.org/downloads/)]

## Installation
---

Clone project and go to directory
```
git clone git@bitbucket.org:michaelps/nginx-for-localhost.git nginx
cd nginx
```

Assuming you have installed Python, you can use the included script `addHost.sh` to configure Nginx to proxy your site, by using command: `./addHost.sh [URI] [PORT]`
```console
./addHost.sh appdev.local 3000
```
  
Add the URI to your hosts-file  
**Linux:** `/etc/hosts`  
**Windows:** `c:\Windows\System32\Drivers\etc\hosts`
```
appdev.local 127.0.0.1
```

Start Nginx
```
docker-compose up -d
```
  
The webapp should now be available at [http://appdev.local](http://appdev.local)