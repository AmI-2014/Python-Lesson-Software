'''
Created on 06/mar/2014

@author: bonino
'''
import pyglet

def play(filename):
    #load the mp3 file
    mp3 = pyglet.media.load(filename, None, True)
    
    # show audio data
    print "format: ", mp3.audio_format
    print "duration: ", mp3.duration
    
    #play
    mp3.play()
       
    #schedule app stop after 20s
    pyglet.clock.schedule_once(lambda d: pyglet.app.exit(), 20)
    
    #run pyglet
    pyglet.app.run()
    

if __name__ == '__main__':
    play(r'blues.mp3') #r stands for raw string
    