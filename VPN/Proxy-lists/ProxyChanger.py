import time

proxy = 0
    

def proxy_change():
    global proxy
    global proxyURL

    if proxy == 1:
        proxyURL = 'https://159.8.114.34:8123'
    if proxy == 2:
        proxyURL = 'https://195.187.63.42:8080'
    if proxy == 3:
        proxyURL = 'https://1.0.170.50:4885'
    if proxy == 4:
        proxyURL = 'https://113.28.90.67:9480'
    if proxy == 5:
        proxyURL = 'https://144.217.240.185:9300'
    

while True:
    proxy += 1
    if proxy == 6:
        proxy -= proxy
    proxy_change()
    print(proxyURL)
    time.sleep(5)