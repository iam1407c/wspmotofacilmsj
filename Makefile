.DEFAULT_GOAL := help
include makefiles/ct.mk

OWNER          	= fesosa
TYPE_APP        = script
SERVICE_NAME    = backend
ENV             ?= dev

PROJECT_NAME    = ${OWNER}-${TYPE_APP}-${SERVICE_NAME}-${ENV}

IMAGE_NAME		= ${PROJECT_NAME}
TAG				= latest

# Ruta al Dockerfile
DOCKERFILE_PATH	= docker/Dockerfile

# Nombre del contenedor
CONTAINER_NAME	= ${PROJECT_NAME}

# Comando por defecto
all: help

# Ayuda
help:
	@echo "Makefile para gestionar el proyecto de WhatsApp Mass Messaging"
	@echo ""
	@echo "Comandos disponibles:"
	@echo "  make build           Construir la imagen Docker"
	@echo "  make run             Ejecutar el contenedor Docker"
	@echo "  make install         Instalar dependencias locales (opcional)"
	@echo "  make clean           Eliminar contenedores e imágenes"
	@echo "  make logs            Ver los logs generados"


# Instalar dependencias locales (para desarrollo fuera de Docker)
install:
	pip install --no-cache-dir -r app/requirements.txt

# Ver los logs
logs:
	@docker ps -q --filter ancestor=$(IMAGE_NAME):$(TAG) | xargs -r docker logs -f
