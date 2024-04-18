Authors: Asukava & Pskytta, Hive Helsinki (soon to be Alumni)

### What?
jobdb == Job Database

A web app for IT job postings in Finland.
It has a crawler which updates the database daily.

### What does it do?
- Crawls through a job listing websites in search for job postings for software developer roles. It is run once a day and it updates SQLite database with new listings it finds.
- Search engine is accessible at --> www.jobdb.xyz

### Deployment
- Deployed on a Oracle Cloud instance running Ubuntu 22.04 LTS.
- Domain name by GoDaddy
- SSL Certificate by Certbot
- Nginx webserver

### Git Clone and stuff
After cloning the project:

1. Run the following command to create a virtual environment:
   
`python -m venv myenv`

2. Run this to activate the environment:

`source myvenv/bin/activate`

3. Run this to install the requirements:

`pip install -r requirements.txt`

## To-Do
- ~~automation for cleaning the database of old job postings.~~
- ~~simplify the code for easier expansion (ongoing)~~
- ~~expand crawling to other websites (requires the item above).~~
- ~~a way to filter intern, junior, senior positions~~
    - ~~requires new SQL database COLUMN~~
- ~~start using https instead of http~~
    - ~~requires a domain name (when using Let's Cert Certbot)~~
- ~~database backup and recovery~~
- ~~design simple and more modern frontend~~
- Facelift
    - filters for job level
- Backend logic
    - improve job level identification
- Devops
    - Github Actions to trigger deployment when branch is merged to main (webhook?)
- System
    - rewrite database backup script
    - organize all project related scripts to one folder
    - documentation for cron jobs happening
    - more filters for malicious GET|POST requests
    - IP Blacklist
