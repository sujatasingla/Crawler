#!/usr/bin/python

import cgi
import codecs
import sys
from boilerpipe.extract import Extractor

form = cgi.FieldStorage()

URL= form["URL"].value
File_path = form["File"].value
save_file=codecs.open("/home/sujata/reviews/"+ File_path +".txt","w","utf8")
extractor = Extractor(extractor='ArticleExtractor', url=URL)
save_file.write(extractor.getText())
save_file.close()

print "Content-Type: text/html\n\n"
print ""
print "<html>"
print "<h2>CGI Script Output</h2>"
print "<p>"
print "The user entered data are:<br>"
print "<b>URL:</b> " + form["URL"].value + "<br>"
print "<b>File Name:</b> " + form["File"].value + "<br>"
print "<b>File Saved Succesfully</b>" "<br>"
print "</p>"
print "</html>"


