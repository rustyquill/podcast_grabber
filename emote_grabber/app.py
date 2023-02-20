import json
import os
from flask import Flask, jsonify
from emote_grabber.grabber import emote_grabber 


CACHE_DIR = '/tmp/emotes/'

try:
    os.makedirs(CACHE_DIR)
except FileExistsError:
    pass

APP = Flask(__name__)
app = APP 
EG = emote_grabber()
CACHE_HITS = [ _ for _ in os.walk(CACHE_DIR)][0][2]


def create_emoji_dict(cache_hits):
    emoji_dict = {}
    for cache_file in cache_hits:
       print(cache_file)
       with open(CACHE_DIR + cache_file) as cache_file:
          emoji_dict.update(json.load(cache_file))
    return emoji_dict 

EMOJI_DICT = create_emoji_dict(CACHE_HITS)

@APP.route('/channels')
def get_channels():
    return jsonify( { "Response": CACHE_HITS } )



@APP.route('/channel/<channel_name>')
def get_emotes(channel_name):
    global EMOJI_DICT
    global CACHE_HITS
    if channel_name == 'favicon.ico' :
       return ''
    cache_hit = check_cache(channel_name)
    if cache_hit is not None:
        return cache_hit
    data = EG.get_emotes(channel_name)
    with open(CACHE_DIR + channel_name, 'x') as cache:
        cache.write(json.dumps(data))
        CACHE_HITS.append(channel_name)
    EMOJI_DICT = create_emoji_dict(CACHE_HITS)
    print(data)
    return jsonify(data)

@APP.route('/emote/<emote_name>')
def get_emojis(emote_name):
    response =  jsonify({'Response': EMOJI_DICT.get(emote_name)}
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@APP.route('/emotes')
def get_all_emojis():
    response = jsonify({ "Response": [ _ for _ in EMOJI_DICT.keys() ] } )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


def check_cache(channel_name):
    if channel_name in CACHE_HITS:
       with open(CACHE_DIR + channel_name) as cache:
          data = json.load(cache)
       return data
    print('no cache')
    return None

if __name__ == '__main__':
   APP.run('0.0.0.0', port=5000)
