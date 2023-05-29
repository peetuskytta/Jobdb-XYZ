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
	5. Ales: URl-generator. Function that generates valid url from a file that includes wanted job titles


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