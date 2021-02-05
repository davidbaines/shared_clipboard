#This module uses the sub-process module to invoke the pbcopy and pbpaste command line utilities, so it should work on all Mac OS X versions.

 
import subprocess

def getClipboardData():
  p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
  retcode = p.wait()
  data = p.stdout.read()
  return data

def setClipboardData(data):
  p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
  p.stdin.write(data)
  p.stdin.close()
  retcode = p.wait()

def openClipboard():
  pass # no-op on the mac

def closeClipboard():
  pass # no-op on the mac
