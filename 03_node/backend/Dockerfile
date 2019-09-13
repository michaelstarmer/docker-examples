FROM node:10
MAINTAINER Michael Pedersen Starmer

# In
RUN npm i -g @adonisjs/cli

COPY ./src /src

WORKDIR /src

RUN npm i

EXPOSE 3333 9229

CMD [ "npm", "start" ]


