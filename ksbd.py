from bs4 import BeautifulSoup
import requests
import pdb

url = "https://killsixbilliondemons.com/comic/kill-six-billion-demons-chapter-1/"
fname = "ksbd.txt"
lc = 0

while True:
    lc += 1

    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")


    text = soup.find('div', {'class':'entry'}).text
    next_button = soup.find('a', {'class': 'navi comic-nav-next navi-next'})
    if (next_button == None):
        break
    else:
        url = next_button['href']

    if (text.rstrip()):
        with open(fname, "a") as f:
            f.write(soup.title.text)
            f.write("\n")
            f.write(text)
            
    print(lc, soup.title.text)
