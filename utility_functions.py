##
#	Contains useful functions for the project.
#
#	Aleksi, you can add new functions here.
#	When you need the function use the import utility
#	in the file you want to use the function.
##

from classes import Job

def save_job(data, url):
    print(data)
    exit()
    a_ref = data.find('a')
    job_id = a_ref.get('data-id')
    job_link = url + a_ref.get('href')
    new_job = Job("Jobi", job_id, job_link)
    print(new_job)
    return new_job