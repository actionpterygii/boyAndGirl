import urllib3
from bs4 import BeautifulSoup
import certifi

wish = "http://www.kanji-jiten.jp/namelist/index22.html"



def parse(url):
    http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())
    r = http.request('GET', url)
    soup = BeautifulSoup(r.data, 'html.parser')
    # return soup.select_one("#main > [class=\"namaeyomi\"]:nth-child(2)").string
    return soup.select_one("#main > [class=\"namaeyomi\"]:last-of-type").string
    # return soup.select_one("#main > div:nth-child(8)").string

print (parse(wish))


