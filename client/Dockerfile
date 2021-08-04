FROM node:12.7.0-alpine

# set working directory
WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json
RUN npm ci
RUN npm install react-scripts@4.0.3 -g --silent

# start app
CMD ["npm", "start"]
