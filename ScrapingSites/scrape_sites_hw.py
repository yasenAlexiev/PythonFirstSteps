# TASK: Import any libraries you think you'll need to scrape a website.
import bs4
import requests

# TASK: Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/
# and get the HMTL text from the homepage.

url = "http://quotes.toscrape.com/"
req_quotes = requests.get(url)


# TASK: Get the names of all the authors on the first page.
def get_authors(soup):
    result = set()
    authors = soup.select(".author")
    for author in authors:
        result.add(author.text)

    return result


soup = bs4.BeautifulSoup(req_quotes.text, "lxml")
print(get_authors(soup))


# TASK: Create a list of all the quotes on the first page.


quotes_tags = soup.select(".text")
quotes = [quote.text for quote in quotes_tags]
print(quotes)


# TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown
# on the top right from the home page (e.g Love,Inspirational,Life, etc...).
# HINT: Keep in mind there are also tags underneath each quote, try to find a class only present in the top right tags,
# perhaps check the span.

top_ten_tags = soup.select(".tag-item")
for tag in top_ten_tags:
    print(tag.text)


# Use what you know about for loops and string concatenation to loop through all the pages
# and get all the unique authors on the website.

url_with_pages = "https://quotes.toscrape.com/page/{}/"
page = 1
unique_authors = set()
while True:
    page_req = requests.get(url_with_pages.format(page))

    soup = bs4.BeautifulSoup(page_req.text, "lxml")
    unique_authors = unique_authors.union(get_authors(soup))

    if len(soup.select(".next")) == 0:
        break

    page += 1

print(unique_authors)