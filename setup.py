"""Do setup for uploading to pypi
"""
import setuptools

with open("README.md", "r") as readme:
	long_description = readme.read()

setuptools.setup(
	name="importsize",
	version="2020",
	author="FredHappyface",
	description="Use this module to get the sizes of used imports in a project",
	long_description=long_description,
    long_description_content_type="text/markdown",
	url="https://github.com/FHPythonUtils/ImportSize",
	packages=setuptools.find_packages(),
	classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
	entry_points={
    	'console_scripts': [
    		'importsize=importsize:cli',
    	],
    },
	python_requires='>=3.0',
)
