
from Page.Admin.Income_Center.Payment_Methods import PaymentMethods
def test_01(admin):
    admin=PaymentMethods(admin)
    admin.open_page()
    assert 1==2