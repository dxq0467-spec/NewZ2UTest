import os
import time
import allure
from Utils.data_reader import read_yaml
import pytest
from playwright.sync_api import sync_playwright, Page


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as f:
        browser=f.chromium.launch(
            headless=False,   # 调试改为False；线上运行改为True
            slow_mo=300,
            args =["--start-maximized"])
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def admin(browser):
    cookie_file='User/json/user.json'
    context=browser.new_context(
        no_viewport=True,
        ignore_https_errors=True,
        storage_state=cookie_file if os.path.exists(cookie_file) else None)
    page=context.new_page()
    page.goto("http://new.z2u.test/admin")
    if '登录' in page.title():#判断是否登录
        time.sleep(60)
        print("需要手动登录管理员账号，请在60秒内完成登录！")
        page.context.storage_state(path=cookie_file)
    yield page
    page.close()
@pytest.fixture(scope="session")
def config():
    yaml=read_yaml('Config/config.yaml')
    if yaml is None:
        raise ValueError("product_data.yaml 读取失败，请检查文件路径和内容")
    return yaml

def pytest_runtest_makereport(item,call):
    if call.when=="call"and call.excinfo is not None:
        page_fixtures=[]
        for name,value in item.funcargs.items():
            if isinstance(value,Page):
                page_fixtures.append((name,value))
        for name,page in page_fixtures:
            try:
                screenshot_bytes = page.screenshot(full_page=True)
                allure.attach(
                    screenshot_bytes,
                    name=f"失败截图【{name}】",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as err:
                print(f"[{name}] 截图捕获异常：{err}")