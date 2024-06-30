"""
A script to convert a TOML file to a list of tasks.
"""

import toml


class tomltasks:
    def __init__(self, filename=None):
        self.dic = toml.load(filename)
        self.tasks = self.generate_times(self.parse_dict(self.dic, []))

    def parse_dict(dic: dict, category: list) -> list:
        for k in dic.keys():
            if dic[k] is str and dic[k] == "name":  # Task found
                tasks_list.append(dic[k])
        return []

    def generate_times(tasks_list: list) -> list:
        pass
