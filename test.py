import requests
response = requests.get('http://pyvideo.org/category/50/pycon-us-2014')
import bs4
soup = bs4.BeautifulSoup(response.text)
links = soup.select('div.video-summary-data a[href^=/video]')
links = [a.attrs.get('href') for a in soup.select('div.video-summary-data a[href^=/video]')]
print links
