FROM node:20-slim              # ← node au lieu de python
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build
CMD ["npm", "start"]           
