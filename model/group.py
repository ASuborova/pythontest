class Group:
    def __init__(self, namegroup=None, header=None, footer=None, id=None):
        self.namegroup = namegroup
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.namegroup)

    def __eq__(self, other):
        return self.id == other and self.namegroup == other

