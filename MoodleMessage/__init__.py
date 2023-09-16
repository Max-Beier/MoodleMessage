from MoodleMessage.send import send_text


class Messanger:
    hostname = ""
    session = ""
    session_token = ""
    conversation_id = ""

    def __init__(self, hostname, session_token, conversation_id, session) -> None:
        self.hostname = hostname
        self.session_token = session_token
        self.conversation_id = conversation_id
        self.session = session

    def send_text(self, text):
        send_text(text, self.conversation_id, self.hostname, self.session, self.session_token)

    def send_image(self, image_url):
        text = f'<img src="{image_url}"/>'
        send_text(text, self.conversation_id, self.hostname, self.session_token, self.session)
