import importlib
from pathlib import Path
from typing import cast, Iterable, Any

from analyzers.data import LanguageData, TextData, HtmlData


DataTypes = LanguageData | TextData | HtmlData


class Analyzer:
	__package__: str
	changed: bool
	_data: DataTypes

	def getData( self ) -> DataTypes:
		pass

	def getExtensions( self ) -> Iterable[str]:
		pass

	def supports( self, file: Path ) -> bool:
		pass

	def analyze( self, path: Path ) -> None:
		pass

	def getCategory(self) -> str:
		pass


_extAnalyzers: dict[ str, list[ Analyzer ] ] = {}
_analyzers: list[ Analyzer ] = []


def initAnalyzers() -> None:
	analyzersPackage = Path(__path__[0])
	for module in analyzersPackage.rglob('*.py'):
		if module.name.startswith('_') or module.name == 'data.py':
			continue
		mod: Analyzer = cast(
			Analyzer,
			importlib.import_module(
				'.'.join( module.relative_to(analyzersPackage.parent).parts )[:-3]
			)
		)

		_analyzers.append( mod )
		for ext in mod.getExtensions():
			if ext not in _extAnalyzers:
				_extAnalyzers[ ext ] = [ mod ]
			else:
				_extAnalyzers[ ext ].append( mod )


def getAnalyzersForExtension( ext: str ) -> list[ Analyzer ]:
	return _extAnalyzers.get( ext, [] )


def getChangedAnalyzers() -> list[ Analyzer ]:
	return [ analyzer for analyzer in _analyzers if analyzer.changed ]
