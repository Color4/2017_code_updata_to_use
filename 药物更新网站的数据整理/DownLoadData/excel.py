# -*- coding: utf-8 -*-
#!/usr/bin/python
#__author__= "PengZhang"

import xlrd
import xlwt
import os
import sys 

def read_excel():
	workbook = xlrd.open_workbook(r'1.xls')
	##print workbook.sheet_names()
	sheet2_name = workbook.sheet_names()[0]
	sheet2 = workbook.sheet_by_index(0)
	#sheet2 = workbook.sheet_by_name(sheet2)
	for i in range(2,22):
		rows_sample = sheet2.row(i)[1].value.encode('utf-8')
		rows_stats = sheet2.row(i)[2].value.encode('utf-8') 
		rows_names = sheet2.row(i)[3].value.encode('utf-8')
		rows_used = sheet2.row(i)[4].value.encode('utf-8')
		rows_title = sheet2.row(i)[5].value.encode('utf-8')
		print rows_sample, rows_stats, rows_names, rows_used, rows_title
	#rows = sheet2.row_values().encode('utf-8')

#read_excel()
	
with open('/work/home/zhangp/DownLoadData/output_v1.txt', 'w')as stat: 
	with open('/work/home/zhangp/DownLoadData/output_v2.txt', 'w')as stat_v1:
		for j in range(1,246):
		#for j in range(1,3):
			down_load_path = 'curl http://www.chinadrugtrials.org.cn/eap/clinicaltrials.downloadExcel?currentpage='+ str(j) +'> 1.xls'
			os.system(down_load_path)
			workbook = xlrd.open_workbook(r'1.xls')
			sheet2_name = workbook.sheet_names()[0]
			sheet2 = workbook.sheet_by_index(0)
			for i in range(2,22):
				rows_sample = sheet2.row(i)[1].value.encode('utf-8')
				rows_stats = sheet2.row(i)[2].value.encode('utf-8')
				rows_names = sheet2.row(i)[3].value.encode('utf-8')
				rows_names = rows_names.replace('\r','').replace('\n','').replace('\t','')
				rows_used = sheet2.row(i)[4].value.encode('utf-8')
				rows_used = rows_used.rstrip()
				rows_used = rows_used.rstrip('\n')
				rows_used = rows_used.rstrip('\t')
				rows_used = rows_used.rstrip('\r')
				rows_used = rows_used.replace('\r','').replace('\n','').replace('\t','').replace(' ','')
				rows_title = sheet2.row(i)[5].value.encode('utf-8')
				rows_title = rows_title.replace('\r','').replace('\n','').replace('\t','')
				print rows_sample, rows_stats, rows_names, rows_used, rows_title
				stat.write('%s\t%s\t%s\t%s\t%s\n'%(rows_sample,rows_stats,rows_names,rows_used,rows_title))
				stat_v1.write('%s\t%s\t%s\t%s\n'%(rows_sample,rows_stats,rows_names,rows_title))
