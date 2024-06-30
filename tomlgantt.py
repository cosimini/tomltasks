"""
A script to convert a TOML file to a list of tasks.
"""

import toml


class tomltasks:
    tasks_list_features = {"title": None, "start_day": None, "deadline": None, "notes": None, "shortnames": None}

    def __init__(self, filename):
        self.tasks = self.generate_times(self.parse_dict(toml.load(filename), []))

    def parse_dict(dic: dict, category: list) -> list:
        for k in dic.keys():
            pass
        return []

    def generate_times(tasks_list: list) -> list:
        pass
