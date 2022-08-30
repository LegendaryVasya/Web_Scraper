#Stage 2/5
# import requests
# import json
# from bs4 import BeautifulSoup
#
# # Making a get request
# url = input()
# response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
#
# # print response
# if response and 'imdb 'and 'title' in url:
#     soup = BeautifulSoup(response.content, 'html.parser')
#     film_dict = {'title': soup.find('h1').text, 'description': soup.find('span', {'data-testid': 'plot-l'}).text}
#     # json_str = json.dumps(dic)
#     print(film_dict)
# else:
#     print('Invalid movie page!')


# #Stage 3/5
# import requests
#
# url = input()
# r = requests.get(url)
# if r:
#     page_content = r.content
#     file = open('source.html', 'wb')
#     file.write(page_content)
#     print('Content saved.')
# else:
#     print(f'The URL returned {r.status_code}!')


# #Stage 4/5
#
# import requests
# from bs4 import BeautifulSoup
# import string
#
# DMN = "https://www.nature.com"
# url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
#
# r = requests.get(url)
#
# if r:
#     soup = BeautifulSoup(r.content, "html.parser")
#     article = soup.find_all("article", {"class": "u-full-height c-card c-card--flush"})
#     for i in article:
#         if_news = i.find("span", {"class": "c-meta__type"}).text
#         if if_news == "News":
#             title = i.find("a", {"data-track-label": "link"}).text
#             print(title)
#             ttl = title.maketrans(" ", "_", string.punctuation)
#             filename = title.translate(ttl)
#             print(filename)
#
#             link = i.find("a").get("href")
#             art_link = DMN + link
#             new_req = requests.get(art_link)
#
#             new_soup = BeautifulSoup(new_req.content, "html.parser")
#             body = new_soup.find("div", {"class": "c-article-body u-clearfix"}).text.strip()
#             with open(f"{filename}.txt", "wb") as file:
#                 file.write(body.encode())
#
# else:
#     print(r.status_code)




#Stage 5/5
import requests
from bs4 import BeautifulSoup
import string
import os


DMN = "https://www.nature.com"
url = "https://www.nature.com/nature/articles"
n_page = int(input())
type_article = input()

for num_p in range(1, n_page + 1):
    payload = {"searchType": "journalSearch", "sort": "PubDate", "year": "2020", "page": "{}".format(str(num_p))}
    r = requests.get(url, params = payload)

    current_path = os.path.join(os.getcwd(), "Page_{}".format(str(num_p)))
    if not os.path.exists(current_path):
            os.mkdir(current_path)

    if r:
        soup = BeautifulSoup(r.content, "html.parser")
        article = soup.find_all("article", {"class": "u-full-height c-card c-card--flush"})
        for i in article:
            if_type = i.find("span", {"class": "c-meta__type"}).text
            if if_type == type_article:
                title = i.find("a", {"data-track-label": "link"}).text.strip()  # get title
                ttl = title.maketrans(" ", "_", string.punctuation)
                filename = title.translate(ttl)

                link = i.find("a").get("href")
                actual_link = DMN + link
                new_req = requests.get(actual_link)
                new_soup = BeautifulSoup(new_req.content, "html.parser")
                body = new_soup.find("div", {"class": "c-article-body u-clearfix"}).text.strip()

                try:
                    doc_name = os.path.join(current_path, "{}.txt".format(filename))
                    with open(doc_name, "wb") as file:
                        file.write(body.encode())
                        print('Saved all articles.')
                except OSError:
                        print("OSError occur")

    else:
        print(r.status_code)








# BeautifulSoup: working with HTML
# Health issues

# You are given a link to the WHO health topics. Read this link from the input, get all text paragraphs from all the a
# tags and single out the topic titles starting with the letter S. Print the final list. Beware of empty lines.
#
# For example, for this input and letter L (here we provide the link to the archive for consistency's sake):
#
# http://web.archive.org/web/20201201053628/https://www.who.int/health-topics
# the output should be:
#
# ["Landslides", "Lassa fever", "Leishmaniasis", "Leprosy", "Lymphatic filariasis"]
#
#
# Hint
#
# There is no need to overcomplicate the solution by difficult operations with tags, the problem can be solved by just
# going through the text paragraphs and picking the ones between Schistosomiasis and Sustainable Development Goals since
# these are the first and the last topics that should be in your list. Alternatively, you can go through a tags and check
# if the link inside href attribute contains the word topics or entity. If yes, save the text into the list.


# import requests
#
# from bs4 import BeautifulSoup
#
# letter = 'S'
# url = input()
#
# r = requests.get(url)
#
# list = BeautifulSoup(r.content, 'html.parser').find_all('a')
#
# blank_list = []
#
# for list_element in list:
#     if (list_element.text.startswith(letter) and len(list_element.text) > 1) and ('topics' in list_element.get('href') or 'entity' in list_element.get('href')):
#         blank_list.append(list_element.text)
# print(blank_list)
