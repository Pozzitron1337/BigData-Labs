#!/home/ippolit/anaconda3/bin/python
import sys
import re
import datetime

t = sys.stdin.read()
print("Content-type: text/html; charset=utf-8\n\n<html><body bgcolor=yellow>")
print("<p>"+t+"</p>")
json =t.split('\n')
t=""

for i in range(len(json)):
    t=t+" "+json[i]
t=re.sub('^\s','',t)
total = re.findall('\"total\" : (\d+),', t)
print("<b>Found: "+total[0]+"</b><hr><ol>")
title = re.findall('"title" : "(.*?)",', t)
text = re.findall('"textBody" : "(.*?)",', t)
url = re.findall('"URL" : "(.*?)"', t)
for j in range(len(title)):
    doc_ind=j+1
    print("<li><b>"+": "+title[j]+"</b>")
    print("<br>"+text[j])
    print("<br><i>"+url[j]+"</i><br /><hr>")

print("</ol></body></html>")