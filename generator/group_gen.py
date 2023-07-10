import jsonpickle
from data.groups import Group
from generator.group import random_string
import os

data = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 10),
          footer=random_string("footer", 10))
    for i in range(5)]

f = "data/group_gen.json"
convert_json = jsonpickle.encode(data)

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out: out.write(convert_json)
