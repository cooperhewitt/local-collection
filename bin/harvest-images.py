#!/usr/bin/env python

##
##
## This script simply downloads all the "b" images available in the Cooper Hewitt Collection
## and places them all in an images folder within the same repo
## 
##

import os
import sys
import json
import requests
import shutil

if __name__ == '__main__':
    
    whoami = os.path.abspath(sys.argv[0])
    bindir = os.path.dirname(whoami)
    root = os.path.dirname(bindir)

    ## assumes your collection repository in clones alongside this one. As in:    
    ## .
    ## ..
    ## collection
    ## this-repo
    
    collection = os.path.dirname(root)
    collection = os.path.join(collection, 'collection')

    objects = os.path.join(collection, 'objects')

    for root, dirs, files in os.walk(objects):

        for f in files:
            path = os.path.join(root, f)
            data = json.load(open(path, 'r'))
            images = data['images']
            
            for i in images:
                b = i['b']
                url = b['url']
                filename = url.split('/')[-1]

                ## if file already exists, skip it
                if os.path.exists('../images/' + filename):
                    continue
                    
                print "Processing object: " + data['id'] + " and image: " + url
                
                r = requests.get(url, stream=True)
                with open('../images/' + filename, 'wb') as out_file:
                        shutil.copyfileobj(r.raw, out_file)
                del r
                        
                        
                        
                    
