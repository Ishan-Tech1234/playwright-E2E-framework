
def test_google_search(page):
     page.goto("https://www.google.com/")
     print(page.title())