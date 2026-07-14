from events.member_join import member_join
from events.message_sent import message_sent
from events.ready import ready

def startEvents(bot):
    ready(bot)
    member_join(bot)
    message_sent(bot)
