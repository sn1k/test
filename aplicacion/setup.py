from setuptools import setup

setup(name='aplicacion',
	version='0.1',
	description='Web application about polls',
	url='https://github.com/lorenmanu/submodulo-lorenzo',
	author='Lorenzo Manuel Rosas Rodriguez',
	author_email='lorenrr1@gmail.com',
	license='GNU GPL',
	packages=['aplicacion'],
	install_requires=['django','wheel'],
	zip_safe=False)
