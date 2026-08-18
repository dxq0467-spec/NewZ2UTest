import allure
from Page.Admin.Income_Center.Payment_Methods import PaymentMethodsFlow
def test_01(admin):
    admin=PaymentMethodsFlow(admin)
    with allure.step('1'):
        admin.insert_method_flow(name="1",alias="2",fixed_free="2",sort="1000",payment_free='2',min_amount='2')
        # admin.search_method_flow(keyword='1')
        # admin.delete_method_flow(name='1')
        # assert 1==2