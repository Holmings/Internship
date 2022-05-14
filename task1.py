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

isDomainDirect(sys.argv[1])