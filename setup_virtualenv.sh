#!/bin/bash
if [ ! -d ".env" ]; then
    virtualenv .env &&
    source .env/bin/activate &&
    pip install -r requirements.txt &&
    nodeenv -p -r node-requirements.txt
else
    source .env/bin/activate
fi

