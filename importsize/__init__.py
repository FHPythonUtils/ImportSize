#!/usr/bin/env python3
"""Leverage pipreqs to get list of modules (why reinvent the wheel?)
"""
import os
import re
import argparse
import requests
from pip._internal.utils.misc import get_installed_distributions
from pipreqs.pipreqs import(
	get_all_imports,
	get_pkg_names
)

def calc_container(path):
	''' Get size of installed module from path'''
	total_size = 0
	for dirpath, _dirnames, filenames in os.walk(path, followlinks=True):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			total_size += os.path.getsize(fp)
	return total_size


def getSize(size, siMag=0):
	'''Get human readable size '''
	siMagMap = [" B", " KB", " MB", " GB", " TB", " PB"]
	if size > 1024:
		return getSize(size/1024, siMag+1)
	return "{0:.3f}{1}".format(size, siMagMap[siMag])


def getModuleSize(moduleName):
	'''Get the size of a given module as a string '''
	for dist in get_installed_distributions():
		if moduleName == dist.project_name:
			path = os.path.join(dist.location, dist.project_name)
			size = calc_container(path)
			if size:
				return "size={}".format(getSize(size))
	return getOnlineSize(moduleName)


def getOnlineSize(moduleName):
	'''If we fail to get the local size, then get the (slightly inaccurate)
	size on pypi.org '''
	url = "https://pypi.org/project/" + moduleName + "/"
	request = requests.get(url)
	try:
		return "size=" + re.findall(r"\((.*?B)\)", request.text)[0].upper()
	except IndexError:
		return "size=failed to calculate"


def cli():
	'''Cli entry point '''
	parser = argparse.ArgumentParser(
		description="Use this module to get the sizes of used imports in a project")
	parser.add_argument("path", action="store", help="path of program")
	args = parser.parse_args()

	candidates = get_all_imports(args.path,
		encoding="utf8",
		extra_ignore_dirs=False,
		follow_links=True)
	candidates = get_pkg_names(candidates)

	for candidate in candidates:
		print("{0:16}" .format(candidate) + ": " + getModuleSize(candidate))


if __name__ == "__main__":
	cli()
