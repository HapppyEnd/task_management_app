# Используем базовый образ node
FROM node:14

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json для установки зависимостей
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем остальные файлы проекта
COPY . .

# Задаем порт 3000
EXPOSE 3000

# Запускаем приложение
CMD ["npm", "start"]