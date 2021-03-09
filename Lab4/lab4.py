import os
import subprocess
import time
import re
import cgi


def start_elastic():
    elastic_logs=open("elastic_logs.txt","w")
    elastic=subprocess.Popen(["../elasticsearch-7.11.1/bin/elasticsearch"],stdout=elastic_logs)
    return elastic

def stop_elastic(elastic):
    elastic.kill()
    time.sleep(5)

def start_server():
    server_logs=open("server_logs.txt","w")
    server=subprocess.Popen(["python3 -m http.server --cgi"],stdout=server_logs)
    return server

def stop_server(server):
    server.kill()
    time.sleep(5)

if __name__ == "__main__":
    menu='''0.exit
1.start elastic
2.stop elastic
3.check_elastic
4.start server #server will be located on http://localhost:8000
5.stop server
    ''';
    elastic=None
    server=None
    while True:
        print(menu)
        choise=int(input("Еnter your choise: "))
        if choise == 0:
            exit()
        if choise == 1:
            elastic = start_elastic()
        if choise == 2:
            stop_elastic(elastic)
        if choise == 3:
            check_elastic_server()
        if choise == 4:
            server=start_server()
        if choise == 5:
            stop_server(server)