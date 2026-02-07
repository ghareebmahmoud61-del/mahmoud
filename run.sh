#!/bin/bash

# Script to run a Docker container with the specified SHA256 image digest
# Usage: ./run.sh

IMAGE_DIGEST="sha256:28c86dc782966929b09e951f0580826027c0b80e9ba38868e1fc6811dfb8bade"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Error: Docker is not installed or not in PATH"
    echo "Please install Docker from: https://docs.docker.com/get-docker/"
    exit 1
fi

# Check if Docker daemon is running
if ! docker info &> /dev/null; then
    echo "Error: Docker daemon is not running"
    echo "Please start Docker and try again"
    exit 1
fi

echo "Running Docker container with image digest: $IMAGE_DIGEST"
echo "Note: If you get an error about the image not being found, you may need to"
echo "      specify a repository name (e.g., ubuntu@$IMAGE_DIGEST)"
echo ""

# Run the Docker container
if docker run "$IMAGE_DIGEST"; then
    echo ""
    echo "Container executed successfully"
else
    echo ""
    echo "Error: Failed to run container"
    echo "This may happen if:"
    echo "  - The image digest doesn't exist in any accessible registry"
    echo "  - You need to provide a repository name (e.g., ubuntu@sha256:...)"
    echo "  - Network connectivity issues"
    exit 1
fi
