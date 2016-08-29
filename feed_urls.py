import requests
from bs4 import BeautifulSoup
from feedfinder2 import find_feeds

source_url = "https://github.com/sarojaba/awesome-devblog/blob/master/README.md"

"""
1. source_url에서 a 태그 리스트 모두 가져오기
2. 각 사이트의 rss가 있는지 검사
3. rss가 있다면 미리 준비된 키워드가 포함된 최근 일주일 안에 올라온 글이 있는지 검사해보고 있으면 url 가져옴
4. 각 url 글과 제목만 가져와서 email로 쏜다.
5. 최대 50개 정도가 좋을듯
"""


def get_available_urls(source_url):

    html = requests.get(source_url).text
    soup = BeautifulSoup(html, "lxml")

    all_a = soup.find_all('a', href=True)
    github_domain = "github.com"

    return [a['href'] for a in all_a if a['href'] is not None
            and len(a['href']) > 0 and github_domain not in a['href']
            and a['href'][0] != "/" and a['href'][0:4] == "http"]


# def convert_rss_feed_url(urls):
#     return urls
#     ret_list = []
#     for url in urls:
#         rss_urls = find_feeds(url)
#         if rss_urls is not None and len(rss_urls) > 0:
#             ret_list.append(rss_urls[0])
#     return ret_list


available_urls = get_available_urls(source_url)

for u in available_urls:
    feed_urls = find_feeds(u)
    print("{},{}".format(u, feed_urls[0] if feed_urls is not None and len(feed_urls) > 0 else ''))
