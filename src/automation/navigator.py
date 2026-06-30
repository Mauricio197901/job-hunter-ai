from src.automation.browser import Browser


class Navigator:
    def __init__(self, headless=True):
        self.browser = Browser(headless=headless)

    def start(self):
        self.browser.start()

    def open(self, url):
        print(f"Abrir: {url}")
        self.browser.open(url)

    def screenshot(self, filename):
        self.browser.screenshot(filename)

    def title(self):
        return self.browser.title()

    def stop(self):
        self.browser.stop()