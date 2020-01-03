#!/usr/bin/env python3

from fedora_messaging.api import publish, Message
from fedora_messaging.config import conf

conf.setup_logging()
message= Message(
    topic="tutorial.topic",
    body={'reason': "test message"}
)
publish(message)
