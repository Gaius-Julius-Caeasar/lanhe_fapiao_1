# coding=utf-8
# 编译日期：2020-06-23 14:25:53
# 版权所有：www.i-search.com.cn
import time
import pdb
from ubpa.ilog import ILog
from ubpa.base_img import *
import getopt
from sys import argv
import sys
import ubpa.iie as iie
import ubpa.ikeyboard as ikeyboard

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
      
    def flow1(self):
        #RPACodeMarked.....2314162044320
        # 鼠标点击
        self.__logger.debug('Flow:flow1,StepNodeTag:2314162044320,Note:')
        iie.do_click_pos(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',url=r'https://inv-veri.chinatax.gov.cn/index.html',selector=r'#fpdm',button=r'left',curson=r'center',times=1,run_mode=r'unctrl',continue_on_error=r'break',waitfor=10)
        # 键盘输入
        self.__logger.debug('Flow:flow1,StepNodeTag:2314172690122,Note:输入发票代码')
        time.sleep(0.5)
        ikeyboard.key_send_cs(text='04403190011',waitfor=10)
        # 键盘输入
        self.__logger.debug('Flow:flow1,StepNodeTag:2314184991924,Note:')
        time.sleep(0.5)
        ikeyboard.key_send_cs(text='{TAB}',waitfor=10)
        # 键盘输入
        self.__logger.debug('Flow:flow1,StepNodeTag:2314191450626,Note:输入发票号码')
        time.sleep(0.5)
        ikeyboard.key_send_cs(text='23838102',waitfor=10)
        # 键盘输入
        self.__logger.debug('Flow:flow1,StepNodeTag:2314202733030,Note:')
        time.sleep(0.5)
        ikeyboard.key_send_cs(text='{TAB}',waitfor=10)
        # 键盘输入
        self.__logger.debug('Flow:flow1,StepNodeTag:2314205211432,Note:开票日期')
        time.sleep(0.5)
        ikeyboard.key_send_cs(text='20200611',waitfor=10)
        # 键盘输入
        self.__logger.debug('Flow:flow1,StepNodeTag:2314221025834,Note:')
        time.sleep(0.5)
        ikeyboard.key_send_cs(text='{TAB}',waitfor=10)
        # 键盘输入
        self.__logger.debug('Flow:flow1,StepNodeTag:2314221967436,Note:输入开具金额')
        time.sleep(0.5)
        ikeyboard.key_send_cs(text='937.34',waitfor=10)
      
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
    pro.flow1()
    ___logger = ILog(__file__)
    ___logger.debug('Class:Main,ProTag:Quit,Note:Exit')
