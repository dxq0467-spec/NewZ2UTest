from Base.Base import PageBase


class PaymentSettings(PageBase):

    # =============== 筛选条件 ================
    pay_category = 'button#searchForm.payType'
    show_status = 'select#searchForm.isShow'
    pay_type_filter = 'select#searchForm.commonType'
    support_topup_filter = 'select#searchForm.supportTopup'
    support_refund_filter = 'select#searchForm.supportRefund'
    reject_risk_filter = 'select#searchForm.isReject'
    keyword_search = 'input#searchForm.keyword'
    search_button = 'button.fi-color.fi-color-primary.fi-bg-color-600.fi-btn.fi-size-sm'
    reset_button = 'button.fi-btn.fi-size-sm'

    # =============== 列表页操作 ================
    insert_button = 'button.fi-ac-btn-action.fi-btn.fi-size-md.fi-color.fi-color-primary.fi-bg-color-600'
    edit_button = 'button.fi-ac-link-action.fi-link.fi-size-sm.fi-color.fi-color-primary.fi-text-color-600'
    column_manage_button = 'button.fi-btn.fi-size-sm'

    # =============== 基础信息 ================
    pay_name = 'input#mountedActionSchema0.pay_name'
    pay_full_name = 'input#mountedActionSchema0.val'
    pay_param_val = 'input#mountedActionSchema0.pay_val'
    pay_category_field = 'input#mountedActionSchema0.pay_type'
    sortby = 'input#mountedActionSchema0.sort'
    unique_token = 'input#mountedActionSchema0.token'
    payment_img = 'div.filepond--root input.filepond--browser'
    notice = 'input#mountedActionSchema0.notice'

    # =============== 支付手续费 ================
    pay_free_per = 'input#mountedActionSchema0.pay_free_per'
    fixed_free = 'input#mountedActionSchema0.fixed_free'
    fixed_free_cur = 'input#mountedActionSchema0.currency'
    more_fee = 'input#mountedActionSchema0.more_fee'

    # =============== 退款设置 ================
    support_refund = 'select#mountedActionSchema0.support_refund'
    refund_free_per = 'input#mountedActionSchema0.refund_free_per'
    fixed_refund_free = 'input#mountedActionSchema0.refund_free'
    fixed_refund_free_cur = 'input#mountedActionSchema0.refund_cur'

    # =============== 币种与金额限制 ================
    min_pay_amt = 'input#mountedActionSchema0.min_amt'
    min_amt_cur = 'input#mountedActionSchema0.min_amt_cur'
    channel_cur = 'input#mountedActionSchema0.charge_cur'

    # =============== 能力与风险 ================
    is_show = 'button#mountedActionSchema0.is_show'
    support_topup = 'button#mountedActionSchema0.support_topup'
    is_reject = 'button#mountedActionSchema0.is_reject'
    pay_type = 'select#mountedActionSchema0.common_type'

    # =============== 提交按钮（对话框内） ================
    submit_button = 'dialog button.fi-ac-btn-action.fi-btn.fi-size-md.fi-color.fi-color-primary.fi-bg-color-600'

    # =============== 页面导航 ================
    def open_page(self):
        url = self.base_url + '/admin/payment-settings'
        self.open_url(url)

    # =============== 筛选条件操作 ================
    def select_pay_category(self, value):
        """选择支付方式"""
        self.click(self.pay_category)
        self.page.get_by_role('option', name=value).click()

    def select_show_status(self, value):
        """选择显示状态"""
        self.select_dropdown(self.show_status, value)

    def select_pay_type_filter(self, value):
        """选择支付类型"""
        self.select_dropdown(self.pay_type_filter, value)

    def select_support_topup_filter(self, value):
        """选择是否支持充值"""
        self.select_dropdown(self.support_topup_filter, value)

    def select_support_refund_filter(self, value):
        """选择是否支持退款"""
        self.select_dropdown(self.support_refund_filter, value)

    def select_reject_risk_filter(self, value):
        """选择是否拒绝风险"""
        values = {
            "open" : "1",
            "close":"2"
        }
        select = values.get(value)
        self.select_dropdown(self.reject_risk_filter, select)

    def input_keyword(self, value):
        """输入搜索关键词"""
        self.input_text(self.keyword_search, value)

    def click_search_button(self):
        """点击搜索按钮"""
        self.click(self.search_button)

    def click_reset_button(self):
        """点击重置按钮"""
        self.click(self.reset_button)

    # =============== 列表页操作 ================
    def page_insert_button(self):
        """点击添加按钮"""
        self.click(self.insert_button)

    def page_edit_button(self):
        """点击编辑按钮"""
        self.click(self.edit_button)

    def page_edit_button_by_name(self, name):
        """点击编辑按钮"""
        self.click(self.edit_button)
        row = self.page.get_by_role('row', name=name)
        row.get_by_role('button', name='编辑').click()

    def page_column_manage_button(self):
        """点击列管理按钮"""
        self.click(self.column_manage_button)

    # =============== 基础信息输入 ================
    def input_pay_name(self, value):
        """输入支付方式名称"""
        self.input_text(self.pay_name, value)

    def input_pay_full_name(self, value):
        """输入支付方式完整名称"""
        self.input_text(self.pay_full_name, value)

    def input_pay_param_val(self, value):
        """输入支付参数值"""
        self.input_text(self.pay_param_val, value)

    def input_pay_category_field(self, value):
        """输入支付方式字段"""
        self.input_text(self.pay_category_field, value)

    def input_sort(self, value):
        """输入排序"""
        self.input_text(self.sortby, value)

    def input_unique_token(self, value):
        """输入唯一令牌"""
        self.input_text(self.unique_token, value)

    def input_payment_img(self):
        """上传支付方式图片"""
        self.upload_img(self.payment_img)

    def input_notice(self, value):
        """输入支付方式备注"""
        self.input_text(self.notice, value)

    # =============== 手续费输入 ================
    def input_pay_free_per(self, value):
        """输入支付方式免费比例"""
        self.input_text(self.pay_free_per, value)

    def input_fixed_free(self, value):
        """输入固定免费金额"""
        self.input_text(self.fixed_free, value)

    def input_fixed_free_cur(self, value):
        """输入固定免费金额币种"""
        self.input_text(self.fixed_free_cur, value)

    def input_more_fee(self, value):
        """输入额外费用备注"""
        self.input_text(self.more_fee, value)

    # =============== 退款设置 ================
    def select_support_refund(self, value):
        """选择是否支持退款"""
        self.select_dropdown(self.support_refund, value)

    def input_refund_free_per(self, value):
        """输入退款免费比例"""
        self.input_text(self.refund_free_per, value)

    def input_fixed_refund_free(self, value):
        """输入固定退款免费金额"""
        self.input_text(self.fixed_refund_free, value)

    def input_fixed_refund_free_cur(self, value):
        """输入固定退款免费金额币种"""
        self.input_text(self.fixed_refund_free_cur, value)

    # =============== 币种与金额限制 ================
    def input_min_pay_amt(self, value):
        """输入最低支付金额"""
        self.input_text(self.min_pay_amt, value)

    def input_min_amt_cur(self, value):
        """输入最低支付金额币种"""
        self.input_text(self.min_amt_cur, value)

    def input_channel_cur(self, value):
        """输入渠道币种"""
        self.input_text(self.channel_cur, value)

    # =============== 开关操作 ================
    def toggle_is_show(self):
        """切换是否显示"""
        self.click(self.is_show)

    def toggle_support_topup(self):
        """切换是否支持充值"""
        self.click(self.support_topup)

    def toggle_is_reject(self):
        """切换是否拒绝风险"""
        self.click(self.is_reject)

    # =============== 支付类型 ================
    def select_pay_type(self, value):
        """选择支付方式"""
        self.select_dropdown(self.pay_type, value)

    # =============== 表单提交 ================
    def page_submit_button(self):
        """点击提交按钮"""
        self.click(self.submit_button)

    # =============== 业务流程 ================
    class PaymentSettingsFlow:
        def __init__(self, page):
            self.page = page
            self.payment_settings = PaymentSettings(page)

        def insert_payment_flow(self, pay_name, pay_full_name, sort, token):
            """新增支付方式流程"""
            self.payment_settings.open_page()
            self.payment_settings.page_insert_button()
            self.payment_settings.input_pay_name(pay_name)
            self.payment_settings.input_pay_full_name(pay_full_name)
            self.payment_settings.input_sort(sort)
            self.payment_settings.input_unique_token(token)
            self.payment_settings.page_submit_button()

        def edit_payment_flow(self, name):
            """编辑支付方式流程"""
            self.payment_settings.open_page()
            self.payment_settings.page_edit_button_by_name(name)

        def filter_payment_flow(self, keyword='', show_status='', pay_type=''):
            """筛选支付方式流程"""
            self.payment_settings.open_page()
            if keyword:
                self.payment_settings.input_keyword(keyword)
            if show_status:
                self.payment_settings.select_show_status(show_status)
            if pay_type:
                self.payment_settings.select_pay_type_filter(pay_type)
            self.payment_settings.click_search_button()