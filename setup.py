from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Apple :: MacOS',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  'Programming Language :: Python :: 3.4',
  'Programming Language :: Python :: 3.5',
  'Programming Language :: Python :: 3.6',
]
 
setup(
  name='LivePrice',
  version='1.0',
  description='',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Ates Kursunoglu',
  author_email='ateskursunoglu2@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='stock price', 
  packages=find_packages(),
  install_requires=['bs4','requests'] 
)