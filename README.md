# tomltasks
A python library to visualize tasks described in a TOML file. Also produces Gantt charts.

# Usage
Create a TOML file describing the tasks, use test.toml as reference. The python class in tomlgantt.py loads the associated dictionary, creates a list of tasks from it with, automatically assign start and end time, and finally plots a Gantt chart.
