import urllib.request
import xml.etree.ElementTree as ET

# Prompt for the target URL
url = input("Enter location: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_2437013.xml"

print("Retrieving", url)
connection = urllib.request.urlopen(url)
data = connection.read()
print(f"Retrieved {len(data)} characters")

# Parse the XML string
tree = ET.fromstring(data)

# Find all <count> tags using XPath
counts = tree.findall(".//count")

# Sum all count values
total_sum = sum(int(count.text) for count in counts)

print("Count:", len(counts))
print("Sum:", total_sum)
