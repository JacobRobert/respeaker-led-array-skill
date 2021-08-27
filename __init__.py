from mycroft import MycroftSkill, intent_file_handler
from four_mic_hat_interfaces.pixels import Pixels


class RespeakerLedArray(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        LED_pattern = self.settings.get('LED_pattern')

    @intent_file_handler('array.led.respeaker.intent')
    def handle_array_led_respeaker(self, message):
        self.speak_dialog('array.led.respeaker')


def create_skill():
    return RespeakerLedArray()

