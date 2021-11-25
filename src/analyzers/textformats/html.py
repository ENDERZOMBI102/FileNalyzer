import re
from pathlib import Path
from re import Pattern
from typing import Final

import util
from analyzers import HtmlData


_pattern: Final[Pattern] = re.compile( '<[a-zA-Z]+' )
_data = HtmlData()
changed: bool = False


def getData() -> HtmlData:
	return _data


def getExtensions() -> tuple[ str ]:
	return '.html',


def supports( file: Path ) -> bool:
	return util.getExtension(file) in getExtensions()


def analyze( path: Path ) -> None:
	global changed
	if not changed:
		changed = True
	multiLineCommentOpen: bool = False
	for line in path.read_text().splitlines():
		line = line.strip()
		if line.startswith('<!--'):
			if multiLineCommentOpen:
				multiLineCommentOpen = False
			else:
				multiLineCommentOpen = True
		if multiLineCommentOpen:
			_data.commentLines += 1
			if '-->' not in line:
				continue
			else:
				line = line[ : line.index('-->') ]
		_data.emptyLines += line.replace('\t', '').replace(' ', '') == ''
		_data.whitespaces += line.count(' ')
		_data.whitespaces += line.count('\t')
		_data.divs += line.count('<div')
		_data.styleTags += line.count('<style')
		_data.scriptTags += line.count('<script')
		_data.totalLines += 1
	_data.tags += len( re.findall( _pattern, path.read_text() ) )


def getCategory() -> str:
	return __package__
