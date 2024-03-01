#REST-representational state transfer

import requests
response = requests.get("http://216.10.245.166/Library/GetBook.php", params={'ID':'huj878'},)
print(response.text)