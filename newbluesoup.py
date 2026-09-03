import ssl
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ").strip()
if not (url.startswith("http://") or url.startswith("https://")):
    url = "https://" + url

count = int(input("Enter count: "))
position = int(input("Enter position: "))

last_name = None

for i in range(count):
    print(f"Retrieving: {url}")
    html = urllib.request.urlopen(url, context=ctx).read()
  

    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")

    if len(tags) < position:
        print(f"Error: Found only {len(tags)} links, but position {position} was requested.")
        break

    target_tag = tags[position - 1]
    href = target_tag.get("href", None)

    if not href:
        print("Error: Target tag has no 'href' attribute.")
        break

   
    url = urljoin(url, href)
    last_name = target_tag.text

print(f"Last URL: {url}")
print(f"Last Name: {last_name}")
