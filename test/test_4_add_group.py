from model.group import Group
import pytest
from data.groups import testdata


# @pytest.mark.parametrize("group", testdata, ids=(repr(x) for x in testdata))
# def test_add_group(app, group):
def test_add_group(app, data_groups):
    group = data_groups
    old_groups = app.gr.get_group_list()
    app.gr.create_group(group)
    assert len(old_groups) + 1 == app.gr.count()
    new_groups = app.gr.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_max) == sorted(new_groups, key=Group.id_max)




