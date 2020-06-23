# coding=utf-8
# 编译日期：2020-06-23 15:59:20
# 版权所有：www.i-search.com.cn
import time
import pdb
from ubpa.ilog import ILog
from ubpa.base_img import *
import getopt
from sys import argv
import sys
import ubpa.iocr as iocr
import ubpa.itools.rpa_str as rpa_str

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
        #RPACodeMarked.....2314131980112
        #增值税发票OCR
        self.__logger.debug('Flow:flow1,StepNodeTag:2314131980112,Note:')
        tvar2314131980112 = iocr.vat_recognize(image_path='C:/Users/jky/Desktop/微信图片_20200623100526.png',apiKey='	8159a500cc9d4a69a71e6ac14263f029',secretKey='2d078aa8c13741239b3d00ced85832e3')
        # 输出
        self.__logger.debug('Flow:flow1,StepNodeTag:23155752736173,Note:')
        rpa_str.iprints(tvar2314131980112)
      
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
