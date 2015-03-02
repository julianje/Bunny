from setuptools import setup

def readme():
	with open('README.md') as f:
		return f.read()

setup(name='Bunny',
	version='0.0.1',
	description='Hop around the experiment space',
	long_description=readme(),
	url='http://gibthub.com/julianje/bunny',
	author='Julian Jara-Ettinger',
	author_email='jjara@mit.edu',
	license='MIT',
	packages=['Bunny'],
	install_requires=[
		'numpy',
		'matplotlib'
	],
	include_package_data=True,
	zip_safe=False)