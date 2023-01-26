from emote_grabber.emote_grabber import emote_grabber


EG           = emote_grabber()
CHANNEL_NAME = 'askmartyn'
TEST_EMOTE   = 'askmar1Eelee'
TEST_URL     = 'https://static-cdn.jtvnw.net/emoticons/v2/emotesv2_6a8f5678406e4b37983d0c19a71bdba1/static/light/2.0'



def test_get_channel_url():
    assert EG.get_channel_url(CHANNEL_NAME) == 'https://twitchemotes.com/channels/518594054'


def test_get_emotes():
    assert EG.get_emotes()[TEST_EMOTE] == TEST_URL
    
