# coding=utf-8
# 编译日期：2020-10-30 11:41:28
# 版权所有：www.i-search.com.cn
import ubpa.init_input as iinput
from ubpa.base_util import StdOutHook, ExceptionHandler
import ubpa.iimg as iimg
import ubpa.ikeyboard as ikeyboard
import ubpa.iie as iie
import ubpa.itools.rpa_str as rpa_str
import ubpa.iocr as iocr
import time
import pdb
from ubpa.ilog import ILog
from ubpa.base_img import set_img_res_path
import getopt
from sys import argv
import sys
import os

class lanhe_fapiao_1:
     
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
        ILog.JOB_NO, ILog.OLD_STDOUT = self.job_no, sys.stdout
        sys.stdout = StdOutHook(self.job_no, sys.stdout)
        ExceptionHandler.JOB_NO, ExceptionHandler.OLD_STDERR = self.job_no, sys.stderr
        sys.excepthook = ExceptionHandler.handle_exception
        if('input_arg' in kwargs.keys()):
            self.input_arg = kwargs['input_arg']
            if(len(self.input_arg) <= 0):
                self.input_arg = iinput.load_init(__file__)
            if self.input_arg is None:
                sys.exit(0)
        self.dict_info={'AmountInWords':'佰叁拾圆叁角肆分','NoteDrawer':'谢登梅','SellerAddress':'深州市龙华区庆湾街道庆津大道乌庆旺路文汇处民治商务中心1栋115栋、2、3栋、4幢009栋7553323188', 'CommodityPrice':'[]','CommodityNum':'[]','SellerRegisterNum': '91440300689404127F','SellerBank':'农业银行龙华支行41028900040099987','Remarks':'订单号1047426466044621910支付日期2020-06-07','CommodityTaxRate':'[]','TotalTax':'62.05', 'CheckCode':'17960524178417916383','InvoiceCode': '044031900111','InvoiceDate':'2020年06月11日', 'PurchaserRegisterNum':'91440300MA5EGKDJ92','InvoiceTypeOrg': '深圳增值税电子普通发票','Password':'','PurchaserBank':'', 'AmountInFiguers':'937.34','Checker':'郑晓碧','TotalAmount': '875.29','CommodityAmount':"[{'row':'1','word':'875.29'}]", 'PurchaserName':'深圳市蓝禾技术有限公司','CommodityType': '[]','InvoiceType':'电子普通发票','PurchaserAddress':'', 'CommodityTax':"[{'row':'1','word':'62.05'}]", 'CommodityUnit':'[]','Payee':'刘笑额','SellerName':'深圳康润华商贸有限公司','CommodityName':"[{'row':'1','word':'(详见销货清单'}]",'InvoiceNum':'23838102'}
      
    def flow1(self):
        #增值税发票OCR
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:20201030113643160121,Title:增值税发票OCR,Note:')
        tvar_20201030113643161122=iocr.vat_recognize(image_path='E:/fapiao/不干胶发票0608.pdf')
        print('[flow1] [增值税发票OCR] [20201030113643160121]  返回值：[' + str(type(tvar_20201030113643161122)) + ']' + str(tvar_20201030113643161122))
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:20201030113715259124,Title:输出,Note:')
        rpa_str.iprints(tvar_20201030113643161122)
      
    def flow2(self):
        yzm_pic=None
        tishi=None
        list_1=['电子普通发票','深圳增值税电子普通发票','91440300MA5EGKDJ92', '2020年06月11日','044031900111','23838102', '17960524178417916383','875.29','62.05','937.34',"[{'row': '1', 'word': '(详见销货清单'}]"]
        dict_info={'AmountInWords':'佰叁拾圆叁角肆分','NoteDrawer':'谢登梅','SellerAddress':'深州市龙华区庆湾街道庆津大道乌庆旺路文汇处民治商务中心1栋115栋、2、3栋、4幢009栋7553323188', 'CommodityPrice':'[]','CommodityNum':'[]','SellerRegisterNum': '91440300689404127F','SellerBank':'农业银行龙华支行41028900040099987','Remarks':'订单号1047426466044621910支付日期2020-06-07','CommodityTaxRate':'[]','TotalTax':'62.05', 'CheckCode':'17960524178417916383','InvoiceCode': '044031900111','InvoiceDate':'2020年06月11日', 'PurchaserRegisterNum':'91440300MA5EGKDJ92','InvoiceTypeOrg': '深圳增值税电子普通发票','Password':'','PurchaserBank':'', 'AmountInFiguers':'937.34','Checker':'郑晓碧','TotalAmount': '875.29','CommodityAmount':"[{'row':'1','word':'875.29'}]", 'PurchaserName':'深圳市蓝禾技术有限公司','CommodityType': '[]','InvoiceType':'电子普通发票','PurchaserAddress':'', 'CommodityTax':"[{'row':'1','word':'62.05'}]", 'CommodityUnit':'[]','Payee':'刘笑额','SellerName':'深圳康润华商贸有限公司','CommodityName':"[{'row':'1','word':'(详见销货清单'}]",'InvoiceNum':'23838102'}
        code=None
        #网站
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:2317224431623,Title:网站,Note:')
        time.sleep(0.5)
        iie.open_url(ie_path='C:/Program Files (x86)/Internet Explorer/iexplore.exe',url='https://inv-veri.chinatax.gov.cn/index.html')
        time.sleep(0.5)
        # Try异常
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:flow2,StepNodeTag:20201027172041803566,Title:Try异常,Note:')
        try:
            #鼠标点击
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201027172049219568,Title:鼠标点击,Note:')
            iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20201029175005894.png',image_size=r'64X15',win_title=r'此站点不安全 - Internet Explorer',continue_on_error='break',img_res_path = self.path)
            #鼠标点击
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201027172102123570,Title:鼠标点击,Note:')
            iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20201029175415351.png',image_size=r'161X28',win_title=r'此站点不安全 - Internet Explorer',continue_on_error='break',img_res_path = self.path)
        except Exception as e:
            pass
        finally:
            pass
        #热键输入
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:240950181343,Title:热键输入,Note:')
        ikeyboard.key_send_cs(waitfor=10.000,text=r'#{UP}')
        time.sleep(2.5)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:2317224431622,Title:鼠标点击,Note:')
        iie.do_click_pos(waitfor=10.000,run_mode='unctrl',button='left',curson='center',continue_on_error='break',win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',selector=r'#fpdm',url=r'https://inv-veri.chinatax.gov.cn/index.html')
        time.sleep(0.8)
        #模拟按键
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:2317224431621,Title:模拟按键,Note:输入发票代码')
        time.sleep(0.5)
        ikeyboard.key_send_cs(waitfor=10.000,text='044031900111')
        time.sleep(0.6)
        #模拟按键
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:2317224431620,Title:模拟按键,Note:')
        time.sleep(0.5)
        ikeyboard.key_send_cs(waitfor=10.000,text='{TAB}')
        #模拟按键
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:2317224431619,Title:模拟按键,Note:输入发票号码')
        time.sleep(0.5)
        ikeyboard.key_send_cs(waitfor=10.000,text='23838102')
        #模拟按键
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:2317224431618,Title:模拟按键,Note:')
        time.sleep(0.5)
        ikeyboard.key_send_cs(waitfor=10.000,text='{TAB}')
        #模拟按键
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:2317224431617,Title:模拟按键,Note:开票日期')
        time.sleep(0.5)
        ikeyboard.key_send_cs(waitfor=10.000,text='20200611')
        #模拟按键
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:2317224431616,Title:模拟按键,Note:')
        time.sleep(0.5)
        ikeyboard.key_send_cs(waitfor=10.000,text='{Tab}')
        #图片检测
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:2317224431613,Title:图片检测,Note:判断输入内容')
        tvar_2020102717112596416=iimg.img_exists(waitfor=30.000,win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',image=r'snapshot_20201030101359793.png',img_res_path = self.path)
        print('[flow2] [图片检测] [2317224431613]  返回值：[' + str(type(tvar_2020102717112596416)) + ']' + str(tvar_2020102717112596416))
        time.sleep(0.5)
      
    def Main(self):
        #子流程
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20201027172332623803,Title:子流程,Note:')
        tvar202010271723326238031=self.flow2()
        print('[Main] [子流程] [20201027172332623803]  返回值：[' + str(type(tvar202010271723326238031)) + ']' + str(tvar202010271723326238031))
 
if __name__ == '__main__':
    ILog.begin_init()
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
    pro = lanhe_fapiao_1(robot_no=robot_no,proc_no=proc_no,job_no=job_no,input_arg=input_arg)
    pro.flow1()
