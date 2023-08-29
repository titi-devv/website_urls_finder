# Website URLS Finder 🕷️

This Python script is a spider web crawler designed to extract URLs and subdomains from a given starting URL. It uses the `requests` library to fetch web pages, `BeautifulSoup` for HTML parsing, and regular expressions to extract relevant information.

## Getting Started 🚀

1. Make sure you have Python installed.

2. Clone this repository: `git clone https://github.com/thib-web3/website_urls_finder.git`
   
3. Go in the root folder: `cd website_urls_finder`
   
4. Install the required packages using the following command: `pip install -r requirements.txt`.

## Usage 📋

Run the `index.py` script with the URL you want to start crawling from as a command-line argument. For example:

```bash
python index.py https://example.com
```

The script will initiate the crawling process and extract URLs and subdomains related to the provided starting URL. It will then filter and save the results as a JSON: `/example.json`.

## Features 🛠️

- Extracts URLs and subdomains from a starting URL.
- Filters out irrelevant URLs and subdomains such as JavaScript links and anchor tags.
- Removes duplicate URLs.
- Save locally extracted and filtered URLs.

## Credits 🙌

- The script utilizes the `requests` library for making HTTP requests: [Requests](https://docs.python-requests.org/en/master/)
- HTML parsing is performed using `BeautifulSoup`: [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- Regular expressions are used for URL extraction and manipulation.

## License 📄

This project is licensed under the MIT License.

## Author 👤

- [titi]
