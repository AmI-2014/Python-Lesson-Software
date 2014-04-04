'''
Created on 06/mar/2014

@author: Dario Bonino <dario.bonino@polito.it>

Copyright (c) 2014 Dario Bonino
 
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
 
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
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
    