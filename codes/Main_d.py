# coding=utf-8
# 编译日期：2020-06-24 09:50:58
# 版权所有：www.i-search.com.cn
import time
import pdb
from ubpa.ilog import ILog
from ubpa.base_img import *
import getopt
from sys import argv
import sys
from ubpa.itools import rpa_import
GlobalFun = rpa_import.import_global_fun(__file__)
import ubpa.ibox as ibox
import ubpa.iexcel as iexcel
import ubpa.iie as iie
import ubpa.iimg as iimg
import ubpa.ikeyboard as ikeyboard
import ubpa.iocr as iocr

class lanhe_fapiao:
     
    def __init__(self,**kwargs):
        self.__logger = ILog(__file__)
        self.path = set_img_res_path(__file__)
        self.robot_no = ''
        self.proc_no = ''
        self.job_no = ''
        self.input_arg = ''
        if('robot_no' in kwargs.keys()):
            self.robot_no = kwargs['robot_no']
        if('proc_no' in kwargs.keys()):
            self.proc_no = kwargs['proc_no']
        if('job_no' in kwargs.keys()):
            self.job_no = kwargs['job_no']
        if('input_arg' in kwargs.keys()):
            self.input_arg = kwargs['input_arg']
            self.input_arg = self.input_arg.replace("\\","/")
        self.dict_info={'AmountInWords':'佰叁拾圆叁角肆分','NoteDrawer':'谢登梅','SellerAddress':'深州市龙华区庆湾街道庆津大道乌庆旺路文汇处民治商务中心1栋115栋、2、3栋、4幢009栋7553323188', 'CommodityPrice':'[]','CommodityNum':'[]','SellerRegisterNum': '91440300689404127F','SellerBank':'农业银行龙华支行41028900040099987','Remarks':'订单号1047426466044621910支付日期2020-06-07','CommodityTaxRate':'[]','TotalTax':'62.05', 'CheckCode':'17960524178417916383','InvoiceCode': '044031900111','InvoiceDate':'2020年06月11日', 'PurchaserRegisterNum':'91440300MA5EGKDJ92','InvoiceTypeOrg': '深圳增值税电子普通发票','Password':'','PurchaserBank':'', 'AmountInFiguers':'937.34','Checker':'郑晓碧','TotalAmount': '875.29','CommodityAmount':"[{'row':'1','word':'875.29'}]", 'PurchaserName':'深圳市蓝禾技术有限公司','CommodityType': '[]','InvoiceType':'电子普通发票','PurchaserAddress':'', 'CommodityTax':"[{'row':'1','word':'62.05'}]", 'CommodityUnit':'[]','Payee':'刘笑额','SellerName':'深圳康润华商贸有限公司','CommodityName':"[{'row':'1','word':'(详见销货清单'}]",'InvoiceNum':'23838102'}
      
    def flow2(self):
        yzm_pic=None
        tishi=None
        list_1=['电子普通发票','深圳增值税电子普通发票','91440300MA5EGKDJ92', '2020年06月11日','044031900111','23838102', '17960524178417916383','875.29','62.05','937.34',"[{'row': '1', 'word': '(详见销货清单'}]"]
        dict_info={'AmountInWords':'佰叁拾圆叁角肆分','NoteDrawer':'谢登梅','SellerAddress':'深州市龙华区庆湾街道庆津大道乌庆旺路文汇处民治商务中心1栋115栋、2、3栋、4幢009栋7553323188', 'CommodityPrice':'[]','CommodityNum':'[]','SellerRegisterNum': '91440300689404127F','SellerBank':'农业银行龙华支行41028900040099987','Remarks':'订单号1047426466044621910支付日期2020-06-07','CommodityTaxRate':'[]','TotalTax':'62.05', 'CheckCode':'17960524178417916383','InvoiceCode': '044031900111','InvoiceDate':'2020年06月11日', 'PurchaserRegisterNum':'91440300MA5EGKDJ92','InvoiceTypeOrg': '深圳增值税电子普通发票','Password':'','PurchaserBank':'', 'AmountInFiguers':'937.34','Checker':'郑晓碧','TotalAmount': '875.29','CommodityAmount':"[{'row':'1','word':'875.29'}]", 'PurchaserName':'深圳市蓝禾技术有限公司','CommodityType': '[]','InvoiceType':'电子普通发票','PurchaserAddress':'', 'CommodityTax':"[{'row':'1','word':'62.05'}]", 'CommodityUnit':'[]','Payee':'刘笑额','SellerName':'深圳康润华商贸有限公司','CommodityName':"[{'row':'1','word':'(详见销货清单'}]",'InvoiceNum':'23838102'}
        code=None
        #网站
        self.__logger.debug('Flow:flow2,StepNodeTag:2317224431623,Note:')
        iie.open_url(url='https://inv-veri.chinatax.gov.cn/index.html')
        time.sleep(0.5)
      
    def Main(self):
        pass
 
if __name__ == '__main__':
    robot_no = ''
    proc_no = ''
    job_no = ''
    input_arg = ''
    try:
        argv = sys.argv[1:]
        opts, args = getopt.getopt(argv,"hr:p:j:i:",["robot = ","proc = ","job = ","input = "])
    except getopt.GetoptError:
        print ('robot.py -r <robot> -p <proc> -j <job>')
    for opt, arg in opts:
        if opt == '-h':
            print ('robot.py -r <robot> -p <proc> -j <job>')
        elif opt in ("-r", "--robot"):
            robot_no = arg
        elif opt in ("-p", "--proc"):
            proc_no = arg
        elif opt in ("-j", "--job"):
            job_no = arg
        elif opt in ("-i", "--input"):
            input_arg = arg
    pro = lanhe_fapiao(robot_no=robot_no,proc_no=proc_no,job_no=job_no,input_arg=input_arg)
    pro.flow2()
    ___logger = ILog(__file__)
    ___logger.debug('Class:Main,ProTag:Quit,Note:Exit')
