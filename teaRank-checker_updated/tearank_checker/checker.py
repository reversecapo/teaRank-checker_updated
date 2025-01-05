import requests

def check_package_in_pypi(package_name):
    """Check if a package exists in PyPI."""
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

def simulate_tearank(package_name):
    """Simulate a teaRank detection."""
    if check_package_in_pypi(package_name):
        print(f"Package '{package_name}' exists in PyPI. Simulating teaRank...")
        # Simulate a random teaRank score (e.g., based on dependencies or downloads)
        import random
        tearank = random.randint(1, 100)
        print(f"teaRank for '{package_name}': {tearank}")
    else:
        print(f"Package '{package_name}' not found in PyPI.")
