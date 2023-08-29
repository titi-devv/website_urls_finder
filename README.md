# Website URLS Finder 🕷️

This Python script is a spider web crawler designed to extract URLs and subdomains from a given starting URL. It uses the `requests` library to fetch web pages, `BeautifulSoup` for HTML parsing, and regular expressions to extract relevant information.

## Getting Started 🚀

1. Make sure you have Python installed.

2. Install the required packages using the following command: `pip install -r requirements.txt`

3. Clone this repository.

## Usage

Run the `index.py` script with the URL you want to start crawling from as a command-line argument. For example:

```bash
python index.py https://example.com
```

The script will initiate the crawling process and extract URLs and subdomains related to the provided starting URL. It will then filter and save the results as a JSON: `/example.json`.

## Features 🛠️

Extracts URLs and subdomains from a starting URL.
Filters out irrelevant URLs and subdomains such as JavaScript links and anchor tags.
Removes duplicate URLs.
Displays extracted and filtered URLs.
Customization
You can modify the behavior of the script by adjusting the regular expressions or by extending the class to include additional functionality.

## Credits 🙌

The script utilizes the requests library for making HTTP requests: Requests
HTML parsing is performed using BeautifulSoup: BeautifulSoup
Regular expressions are used for URL extraction and manipulation.

## License 📄

This project is licensed under the MIT License.

## Author 👤

- [titi]
