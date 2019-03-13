import urllib3
from bs4 import BeautifulSoup
import certifi

wish = "https://www.weblio.jp/ontology/%E6%97%A5%E6%9C%AC%E3%81%AE%E8%8A%B8%E8%83%BD%E4%BA%BA_1"



def parse(url):
    http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())
    r = http.request('GET', url)
    soup = BeautifulSoup(r.data, 'html.parser')
    return soup.select_one("#mainL > div.mainBoxB > div > div.subCatWordsL > div:nth-child(1) > a").string

print (parse(wish))
