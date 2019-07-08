from bs4 import BeautifulSoup
import urllib.request

import requests
class Mrcong():
    def __init__(self,url,profile):
        self.url = url
        self.profile = profile
    def connect(self):
        return requests.get(f"{self.url},{self.profile}")
    def soup(self):
        return BeautifulSoup(self.connect().content,'lxml')
    def tab(self):
        if self.soup() != '':
            return self.soup().find_all('img')

data = Mrcong('https://mrcong.com/','498-hinh-nen-cuc-lang-man-va-de-thuong-danh-rieng-cho-ngay-valentine')
imgs = (data.tab())
i = 0
for img in imgs:
    try:
        urllib.request.urlretrieve(img['src'],str(i)+".jpg")
        i = i + 1
    except:
        print('Da download thanh cong')

if __name__ == '__main__':
    Mrcong()


# urllib.request.urlretrieve("https://i1.wp.com/1.bp.blogspot.com/-iJSORpD0D0o/WKK2L-jhcrI/AAAAAAAAHgo/bhkd_hmvxrQoP6e3BLjt_W8PCVLqNixFQCLcB/s1600/MrCong.com-Hinh-nen-Valentine-dep-208.jpg?w=618&ssl=1", "./img/local-filename.jpg")

# urllib3.get_host('http://www.digimouth.com/news/media/2011/09/google-logo.jpg',"phuc.jpg")
# https://i0.wp.com/3.bp.blogspot.com/-CzftWE33fLI/WKK2K5KrrCI/AAAAAAAAHgI/yAVYbcKYfVkPEfYhPgcZ0RDEHPruPy3jQCLcB/s1600/MrCong.com-Hinh-nen-Valentine-dep-029.jpg?w=618&ssl=1
# soup = BeautifulSoup(data.connect().content,'lxml')
# img = soup.find_all(('img'))
# print(img)
# url = 'https://mrcong.com/'
# profile = '498-hinh-nen-cuc-lang-man-va-de-thuong-danh-rieng-cho-ngay-valentine'
# respone = requests.get(f"{url},{profile}")
# soup = BeautifulSoup(respone.content,'lxml')
# imgs = soup.find_all('img')
# for img in imgs:
#     print(img['src'])

