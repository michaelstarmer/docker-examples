FROM node:10.15.1
ENV NPM_CONFIG_LOGLEVEL warn

COPY ./src/package*.json /app/
COPY ./src /app/

WORKDIR /app
RUN npm i

EXPOSE 3000

CMD ["npm", "start"]
