from setuptools import setup

setup(
   name='src',
   version='1.0',
   description='Meme Generator for python',
   author='Julian Brandt',
   author_email='julianbrrandt@gmail.com',
   packages=['src'],
   install_requires=["pillow", "requests"],
)