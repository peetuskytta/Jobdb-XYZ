# Crawler
Python job posting webcrawler to list interesting job postings.

To create the virtual environment use this: `python3 -m venv myenv`

To activate the virtual environment use this `source venv/bin/activate`

To deactivate the virtual use this `deactivate`

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

Peetu Notes:
-- Peetu = best
-- Updated the logic for saving the relevant data of a job. Useful when deciding and ranking the jobs.

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
