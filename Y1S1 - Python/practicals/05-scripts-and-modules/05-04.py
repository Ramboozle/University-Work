# Write a program that takes a URL as a command-line argument and reports
#  whether or not there is a working website at that address.
#  Hint: You need to get the HTTP response code.
#  Another Hint: StackOverflow is your friend.

import sys, requests

url = sys.argv[1]
response = requests.get(url)
if response.status_code == 200:
    print(f"URL {url} is working")
else:
    print(f"URL {url} is not working")