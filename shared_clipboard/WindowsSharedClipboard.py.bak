# The Windows SharedClipboard Module (WindowsSharedClipboard.py). 
# This module uses the win32clipboard APIs from the Win32 extensions to access the Windows clipboard.

import win32clipboard

def openClipboard():
  win32clipboard.OpenClipboard()

def closeClipboard():
  try:
    win32clipboard.CloseClipboard()
  except Exception, e:
    print e
    pass

def getClipboardData():
  from win32clipboard import CF_TEXT
  if win32clipboard.IsClipboardFormatAvailable(CF_TEXT):
    return win32clipboard.GetClipboardData()
  else:
    return None

def setClipboardData(data):
  win32clipboard.EmptyClipboard()
  win32clipboard.SetClipboardData(win32clipboard.CF_TEXT, data)