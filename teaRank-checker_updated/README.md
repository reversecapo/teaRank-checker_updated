# teaRank Checker

This project simulates teaRank detection for Python packages using PyPI.

## Features
- Checks if a package exists in PyPI.
- Simulates a teaRank score based on random factors.

## Installation
Install the package using pip:
```
pip install tearank-checker
```

## Usage
Run the module to simulate teaRank for a given package:
```
python -m tearank_checker.checker
```

Example:
```
Enter the package name to check: requests
Package 'requests' exists in PyPI. Simulating teaRank...
teaRank for 'requests': 78
```

## Testing
Run tests using pytest:
```
pytest
```
