import requests


class Crawler:

    def __init__(self, url, proxies):
        self.urls = url
        self.proxies = proxies
        self.checkme = f'url = {self.urls}\nproxy = {self.proxies}'

    def webscraper(self, url, proxies):
        """
        takes in a url and a proxy if provided and connects to url
        :param url: single quoted string
        :param proxies: dict: {'http':'proxy.address'}
        :return: nothing yet
        """
        # read in url however you need to read it from file
        try:
            r = requests.get(url, proxies)
            if r.status_code == 200:
                if r.text is not None:
                    return r.text
        except requests.exceptions.ConnectionError:
            print('connection error\n')
            print(f'url: {url} proxy: {proxies}')
