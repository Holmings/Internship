import urllib.request, json 
import sys


with urllib.request.urlopen("https://openx.com/sellers.json") as url:
    data = json.loads(url.read().decode())
  

def isDomainDirect(name):
    for seller in data['sellers']:
        if seller['domain']==name:
            if seller['seller_type'] == "INTERMEDIARY":
              print("Indirect")
            elif seller['seller_type'] == "PUBLISHER":
              print("Direct")
            break
def MaxDepth():
  i=0
  for client in data['sellers']:
    i=i+1
  print("Max depth is: ", i)

if sys.argv[1] == 'max':
  MaxDepth()
else:
  isDomainDirect(sys.argv[1])
