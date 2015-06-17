# Offline-r2e
## patched rss2email + webmail + offlineimap + maildir email client = online cum offline feed reader
[rss2email](http://www.allthingsrss.com/rss2email/) can converts rss feeds into emails but this works well only if are running a mail server. Offline-r2e works by patching rss2email to use a custom python script instead of sendmail to send emails. The custom python script r2e2maildir.py writes the emails to a local [maildir](https://en.wikipedia.org/wiki/Maildir) folder instead of sending the email out via smtp or sendmail. We can then use [offlineimap](http://offlineimap.org/) to upload the saved emails to our favourite cloud email provider via [IMAP](https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol). The result is an online feed reader. For an offline feed reader, we can use any maildir compatible email client to read the local maildir folder.

This repository contains the custom python script r2e2maildir.py and a file patch-rss2email giving instructions on patching rss2email.py

For more details about the motivation for this project and the approach see my blog post.
