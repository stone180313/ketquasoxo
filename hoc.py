class sinhvien():

    def __init__(self,name,tuoi):
        self.name = name
        self.tuoi = tuoi
    def show(self):
        print('ten toi la',self.name,self.tuoi)

thongtin =sinhvien("phuc",20)
thongtin.show()

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