import requests
import string
import json
import random
from pprint import pprint
from clint.textui import puts, colored

def rectxt():
    numb = random.randint(0,30)
    numb = str(numb)
    #categ  = input('Which number: ')
    r2 = requests.get('http://api.trademe.co.nz/v1/Search/General.json?category=' + numb + '&sort_order=BidsMost')
    r3 = requests.get('http://api.trademe.co.nz/v1/Listings/Latest.json')
    j2 = json.loads(r2.text)
    j3 = json.loads(r3.text)
    #pprint(j2)  #here's the final respone, printed out nice an readable format
    #ed2 = str(j2)
    x = j3[u'List']
    #pprint(x)
    for info in x:
         ContentPath = info[u'CategoryPath']      
         ContentPath = str(ContentPath)
        
         ContentRegion = info[u'Region']
         ContentRegion = str(ContentRegion)
         
         ContentTitle = info[u'Title']
         ContentTitle = str(ContentTitle)
         
         ContentBuyNow = info[u'PriceDisplay']
         ContentBuyNow = str(ContentBuyNow)
         
         ContentSuburb = info[u'Suburb']
         ContentSuburb = str(ContentSuburb)
         #ContentImage = info[u'PictureHref']
         #ContentImage = str(ContentImage)
         #pprint(ContentTitle)
         #puts(colored.red(ContentTitle))
         #pprint(ContentPath)
         #puts(colored.white(ContentPath))
         #pprint(ContentRegion)
         #puts(colored.green(ContentRegion))
         #pprint(ContentBuyNow)
         files = open('tradeData', 'w')
         title = open('tradeTitle', 'w')
         #imagePic = open('imagePic', 'w')
         #imagePic.write(ContentImage)
         #imagePic.close()
         title.write(ContentTitle)
         title.close()
         files.write('<h1> <p>')
         files.write(ContentTitle)
         files.write('</h1></p><h2><p>')
         files.write('Buy now: ') 
         files.write(ContentBuyNow)
         files.write('</p>')
         files.write('Area: ')
         files.write(ContentRegion)
         files.write(', ')
         files.write(ContentPath)
         files.write(' - ')
         files.write(ContentSuburb)
         files.write('</h2>')
         #files.write('<img class=\"aligncenter\" alt=\"\" src =\"')
         #files.write(ContentImage)
         #files.write('\" width=\"300\" height=\"150\" />')
         files.close()
rectxt()
