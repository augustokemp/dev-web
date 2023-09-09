FROM node:14.21.3

WORKDIR /app

COPY package*.json /app/

RUN npm install -g npm@7

RUN npm install

COPY ./ /app/

ARG FRONTEND_ENV=production

ENV VUE_APP_ENV=${FRONTEND_ENV}