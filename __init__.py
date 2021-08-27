from mycroft import MycroftSkill, intent_file_handler


class RespeakerLedArray(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('array.led.respeaker.intent')
    def handle_array_led_respeaker(self, message):
        self.speak_dialog('array.led.respeaker')


def create_skill():
    return RespeakerLedArray()

