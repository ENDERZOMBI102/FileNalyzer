from pathlib import Path

import util
from analyzers import TextData

_data = TextData(  )
changed: bool = False


def getData() -> TextData:
	return _data


def getExtensions() -> tuple[str]:
	return '.txt',


def supports( file: Path ) -> bool:
	return util.getExtension(file) in getExtensions()


def analyze( path: Path ) -> None:
	global changed
	if not changed:
		changed = True
	for line in path.read_text().splitlines():
		line = line.strip()
		_data.emptyLines += line.replace( '\t', '' ).replace( ' ', '' ) == ''
		_data.whitespaces += line.count( ' ' )
		_data.whitespaces += line.count( '\t' )
		_data.totalLines += 1


def getCategory() -> str:
	return __package__
