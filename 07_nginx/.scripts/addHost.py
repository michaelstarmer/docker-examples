import string
import sys
import os

SITES_DIR = './data/nginx/sites.d/'
UPSTREAM_DIR = './data/nginx/'

# make sure we have only URI and PORT
if(sys.argv.__len__() != 3):
  print("\nYou must specify exacly 2 arguments: URI and PORT\nExample: ./addHost mywebsite.local 8080\n")
  exit()

# get args
inputUrl  = sys.argv[1]
inputPort = sys.argv[2]
site      = inputUrl.split('.')[0]

def validate():
  if (inputUrl.split('.').__len__() < 2):
    print("You have to add a full domain. Eg.: webapp.local 8080")
    exit()
  
  return True
  
class bcolors:
  GREEN = '\033[92m'
  RED = '\033[91m'
  BLUE = '\033[94m'
  ENDC = '\033[0m'

# Init. folders
def initializeDirs():
  try:
    os.makedirs('./data/nginx/sites.d')
    print('Created Nginx folders...')
  except FileExistsError:
    pass

def getExistingEntries():
  return [x.split('.')[0] for x in os.listdir(SITES_DIR)]

# Create .conf-file or append to existing
def addConf(newFile):
  filein = open(".scripts/template_site").read()
  
  filein = filein.replace('$URI', inputUrl)
  filein = filein.replace('$PORT', inputPort)
  
  f = open(SITES_DIR+site+'.conf', ('w+', 'a+')[newFile])
  f.write(filein)
  f.close()
  
validate()
initializeDirs()
addConf((False, True)[site in getExistingEntries()])

# add upstream entry
#upstream = open(UPSTREAM_DIR+'upstream.conf', 'a')

print('\nSuccessfully added '+inputUrl+':'+inputPort+' to nginx.\n'+bcolors.GREEN+'Remember to update your hosts-file: '+'127.0.0.1 '+inputUrl+'\n')
