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

animal = Group("Animal")
mammals = Group("Mammal")
animal.add_group(mammals)

users = ['Cute_Bamboo', 'Big_Dog', 'Meow_cat', 'MR_Zebra']
animal.users = users

mammal_users = ['Mr_Bat', 'Human_race']
mammals.users = mammal_users


new_specie = Group("NEW SPECIE")


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


def test_function3(animal):
    if not animal.users:
        print("PASS")
    else:
        print("FAIL")


def test_function4(new_specie):
    if not new_specie.groups:
        print("PASS")
    else:
        print("FAIL")


def test_user_not_in_group(parent_group, user):  # add edge case checking user not in group
    if user in parent_group.users:
        print("PASS")
    else:
        print("FAIL")


def test_empty_user(parent_group):  # add edge case checking user not in group
    if parent_group.users:
        print("FAIL")
    else:
        print("PASS")


test_function1(parent, child)
test_function2(parent, child)
test_function3(animal)
test_function4(new_specie)


test_user_not_in_group(mammals, 'Cute_Bamboo')  # should FAIL
test_user_not_in_group(animal, 'Cute_Bamboo')  # should PASS
test_empty_user(parent)  # should fail



