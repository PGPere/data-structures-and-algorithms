import requests
from bs4 import BeautifulSoup
import re


def get_citations_needed_count(url):

    URL = url
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    text = []

    for word in soup.find_all('p'):

        find_all_example = word.get_text()
        text.append(find_all_example)

    number_of_sentences = len(text)

    counter = 0

    for i in range(number_of_sentences):
        if re.findall("citation", text[i]):
            counter += 1

    print(counter)


def get_citations_needed_report(url):

    URL = url
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    text = []

    for word in soup.find_all('p'):

        find_all_example = word.get_text()
        text.append(find_all_example)

    number_of_sentences = len(text)

    for i in range(number_of_sentences):
        if re.findall("citation", text[i]):
            print(text[i])


if __name__ == "__main__":
    get_citations_needed_count(
        'https://en.wikipedia.org/wiki/Pittsford,_New_York')
    get_citations_needed_report(
        'https://en.wikipedia.org/wiki/Pittsford,_New_York')
