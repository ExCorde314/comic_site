# Comic Website

[![Build Status](https://travis-ci.org/ExCorde314/comic_site.svg?branch=stylization)](https://travis-ci.org/ExCorde314/comic_site)

This repository contains the code for the django web application for my comic site, comediccat.com. The web application is a django web server served by gunicorn. A NGINX server acts as a public facing reverse proxy.

## Tools Employed

Below are the following tools used:

+ Docker
+ NGINX
+ Travis-CI
+ Selenium
+ Python 3
+ Django 2.0
+ 

### Testing

Below is the command for running the selenium tests on windows:

`python3 selenium_tests/selenium_tests.py --driver='./selenium_tests/chromedriver.exe'`

or on linux:

`python3 selenium_tests/selenium_tests.py --driver='./selenium_tests/chromedriver'`

