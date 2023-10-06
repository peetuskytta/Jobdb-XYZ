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
software developer roles.
- It runs once a day and updates SQLite database with new listings it finds.
- There is also a web application that asks email and keywords from user. The
keywords are used to search database on the server for jobs matching those
keywords and returns title and a link to the job posting.

## Deployment
- Deployed on a Oracle Cloud running Oracle Linux Server 8.8. (Full deployment under construction)
Steps we took with the server:
1. create usernames and home folders for both of us.
2. connect to the server via SSH.
3. write scripts to update the server on midnight.
4. create a group for both users to facilitate permission handling.
5. install required services with `yum`
6.

## Useful Information

In case you wish to clone the project we recommend Linux as the operating system.

To create the virtual environment use `python3 -m venv myenv`

To activate the virtual environment use `source myvenv/bin/activate`

To deactivate the virtual environment use `deactivate`

To install the required libraries use `sudo pip install bs4 requests`
>>>>>>> 10088fd1003ce86ed985ff4bd341aa91bc4cddd6
