import jsonpickle
from data.groups import Group
from generator.group import random_string
import os
import json
import getopt
import sys

obj = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 10),
          footer=random_string("footer", 10))
    for i in range(5)]


# obj = Group(name="name_gen", header="header_gen", footer="footer_gen")
f = "data/group_gen.json"
n = 5

convert_json = jsonpickle.encode(obj)

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(convert_json, default=lambda x: x.__dict__, indent=2))
