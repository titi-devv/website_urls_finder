import requests
import json
import sys
from crawler import SitemapFinder, WebCrawler, get_domain_name

"""
# Find a format every URLs from sitemaps
This is a tool developed by Thibot

It will find your sitemap file. It will take few seconds.
"""


def main(url):
    domain_name = get_domain_name(url)

    if domain_name:
        print(f"Extracted domain: {domain_name}")
        try:
            if requests.get(url).status_code == 200:
                # sitemap_finder = SitemapFinder(url)
                # urls = sitemap_finder.get_all_urls
                # if len(urls) == 0:
                crawler = WebCrawler(url)
                print('crawler')
                urls = crawler.get_all_urls

                urls = {
                    "urls": urls
                }
                with open(f"{domain_name}.json", 'w') as json_file:
                    json.dump(urls, json_file)
                print('urls', urls)
        except:
            print('Error')
    else:
        print("Domain not found in the URL.")


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
