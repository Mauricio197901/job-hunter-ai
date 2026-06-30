from playwright.sync_api import sync_playwright


class Browser:

    def __init__(self, headless=True):
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=self.headless
        )
        self.page = self.browser.new_page()

    def open(self, url):
        self.page.goto(url, wait_until="domcontentloaded")

    def title(self):
        return self.page.title()

    def screenshot(self, filename):
        self.page.screenshot(path=filename, full_page=True)

    def stop(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()