import requests
import string
import json


def getInfo():
    files = open('doc', 'w')
    watSub = input('What subreddit? ')
    r2 = requests.get('http://www.reddit.com/r/' + watSub + '.json')
 
    
    j2 = json.loads(r2.text)
    
    #pprint(j2)  #here's the final respone, printed out nice an readable format
    #ed2 = str(j2)
    x = j2[u'data'][u'children']
    #pprint(x)
    for info in x:
         contentText = info[u'data'][u'selftext']      
         ContentText = str(contentText)
         
         contentTitle = info[u'data'][u'title']
         contentTitle = str(contentTitle)
         
         contentScore = info[u'data'][u'score']
         contentScore = str(contentScore)
         
         contentUrl = info[u'data'][u'url']
         contentUrl = str(contentUrl)
         
         contentAuthor = info[u'data'][u'author']
         contentAuthor = str(contentAuthor)
         
         
         titleData = open('titleData', 'w')
         titleData.write(watSub)
         titleData.write(' - ')
         titleData.write(contentTitle)
         titleData.close()
         redditData = open('redditdrawn', 'w')
         redditData.write('<h1><strong>')
         redditData.write(contentTitle)
         redditData.write('</strong></h1><p>')
         redditData.write(contentText)
         redditData.write(' Score: ')
         redditData.write(contentScore)
         redditData.write('<p><img alt="" src="')
         redditData.write(contentUrl)
         redditData.write('" width="800" height="600" />')
         redditData.write(' <i><h3> - ')
         redditData.write(contentAuthor)
         redditData.write('</i></h3>')
         redditData.close()
        
getInfo()
