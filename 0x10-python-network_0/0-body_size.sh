#!/bin/bash
# script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
URL="http://daf2007ee0ed.e0e9d352.hbtn-cod.io:5000"
curl -sI $URL | grep -i Content-Length | awk '{print $2}'
