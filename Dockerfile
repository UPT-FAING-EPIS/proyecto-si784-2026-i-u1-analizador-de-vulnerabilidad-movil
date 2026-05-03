# Imagen base ligera de Python
FROM python:3.11-slim

# Evitar archivos temporales y asegurar logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instalar dependencias del sistema para PostgreSQL
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar librerías de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . .

# Exponer el puerto de Streamlit
EXPOSE 8501

# Comando de inicio
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]