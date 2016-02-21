## local-collection

This is a set of tools and scripts to make the process of creating a local copy of the Cooper Hewitt collection data a little easier.

To make use of this repository do the following:

1. Clone the [collection](http://github.com/cooperhewitt/collection) repo alongside this one.
2. Run scripts from within the /bin directory
3. Place these two repos somewhere that has a lot of disk space if you plan to harvest all the images
4. Use pip install -r requirements.txt to install any dependancies
5. Use python 2.7

Your directory stucture should look like the following

    .
    ..
    collection
    local-collection (this repo)


### Utils

* bin/harvest-images.py - does what it sounds like. It downloads all the "b" resoltuion images for each object in the collection.

### API

This repo contains a [Flask](http://flask.pocoo.org) based API which can serve JSON files found in the collection repo. It doesn't do much else at the moment.

To run the API:

    $ cd api
    $ python little-api.py

Then to try it go to http://127.0.0.1:5000/objects/152749803

