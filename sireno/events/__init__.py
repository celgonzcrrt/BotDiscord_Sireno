from .member_join import member_join
from .message_sent import message_sent
from .ready import ready

def startEvents(bot):
    ready(bot)
    member_join(bot)
    # message_sent(bot)
