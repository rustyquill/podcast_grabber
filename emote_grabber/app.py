from flask import Flask
from emote_grabber.grabber import emote_grabber 
app = Flask(__name__)


@app.route('/<channel_name>')
def get_emotes(channel_name):
    if channel_name == 'favicon.ico' :
       return ''
    eg = emote_grabber(channel_name)
    emotes = eg.get_emotes()
    return emotes


if __name__ == '__main__':
   app.run('0.0.0.0', port=5001)
