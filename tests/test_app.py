from emote_grabber.app import get_emotes


def test_get_channel_url():
    assert 'askmar1Eelee' in get_emotes('askmartyn')
    assert 'limmy4k' in get_emotes('limmy')


