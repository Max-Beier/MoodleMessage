from MoodleMessage.send import send


class MoodleMessage:
    hostname = ""
    session_token = ""

    def __init__(self, hostname, session_token) -> None:
        self.hostname = hostname
        self.session_token = session_token

    def send_message(self, text, conversation_id):
        send_text(text, conversation_id, self.hostname, self.session_token)
