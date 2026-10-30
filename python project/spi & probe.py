import sys
import requests

def urls(out_file):
    url2 = sys.stdin.read().splitlines()

    res_url = []
    bad_url = []

    for url in urls:
        try:
            response = requests.head(url)
            if response.status_code == 200:
                res_url.append(url)

        except requests.exceptions.MissingSchema:
            bad_url.append(url)
            continue
        except requests.exceptions.ConnectionError:
            bad_url.append(url)
            continue
    with open(out_file, 'w') as file:
        file.write('\n'.join(res_url))
    print(f"Saved URLS {out_file}")

out_file = "filteref_urls.txt"
urls(out_file)