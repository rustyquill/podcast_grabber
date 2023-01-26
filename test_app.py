from emote_grabber.app import get_emotes
TEST_EMOTE = 'askmar1Lookballs'


def test_get_channel_url():
    assert TEST_EMOTE in get_emotes('askmartyn')
