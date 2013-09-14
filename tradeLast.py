'''
Created on 6/12/2012
 
@author: Will
'''
import pylast
import pprint
from subprocess import Popen
API_KEY = '917060f2353e4ad89224f2295e146ddf'
API_SECRET = '9407d29e78647abbc1bc440d94aa1f70'
passworz = 'eatgrass123'
username = "galf666"
password_hash = pylast.md5(passworz)

network = pylast.LastFMNetwork(API_KEY, api_secret =
API_SECRET, username=username, password_hash=password_hash)
 
#arti = input("Enter the artist name: ")

artLord = input('Artist: ')
artist = network.get_artist(artLord)

#album = network.get_album(artist)

 
artBio = artist.get_bio_content()
pprint.pprint(artBio)
#artSimilar = artist.get_similar(20)
#artSimilar = str(artSimilar)
#pprint.pprint(artSimilar)

artImage = artist.get_cover_image(size=4)
pprint.pprint(artImage)
Popen(["firefox", artImage])

#artDefulat = artist.get_top_albums()
#artDefalat = str(artDefulat)
#pprint.pprint(artDefulat)

artPower = artist.get_bio_summary()
artPower = str(artPower)
pprint.pprint(artPower)
#artTop = artist.get_top_tracks()
#pprint.pprint(artTop) 
 
#topTrack = artist.getTopTracks()
#pprint.pprint(topTrack) 



doc = open('LastData', 'w')
doc.write('<h2><b>')
doc.write(artLord)
doc.write('</h2></b>')
#doc.write(artBio)
doc.write('Breaking News: ')
#doc.write(artPower)
doc.write(' - ')
#doc.write(artDefalat)
doc.write('<img class=\"aligncenter\" alt=\"\" src =\"')
doc.write(artImage)
doc.write('\" width=\"60\" height=\"30\" />')
#doc.write(artSimilar)
doc.close
