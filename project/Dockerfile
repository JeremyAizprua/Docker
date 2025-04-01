# Usamos una imagen base de Python
FROM python:3.8-slim

# Configuramos el directorio de trabajo
WORKDIR /app

# Copiamos los archivos de la aplicación
COPY . /app

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto que usará Flask
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
