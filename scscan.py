import argparse
import requests
import whois
import shodan
import socket

def web_scan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Website: {url}")
            print(f"Status: {response.status_code}")
            print(f"Title: {response.text.split('<title>')[1].split('</title>')[0]}")
            print(f"Server: {response.headers.get('Server', 'Unknown')}")
            print(f"Robots.txt: {requests.get(f'{url}/robots.txt').text}")
            print(f"Whois: {whois.whois(url)}")
        else:
            print(f"Website: {url}")
            print(f"Status: {response.status_code}")
            print(f"Whois: {whois.whois(url)}")
    except requests.exceptions.RequestException as e:
        print(f"Error scanning website: {e}")

def ip_scan(ip, ports=None):
    try:
        if ports is None:
            ports = range(1, 65535)
        else:
            ports = map(int, ports.split(','))
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()
    except socket.error as e:
        print(f"Error scanning IP: {e}")

def shodan_scan(target):
    try:
        api = shodan.Shodan('VFCxm8FLgzg4xDHA6IylUcjX37fiSoev')
        results = api.search(target)
        print(f"Shodan Results for {target}:")
        for result in results['matches']:
            print(f"IP: {result['ip_str']}")
            print(f"Port: {result['port']}")
            print(f"Data: {result['data']}")
            print("---")
    except shodan.APIError as e:
        print(f"Error scanning with Shodan: {e}")

def find_info(target):
    try:
        print(f"Whois information for {target}:")
        print(whois.whois(target))
    except whois.parser.PywhoisError as e:
        print(f"Error finding information: {e}")

def wordlist_url_scan(url, wordlist_file):
    try:
        with open(wordlist_file, 'r') as file:
            wordlist = file.read().splitlines()
        for word in wordlist:
            try:
                response = requests.get(f"{url}/{word}")
                if response.status_code == 200:
                    print(f"Found: {url}/{word}")
            except requests.exceptions.RequestException:
                pass
    except FileNotFoundError:
        print(f"Wordlist file not found: {wordlist_file}")

def main():
    parser = argparse.ArgumentParser(description='Security Scanner')
    parser.add_argument('-web-scan', help='Scan a website')
    parser.add_argument('-ip-scan', help='Scan an IP')
    parser.add_argument('-p', help='Specify ports to scan')
    parser.add_argument('-shodan-scan', help='Scan with Shodan')
    parser.add_argument('-find-info', help='Find information about a target')
    parser.add_argument('-wordlist-url', help='Wordlist file for URL scanning')
    args = parser.parse_args()

    if args.web_scan:
        web_scan(args.web_scan)
    elif args.ip_scan:
        ip_scan(args.ip_scan, args.p)
    elif args.shodan_scan:
        shodan_scan(args.shodan_scan)
    elif args.find_info:
        find_info(args.find_info)
    elif args.wordlist_url:
        if not args.web_scan:
            print("Please provide a website URL with -web-scan to scan with a wordlist.")
        else:
            wordlist_url_scan(args.web_scan, args.wordlist_url)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
