#!/home/ippolit/anaconda3/bin/python
import os
import re
import cgi
import cgitb
import subprocess
cgitb.enable()
form = cgi.FieldStorage()
query = form.getfirst("query", "Query not defined")
src = form.getfirst("src", "Source not defined")
#pwd : /BigData-Labs/Lab4
os.system('"./cgi-bin/test_json.sh" %s %s' % (query, src))
