import jsonpickle
from model.contact import Contact
import random
import string
import os.path
import getopt
import sys
# from data.contacts import testdata

try:
    opts, arg = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits
    address_email = ["@gmail.com", "@mail.ru", "@ya.ru"]
    number = string.digits
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    day = ["1", "2", "3", "4", "5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
    if prefix == 'email':
        return ("".join(random.choice(symbol) for i in range(random.randrange(maxlen)))
                + random.choice(address_email))
    elif prefix == 'number':
        return "".join(random.choice(number) for i in range(maxlen))
    elif prefix == 'bday':
        return "".join(random.choice(day))
    elif prefix == 'bmonth':
        return "".join(random.choice(month))
    return prefix + "".join(random.choice(symbol) for i in range(random.randrange(maxlen)))


testdata = [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            title=random_string("title", 10), companyname=random_string("companyname", 10),
            address=random_string("address", 50), homephone=random_string("number", 11),
            mobilephone=random_string("number", 11), workphone=random_string("number", 11),
            fax=random_string("number", 11), mainemail=random_string("email", 5), email2=random_string("email", 5),
            email3=random_string("email", 5), bday=random_string("bday", 2), bmonth=random_string("bmonth", 2),
            byear=random_string("number", 4), aday=random_string("bday", 2), amonth=random_string("bmonth", 2),
            ayear=random_string("number", 4))
            for i in range(n)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))


