import json
import ssl
import urllib.request

url = input("Enter location: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_2437014.json"

print("Retrieving", url, flush=True)

# Ignore SSL certificate errors if needed
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Add User-Agent header and set a timeout
req = urllib.request.Request(
    url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
)

try:
    with urllib.request.urlopen(req, timeout=10, context=ctx) as response:
        data = response.read().decode()
        print(f"Retrieved {len(data)} characters")

        info = json.loads(data)
        comments = info.get("comments", [])

        total_sum = sum(item["count"] for item in comments)

        print("Count:", len(comments))
        print("Sum:", total_sum)

except Exception as e:
    print("Error fetching data:", e)
