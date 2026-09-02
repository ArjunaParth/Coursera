import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(count):
    print(f"Retrieving: {url}")
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all anchor tags
    tags = soup('a')
    
    # Get the tag at the specified position (Convert 1-based position to 0-based index)
    target_tag = tags[position - 1]
    
    # Extract link for the next iteration
    url = target_tag.get('href', None)

# Print final result after the loop ends
print(f"Retrieving: {url}")
print(f"Last Name: {target_tag.text}")
