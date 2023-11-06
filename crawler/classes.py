##
#   A class Job.
##

class Job:
    def __init__(self, title, url, descr, category, lvl):
        self.title = title
        self.url = url
        self.category = category
        self.descr = descr
        self.lvl = lvl

        # This defines how the class job should be printed.
    def __str__(self):
        return f"""
            Job Title:{self.title}\n\n
            Description:\n{self.descr}\n\n
            URL: {self.url}\n\n
            Category: {self.category}\n\n
            Level: {self.lvl}\n"""
            HEHEHE
