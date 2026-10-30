import requests
from bs4 import BeautifulSoup

bad_chars = ['<', '>', '"', "'", ';', '--', '/*', '*/', '{', '}', '(', ')', '=', '+', '-']


def spider_inputs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    form = soup.find("form")
    if not form:
        print("No forms found on the page.")
        return [], url

    action = form.get("action")
    post_url = action if action else url

    inputs = form.find_all("input")

    return inputs, post_url


def test_inputs(url, post_url, inputs):
    results = {}

    for input_field in inputs:
        name = input_field.get("name")

        if not name:
            continue

        for char in bad_chars:
            payload = {name: char}

            try:
                response = requests.post(post_url, data=payload)

                key = f"{post_url} | field: {name} | payload: {char}"
                results[key] = response.status_code

            except requests.RequestException as e:
                results[f"ERROR {name}"] = str(e)

    return results


def main():
    url = input("Enter the URL to scan for vulnerabilities: ")

    inputs, post_url = spider_inputs(url)

    if not inputs:
        print("No input fields found on the page.")
        return

    results = test_inputs(url, post_url, inputs)

    for key, value in results.items():
        print(f"{key} -> Status Code: {value}")


if __name__ == "__main__":
    main()