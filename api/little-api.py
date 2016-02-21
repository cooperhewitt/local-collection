#!/usr/bin/env python

##
##
## This is a little Flask based API that serves JSON files stored in
## the collection repo.
##
##

import os
import sys
import json

from flask import Flask
from flask import request
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return "local-collection"

## Basic route to get object data by object id
@app.route('/objects/<object_id>')
def get_object(object_id):
    
    whoami = os.path.abspath(sys.argv[0])
    apidir = os.path.dirname(whoami)
    root = os.path.dirname(apidir)

    ## assumes your collection repository in clones alongside this one. As in:    
    ## .
    ## ..
    ## collection
    ## this-repo
    
    collection = os.path.dirname(root)
    collection = os.path.join(collection, 'collection')

    objects = os.path.join(collection, 'objects')

    path = id2path(object_id)
    objectdir = os.path.join(objects, path)
    filename = object_id + '.json'

    return send_from_directory(objectdir, filename, as_attachment=False)



def id2path(id):

    tmp = str(id)
    parts = []

    while len(tmp) > 3:
        parts.append(tmp[0:3])
        tmp = tmp[3:]

    if len(tmp):
        parts.append(tmp)

    return os.path.join(*parts)


if __name__ == "__main__":
    app.run()
