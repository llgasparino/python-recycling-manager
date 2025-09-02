# syntax=docker/dockerfile:1.6

############################################
# Base stage
############################################
FROM python:3.11-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Instala dependências do sistema (se precisar de build de libs futuras)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

# Instala dependências Python
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia código
COPY recycling_manager ./recycling_manager
COPY app.py ./

# Porta padrão do Flask
EXPOSE 5000

# Variáveis para flask run (produção simples)
ENV FLASK_APP=app \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_ENV=production

############################################
# Development stage (opcional)
############################################
FROM base AS dev
COPY requirements-dev.txt ./
RUN pip install -r requirements-dev.txt || true

############################################
# Final image (runtime)
############################################
FROM base AS final
# Se quiser copiar apenas o site-packages final de outra stage, manter simples agora

CMD ["flask", "run"]
