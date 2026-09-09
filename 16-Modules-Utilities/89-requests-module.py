# requests module - is an HTTP library that enables developers to send HTTP requests in Python.
# this module enables you to send HTTP requests using python code and make it possible to inetract with APIs and web services.

# GET Request - A GET request is used to retrieve/fetch data from a server or API.

import requests

response = requests.get("https://jobgeniusai.vercel.app/")

print(response.status_code)
print(response.text)


# POST Request - A POST request is used to send/submit data to a server or API, usually to create or process some data.

import requests

url = "https://example.com/api/users"

data = {
    "name": "Dev",
    "age": 22
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())


# BeautifulSoup (bs4) - BeautifulSoup is a Python library used to parse HTML and XML documents 
# and extract useful information such as headings, paragraphs, links, tables, etc.

import requests
from bs4 import BeautifulSoup

url = "https://jobgeniusai.vercel.app/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)

# Extract Heading

import requests
from bs4 import BeautifulSoup

url = "https://jobgeniusai.vercel.app/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

heading = soup.find("h1")

print(heading.text)

# Extract All Links

import requests
from bs4 import BeautifulSoup

url = "https://jobgeniusai.vercel.app/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

for link in links:
    print(link.text)
    print(link.get("href"))