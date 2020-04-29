FROM node:lts-alpine

# make the 'app' folder the current working directory
WORKDIR /app

RUN npm install -g http-server

# copy both 'package.json'
COPY package.json ./

# and 'yarn.lock' (if available)
COPY yarn.lock ./

# install project dependencies
RUN yarn

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN yarn start

EXPOSE 8088

CMD [ "yarn", "start" ]