# Default target
all: run

# Prompt the user for the OpenAI API key and create the .env file
create-env:
	@echo "Please enter your OpenAI API key:"
	@read OPENAI_API_KEY; \
	echo "OPENAI_API_KEY=$$OPENAI_API_KEY" > .env

# Build the Docker image
build:
	docker build -t openai-integration-app .

# Run the Docker container
run: create-env build
	docker run --env-file .env -p 4000:80 openai-integration-app

# Stop the Docker container
stop:
	docker stop $$(docker ps -q --filter ancestor=openai-integration-app)

# Run flake8 linter
lint:
    flake8 .

# Clean up the .env file
clean:
	rm -f .env

# Deploy changes: stop the container, clean the .env file, and rebuild everything
deploy-changes: stop clean all