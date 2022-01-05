import time
from urllib.request import Request, urlopen

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
    loca = str(input('[+]Enter the number of your choice: '))
    
    try:
        proxy_ip_set()
    except ValueError:
        print('[-] The number you entered is invalid.\n\nExiting...')
        exit()

def proxy_ip_set():
    global loca

    if loca == '1':
        proxy = '81.255.13.197'     # France
        print(f'[+] Connecting to {proxy} (France)...')
    elif loca == '2':
        proxy = '217.97.101.134'    # Poland
        print(f'[+] Connecting to {proxy} (Poland)...')
    elif loca == '3':
        proxy = '124.121.92.216'    # Thailand
        print(f'[+] Connecting to {proxy} (Thailand)...')
    elif loca == '4':
        proxy = '58.176.147.14'     # Hong Kong
        print(f'[+] Connecting to {proxy} (Hong Kong)...')
    elif loca == '5':
        proxy == '47.89.153.213'    # Canada
        print(f'[+] Connectiing to {proxy} (Canada)...')
    else:
        print('[-] The number you entered is invalid.\n\nExiting...')
        exit()

def test():
    global proxy

    print(f'Proxy IP: {proxy}.\nChecking IP...')
    IP = urlopen(Request('https://api.ipify.org/')).read().decode()
    print(f'Your IP is {IP}.')

if __name__ == "__main__":
    main()