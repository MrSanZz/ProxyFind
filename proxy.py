import requests, time, random, os, random
from requests.exceptions import Timeout
global user_agents
user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
if os.name == 'posix':
    os.system('clear')
elif os.name == 'nt':
    os.system('cls')
def start_proxy(a, typs):
    while True:
        try:
            headers = {
                "User-Agent": random.choice(user_agents)
            }
            count = random.randint(1,260)
            url = 'https://api.proxyscrape.com/?request=displayproxies&proxytype={}&timeout={}&country=all'.format(typs, count)
            response = requests.get(url, timeout=7, headers=headers)
            print(count, response.status_code, end='\r')
            if response.status_code == 200:  # Check if the request is successful
                with open(a, 'a') as file:
                    file.write(response.text)
            elif response.status_code == 429:
                print("coldown for 20sec..                                 ", end='\r')
                time.sleep(20)
        except Timeout:
            print('Timeout')
            pass
        except requests.exceptions.ProxyError:
            continue

if __name__ == '__main__':
    a = input("save as : ")
    typs = input("Proxy Type[http / socks4/ socks5]: ")
    start_proxy(a, typs)
