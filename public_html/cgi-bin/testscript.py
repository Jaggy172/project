#!/usr/local/bin/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<html><head><TITLE>CGI script output</TITLE></head>"
print "<body><H1>Form values</H1>"
print "<table><tr><th>Key</th><th>Value</th></tr>"

for k in form.keys():
        print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k])

print "<table>"

print "</body></html>"

cleandata={}
try:
    cleandata['sequence']=check_sequence(form['sequence'])
    ...
except Exception, e:
    do_error(e)

def  check_sequence(sequence):
     ....

def do_error(error):
    '''There has been an error, concentrate!'''
