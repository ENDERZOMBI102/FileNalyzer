import re
from pathlib import Path
from re import Pattern
from typing import Final

import util
from analyzers import LanguageData


_pattern: Final[ Pattern ] = re.compile( 'class [A-z]+\([A-z= ,]*ABC[A-z= ,]*\):' )
_data = LanguageData(
	lang='Python'
)
changed: bool = False


def getData() -> LanguageData:
	return _data


def getExtensions() -> tuple[ str, str ]:
	return '.py', 'pyw',


def supports( file: Path ) -> bool:
	return util.getExtension(file) in getExtensions()


def analyze( path: Path ) -> None:
	global changed
	if not changed:
		changed = True
	multiLineCommentOpen: bool = False
	for line in path.read_text().splitlines():
		line = line.strip()
		if line.startswith('"""'):
			if multiLineCommentOpen:
				multiLineCommentOpen = False
			else:
				multiLineCommentOpen = True
		if multiLineCommentOpen:
			_data.commentLines += 1
			continue
		_data.commentLines += line.startswith( '#' )
		_data.emptyLines += line.replace('\t', '').replace(' ', '') == ''
		_data.whitespaces += line.count(' ')
		_data.whitespaces += line.count('\t')
		_data.funcs += line.count('def')
		_data.classes += line.count('class')
		_data.interfaces += len( re.findall( _pattern, line ) )
		_data.totalLines += 1


def getCategory() -> str:
	return __package__
