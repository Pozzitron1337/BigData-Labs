#!python 3.8.3
#!OS Linux ippolit-PC 5.0.0-32-generic #34~18.04.2-Ubuntu SMP Thu Oct 10 10:36:02 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

import os
import re
import time
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError

rss_links_given=[
    "https://habr.com/ru/rss/all/all/?fl=ru",
    "https://3dnews.ru/news/rss/",
    "https://www.mobile-review.com/news/feed/",
    "https://techtoday.in.ua/feed",
    "https://pcnews.ru/feeds/latest/news/",
    "https://pcnews.ru/feeds/latest/articles/",
    "https://ko.com.ua/rss.xml/",
    "https://ko.com.ua/rss/article",
    "https://www.helpnetsecurity.com/feed/",
    #"https://www.itweek.ru/rss/" даний rss містив погані дані,тому був вилучений
    ]

rss_links_my=["http://feeds.feedburner.com/Itcua?format=xml",
              "https://ichip.ru/out/rss/main/main.xml"]

rss_links=rss_links_given + rss_links_my

def get_rss_feeds_using_os():
    iteration=0;
    for link in rss_links:
        file_name=str(iteration)+"_"+re.match(r"http[s]*://([\w.]*)",link).group(1)+"_"+str(time.asctime()).replace(" ","_")+".xml";
        os.system("curl -o "+"rss_feeds/"+file_name+" "+link);
        iteration+=1;


def union_all_feeds():
    items=ET.Element('items')
    itemList=[]
    for (_, _, filenames) in os.walk("rss_feeds"):
        for filename in filenames:
            print(filename)
            try:
                tree=ET.parse("rss_feeds/"+filename);
            except ParseError:
                continue;
            root = tree.getroot() 
            for item in root.findall('./channel/item'):
                newitem=ET.SubElement(items,'item')
                itemList.append(newitem)
                for component in item: 
                    #print(component.tag)
                    #print(str(component.text))
                    newcomponent=ET.SubElement(newitem,component.tag)
                    newcomponent.text=component.text
        final=ET.tostring(items, encoding='utf8', method='xml').decode('utf-8')
        file=open("rss_feeds.xml","a")
        file.write(final);
        file.close();

get_rss_feeds_using_os()
union_all_feeds()

