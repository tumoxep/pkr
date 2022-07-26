FROM node:16 as build
WORKDIR /app
COPY package*.json ./
RUN yarn install
COPY ./ .
RUN yarn build

FROM nginx as deploy
RUN mkdir /app
COPY --from=build /app/dist /app
CMD ["nginx", "-g", "daemon off;"]
