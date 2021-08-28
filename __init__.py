from mycroft import MycroftSkill, intent_file_handler
#import sys
#sys.path.append('./four_mic_hat_interface')
from .pixels import Pixels
#import pixels
#from .test import test

class RespeakerLedArray(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        LED_pattern = self.settings.get('LED_pattern')
        self.pixels = Pixels(LED_pattern)

        '''Link to all message event types: https://mycroft-ai.gitbook.io/docs/mycroft-technologies/mycroft-core/message-types'''
        
        
        self.add_event('recognizer_loop:record_begin', self.handle_listener_started)  
        self.add_event('recognizer_loop:record_end', self.handle_listener_ended)
        self.add_event('recognizer_loop:wakeword', self.handle_wakeword)
        self.add_event('mycroft.awaken', self.handle_mycroft_awoken)
        self.add_event('mycroft.stop' , self.handle_mycroft_stop)
        self.add_event('recognizer_loop:sleep', self.handle_sleep)
        #self.add_event('speak', self.handle_speak)
        self.add_event('recognizer_loop:audio_output_start', self.handle_audio_output_start)
        self.add_event('recognizer_loop:audio_output_end', self.handle_audio_output_end)

    #     #self.add_event('complete_intent_failure', self.handle_complete_intent_failure)
    #     #mycroft.audio.service

    

    def handle_listener_started(self, message):
        self.pixels.listen()

    def handle_listener_ended(self, message):
        self.pixels.think()
    
    def handle_wakeword(self, message):
        self.pixels.wakeup()
    
    def handle_mycroft_awoken(self, message):
        self.pixels.wakeup()

    def handle_mycroft_stop(self, message):
        self.pixels.off()

    def handle_sleep(self, message):
        self.pixels.off()

    def handle_speak(self, message):
        self.pixels.speak()

    def handle_audio_output_start(self, message):
        self.pixels.speak()

    def handle_audio_output_end(self, message):
        self.pixels.off()


    #def handle_complete_intent_failure(self):



def create_skill():
    return RespeakerLedArray()

