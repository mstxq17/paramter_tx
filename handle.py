#! /usr/bin/python
# -*- coding:utf-8 -*-

import re
import urlparse
import matplotlib.pyplot as plt
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# import pandas as pd 


def Getparams(filename):
	param_dict = {}
	pattern = re.compile(r'http://(.*?)/')
	with open(filename,"r") as f1:
		for lines in f1:
			result = pattern.match(lines)
			if result is not None:
				if urlparse.urlparse(lines).query != '':
			 		for param in urlparse.urlparse(lines).query.split('&'):
			 			if param !='\n' and param !='': 
			 				param = param.strip()
			 				host = result.group(0)
			 				param_dict.setdefault(host,set()).add(param.split('=')[0]) #一键对多个值 利用set可以去重复

	# print param_dict
	#进行合并 先转为数组 在利用字典特性
	param_list=[]
	param_num = {}
	for key, value in param_dict.items():
		param_list=param_list+list(value)
	for i in param_list:
		if param_list.count(i)>1:
			param_num[i] = param_list.count(i)
	return param_num
	
		#test http://pubgm.qq.com/zlkdatasys/a20171229jdcs/index.shtml?id=17&test=1
	# url  = 'http://pubgm.qq.com/zlkdatasys/a20171229jdcs/index.shtml?id=17&test=1'
	# for param in urlparse.urlparse(url).query.split('&'):
	# 	print param.split('=')[0]
def  GetPieChart(param_num):
	s = param_num #方便写代码 后期代换
	s_lables = list(sorted(s.keys())) #获取字典的键值并且进行排序操作
	s_sizes = [s.get(s_lables[i]) for i in range(len(s_lables))]
	fig =  plt.figure(figsize=(15,8)) #创建图表
	patches,l_text,p_text = plt.pie(x=s_sizes,labels=s_lables,autopct='%3.1f%%',shadow=True,labeldistance=1.1,startangle=90,pctdistance=0.6)
	plt.legend(loc= 'upper center',bbox_to_anchor=(-0.1,1))
	plt.title('param',fontsize=25)
	plt.show()
	plt.savefig('piechart.png')
def  GetBarChart(s):
	s_lables = list(sorted(s.keys())) #获取字典的键值并且进行排序操作
	s_sizes = [s.get(s_lables[i]) for i in range(len(s_lables))]
	fig = plt.figure(figsize=(12,8)) #创建宽12 长8的大小图表
	ax1 = fig.add_subplot(111)
	ax1.set_title('Param Analy')
	N = len(s_lables)
	xticks = np.arange(N)
	width = 3
	bars = ax1.bar(xticks,s_sizes,width=width,edgecolor='none',color='#87CEFA')
	#设置 x y轴坐标
	ax1.set_xlabel('key')
	ax1.set_ylabel('value')
	#赋x值
	ax1.set_xticks(xticks)
	#ax1.set_xticklabels(s_lables,size='small',rotation=45)
	ax1.set_xticklabels('')
	plt.show()
	plt.savefig('barchart.png')
def SaveFile(s):
	with open('param_handle.txt',"w") as f1:
		for i in s.keys():
			f1.write(i+'\n')
	f1.close()


def main():
	filename="param.txt"
	param_num = Getparams(filename)
	#GetPieChart(param_num)
	GetBarChart(param_num)
	SaveFile(param_num)
if __name__ == '__main__':
	main()
