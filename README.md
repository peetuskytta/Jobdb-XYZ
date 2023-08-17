# Crawler
Authors: Asukava & Pskytta, Hive Helsinki Alumni
## What?
A web crawler written in Python.

## Why?
Idea is to have a simple web app that we could use through browser to find 5 or more positions
where we could apply to daily.
## What does it do?
- Crawls through a job listing website in search for job postings for
software developer roles.
- It runs once a day and updates SQLite database with new listings it finds.
- There is also a web application that asks email and keywords from user. The
keywords are used to search database on the server for jobs matching those
keywords and returns title and a link to the job posting.

## Deployment
- Deployed on a Oracle Cloud running Oracle Linux Server 8.8. (Full deployment under construction)

## Useful Information

In case you wish to clone the project we recommend Linux as the operating system.

To create the virtual environment use `python3 -m venv myenv`

To activate the virtual environment use `source myvenv/bin/activate`

To deactivate the virtual environment use `deactivate`

To install the required libraries use `sudo pip install bs4 requests`
