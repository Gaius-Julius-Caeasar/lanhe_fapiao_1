# coding=utf-8
# 编译日期：2020-06-23 17:41:08
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
        time.sleep(3)
        # 鼠标点击
        self.__logger.debug('Flow:flow2,StepNodeTag:2317224431622,Note:')
        iie.do_click_pos(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',url=r'https://inv-veri.chinatax.gov.cn/index.html',selector=r'#fpdm',button=r'left',curson=r'center',times=1,run_mode=r'unctrl',continue_on_error=r'break',waitfor=10)
        time.sleep(0.8)
        # 键盘输入
        self.__logger.debug('Flow:flow2,StepNodeTag:2317224431621,Note:输入发票代码')
        time.sleep(0.5)
        ikeyboard.key_send_cs(text='044031900111',waitfor=10)
        time.sleep(0.6)
        # 键盘输入
        self.__logger.debug('Flow:flow2,StepNodeTag:2317224431620,Note:')
        time.sleep(0.5)
        ikeyboard.key_send_cs(text='{TAB}',waitfor=10)
        # 键盘输入
        self.__logger.debug('Flow:flow2,StepNodeTag:2317224431619,Note:输入发票号码')
        time.sleep(0.5)
        ikeyboard.key_send_cs(text='23838102',waitfor=10)
        # 键盘输入
        self.__logger.debug('Flow:flow2,StepNodeTag:2317224431618,Note:')
        time.sleep(0.5)
        ikeyboard.key_send_cs(text='{TAB}',waitfor=10)
        # 键盘输入
        self.__logger.debug('Flow:flow2,StepNodeTag:2317224431617,Note:开票日期')
        time.sleep(0.5)
        ikeyboard.key_send_cs(text='20200611',waitfor=10)
        # 键盘输入
        self.__logger.debug('Flow:flow2,StepNodeTag:2317224431616,Note:')
        time.sleep(0.5)
        ikeyboard.key_send_cs(text='{TAB}',waitfor=10)
        # 图像检测
        self.__logger.debug('Flow:flow2,StepNodeTag:2317224431613,Note:判断输入内容')
        tvar2317224431613 = iimg.img_exists(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',img_res_path=self.path,image=r'snapshot_20200623142820581.png',fuzzy=True,confidence=0.85,waitfor=30)
        time.sleep(0.5)
        # IF-N分支
        self.__logger.debug('Flow:flow2,StepNodeTag:2317224431614,Note:判断')
        if tvar2317224431613:
            # 键盘输入
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431612,Note:输入校验码')
            time.sleep(0.5)
            ikeyboard.key_send_cs(text='916383',waitfor=10)
        else:
            # 键盘输入
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431615,Note:输入开具金额')
            time.sleep(0.5)
            ikeyboard.key_send_cs(text='937.34',waitfor=10)
        # While循环
        self.__logger.debug('Flow:flow2,StepNodeTag:2317224431611,Note:')
        while 1:
            # 鼠标点击
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431627,Note:')
            time.sleep(0.5)
            iie.do_click_pos(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',url=r'https://inv-veri.chinatax.gov.cn/index.html',selector=r'#yzm_img',button=r'left',curson=r'center',times=1,run_mode=r'unctrl',continue_on_error=r'break',waitfor=10)
            time.sleep(5)
            # 鼠标移动
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431628,Note:')
            iie.do_moveto_pos(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',url=r'https://inv-veri.chinatax.gov.cn/index.html',selector=r'#content2 > TABLE:nth-of-type(1) > TBODY:nth-of-type(1) > TR:nth-of-type(6) > TD:nth-of-type(1)',curson=r'center',waitfor=10)
            time.sleep(5)
            # 截图
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431610,Note:')
            tishi = iimg.capture_image(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',win_text=r'',left_indent=1253,top_indent=572,width=210,height=36,waitfor=30)
            time.sleep(0.8)
            # 截图
            self.__logger.debug('Flow:flow2,StepNodeTag:231722443169,Note:')
            yzm_pic = iimg.capture_image(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',win_text=r'',left_indent=992,top_indent=620,width=139,height=64,waitfor=30)
            time.sleep(0.8)
            # 自定义函数
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431625,Note:')
            tvar2317224431625 = GlobalFun.code_color(tishi,yzm_pic)
            #验证码
            self.__logger.debug('Flow:flow2,StepNodeTag:231722443168,Note:')
            code = iocr.vcode_recognize(image_path=tvar2317224431625,code_type=8001,apiKey='8159a500cc9d4a69a71e6ac14263f029',secretKey='2d078aa8c13741239b3d00ced85832e3')
            time.sleep(1)
            # 鼠标点击
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431629,Note:')
            iie.do_click_pos(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',url=r'https://inv-veri.chinatax.gov.cn/index.html',selector=r'#yzm',button=r'left',curson=r'center',times=1,run_mode=r'unctrl',continue_on_error=r'break',waitfor=10)
            # 键盘输入
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431626,Note:')
            time.sleep(0.5)
            ikeyboard.key_send_cs(text=code,waitfor=10)
            # 鼠标点击
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431631,Note:')
            iie.do_click_pos(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',url=r'https://inv-veri.chinatax.gov.cn/index.html',selector=r'#checkfp',button=r'left',curson=r'center',times=1,run_mode=r'unctrl',continue_on_error=r'break',waitfor=10)
            time.sleep(3)
            # 图像检测
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431630,Note:')
            tvar2317224431630 = iimg.img_exists(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',img_res_path=self.path,image=r'snapshot_20200623152556855.png',fuzzy=True,confidence=0.85,waitfor=5)
            # IF-N分支
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431632,Note:')
            if tvar2317224431630:
                # 鼠标点击
                self.__logger.debug('Flow:flow2,StepNodeTag:2317224431634,Note:')
                iie.do_click_pos(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',url=r'https://inv-veri.chinatax.gov.cn/index.html',selector=r'#popup_ok',button=r'left',curson=r'center',times=1,run_mode=r'unctrl',continue_on_error=r'break',waitfor=10)
                time.sleep(0.8)
                # 鼠标点击
                self.__logger.debug('Flow:flow2,StepNodeTag:2317224431635,Note:')
                iie.do_click_pos(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',url=r'https://inv-veri.chinatax.gov.cn/index.html',selector=r'#yzm',button=r'left',curson=r'center',times=1,run_mode=r'unctrl',continue_on_error=r'break',waitfor=10)
                time.sleep(0.8)
                # 热键输入
                self.__logger.debug('Flow:flow2,StepNodeTag:2317224431636,Note:')
                ikeyboard.key_send_cs(text='^a',waitfor=10)
                # 键盘输入
                self.__logger.debug('Flow:flow2,StepNodeTag:2317224431637,Note:')
                time.sleep(0.5)
                ikeyboard.key_send_cs(text='{BACKSPACE}',waitfor=10)
            else:
                # Break中断
                self.__logger.debug('Flow:flow2,StepNodeTag:2317224431633,Note:')
                break
        # 图像检测
        self.__logger.debug('Flow:flow2,StepNodeTag:2317224431639,Note:')
        tvar2317224431639 = iimg.img_exists(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',img_res_path=self.path,image=r'snapshot_20200623153842415.png',fuzzy=True,confidence=0.85,waitfor=30)
        # IF-N分支
        self.__logger.debug('Flow:flow2,StepNodeTag:2317224431638,Note:')
        if tvar2317224431639:
            # 代码块
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431745,Note:')
            list_1.append('否')
            #单元格写入
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431640,Note:')
            iexcel.write_cell(path='C:/Users/jky/Desktop/fapiao_info.xlsx',cell='A2',text=list_1,file_type='excel')
            # 鼠标点击
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431642,Note:')
            iie.do_click_pos(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',url=r'https://inv-veri.chinatax.gov.cn/index.html',selector=r'#closebt',button=r'left',curson=r'center',times=1,run_mode=r'unctrl',continue_on_error=r'break',waitfor=10)
            # 消息框
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431747,Note:')
            ibox.msgs_box('结束',timeout=0)
        else:
            # 代码块
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431746,Note:')
            list_1.append('是')
            #单元格写入
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431641,Note:')
            iexcel.write_cell(path='C:/Users/jky/Desktop/fapiao_info.xlsx',cell='A2',text=list_1,file_type='excel')
            # 消息框
            self.__logger.debug('Flow:flow2,StepNodeTag:2317224431743,Note:')
            ibox.msgs_box('结束',timeout=3)
      
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
