class MagnetoProvider:
    def __init__(self, page):
        self.page = page

    def search(self, query):
        self.page.goto("https://www.magneto365.com")
        self.page.wait_for_timeout(3000)

        try:
            self.page.fill("input", query)
            self.page.keyboard.press("Enter")
        except:
            pass

        self.page.wait_for_timeout(5000)

        return [{
            "title": "demo job",
            "company": "magneto",
            "location": "cali",
            "url": "https://example.com",
            "source": "magneto"
        }]