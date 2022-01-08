import requests

proxies = {
    'https': 'https://34.77.73.11:80'     #e.g: https://ip:port
}

response = requests.get('https://ipinfo.org/json', proxies=proxies)
#print(response.json()['country'])      for specific results
print(response.text)