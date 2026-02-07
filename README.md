# mahmoud

## Running the Docker Container

This repository contains a script to run a Docker container using a specific SHA256 image digest.

### Prerequisites

- Docker must be installed and running on your system

### Usage

To run the Docker container with the specified SHA256 image digest, execute:

```bash
./run.sh
```

The script will run the Docker image with digest:
```
sha256:28c86dc782966929b09e951f0580826027c0b80e9ba38868e1fc6811dfb8bade
```

### Manual Execution

You can also run the Docker container manually with:

```bash
docker run sha256:28c86dc782966929b09e951f0580826027c0b80e9ba38868e1fc6811dfb8bade
```

### Note

If you need to run an image from a specific repository using this digest, use the format:
```bash
docker run <repository>@sha256:28c86dc782966929b09e951f0580826027c0b80e9ba38868e1fc6811dfb8bade
```

For example:
```bash
docker run ubuntu@sha256:28c86dc782966929b09e951f0580826027c0b80e9ba38868e1fc6811dfb8bade
```