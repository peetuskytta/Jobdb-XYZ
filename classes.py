##
# 	Add any new classes to this file.
##

class Job:
    def __init__(self, title, id, url):
        self.title = title
        self.id = id
        self.url = url

	# This defines how the class job should be printed.
    def __str__(self):
        return f"Job: {self.title}\nID: {self.id}\nURL: {self.url}\n"
