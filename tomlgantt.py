"""
A script to convert a TOML file to a list of tasks.
"""

import toml


class tomltasks:
    tasks_list_features = {"title": str, "start_day": None, "deadline": None, "notes": str, "shortnames": dict}
    task_features = {}
    groups_features = {"g_name": str}

    def __init__(self, filename):
        self.tasks = self.generate_times(self.parse_dict(toml.load(filename), []))

    def parse_dict(dic: dict, category: list) -> list:
        level_dict = []
        for k in dic.keys():
            pass
        return level_dict

    def generate_times(tasks_list: list) -> list:
        pass
