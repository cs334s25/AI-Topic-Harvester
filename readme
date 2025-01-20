# AI Topic Harvester

This project extracts text from PDF files and uses OpenAI's GPT-4 to parse the text and identify primary and secondary topics.

## Features

- Extracts text from PDF files.
- Uses OpenAI's GPT-4 to analyze the text and identify primary and secondary topics.
- Dockerized for easy setup and deployment.

## Setup

### Prerequisites

- Python 3.9 or higher
- Docker
- Make

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/ai-topic-harvester.git
    cd ai-topic-harvester
    ```

2. **Build and run the Docker container using Make:**

    ```sh
    make build
    make run
    ```

3. **Stop the Docker container:**

    ```sh
    make stop
    make clean
    ```

### Deploy Changes:

This function stops the running container, cleans the `.env` file, and rebuilds everything from scratch. It ensures that the environment is reset and all changes are deployed correctly.
    
    make deploy-changes

#### Steps:
1. **Stop**: Stops the currently running container.
2. **Clean**: Cleans the `.env` file to remove any existing configurations.
3. **Rebuild**: Rebuilds the entire environment to apply the latest changes.