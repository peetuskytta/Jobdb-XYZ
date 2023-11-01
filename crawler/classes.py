##
#   A class Job.
##

class Job:
    def __init__(self, title, id, url, description, category, level):
        self.id = id
        self.title = title
        self.url = url
        self.category = category
        self.description = description
        self.level = level

        # This defines how the class job should be printed.
    def __str__(self):
        return f"""ID: {self.id}\n
            Job Title:{self.title}\n\n
            Description:\n{self.description}\n\n
            URL: {self.url}\n\n
            Category: {self.category}\n\n
            Level: {self.level}"""
