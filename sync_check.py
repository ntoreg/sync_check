#!/bin/env python
# -*- coding: utf-8 -*-
#
# Check if the files are synchronized
# 同じ内容のファイルがある場合一方を削除してシンボリックリンクにする。

import sys
import glob
import os
import subprocess

dir1 = 'dir1'
dir2 = 'dir2'
files = glob.glob(dir1 + '/*.ext')

for file in files:
    file_name = os.path.basename(file)
    cmd_diff = "/usr/bin/diff -Bwu %s/%s %s/%s" % (dir1, file_name, dir2, file_name)
    ret = subprocess.Popen(cmd_diff, shell=True, stdout=subprocess.PIPE)
    line = str(ret.stdout.read())
    if not line:
        print "- [ ] %s" % file # Markdown format
        cmd_mv = "mv %s %s/%s_old" % (file, dir1, file_name)
        cmd_ln = "cd %s && /bin/ln -s ../%s/%s" % (dir1, dir2, file_name)
        subprocess.Popen(cmd_mv, shell=True)
        subprocess.Popen(cmd_ln, shell=True)
    else:
        print "- [ ] %s" % file
        print '```'
        print line
        print '```\n'

