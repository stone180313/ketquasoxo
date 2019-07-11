import requests
import json
import datetime
import pyfiglet
v = 2
phucle = pyfiglet.figlet_format("PhucLe")
print(phucle)
time = datetime.datetime.now()
# class doge():
#
#     def __init__(self,vi):
#         self.vi = vi
#     # def conect(self):
#     #     query = {
#     #         1: 'get_address_balance',
#     #         2: 'get_address_received',
#     #         3: 'get_address_spent',
#     #         4: 'get_tx_unspent',
#     #         5: 'get_tx_received',
#     #         6: 'get_tx_spent'
#     #     }
#     #     a = int(input('''
#     #     Gõ 1 Lấy thông tin tài khoản
#     #     Gõ 2 Lịch sử tk nhận
#     #     Gõ 3 Lịch sử tk gửi
#     #     Gõ 4 Lịch sủ chưa nhận tin xác nhận
#     #     Gõ 5 Lịch sử gói tin xác nhận
#     #     Vui lòng nhập số :
#     #
#     #    '''))
#     #     if a == 1:
#     #         requests.get('https://chain.so/api/v2/get_address_balance/DOGE/' + self.vi)
#     #         doge.conect(data).json
#
#
#
# # D6UraoVYxTtP6gkhWMhUxErEEP98pUspdN
# asd = input('Nhập Số Ví Cần Kiểm Tra Số Dư >> :')
# # vi = doge(asd)
# # data = vi.conect().json()
# # for dat in data :
# #     print('Dia chi vi:',data['data']['address'])
# #     print('So du :', data['data']['confirmed_balance'])
# #     break
# # query = {
# #     1: 'get_address_balance',
# #     2: 'get_address_received',
# #     3: 'get_address_spent',
# #     4: 'get_tx_unspent',
# #     5: 'get_tx_received',
# #     6: 'get_tx_spent'
# # }
# # a = int(input('''
# #  Gõ 1 Lấy thông tin tài khoản
# #  Gõ 2 Lịch sử tk nhận
# #  Gõ 3 Lịch sử tk gửi
# #  Gõ 4 Lịch sủ chưa nhận tin xác nhận
# #  Gõ 5 Lịch sử gói tin xác nhận
# #  Vui lòng nhập số :
# #
# # '''))
def checkgiaodich():

    vi = input("Vi cần kiểm tra :>>>>")
    a = int(input(  ''' 
                Nhập Số 1 Cần Kiểm Tra Số Dư >> :
                Nhập Số 2 Cần Kiểm Tra Tài Khoản Nhận
                Nhập Số 3 Cần Kiểm Tra Mẫu tin gửi đi
                '''))
    if a == 1:
        data = requests.get('https://chain.so/api/v2/get_address_balance/DOGE/' + vi)
        loai = data.json()
        print('Địa chỉ ví DOGE :',loai['data']['address'])
        print('Số dư ví:',loai['data']['confirmed_balance'])

    elif a == 2 :
        data = requests.get('https://chain.so/api/v2/get_address_received/DOGE/' + vi)
        loai = data.json()
        print('Địa chỉ ví :',loai['data']['address'])
        print('Số dư bạn nhận đươc:',loai['data']['confirmed_received_value']+ " "+ 'DOGE')
        print('Địa chỉ ví :',loai)


    elif a == 3:
        data = requests.get('https://chain.so/api/v2/get_tx_spent/DOGE/' + vi)
        loai = data.json()
        print('Mẫu tin gửi đi của ví :', loai['data']['txs'])
    elif a == 4:
        data = requests.get('https://chain.so/api/v2/get_tx_unspent/DOGE/' + vi)
        loai = data.json()
        print('Mẫu tin gửi đi koh thành của ví :', loai['data']['txs'])
    elif a == 5:
        data = requests.get('https://chain.so/api/v2/get_tx_received/DOGE/' + vi)
        loai = data.json()
        print('Mẫu tin nhận của ví :', loai['data']['txs'])
    else:
        data = requests.get('https://chain.so/api/v2/get_tx_received/DOGE/' + vi)
        loai = data.json()
        print(loai)
while True:
    checkgiaodich()
    pass