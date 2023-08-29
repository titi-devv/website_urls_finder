import requests
from bs4 import BeautifulSoup
import re
import requests
from urllib.parse import urlparse
from usp.tree import sitemap_tree_for_homepage


def get_domain_name(url):
    domain_regex = r'^(?:https?:\/\/)?(?:www\.)?([a-zA-Z0-9.-]+)\.[a-zA-Z]{2,}(?:\/.*)?$'
    match = re.search(domain_regex, url)
    if match:
        domain = match.group(1)
        return domain
    else:
        print("Domain not found in the URL.")
        return None


class SitemapFinder:
    def __init__(self, url):
        self.url = url
        self.get_all_urls = self.sitemap_urls(url)

    def sitemap_urls(self, url):
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = "https://" + url
        tree = sitemap_tree_for_homepage(url)
        urls = []
        for page in tree.all_pages():
            page = page.url
            urls.append(page)
        return urls


class WebCrawler:
    def __init__(self, url):
        self.url = url
        self.domain_name = get_domain_name(url)
        self.urls = self.get_urls([url])
        self.subdomains = self.get_subdomains(self.urls, self.domain_name)
        self.subdomain_urls = self.get_urls(self.subdomains)
        self.all_urls = self.urls + self.subdomain_urls
        self.get_all_urls = self.filtered_urls()

    def get_urls(self, urls):

        all_urls = []
        for url in urls:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                for link in soup.find_all('a'):
                    href = link.get('href')
                    if href and '#' not in href and 'javascript' not in href:
                        all_urls.append(href)

                for i in range(len(all_urls)):
                    if all_urls[i] != None and len(all_urls[i]) > 0:
                        if '#' not in all_urls[i] and 'javascript' not in all_urls[i]:
                            if all_urls[i] is not None and all_urls[i][0] == '/':
                                all_urls[i] = url + all_urls[i]
                # Removes duplicates
        all_urls = list(set(all_urls))
        return all_urls

    def get_subdomains(self, urls, domain_name):
        all_subdomains = []
        for url in urls:
            if url != None:
                if f'.{domain_name}' in url:
                    if 'https://' in url:
                        subdomain = re.findall(
                            rf'https://(.*?)\.{re.escape(domain_name)}', url)
                        if subdomain:
                            if subdomain[0] != 'www':
                                if subdomain[0] != 'next':
                                    all_subdomains.append(url)
        all_subdomains = list(set(all_subdomains))
        return all_subdomains

    def filtered_urls(self):
        filtered_urls = []
        for url in self.all_urls:
            if self.domain_name in url:
                filtered_urls.append(url)
        return filtered_urls
