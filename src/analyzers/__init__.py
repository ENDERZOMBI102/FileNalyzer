import importlib
from pathlib import Path
from typing import cast, Iterable, Any

from analyzers.data import LanguageData, TextData, ImgData, AudioData, BinData


class Analyzer:
	__package__: str

	def getData( self ) -> LanguageData | TextData | ImgData | AudioData | BinData:
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


def initAnalyzers() -> None:
	analyzersPackage = Path(__path__[0])
	for module in analyzersPackage.rglob('*.py'):
		if module.name.startswith('_'):
			continue
		mod: Analyzer = cast(
			Analyzer,
			importlib.import_module(
				'.'.join( module.relative_to(analyzersPackage.parent).parts )[:-3]
			)
		)

		for ext in mod.getExtensions():
			if ext not in _extAnalyzers:
				_extAnalyzers[ ext ] = [ mod ]
			else:
				_extAnalyzers[ ext ].append( mod )


def getAnalyzerForExtension(ext: str) -> list[Analyzer]:
	return _extAnalyzers.get( ext, [] )

