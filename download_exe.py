#!/usr/bin/env python3
import os
import urllib
import re
from html.parser import HTMLParser
import requests


class DownloaderHTMLParser(HTMLParser):
    """It's gathering values from given wanted_attrs.
    After feeding call get_all_addresses for list of wanted values'"""
    def __init__(self, wanted_attrs: tuple) -> None:
        super().__init__()
        self._attrs = wanted_attrs
        self._addresses = [''][1:]
        self.base_address = ''

    def handle_startendtag(self, tag: str, attrs: list):
        if tag == 'base':
            for attr in attrs:
                if attr == 'href':
                    self.base_address = attr[1]
        else:
            for attr in attrs:
                if attr[0] in self._attrs:
                    self._addresses.append(attr[1])

    def handle_starttag(self, tag: str, attrs: list):
        if tag == 'base':
            for attr in attrs:
                if attr == 'href':
                    self.base_address = attr[1]
        else:
            for attr in attrs:
                if attr[0] in self._attrs:
                    self._addresses.append(attr[1])

    def get_all_addresses(self) -> list:
        """get list of gathered values"""
        return self._addresses

def filter_addresses(addresses: list, pattern):
    """addresses - list of paths/links
    pattern - phrase which all addresses must contain
    OR
    pattern - regex"""
    rec = re.compile(pattern)
    for address in addresses:
        if rec.search(address) is not None:
            yield address


def make_full_link(link: str, url: str, base) -> str:
    return urllib.parse.urljoin(url, link)


def get_filtered_addresses(url: str, pattern: str, BASE):
    source_code = requests.get(url)
    plain_text = source_code.text
    parser = DownloaderHTMLParser(('href', 'src'))
    parser.feed(plain_text)
    parser.close()
    if parser.base_address != '':
        BASE.append(parser.base_address)
    return filter_addresses(parser.get_all_addresses(), pattern)


# main
def download_from_url(url: str, pattern: str, download=True):
    base_address = [str][1:]
    links = get_filtered_addresses(url, pattern, base_address)
    if not download:
        print('Just listing files that would be downloaded, -d to download')
    else:
        # prepare directory for downloaded files
        if 'downloaded' not in os.listdir():
            os.mkdir('downloaded')
    for link in links:
        link = make_full_link(link, url, base_address)
        if download:
            print("Downloading: " + link)
            urllib.request.urlretrieve(link, os.path.join('downloaded', link.rpartition('/')[-1]))
        else:
            print(link)
