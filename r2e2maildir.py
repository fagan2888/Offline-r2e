#!/usr/bin/env python3
import sys, time
from email.parser import Parser
import mailbox

# Where is the (root) maildir folder located ?
rootfolder = '~/myMaildir/' 

# Where should I write error messages (sys.stderr will not work when run in background)
# Alternative is to import the logging module and write to syslog
error_file = '~/r2e-errors'
f = open(error_file, 'a')

# How do I map feeds to subfolders?
# This is a dictionary with the feed_url as the key and the subfolder as the value
labels = {
    "http://aswathdamodaran.blogspot.com/feeds/posts/default" : "B.FinEco.Aswath-Damodaran",
    "http://www.schneier.com/blog/index.rdf" : "B.M.Bruce-Schenier",
    "http://ftalphaville.ft.com/blog/?feed=rss2" : "B.NP.FT_Alphaville",
}

# behave like sendmail and read message from stdin
msg = sys.stdin.read()
# pick up the feed from the X-RSS-Feed header set by rss2email
feed = Parser().parsestr(msg)['X-RSS-Feed']
# some websites now automatically redirect http:// requests to https://
# so we check for http:// even if X-RSS-Feed says https://
feed2 = feed.replace('https://', 'http://') 
if feed in labels.keys():
    folder = labels[feed]
elif feed2 in labels.keys():
    folder = labels[feed2]
else:
# we have encountered a feed that we cannot handle because it is not
# there in labels so we write an error log and return a failure code
# to rss2email
    f.write(time.strftime("%d %b %y") +'\n' +
            'Not found:' + feed + '\n   AND  :' + feed2 + '\n' )
    sys.exit(1)

# add the message to the correct maildir subfolder
myfolder = rootfolder + folder
md = mailbox.Maildir(myfolder)
md.add(mailbox.Message(msg))
sys.exit(0)
