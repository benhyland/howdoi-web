#!/bin/sh

# for now, just mix it in with whatever else is deployed

scp -r ./cgi-bin/* root@bhyland.co.uk:/usr/lib/cgi-bin/

scp ./howdoi.html root@bhyland.co.uk:/var/www/
