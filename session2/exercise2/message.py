from __future__ import annotations

class Message:
    def __init__(self, user: str, msg: str) -> None:
        self.message = msg
        self.user = user

    def encode(self) -> bytes:
        # joines attributes separated by |
        msg =  "|".join([self.user, self.message])
        # encode string in utf-8 encoding in a bytes object, required for sending
        msg = msg.encode()
        return msg
    
    @classmethod #definition of classmethod
    def parse(cls, msg:bytes) -> Message:
        # reverse to encode
        msg = msg.decode()
        msg = msg.split("|")

        # create Message object
        msg = Message(*msg)
        return msg
    
    def __repr__(self) -> str:
        return f"[{self.user}]: {self.message}"
