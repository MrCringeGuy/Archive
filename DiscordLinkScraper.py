#Crappy idea for an image scraper thingy

# try opening url based on https://cdn.discordapp.com/attachments/914687440315371603/929791144878034944/PXL_20220109_173733852.jpg
# except error of some sort then print nothing
# gen random letters/numbers and a file name

import requests

amt = int(input('[*] How many links to try: '))

for n in amt:
    print(f'[{i + 1}]')
    try:
        request(f'[{i + 1}]     {url}')
        print(f'[+] {url}')
    except SomethingError:
        print('[{i + 1}]     [-]')
