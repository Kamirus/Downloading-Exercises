import requests
import urllib
from bs4 import BeautifulSoup


# filter hrefs from url containing <phrase>
def get_links_with(url, phrase):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")

    links = soup.findAll('a')
    hrefs = []
    for elem in links:
        x = elem.get('href')
        if x is None:
            continue
        if x.find(phrase) is 0 and x not in hrefs:
            hrefs.append(x)
    return hrefs


# returns url without last segment: returned/last-slash-chopped
def prepare_sub_link(url):
    res = url.rpartition('/')
    return res[0] + res[1]  # add / sign at the end


# main
def download(url, phrase):
    links = get_links_with(url, phrase)
    pre_link = prepare_sub_link(url)

    for link in links:
        task_url = pre_link + link
        urllib.urlretrieve(task_url, link.partition('/')[-1])


URL2 = "http://www.ii.uni.wroc.pl/~prz/2015zima/java/java.html"
URL = "http://www.ii.uni.wroc.pl/~prz/2016lato/cpp/cpp.html"
PHRASE = 'zad'

download(URL2, PHRASE)

