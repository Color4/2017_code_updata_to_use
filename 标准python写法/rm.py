#!/usr/bin/python
# -*-coding: utf-8 -*-
# __author__ = "PengZhang"

import os
import string
import argparse
import shutil
import json
import time
import subprocess
import sys
import time

usage = "写任务参数的抬头标准，生产使用\n"
usage += "\n"
usage += "重要信息说明，让人读的\n"
usage += "---------举个栗子----------\n"
usage += "\n"
usage += "这个必须有\n"

parser = argparse.ArgumentParser(description = usage)
parser.add_argument("-i", "--id", help="帮助说明信息，必填时候复制", required = True)
parser.add_argument("-o", "--output_dir", help="帮助说明信息，必填时候复制", required = True)
parser.add_argument("-t", "--time", help="帮助说明信息，选择填写时候复制，会给默认参数", default = 20)

args = vars(parser.parse_args())

if args['output_dir'] and not os.path.exists(args['output_dir']):
	os.mkdir(args['output_dir'])

try:
	args['time'] = int(args['time'])
except:
	print "一些解释说明，系统退出"
	sys.exit(0)

print args['output_dir']
print args['id']
print args['time']


