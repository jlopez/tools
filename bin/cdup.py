#!/usr/bin/env python
import glob
import os
import os.path
import sys

if len(sys.argv) != 2:
  print '..'
  sys.exit()
target = sys.argv[1]
cwd = os.getcwd()
while True:
  paths = glob.glob(os.path.join(cwd, target))
  if paths:
    print paths[0]
    break
  cwd = os.path.abspath(os.path.join(cwd, '..'))
  if cwd == '/':
    print '.'
    break
