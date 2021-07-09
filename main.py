import time
import argparse
import requests

def push(emailAddress, password):
    session = requests.session()
    data = {
        'email_address': emailAddress,
        'password': password,
        'persistent': 'True'
    }  # login data
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'referer': 'https://kindle4rss.com/feeds/explore/?bundles=zh'
    }
    session.headers = headers
    session.post('https://kindle4rss.com/login/', data=data)
    time.sleep(5)
    r = session.post('https://kindle4rss.com/send_now/')
    return r.status_code

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automatic Script for Kindle4rss")
    parser.add_argument('-u', '--user', type=str, required=True, help='User Name, Mostly E-mail Address')
    parser.add_argument('-p', '--password', type=str, required=True, help='Login Password')
    args = parser.parse_args()

    code = push(args.user, args.password)
    today = time.strftime("%Y-%m-%d")
    if code == 200:
        print(f"{today}: push rss success!")
    else:
        print(f"{today}: push rss fault!")
