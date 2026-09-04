import urllib.request
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
total_sum = 0
count = 0

for tag in tags:
  
    total_sum += int(tag.contents[0])
    count += 1

print(f'Count {count}')
print(f'Sum {total_sum}')
