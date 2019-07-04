import datetime
import pyfiglet
from prettytable import PrettyTable
phucle = pyfiglet.figlet_format("CanChi")
print(phucle)
print(f'Tiện ích xem tuổi can chi vui lòng nhập giá trị số')
can = {0:"canh",1:"tân",2:"nhâm",3:"quý",4:"giáp",5:"ất",6:"bính",7:"dinh",8:"mậu",9:"kỷ"}
chi = {0:"tý",1:"sửu",2:"dần",3:"mão",4:"thìn",5:"tỵ",6:"ngọ",7:"mùi",8:"thân",9:"dậu",10:"tuất",11:"hợi"}
menhcan = {1:["Giáp","Ất"],2:["Bính","Đinh"],3:["Mậu","Kỷ"],4:["Canh","Tân"],5:["Nhâm","Quý"]}
menhchi ={0:["Tý","Sửu","Ngọ","Mùi"],1:["Dần","Mão","Thân","Dậu"],2:["Thìn","Tỵ","Tuất","Hợi"]}
while True:
  namsinh = input(f'Nhập năm sinh >>> ')
  tinhcan = int(namsinh[3:4])
  tinhchi = int(namsinh[2:4]) % 12
  x = PrettyTable()
  x.field_names = ["Năm Sinh", "Can"," Chi"]
  x.add_row([namsinh,can.get(tinhcan),chi.get(tinhchi)])
  print(x)
  pass
