import requests
from bs4 import BeautifulSoup
import lxml
import urllib
import os

URL = 'https://fabiaoqing.com/biaoqing/lists/page/'
PAGE_LIST = []


for x in range(1,3):
    url = URL + str(x) + '.html'
    PAGE_LIST.append(url)


def download_img():
    split_list = url.split('/')
    filename = split_list.pop()
    path = os.path.join('images', filename)
    urllib.request.urlretrieve(url, filename = path)



def GET_PAGE(page_url):

    headers = {
        'Host' : 'https://fabiaoqing.com/biaoqing/lists/page',
        'Upgrade-Insecure-Requests' : '1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',

    }
    # heads = {'user-agent':''}

    res = requests.get(page_url, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml')
    img_list = soup.find_all('img',attrs={'class' : 'ui image lazy'})
    for img in img_list:
        url = img['data-original']
        download_img(url)
        print(url)

def main():

    for page_url in PAGE_LIST:
        GET_PAGE(page_url)


if __name__ == '__main__':
    main()


