from Page.Admin.Admin_index import AdminINdex
def test_01(admin):
    admin=AdminINdex(admin)
    admin.open_index_page()
    assert 1==2