from bs4 import BeautifulSoup
import requests
import csv

# with open('simple.html', 'r') as f:
#     soup = BeautifulSoup(f, 'lxml')

# this would print the whole document
# print(soup)
# this method add indentation
# print(soup.prettify())

# Access the text of the title tag
# match = soup.title
# match = soup.title.text
# print(match)

# Returns the first div on the page with its child elements
# div = soup.div
# print(div)

# find the div with a class_ of footer and return it
# div = soup.find('div', class_='footer')
# print(div)


# RETURN ALL THE TITLE OF ARTICLES
# articles = soup.find_all('div', class_='article')
# # print(article)
#
# for article in articles:
#     # get the headline (title)
#     headline = article.h2.a.text
#     print(headline)
#     # get the summary
#     summary = article.p.text
#     print(summary)
#     print()

# GET REAL DATA FROM https://coreyms.com/

# get the html of the website
source = requests.get("https://coreyms.com/").text
soup = BeautifulSoup(source, 'lxml')
# create CSV
csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["headline", "summary", "video link"])

for article in soup.find_all('article'):
    # get the headline
    headline = article.h2.a.text
    print(headline)
    # get the summary text
    summary = article.find("div", class_="entry-content").p.text
    print(summary)
    # we can access the attributes like a dictionary in python
    try:
        vid_src = article.find("iframe", class_="youtube-player")['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        # get the link
        yt_link = f"https://youtube.com/watch?v={vid_id}"
    except TypeError:
        yt_link = None

    # if it's succeded print the youtube link
    print(yt_link)
    print()

    csv_writer.writerow([headline, summary, yt_link])

# close FILE
csv_file.close()

# SAVE TO CSV FILE
