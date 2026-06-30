from src.automation.navigator import Navigator

nav = Navigator(headless=False)

nav.start()

nav.open("https://www.google.com")

print(nav.title())

nav.screenshot("google_test.png")

nav.stop()