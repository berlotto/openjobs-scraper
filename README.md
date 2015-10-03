# openjobs-scraper

This code is an example for use Scrapy 1.x to create a webcrawler simply.

This example save all data in one RethinkDB database.

## Envorinment

Use the virtualenv:

```
$ mkvirtualenv scrapy
$ pip install rethinkdb scrapy
```

Create the database:

```
$ python vagascrawler/createdb.py
```

after, run the spider to collect all data and save at DB

```
$ scrapy scrawl openjobs
```
