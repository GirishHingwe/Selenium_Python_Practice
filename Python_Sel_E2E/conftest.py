import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox", help="browser selection"
    )


@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    # service_obj = Service()
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService())
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the pytest Plugins to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    """
    pytest_html = item.config.pluginmanager.get_plugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if(report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__),'reports')
            file_name = os.path.join(reports_dir, report.nodeid.replace( "::","_")+".png")
            print("file name is "+ file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:220px;" '\
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extras.append( pytest_html.extras_html( html ))
            report.extras = extras
    """
    pytest_html = item.config.pluginmanager.getplugin("html")

    outcome = yield
    report = outcome.get_result()

    extras = getattr(report, "extras", [])

    if report.when == "call":

        if report.failed:
            reports_dir = "reports"
            os.makedirs(reports_dir, exist_ok=True)

            file_name = os.path.join(
                reports_dir,
                report.nodeid.replace("::", "_").replace("/", "_") + ".png"
            )

            _capture_screenshot(file_name)

            html = f'''
            <div>
                <img src="{file_name}" width="400"
                     onclick="window.open(this.src)"
                     align="right"/>
            </div>
            '''

            extras.append(pytest_html.extras.html(html))

        report.extras = extras


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)
