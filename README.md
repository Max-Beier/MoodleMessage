# (Unofficial) MoodleMessage API

# How to use
main.py
```py
from MoodleMessage import Messenger


def main():
    hostname = "moodle.myserver.com"
    session = "hpgsmddfs06z7ahih0j1meeih9"
    session_token = "DwYPutoMM5"
    conversation_id = "12218"

    messanger = Messenger(hostname=hostname, session=session, session_token=session_token, conversation_id=conversation_id)

    messanger.send_text(text="Hello, this is foo!")

main()
```
