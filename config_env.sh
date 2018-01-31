#!/bin/sh

hash pip 2>/dev/null || {
   echo >&2 "I require pip but it's not installed.  Aborting.";
   exit 1;
}

sudo pip install beautifulsoup4 urllib3
