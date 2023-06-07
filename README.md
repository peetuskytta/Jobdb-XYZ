# Crawler
Python job posting webcrawler to list interesting job postings.
Authors: Asukava & Pskytta, Hive Helsinki Alumni

In case you wish to clone the project we recommend Linux as the operating system.

To create the virtual environment use `python3 -m venv myenv`

To activate the virtual environment use `source myvenv/bin/activate`

To deactivate the virtual environment use `deactivate`

To install the required libraries use `sudo pip install bs4 requests`

To install other utilities use `sudo apt install sqlite3 sqlbrowser`
- We chose sqlite3 as it is easy to use and we gain SQL and database experience.
- Browsing the database is useful so we decided to use `sqlbrowser` for graphic representation of the database. We are also using terminal commands with the `sqlite` to get familiar with querys.

## Init script

Let's have a script that would be run to download required libraries and maybe even create the virtual environment.
-- TO BE DONE later --

## To-Do
To-Do:
	- Use further parsing for the job_link to cherry-pick based on user input.
	- Job titles that have been sent to you would not be sent again, so some kind of control for that?
	- Further develop data relationships between user and jobs table (foreign key consept)

## DONE
	- get all the duunitori pages with keywords: software developer, system specialist, ohjelmoija, etc. to be parsed and printed out to stdout.
	- Store relevant info to a database.
	- Ales: URl-generator. Function that generates valid url from a file that includes wanted job titles


Notes:
--	https://realpython.com/beautiful-soup-web-scraper-python/
--	study webcrawler detectors
--	consider possibility of being able to communicate with the program via email to change and update desired keywords
--

Peetu Notes:
-- Peetu = best
-- added folder called database where all required databases would be created.
-- Database created
-- collect also the destination "apply"-link and check if it is 404 or not.
-- collect info about level (junior, medior, senior) and insert it to the DB

Ale Notes:
-- Ale = Bestest

BEST PRACTISES:
--	always `git branch` to check on which branch you're on to avoid mistakes
--	always `git pull` first on main branch before making any changes
--	you can check new Notes by using `git checkout <branch>` without having to merge
--	need to change last commit message? use `git commit --amend`