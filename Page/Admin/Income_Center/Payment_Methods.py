import re
from Base.Base import PageBase


class PaymentMethods(PageBase):

    # =============== 列表页操作 ================
    search_input = 'div.fi-ta-search-field div.fi-input-wrp div.fi-input-wrp-content-ctn input.fi-input.fi-input-has-inline-prefix'
    insert_button = 'button.fi-ac-btn-action.fi-btn.fi-size-md.fi-color.fi-color-primary.fi-bg-color-600'
    edit_button = 'button.fi-ac-link-action.fi-link.fi-size-sm.fi-color.fi-color-primary.fi-text-color-600'
    delete_button = 'button.fi-ac-link-action.fi-link.fi-size-sm.fi-color.fi-color-danger.fi-text-color-600'

    # =============== 基础信息 ================
    payment_name = 'input[id="mountedActionSchema0.payment_name"]'
    alias = 'input[id="mountedActionSchema0.alias"]'
    sortby = 'input[id="mountedActionSchema0.sortby"]'
    payment_img = 'div.filepond--root input.filepond--browser'

    # =============== 手续费与最低金额 ================
    payment_free = 'input[id="mountedActionSchema0.payment_free"]'
    fixed_free = 'input[id="mountedActionSchema0.fixed_free"]'
    min_amount = 'input[id="mountedActionSchema0.min_amount"]'
    exc_rate_diff = 'input[id="mountedActionSchema0.exc_rate_diff"]'
    extra_fee = 'input[id="mountedActionSchema0.extra_fee"]'

    # =============== 可用范围 ================
    is_open = 'input[id="mountedActionSchema0.is_open"]'
    currency = 'input[id="mountedActionSchema0.currency"]'
    region = 'input[id="mountedActionSchema0.region"]'

    # =============== 提款方式描述（富文本编辑器） ================
    description_editor = 'div.tiptap.ProseMirror'

    # =============== 提交按钮（对话框内） ================
    submit_button = 'button[x-data="filamentFormButton"]'

    # =============== 提示信息 ================
    alert='div.fi-no-notification-main div.fi-no-notification-text h3.fi-no-notification-title'

    # =============== 删除提示 ================
    delete_confirm='button[x-data="filamentFormButton"]'
    delete_cancel='button.fi-ac-btn-action fi-btn fi-size-md'

    # =============== 页面导航 ================
    def open_page(self):
        """打开提款方式页面"""
        url = self.base_url + '/admin/payout-methods'
        self.open_url(url)
        self.expect_page_have_text(re.compile('提款方式'))
    # =============== 列表页操作 ================
    def page_search(self, value):
        """输入搜索关键词"""
        self.input_text(self.search_input, value)
        self.wait_for_timeout()

    def page_insert_button(self):
        """点击新增提款方式按钮"""
        self.click(self.insert_button)

    def page_edit_button(self):
        """点击编辑按钮（第一行）"""
        self.click(self.edit_button)

    def page_edit_button_by_name(self, name):
        """按名称点击对应行的编辑按钮"""
        row = self.page.get_by_role('row', name=name).first
        row.get_by_role('button', name='编辑').click()

    def page_delete_button(self):
        """点击删除按钮（第一行）"""
        self.click(self.delete_button)

    def page_delete_button_by_name(self, name):
        """按名称点击对应行的删除按钮"""
        row = self.page.get_by_role('row', name=name).first
        row.get_by_role('button', name='删除').click()


    def delete_pop_confirm(self):
        """删除弹出点击确认"""
        self.click(self.delete_confirm)
    def delete_pop_cancel(self):
        """删除弹出点击取消"""
        self.click(self.delete_cancel)


    # =============== 基础信息输入 ================
    def input_payment_name(self, value):
        """输入提款方式名称"""
        self.input_text(self.payment_name, value)

    def input_alias(self, value):
        """输入别名"""
        self.input_text(self.alias, value)

    def input_sort(self, value):
        """输入排序"""
        self.input_text(self.sortby, value)

    def input_payment_img(self):
        """上传提款方式图片"""
        self.upload_img(self.payment_img)

    # =============== 手续费与最低金额输入 ================
    def input_payment_free(self, value):
        """输入提款手续费（%）"""
        self.input_text(self.payment_free, value)

    def input_fixed_free(self, value):
        """输入固定手续费（USD）"""
        self.input_text(self.fixed_free, value)

    def input_min_amount(self, value):
        """输入最低提款金额（USD）"""
        self.input_text(self.min_amount, value)

    def input_exc_rate_diff(self, value):
        """输入汇差"""
        self.input_text(self.exc_rate_diff, value)

    def input_extra_fee(self, value):
        """输入额外费用备注"""
        self.input_text(self.extra_fee, value)

    # =============== 可用范围选择 ================
    def select_is_open(self, value='open'):
        """选择是否开放（open=开放, close=关闭）"""
        values = {
            "open": "1",
            "close": "2"
        }
        if value in values:
            select_value = values[value]
            self.select_dropdown(self.is_open, select_value)

    def select_currency(self, value):
        """选择包含币种（多选）"""
        self.click(self.currency)
        self.page.get_by_role('option', name=value).click()

    def select_region(self, value):
        """选择可用地区（多选）"""
        self.click(self.region)
        self.page.get_by_role('option', name=value).click()

    # =============== 提款方式描述 ================
    def input_description(self, value):
        """输入提款方式描述（当前语言）"""
        self.click(self.description_editor)
        self.input_text(self.description_editor,value)

    def switch_description_tab(self, lang):
        """切换描述语言标签"""
        self.page.get_by_role('tab', name=lang).click()

    # =============== 表单提交 ================
    def page_submit_button(self):
        """点击提交按钮"""
        self.click(self.submit_button)

    # =============== 通用功能 ================
    def wait_for_page_load(self):
        """等待页面加载"""
        self.wait_for_timeout()

    def expect_to_have(self,value):
        """判断页面提示信息"""
        self.expect_locator_have_text(self.alert,value)

    # =============== 业务流程 ================
class PaymentMethodsFlow:
    def __init__(self, page):
        self.page = page
        self.payment_methods = PaymentMethods(page)

    def insert_method_flow(self, name, alias, sort, payment_free, fixed_free, min_amount):
        """新增提款方式流程"""
        self.payment_methods.open_page()
        self.payment_methods.page_insert_button()
        self.payment_methods.input_payment_name(name)
        self.payment_methods.input_alias(alias)
        self.payment_methods.input_sort(sort)
        self.payment_methods.input_payment_free(payment_free)
        self.payment_methods.input_fixed_free(fixed_free)
        self.payment_methods.input_min_amount(min_amount)
        self.payment_methods.page_submit_button()
        self.payment_methods.expect_to_have("提款方式已创建")

    def edit_method_flow(self, name, new_name, new_alias, new_sort):
        """编辑提款方式流程"""
        self.payment_methods.open_page()
        self.payment_methods.page_edit_button_by_name(name)
        self.payment_methods.input_payment_name(new_name)
        self.payment_methods.input_alias(new_alias)
        self.payment_methods.input_sort(new_sort)
        self.payment_methods.page_submit_button()
        self.payment_methods.expect_to_have("提款方式已更新")

    def delete_method_flow(self, name):
        """删除提款方式流程"""
        # self.payment_methods.open_page()
        self.payment_methods.page_delete_button_by_name(name)
        self.payment_methods.delete_pop_confirm()
        self.payment_methods.expect_to_have("提款方式已删除")

    def search_method_flow(self, keyword):
        """搜索提款方式流程"""
        self.payment_methods.open_page()
        self.payment_methods.page_search(keyword)
