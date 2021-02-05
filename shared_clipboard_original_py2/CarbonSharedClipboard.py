# This module uses the native Carbon APIs to access the Mac clipboard.
 
from Carbon.Scrap import (GetCurrentScrap,
                          ClearCurrentScrap)
import MacOS

def getClipboardData():
    try:
      scrap = GetCurrentScrap()
      return scrap.GetScrapFlavorData(flavorType='TEXT')
    except MacOS.Error, e:
      if e[0] != -102:
            # -102 == noTypeErr
            raise
      return ''

def setClipboardData(data):
  ClearCurrentScrap()
  scrap = GetCurrentScrap()
  scrap.PutScrapFlavor(flavorType='TEXT', 0, text)

def openClipboard():
  pass # no-op on the mac

def closeClipboard():
  pass # no-op on the mac
