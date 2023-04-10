# Imagen base de Python
FROM python:3.10.11

# Establecer un directorio de trabajo adecuado
WORKDIR /app

# Copiar los requerimientos de la app y luego instalarlos
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar el código fuente de la app
COPY . .

# Exponer el puerto 8000
EXPOSE 8000

# Ejecutar el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]