import os
import subprocess
import time
import re

def prepare_items(filepath):
    file=open(filepath,'r')
    text=file.read()
    items=text.split('},\n')
    for i in range(len(items)):
        items[i]=items[i]+'}'
    return items

def start_elastic():
    logs=open("logs.txt","w")
    elastic=subprocess.Popen(["../elasticsearch-7.11.1/bin/elasticsearch"],stdout=logs)
    return elastic

def stop_elastic(elastic):
    elastic.kill()
    time.sleep(5)

def check_elastic_server():
    out=os.popen('curl -X GET http://localhost:9200/').read()
    while out.find('Failed to connect') > -1:
        print("Connection failed,trying again...")
        time.sleep(1)
        out=os.popen('curl -X GET http://localhost:9200/').read()
    print(out)

def init_all_items(filepath):
    #CRUD Operation: update
    items=prepare_items(filepath)
    for item in items:
        # print(item)
        # break
        # if item.find('&lt')>-1:
        #     continue
        command="curl -X POST 'http://localhost:9200/test/_doc/' -H 'Content-Type: application/json' -d '"+item+"'"
        os.system(command)

def get_items(url):
    command="curl -X GET "+url;
    os.system(command)

def delete_item(url):
    command="curl -X DELETE "+url;
    os.system(command)


if __name__ == "__main__":
    menu='''0.exit
1.start elastic
2.check elastic
3.stop elastic
4.write rss_feeds.json
    ''';
    elastic=None
    while True:
        print(menu)
        choise=int(input("Еnter your choise: "))
        if choise == 0:
            exit()
        if choise == 1:
            elastic = start_elastic()
        if choise == 2:
            check_elastic_server()
        if choise == 3:
            stop_elastic(elastic)
        if choise == 4:
            init_all_items('rss_feeds.json')
    #init_all_items('rss_feeds.json')
 