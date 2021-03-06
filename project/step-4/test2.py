import sys
from PyQt5.QtWidgets import *
from kiwoom import *
from datetime import datetime
import FinanceDataReader as fdr
import time
import pickle
import util, jk_util
import threading
codes = ['033180','046940']
class StockAuto(threading.Thread):
    def __init__(self):
        self.kiwoom = Kiwoom()
        self.kiwoom.comm_connect()
        self.order_type = 1      #1:매수,2:매도

    def run(self):
        self.send_order()
    def send_order(self):
        print(codes)
        for code in codes:
           self.R_mae_mae(code)
           print(code)

    def R_mae_mae(self, code):
        account = self.get_account()
        nQty = 1
        if code == '033180':
            stock_price = '10000'
        elif code == '046940':
            stock_price = '5500'
        # 조건검색을 통해 저장한 데이타 가져오기
        print(account, code, stock_price)
        self.kiwoom.send_order("send_order", "0101", account, 2, code, nQty, stock_price, "00", "") #매수:1, 매도:2
        result = self.kiwoom.order_result
        if (result == 0):
            print("매도주문을 하였습니다.")
        else:
            print("매도 실패하였습니다.")

    def get_account(self):
        account_list = self.kiwoom.get_login_info("ACCNO")
        return account_list.split(';')[0]


x = StockAuto()
x.start()
x.join()
