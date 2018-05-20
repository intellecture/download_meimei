# 爬取霉霉的照片
from bs4 import BeautifulSoup
import requests
import time
import urllib.request

url = 'https://weheartit.com/inspirations/taylorswift?page='
path = 'D:/aaa/abc.json'
def get_images(url, data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    images = soup.select('img.entry-thumbnail')
    if data == None:
        for image in images:
            data = {
                'image': image.get('src')
            }
            print(data)

def get_pages(start, end):
    for i in range(start, end):
        get_images(url+str(i))
        download(url+str(i))
        time.sleep(2)

def download(data):
    filename = urllib.request.urlretrieve(url, filename=path)
    print('Done')
# def download(url, data):
#     filename = url.split('?')[0].split('/')[-1]# + url.split('/')[-2] + url.split('/')[-1])
#     target = "D:/aaa/{}.json".format(filename)
#     with open(target, "a", encoding="utf-8") as fs:
#         fs.write(str(data))
#         fs.write('\n')
#
#     print('Done')

if __name__ == '__main__':
    get_pages(1, 10)
