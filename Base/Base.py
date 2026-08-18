from playwright.sync_api import Page,expect
from typing import Optional
from Utils.data_reader import read_yaml
from Utils.logger import Logger

class PageBase:
    def __init__(self, page: Page):
        self.page: Page = page
        self.config=read_yaml('Config/config.yaml')
        self.base_url = self.config['BASE_URL']
        self.lang=self.config['LANG']
        self.DEFAULT_TIMEOUT=self.config['DEFAULT_TIMEOUT']
        # 设置全局页面超时
        self.page.set_default_timeout(self.DEFAULT_TIMEOUT)


    def open_url(self, url, timeout: Optional[int] = None):
        """打开网页"""
        self.page.goto(
            url=url,
            wait_until='domcontentloaded',
            timeout=timeout or self.DEFAULT_TIMEOUT
        )

    def input_text(self, locator, text):
        """输入文本"""
        loc=self.get_locator(locator)
        try:
            loc.clear()
            loc.fill(text)
        except Exception as e:
            Logger.error(f"文本输入有误{str(e)}")

    def get_locator(self,locator):
        """定位元素"""
        try:
            loc = self.page.locator(locator)
            return loc
        except Exception as e:
            Logger.error(f"元素未找到/不可见,元素{locator}定位有误{str(e)}")
            raise e
    def get_locator_by_text(self,text):
        """文本定位"""
        try:
            text=self.page.get_by_text(text)
            return text
        except Exception as e:
            Logger.error(f"文本未找到/不可见,文本{text}定位有误{str(e)}")
            raise e

    def get_locators_count(self,locator):
        """获取元素个数"""
        loc = self.page.locator(locator)
        try:
            count=loc.count()
            return count
        except Exception as e:
            raise e

    def get_all_locators(self,locators):
        """定位所有元素"""
        try:
            locs = self.get_locator(locators).all()
            return locs
        except AssertionError as e:
            Logger.error(f"元素未找到/不可见,元素{locators}定位有误{str(e)}")
            raise e

    def get_text(self,locator):
        """获取元素文本"""
        loc = self.get_locator(locator)
        try:
            text=loc.text_content(timeout=self.DEFAULT_TIMEOUT)
            return text
        except Exception as e:
            Logger.error(f"获取文本有误{str(e)}")
            return None

    def click(self, locator):
        """点击元素"""
        loc=self.get_locator(locator)
        try:
            loc.scroll_into_view_if_needed()
            try:
                loc.wait_for(state="visible", timeout=self.DEFAULT_TIMEOUT)
                loc.click()
            except Exception as e:
                loc.click(force=True)
                raise e
        except Exception as e:
            Logger.error(f"按钮点击有误{str(e)}")

    def upload_img(self,locator):
        """上传截图"""
        loc=self.get_locator(locator)
        file_path = r"D:\壁纸\2.jpg"
        loc.set_input_files(file_path)

    def wait_visible(self, locator, timeout: Optional[int] = None):
        """等待元素可见"""
        try:
            self.page.wait_for_selector(locator, timeout=timeout)
        except Exception as e:
            Logger.error(f"等待时间内元素不可见{str(e)}")

    def expect_locator_visible(self, locator):
        """通用封装：断言元素可见"""
        loc= self.get_locator(locator)
        expect(loc).to_be_visible(timeout=self.DEFAULT_TIMEOUT)

    def expect_locator_to_be_attached(self,locator):
        """断言元素存在"""
        loc=self.get_locator(locator)
        try:
            expect(loc).to_be_attached()
            Logger.info("元素存在")
        except AssertionError:
            Logger.error("元素不存在")
            return False


    #
    def expect_locator_hidden(self, locator):
        """拓展配套常用封装（一并写上，日常高频使用）"""
        loc= self.get_locator(locator)
        expect(loc).to_be_hidden(timeout=self.DEFAULT_TIMEOUT)

    #
    def expect_locator_have_text(self, locator, text):
        """断言文本精确匹配"""
        loc= self.get_locator(locator)
        try:
            expect(loc).to_have_text(text, timeout=self.DEFAULT_TIMEOUT)
            Logger.info(f"校验通过：加载文本文本包含【{text}】")
        except AssertionError as e:
            Logger.error(f"校验失败：加载文本文本不包含【{text}】")
            raise e

    def expect_page_have_text(self,text):
        """断言页面标题是否匹配"""
        try:
            expect(self.page).to_have_title(text, timeout=self.DEFAULT_TIMEOUT)
            Logger.info(f"校验通过：页面加载标题文本包含【{text}】")
        except AssertionError as e:
            Logger.error(f"校验失败：页面加载标题文本不包含【{text}】")
            raise e
    #
    def expect_locator_contains_text(self, locator, text):
        """断言文本模糊匹配"""
        loc= self.get_locator(locator)
        try:
            # 尝试断言文本包含
            expect(loc).to_contain_text(text, timeout=self.DEFAULT_TIMEOUT)
            Logger.info(f"校验通过：元素文本包含【{text}】")
            return True
        except AssertionError:
            # 捕获断言失败异常 = 文本不存在
            Logger.error(f"元素文本未包含【{text}】")
            return False

    def _is_locator_exist(self,locator):
        """元素是否存在"""
        loc=self.get_locator(locator)
        num=loc.count()
        if num >0:
            return True
        else:
            return False
    def current_url(self):
        url=self.page.url
        return url
    def target_new_url(self,locator):
        """点击【】按钮"""
        with self.page.expect_popup(timeout=self.DEFAULT_TIMEOUT) as popup_event:
            self.click(locator)
        current_page = popup_event.value
        self.page=current_page
        # 可打印当前地址调试
        current_page.close()
        return current_page.url

    def wait_for_url(self,url):
        self.page.wait_for_url(url)


    def refresh(self):
        """刷新页面"""
        current_url = self.page.url
        # wait_until 固定 domcontentloaded，适配订单后台轮询页面
        self.page.goto(
            url=current_url,
        wait_until = "domcontentloaded",
        timeout = self.DEFAULT_TIMEOUT
        )
        self.wait_for_load_state()

    def wait_for_timeout(self):
        self.page.wait_for_timeout(timeout=2000)

    def wait_for_load_state(self):
        self.page.wait_for_load_state(state = "domcontentloaded",timeout=self.DEFAULT_TIMEOUT)


    def input_more(self, locator, fill_text):
        """多个输入框输入"""
        input_list= self.get_all_locators(locator)
        for input_ele in input_list:
            # 等待元素可见，超时则跳过当前元素
            try:
                expect(input_ele).to_be_visible(timeout=self.DEFAULT_TIMEOUT)
                # 先清空原有内容
                input_ele.clear()
                # 填入文本
                input_ele.fill(fill_text)
            except AssertionError:
                Logger.warning(f"元素隐藏/不存在，跳过填写")
                continue


    def save_storage_state(self,save_path):
        """保存登录Cookie+会话到json（官方标准登录缓存）"""
        self.page.context.storage_state(path=save_path)


    def select_dropdown(self, locator, value):
        """
        原生下拉框选择
        :param value:
        :param locator: 下拉框定位器
        """
        self.wait_visible(locator)
        try:
            self.page.select_option(locator, value=value)
        except Exception as e:
            Logger.error(f"下拉选择框{str(e)}")

    def check_box(self, locator: str):
        """勾选复选框"""
        self.wait_visible(locator)
        self.page.check(locator)

    def uncheck_box(self, locator: str):
        """取消复选框勾选"""
        self.wait_visible(locator)
        self.page.uncheck(locator)

    def is_box_checked(self, locator: str) -> bool:
        """判断复选框是否勾选"""
        return self.page.is_checked(locator)
