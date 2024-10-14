# Construir la imagen Docker
build:
	@ docker build -t $(IMAGE_NAME):$(TAG) -f $(DOCKERFILE_PATH) .

# Ejecutar el contenedor Docker con montaje de volúmenes
run:
	@docker rm -f $(CONTAINER_NAME) || true
	@docker run -d \
		--name $(CONTAINER_NAME) \
		-v $(CURDIR)/app/data:/app/data \
		-v $(CURDIR)/app/logs:/app/logs \
		-v $(CURDIR)/app/main.py:/app/main.py \
		-v $(CURDIR)/app/.env:/app/.env \
		$(IMAGE_NAME):$(TAG)		

# Ingresar al contenedor Docker
shell:
	@docker run -it \
		-v $(CURDIR)/app/data:/app/data \
		-v $(CURDIR)/app/logs:/app/logs \
		-v $(CURDIR)/app/main.py:/app/main.py \
		-v $(CURDIR)/app/.env:/app/.env \
	$(IMAGE_NAME):$(TAG) /bin/sh

# Limpiar contenedores e imágenes Docker
clean:
	@docker ps -a -q --filter ancestor=$(IMAGE_NAME):$(TAG) | xargs -r docker rm -f
	@docker images -q $(IMAGE_NAME):$(TAG) | xargs -r docker rmi -f