##
# 	Add any new classes to this file.
##

class Job:
    def __init__(self, title, id, url, description, category):
        self.id = id
        self.title = title
        self.url = url
        self.category = category
        self.description = description

	# This defines how the class job should be printed.
    def __str__(self):
        return f"ID: {self.id}\nJob Title: {self.title}\n\nDescription:\n{self.description}\n\nURL: {self.url}\n\nCategory: {self.category}"
