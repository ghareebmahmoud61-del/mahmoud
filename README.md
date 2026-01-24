# mahmoud

A Python package by Mahmoud.

## Installation

### From Source

Clone the repository and install:

```bash
git clone https://github.com/ghareebmahmoud61-del/mahmoud.git
cd mahmoud
pip install -e .
```

### Using pip (development mode)

```bash
pip install -e .
```

### Install with development dependencies

```bash
pip install -r requirements-dev.txt
```

## Setup

The package uses standard Python setuptools for installation and distribution.

### Requirements

- Python >= 3.8
- pip

### Configuration

All package configuration is managed through:
- `setup.py` - Main setup script
- `requirements.txt` - Core dependencies
- `requirements-dev.txt` - Development dependencies

## Usage

After installation, you can import the package:

```python
import mahmoud

print(mahmoud.__version__)
print(mahmoud.__description__)
```

## Development

### Running Tests

```bash
pytest
```

### Installing Development Dependencies

```bash
pip install -r requirements-dev.txt
```

## Project Structure

```
mahmoud/
├── mahmoud/           # Main package directory
│   └── __init__.py   # Package initialization
├── setup.py          # Setup script
├── requirements.txt  # Core dependencies
├── requirements-dev.txt  # Development dependencies
├── .gitignore        # Git ignore file
└── README.md         # This file
```

## License

MIT License