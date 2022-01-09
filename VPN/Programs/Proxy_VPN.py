import time
from urllib.request import Request, urlopen
import requests

# using proxies to make a vpn

# France 81.255.13.197
# Poland 217.97.101.134
# Thailand 124.121.92.216
# Hong Kong 58.176.147.14
# Canada 47.89.153.213

# main() is the main program/launcher for the vpn

loca = None

def main():
    unmasked = urlopen(Request('https://api.ipify.org/')).read().decode()
    print(f'[-] Your IP address is {unmasked}.')
    time.sleep(2)
    input('[+] To mask this, just press enter and follow the simple prompts.')
    
    connect_location()

def connect_location():
    global loca

    print('[1] France\n[2] Poland\n[3] Thailand\n[4] Hong Kong\n[5] Canada\n')
    loca = str(input('[+] Enter the number of your choice: '))
    
    try:
        proxy_ip_set()
        proxy_connect()
    except ValueError:
        print('[-] The number you entered is invalid.\n\nExiting...')
        exit()

def proxy_ip_set():
    global loca
    global proxy
    global port

    if loca == '1':
        proxy = 'https://159.8.114.27
        port = '25'     # France
        print(f'[+] Connecting to {proxy} (France)...')
    elif loca == '2':
        proxy = '217.97.101.134'    # Poland
        port = ''
        print(f'[+] Connecting to {proxy} (Poland)...')
    elif loca == '3':
        proxy = 'https://1.0.170.50
        port = '4485'    # Thailand
        print(f'[+] Connecting to {proxy} (Thailand)...')
    elif loca == '4':
        proxy = '1.0.170.50'
        port = '4485'    # Hong Kong
        print(f'[+] Connecting to {proxy} (Hong Kong)...')
    elif loca == '5':
        proxy = '144.217.240.185'
        port = '9300'    # Canada
        print(f'[+] Connectiing to {proxy} (Canada)...')
    else:
        print('[-] The number you entered is invalid.\n\nExiting...')
        exit()

def test():
    global proxy
    global proxies

    print(f'Proxy IP: {proxy}.\nChecking IP...')
    IP = requests.get('https://api.ipify.org/', proxies = proxies)
    print(f'Your IP address is {IP}.')

    if not IP == proxy:
        print('[-] Connection failed.')
    else:
        print('[+] IP address masked.')

def proxy_connect():
    global proxy
    global port
    global proxies
    
    print(proxy)

    proxies = {
        'https': f'https://{proxy}:{port}'
    }

    test()

if __name__ == "__main__":
    main()
