from pathlib import Path

import util
from analyzers import LanguageData

_data = LanguageData(
	lang='EndC',
	interfaces='Not Supported'
)
changed: bool = False


def getData() -> LanguageData:
	return _data


def getExtensions() -> tuple[ str, str ]:
	return '.endc', '.ec'


def supports( file: Path ) -> bool:
	return util.getExtension(file) in getExtensions()


def analyze( path: Path ) -> None:
	global changed
	if not changed:
		changed = True
	multiLineCommentOpen: bool = False
	for line in path.read_text().splitlines():
		line = line.strip()
		if line.startswith( '|*' ):
			if multiLineCommentOpen:
				_data.commentLines += 1
				multiLineCommentOpen = False
			else:
				multiLineCommentOpen = True
		if multiLineCommentOpen:
			if '*|' not in line:
				continue
			else:
				line = line[ : line.index( '*|' ) ]
		_data.emptyLines += line.replace( '\t', '' ).replace( ' ', '' ) == ''
		_data.whitespaces += line.count( ' ' )
		_data.whitespaces += line.count( '\t' )
		_data.funcs += line.count( 'FUNC' )
		_data.classes += line.count( 'TMPLAT' )
		if line.startswith('OWN'):
			_data.imports += line.count('.') + 1
		_data.totalLines += 1


def getCategory() -> str:
	return __package__
