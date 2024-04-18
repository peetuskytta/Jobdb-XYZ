Authors: Asukava & Pskytta, Hive Helsinki (soon to be Alumni)

### What?
A web app for IT job postings in Finland.
It has a crawler which updates the database daily.

### What does it do?
- Crawls through a job listing websites in search for job postings for software developer roles. It is run once a day and it updates SQLite database with new listings it finds.
- Search engine is accessible at --> www.jobdb.xyz

### Deployment
- Deployed on a Oracle Cloud running Ubuntu 22.04 LTS.
- Domain name by GoDaddy
- SSL Certificate by Certbot
- Nginx webserver

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
