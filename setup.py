from setuptools import setup
with open('requirements.txt') as requirements:
   setup(
      name		= 'podcast_grabber',
      version		= '1',
      packages 		= ['podcast_grabber'],
      package_dir	= {'': '.'},
      author		= 'askmartyn',
      description	= 'Selenium based too for reporting on locations of our podcasts in various suppliers',
      install_requires	= [ req for req in requirements.readlines()]
   )
