# Используем базовый образ python
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt для установки зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Задаем порт 5000
EXPOSE 5000

# Запускаем приложение
CMD ["python", "run.py"]