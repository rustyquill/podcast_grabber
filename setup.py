from setuptools import setup
with open('requirements.txt') as requirements:
   setup(
      name		= 'emote_grabber',
      version		= '3.7',
      packages 		= ['emote_grabber'],
      package_dir	= {'': '.'},
      author		= 'askmartyn',
      description	= 'Selenium based too for importing channel twitch emotes',
      install_requires	= [ req for req in requirements.readlines()]
   )
