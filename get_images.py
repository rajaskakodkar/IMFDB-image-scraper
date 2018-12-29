from bs4 import BeautifulSoup
import re
from urllib.request import *
import urllib.request
def get_images(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    images = bs.find_all('img', {'src':re.compile('.jpg')})
    for image in images:
        img_name=image['src'][[x.start() for x in re.finditer(r'/',image['src'])][4]+1:re.search('.jpg',image['src']).end()]
        im='http://www.imfdb.org'+image['src'][:7]+image['src'][13:re.search('.jpg',image['src']).end()]
        urllib.request.urlretrieve(im, img_name)
