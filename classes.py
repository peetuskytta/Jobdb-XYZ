##
# 	Add any new classes to this file.
##

class Job:
    def __init__(self, title, id, url):
        self.id = id
        self.title = title
        self.url = url

	# This defines how the class job should be printed.
    def __str__(self):
        return f"ID: {self.id}\nJob Title: {self.title}\nURL: {self.url}\n"
