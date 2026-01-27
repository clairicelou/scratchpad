#!/usr/bin/env bash
set -euo pipefail

echo "Creating virtual environment..."
python3 -m venv .fml

echo "Installing/upgrading pip..."
.fml/bin/python -m pip install --upgrade pip

echo "Installing packages..."
.fml/bin/python -m pip install numpy matplotlib pandas seaborn scipy scikit-learn ipykernel

echo "Fetching data..."
.fml/bin/python get_data.py

echo "Done. In your notebook, select kernel: .fml"
