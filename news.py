import csv

import feedparser

import utils

javascript = ['javascript', '자바스크립트', 'angular', 'js']

with open('rss.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
    for row in spamreader:
        if len(row) > 1 and row[1] != '':
            parse = feedparser.parse(row[1])
            entries = parse.get('entries')
            for entry in entries:
                title = entry.get('title')
                updated = entry.get('updated')
                if utils.valid_date(updated):
                    print("true")
                # updated_date = utils.convert_to_date_obj(updated)
                # print(updated_date)
                # if title is not None and utils.contains_one_of_list(title, javascript):
                #     print("제목: {}, url: {}".format(entry['title'], entry['link']))



            # print(parse['feed']['link'])
            # response = requests.get(row[1])
            # tree = ET.parse(response.text)
            # root = tree.getroot()
            # events = ElementTree.iterparse(response.raw)

            # for child in root:
            #     print(child.title)

            # rss_data = BeautifulSoup(rss_url, "lxml")
            # print(rss_data)
            # tree = ET.parse(rss_data)
            # root = tree.getroot()
            # for child in root:
            #     print(child)

            # all_a = rss_data.find_all('', href=True)
            # d = feedparser.parse(rss_data)
            # print(d)

    print("end")


