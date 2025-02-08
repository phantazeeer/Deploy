FROM node:20-alpine AS builder
COPY package.json .
RUN npm install --force
COPY . .
RUN npm run build

FROM nginx:1.27-alpine AS runner
COPY --from=builder /dist /usr/share/nginx/html
COPY --from=builder nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 5173
CMD ["nginx", "-g", "daemon off;"]