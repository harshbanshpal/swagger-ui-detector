import requests
from bs4 import BeautifulSoup

def is_swagger_ui(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Check for a common Swagger UI element
            if soup.find('div', id='swagger-ui'):
                return True
    except requests.RequestException as e:
        print(f"Error checking {url}: {e}")
    return False

def check_urls(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]
        for url in urls:
            if is_swagger_ui(url):
                print(f"Swagger UI found at: {url}")
            else:
                print(f"No Swagger UI at: {url}")

# Replace 'urls.txt' with your file path
check_urls('urls.txt')
