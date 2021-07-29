import jsonpickle
from model.group import Group
import random
import string
import os.path
import getopt
import sys

try:
    opts, arg = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits
    return prefix + "".join(random.choice(symbol) for i in range(random.randrange(maxlen)))


testdata = [Group(namegroup="", header="", footer="")] + [
    Group(namegroup=random_string("group_name", 2), header=random_string("Zagolovok", 5), footer=random_string("Podval", 5))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
