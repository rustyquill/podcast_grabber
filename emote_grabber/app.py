from flask import Flask
from emote_grabber.grabber import emote_grabber 
import json

app = Flask(__name__)

eg = emote_grabber()

cache_dir = '/tmp/'


@app.route('/<channel_name>')
def get_emotes(channel_name):
    cache_hit = check_cache(channel_name)
    if cache_hit is not None:
        return cache_hit
    if channel_name == 'favicon.ico' :
       return ''
    data = eg.get_emotes(channel_name)
    with open(cache_dir + channel_name, 'x') as cache:
        cache.write(json.dumps(data))
    return data

def check_cache(channel_name):
    try:
       with open(cache_dir + channel_name) as cache:
          data = json.load(cache)
    except:
       print('no cache')
       return None
    return data   


if __name__ == '__main__':
   app.run('0.0.0.0', port=5001)
