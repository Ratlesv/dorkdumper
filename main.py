import time
from googlesearch import search
from duckduckgo_search import ddg
import sys, getopt
def showAscii(path, delay):
  with open(path, "r") as file:
    for line in file:
      time.sleep(delay)
      print(line, end="")
  time.sleep(0.5)
temp_dorkfile = "dorks.txt"
sleep = True
def yn(a):
  if a == "y" or a == "Y":
    return True
  elif a == "n" or a == "N":
    return False


def quit(conf):
  if conf:
    confirm = input("Are you sure you want to quit? (Y/N)")
    if yn(confirm):
      print("goodbye, world")
      sys.exit()
def promptString(message, default = "default"):
   _str = input(message)
   if _str != "":
     return(_str)
   else:
     return(default)
def promptInt(message):
  _int = input(message)
  if _int.isdigit():
    return(int(_int))
  else:
    promptInt(message)
def yesNoQuit(answer, defaultTo="y", confirmQuit=True):
  if answer == "y" or answer == "Y":
    return (True)
  elif answer == "n" or answer == "N":
    return (False)
  elif answer == "q" or answer == "Q":
    quit(confirmQuit)
  elif defaultTo == "y":
    print("invalid input, defaulting to yes")
    return (True)

  elif defaultTo == "n":
    return (False)
  elif defaultTo == "q":
    quit(confirmQuit)
    print("exiting...")


showAscii("skull.txt", 0.05)
sleepTime = 3

dorkFile = None
try:
  dorkFile = sys.argv[1]
except:
  dorkFile = "bulk.txt"
  print("No file detected. Using default filename of bulk.txt")
try: 
  with open(dorkFile, "r") as textInstance:
    pass
except: 
  print(dorkFile + " is not a valid bulk file.")
  sys.exit()
try:
  sleepTime = sys.argv[2]
except:
  pass
print("\n")


def handleVolumeError(dork, amnt, recursion):
  if recursion > 5:
    return
  print("Handling ddg captcha")
  try:
    counter = 0
    if sleep:
      time.sleep(6 - recursion)
    for item in ddg(dork):
      counter += 1
      urlList.append(item)
      if counter == amnt:
        break
  except:
    handleVolumeError(dork, amnt, recursion + 1)


outputFilename = promptString("Name the log file: ", "dorkdump_output")
print("Saving results to " + outputFilename)
outputFilename += ".txt"
try:
  with open(outputFilename, "x") as testFileInstance:
    pass
except:
  print(
    "Invalid filename. There is either already a file at the destination path, or something else is wrong, who the fuck knows."
  )
  sys.exit()
dorkList = []
urlList = []
with open(dorkFile, "r") as bulk_dork_file:
  print("-Reading dorks from file " + dorkFile + '...\n')
  for line in bulk_dork_file:
    dorkList.append("inurl:" + line)

  print("\n" + str(len(dorkList)) + " DORKS LOADED: \n")

  for dork in dorkList:
    print(dork, end="")
  if sleep:
    time.sleep(0.5)
  print("\n")
  numResults = promptInt("Max results per dork? (minimum of 10) ")
  if numResults < 10:
    numResults = 10
    print("Below minimum value. Defaulting to 10 results per dork")
  print("\n Running searches for " + str(len(dorkList)) +
        " dorks with a maximum of " + str(numResults * len(dorkList)) +
        " results...")
  for dork in dorkList:
    if sleep:
        time.sleep(sleepTime)
    print('getting results for dork "' + dork + '"...\n')
    try:
      for item in search(dork, numResults):
        urlList.append(item)
    except:
       time.sleep(1)
       print("CAPTCHA error. Using duckduckgo-search API instead...")
       counter = 0
       try:
        for item in ddg(dork):
          counter += 1
          urlList.append(item)
          if counter == numResults:
            break
       except:
        handleVolumeError(dork, numResults, 0)
     
  with open(outputFilename, "a") as outFile:
    print("finished searching, writing results to log file...")
    for url in urlList:
      try:
        outFile.write(url + '\n')
      except:
        outFile.write(url["href"] + '\n')

  print("Done writing results to file " + outputFilename + ".")
