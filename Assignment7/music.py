from music21 import *

mysong = "tinynotation: 4/4 c4 c4 c4 d8 e4 e4 d8 e4 f8 g4 c'8 c'8 c'8 g8 g8 g8 e8 e8 e8 c8 c8 c8 g4 f8 e4 d8 c4"

# a b c d e f g

# 4 quarter note
# 8 eighth note

x = converter.parse(mysong)

#Write to a location that you can access -- this is MY location
x.write("MusicXML","C:\\Users\\Hyeon Jin Ryu\\Desktop\\MusicXML.xml")

