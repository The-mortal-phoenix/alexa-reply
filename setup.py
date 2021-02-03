from setuptools import setup, find_packages

setup(
  name='alexa-reply',
  version='0.1.2',
  description='An ai python package to respond to any message suitably',
  long_description=open('README.md').read(),
  long_description_content_type = "text/markdown",
  url = "https://github.com/The-mortal-phoenix/alexa-reply",  
  author='Phenoxis',
  author_email='1e1qwdqwe@gmail.com',
  license='MIT', 
  classifiers=[
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
  keywords='reply, ai, alexa, bot', 
  packages=find_packages(),
  install_requires=['requests'] 
)