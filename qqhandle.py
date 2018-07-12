#!/usr/bin/python
# -*- coding:utf-8 -*- 

import re

#不用处理规则里面的特殊符号比如/n //n
Dominlist = []
pattern=re.compile(r"(.*?)[^qzone|114].qq.com")
with open("qq.txt","r") as f:
	for lines in f:
		result=pattern.match(lines)
		if result is not None:
			Dominlist.append(result.group(0))
del Dominlist[:15]
# print Dominlist
f.close()
f1 = open("qqhandle.txt","w")
for url in Dominlist:
	f1.write("http://"+url.strip()+'\n')




