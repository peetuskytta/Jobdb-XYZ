# Crawler
Python job posting webcrawler to list interesting job postings.

To create the virtual environment use this: `python3 -m venv myenv`

To activate the virtual environment use this `source myvenv/bin/activate`

To deactivate the virtual use this `deactivate`

## Init script

Let's have a script that would be run to install the above venv and libraries required by the project?


## To-Do
To-Do:
	1. get all the duunitori pages with keywords: software developer, system specialist, ohjelmoija, etc. to be parsed and printed out to stdout.
	2. Send the revelant info to a file.
	3. Use further parsing and choose what interests you.
	4. next steps?
	7. Ales: Build a working email service. Also install python and all needed libraries and keep them up to date. Needs to keep admins (ale and peetu) up to date in case of errors (404)
	8. Study web _crawler detectors_!


Notes:
--	https://realpython.com/beautiful-soup-web-scraper-python/
--	study webcrawler detectors
--	consider possibility of being able to communicate with the program via email to change and update desired keywords
-- Let's use also "rule out"-rules to filter out these kind of surprises: https://duunitori.fi/tyopaikat/tyo/lavistajalevytyostokoneen-ohjelmoija-scsar-16832014 (löytyi koska sana ohjelmoija)

Peetu Notes:
-- Peetu = best
-- added folder called database where all required databases would be created.

Ale Notes:
-- Ale = Bestest

BEST PRACTISES:
--	always `git branch` to check on which branch you're on to avoid mistakes
--	always `git pull` first on main branch before making any changes
--	you can check new Notes by using `git checkout <branch>` without having to merge
--	need to change last commit message? use `git commit --amend`

Things done:
	5. Ales: URl-generator. Function that generates valid url from a file that includes wanted job titles
	6. Ales: Research and setup free server.
=======
Authors: Asukava & Pskytta, Hive Helsinki Alumni
## What?
A web crawler written in Python and using the following:
- beautifulsoup (for HTML parsing)
- SQLite (for database)
- flask (web app framework)

## Why?
Idea is to have a simple web app that we could use through browser to find 5 or more positions
where we could apply to daily.
## What does it do?
- Crawls through a job listing website in search for job postings for
=======
Authors: Asukava & Pskytta, Hive Helsinki students

### What?
A Python web crawler / web app to search the database for IT job postings.

### What does it do?
- crawls through a job listing website in search for job postings for
>>>>>>> 4704cc5945e54bb229806675f54a7802dbf5acaf
software developer roles.
- it is run once a day and it updates SQLite database with new listings it finds.
- database is accessible via web app at ip: `129.151.211.126`

### Deployment
- Deployed on a Oracle Cloud running Oracle Linux Server 8.8.

Steps we took with the server:
1. setup users and home folders for both of us.
2. connect to the server via SSH.
3. write scripts to update the server.
4. create a group for both users to facilitate permission handling.
6. setup proper security lists in Oracle to enable internet traffic.
8. setup Apache, pip3 and WSGI
9. setup proper firewall rules
10. set crontab for the crawler to update the database once a day.

## What we used
- Python
    - Flask framework
    - SQLite
- Oracle Cloud Infrastructure
- Linux
    - Apache webserver setup
    - WSGI
    - firewall
    - managing system users and permissions
- SSH
- Bash
- Git

## Useful Information

In case you wish to clone the project we recommend Linux as the operating system.

To create the virtual environment use `python3 -m venv myenv`

To activate the virtual environment use `source myvenv/bin/activate`

To deactivate the virtual environment use `deactivate`

To install the required libraries use `sudo pip install bs4 requests`
=======
## To-Do

- automation for cleaning the database of old job postings.
- simplify the code for easier expansion.
- expand crawling to other websites (requires the item above).
- a way to filter intern, junior, senior positions
    - requires new SQL database COLUMN
- start using https instead of http
- database backup and recovery
    - add logic to the code to identify if the database is being altered/cleaned and use
      the backup instead (during the 00:00 - 04:00 hours)
- design simple and more modern frontend
### Done

- Added database request logging to the app which stores timestamp and IP address to the server side log
- Database backup script added and set on root crontab to run once a day
