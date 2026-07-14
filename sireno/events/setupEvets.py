from member_join import member_join
from ready import ready
from message_sent import message_sent

def startEvents(bot):
    ready(bot)
    member_join(bot)
    message_sent(bot)