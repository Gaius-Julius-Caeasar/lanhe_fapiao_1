# coding=utf-8
# 编译日期：2020-06-23 15:27:45
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
      
    def flow1(self):
        code=None
        yzm_pic=None
        tishi=None
        #RPACodeMarked.....2314350501348
        # While循环
        self.__logger.debug('Flow:flow1,StepNodeTag:2314350501348,Note:')
        while 1:
            # 鼠标点击
            self.__logger.debug('Flow:flow1,StepNodeTag:23151109681113,Note:')
            time.sleep(0.5)
            iie.do_click_pos(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',url=r'https://inv-veri.chinatax.gov.cn/index.html',selector=r'#yzm_img',button=r'left',curson=r'center',times=1,run_mode=r'unctrl',continue_on_error=r'break',waitfor=10)
            time.sleep(0.5)
            # 鼠标移动
            self.__logger.debug('Flow:flow1,StepNodeTag:23151501542118,Note:')
            iie.do_moveto_pos(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',url=r'https://inv-veri.chinatax.gov.cn/index.html',selector=r'#content2 > TABLE:nth-of-type(1) > TBODY:nth-of-type(1) > TR:nth-of-type(6) > TD:nth-of-type(1)',curson=r'center',waitfor=10)
            time.sleep(5)
            # 截图
            self.__logger.debug('Flow:flow1,StepNodeTag:2314353040452,Note:')
            tishi = iimg.capture_image(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',win_text=r'',left_indent=1253,top_indent=572,width=210,height=36,waitfor=30)
            time.sleep(0.8)
            # 截图
            self.__logger.debug('Flow:flow1,StepNodeTag:2314360485954,Note:')
            yzm_pic = iimg.capture_image(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',win_text=r'',left_indent=992,top_indent=620,width=139,height=64,waitfor=30)
            time.sleep(0.8)
            # 自定义函数
            self.__logger.debug('Flow:flow1,StepNodeTag:2314544729489,Note:')
            tvar2314544729489 = GlobalFun.code_color(tishi,yzm_pic)
            #验证码
            self.__logger.debug('Flow:flow1,StepNodeTag:2314593469491,Note:')
            code = iocr.vcode_recognize(image_path=tvar2314544729489,code_type=8001,apiKey='8159a500cc9d4a69a71e6ac14263f029',secretKey='2d078aa8c13741239b3d00ced85832e3')
            time.sleep(1)
            # 鼠标点击
            self.__logger.debug('Flow:flow1,StepNodeTag:23152443697126,Note:')
            iie.do_click_pos(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',url=r'https://inv-veri.chinatax.gov.cn/index.html',selector=r'#yzm',button=r'left',curson=r'center',times=1,run_mode=r'unctrl',continue_on_error=r'break',waitfor=10)
            # 键盘输入
            self.__logger.debug('Flow:flow1,StepNodeTag:23150746702109,Note:')
            time.sleep(0.5)
            ikeyboard.key_send_cs(text=code,waitfor=10)
            # 鼠标点击
            self.__logger.debug('Flow:flow1,StepNodeTag:23152606550130,Note:')
            iie.do_click_pos(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',url=r'https://inv-veri.chinatax.gov.cn/index.html',selector=r'#checkfp',button=r'left',curson=r'center',times=1,run_mode=r'unctrl',continue_on_error=r'break',waitfor=10)
            time.sleep(1)
            # 图像检测
            self.__logger.debug('Flow:flow1,StepNodeTag:23152545559128,Note:')
            tvar23152545559128 = iimg.img_exists(win_title=r'国家税务总局全国增值税发票查验平台 - Internet Explorer',img_res_path=self.path,image=r'snapshot_20200623152556855.png',fuzzy=True,confidence=0.85,waitfor=5)
            # IF-N分支
            self.__logger.debug('Flow:flow1,StepNodeTag:23152627191132,Note:')
            if tvar23152545559128:
                # Continue继续
                self.__logger.debug('Flow:flow1,StepNodeTag:23152712119137,Note:')
                continue
            else:
                # Break中断
                self.__logger.debug('Flow:flow1,StepNodeTag:23152722614139,Note:')
                break
      
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
