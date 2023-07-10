import jsonpickle
from model.contact import Contact
from generator.group import random_string
import os

data = [Contact(firstname="", lastname="", middlename="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
          middlename=random_string("middlename", 10))
    for i in range(5)]

f = "data/contact_gen.json"
convert_json = jsonpickle.encode(data)

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out: out.write(convert_json)
