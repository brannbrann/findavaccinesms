Forked from https://github.com/burgamacha/CVS-covid-vaccine-checker

Great little script that scrapes the CVS website looking for available appointments in your area.

This script keeps the simplicity of the original and adds the ability to send SMS/EMAIL to the 
results.

Requires requests:

1. pip install requests

Since I could not install beepy on a Win10 machine, I chose to have it send a TXT/SMS/EMAIL (thanks Ajay!). You
can also add the ability to send to a Slack channel, if desired.

Everything you need to do this is, outside of requests, is already included with Python3.

To enable sending to Gmail, you should create a new Gmail account. Make note of the new
email address and password. Add those to the script where appropriate. You will also need to enable 
'allow less secure apps' in your Gmail settings to get email flowing.

Just a note on SMS email gateways, there is a comprehensive, worldwide I might add, list here:
https://github.com/typpo/textbelt

Next, the hardcoded 'defaults' for will be different for you.

The state and cities variables should be changed. If you live in the Bay Area, the cities shown
are within 50km of San Francisco. You may need to update the values. I used freemaptools.com to get
the list of cities and compared them to what CVS provides based on state/cities. Update fields as
you see fit.

It would be easy to daemonize the run, however, the time functions would probably need a separate 
thread.