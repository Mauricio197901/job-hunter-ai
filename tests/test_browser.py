from src.automation.browser import Browser

browser = Browser(headless=False)

browser.start()

browser.open("https://www.google.com")

print(browser.title())

browser.screenshot("google.png")

browser.stop()