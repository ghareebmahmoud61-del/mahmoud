#!/bin/bash

# Script to run a Docker container with the specified SHA256 image digest
# Usage: ./run.sh

IMAGE_DIGEST="sha256:28c86dc782966929b09e951f0580826027c0b80e9ba38868e1fc6811dfb8bade"

echo "Running Docker container with image digest: $IMAGE_DIGEST"
docker run "$IMAGE_DIGEST"
