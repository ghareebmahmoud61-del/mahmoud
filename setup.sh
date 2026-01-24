#!/bin/bash

# Professional Agent Setup Script
# Automates the installation and setup process

set -e

echo "========================================"
echo "Professional Agent System - Setup"
echo "========================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3.7 or higher first."
    exit 1
fi

# Display Python version
PYTHON_VERSION=$(python3 --version)
echo "✓ Found $PYTHON_VERSION"
echo ""

# Determine which pip command to use
PIP_CMD=""
if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
elif command -v pip &> /dev/null; then
    PIP_CMD="pip"
else
    echo "Error: pip is not installed."
    echo "Please install pip first."
    exit 1
fi

echo "✓ pip is available ($PIP_CMD)"
echo ""

# Install the package in editable mode
echo "Installing professional-agent package..."
echo ""

$PIP_CMD install -e .

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "You can now use the professional agent:"
echo ""
echo "  from professional_agent import ProfessionalAgent"
echo "  agent = ProfessionalAgent('YourName', 'YourSpecialty')"
echo ""
echo "Run tests with:"
echo "  python3 test_professional_agent.py"
echo ""
