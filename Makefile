.PHONY:  init create-image create-container lint clean-container clean-image

export DOCKER=docker
export PWD=`pwd`
export PYTHONPATH=$PYTHONPATH:$(PWD)
export PROJECT_NAME=streamlits
export MODE=release
export DOCKERFILE=docker/Dockerfile
export IMAGE_NAME=streamlits-image
export CONTAINER_NAME=streamlits-container
export HTTP_HOST_PORT=8888
export HTTP_CONTAINER_PORT=80
export PYTHON=python3


init: init-docker ## initialize repository for traning

init-docker: ## initialize docker image
	$(DOCKER) build -t $(IMAGE_NAME) -f $(DOCKERFILE) .

init-docker-no-cache: ## initialize docker image without cache
	$(DOCKER) build --no-cache -t $(IMAGE_NAME) -f $(DOCKERFILE) .

create-image: init-docker

create-image-no-cache: init-docker-no-cache

create-container: ## create docker container
	$(DOCKER) run -p $(HTTP_HOST_PORT):$(HTTP_CONTAINER_PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME)

down-container: ## remove Docker container
	-$(DOCKER) kill $(CONTAINER_NAME)

clean-container: ## remove Docker container
	-$(DOCKER) rm $(CONTAINER_NAME)

clean-image: ## remove Docker image
	-$(DOCKER) image rm $(IMAGE_NAME)

format:
	- black src
