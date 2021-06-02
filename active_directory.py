class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def __str__(self):
        return f"{self.name}, {self.groups}, {self.users}"

    def __repr__(self):
        return f"{self.name}, {self.groups}, {self.users}"


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    users = group.get_users()
    if user in users:
        return True
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# print(parent)

def test_function1(parent, child):
    if child in parent.get_groups():
        print("PASS")
    else:
        print("FAIL")


def test_function2(child, sub_child):
    if sub_child in child.get_groups():
        print("PASS")
    else:
        print("FAIL")


test_function1(parent, child)
test_function2(parent, child)