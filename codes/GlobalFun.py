# 编译日期：2020-06-23 14:53:35
# 版权所有：www.i-search.com.cn
# coding=utf-8
from PIL import Image

def code_color(a,b):
    
    blank_img=Image.open(r'C:\Users\jky\Desktop\123.png')
    base_img = Image.open(a)  #第一张图片，提示文字
    tmp_img = Image.open(b)  #第二张图片，验证码截图
    blank_img.paste(base_img,(0,0))  #以第一张图的左上角为坐标原点（0，0）为基础拼接图片
    blank_img.paste(tmp_img,(60,60))  #以第一张图的左上角为坐标原点（0，0）为基础拼接图片
    #blank_img.show()  #显示拼接后的图片,如果想查看拼接后的图片，可以将此行前面的注释符号#删除
    #base_img.paste(tmp_img,(0,0))  #以第一张图的左上角为坐标原点（0，0）为基础拼接图片
    #base_img.show()  #显示拼接后的图片,如果想查看拼接后的图片，可以将此行前面的注释符号#删除
    c=r'C:\Users\jky\Desktop\456.png'  #拼接后的图片保存路径
    blank_img.save(c)  #保存拼接后的图片
    return c  #返回拼接后的图片路径