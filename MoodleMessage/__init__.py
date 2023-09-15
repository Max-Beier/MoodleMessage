from MoodleMessage.send import send_text


class MoodleMessage:
    hostname = ""
    session_token = ""
    conversation_id = ""

    def __init__(self, hostname, session_token, conversation_id) -> None:
        self.hostname = hostname
        self.session_token = session_token
        self.conversation_id = conversation_id

    def send_message(self, text):
        send_text(text, self.conversation_id, self.hostname, self.session_token)

    def send_image(self, image_url):
        text = f'<img src="{image_url}"/>'
        send_text(text, self.conversation_id, self.hostname, self.session_token)

    def send_text_array(self, text_array):
        for text in text_array:
            pass

    def send_image_array(self, image_url_array):
        for url in image_url_array:
            pass