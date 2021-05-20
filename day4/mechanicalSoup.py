import mechanicalsoup
name = input("enter book name")
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.google.com")
browser.select_form('form[action="/search"]')
browser['q'] = "intitle:index.of?pdf"+ name
browser.submit_selected(btnName="btnG")

for link in browser.links():
    urlLink = link.attrs['href']
    print(urlLink)