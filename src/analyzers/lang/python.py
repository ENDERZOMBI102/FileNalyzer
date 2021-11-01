from pathlib import Path
from typing import Any

from analyzers import LanguageData


_data = LanguageData(
	lang='Python'
)


def getData() -> LanguageData:
	return _data


def getExtensions() -> tuple[ str, str ]:
	return '.py', 'pyw'


def supports( file: Path ) -> bool:
	return True


def analyze( path: Path ) -> None:
	pass


def getCategory() -> str:
	return __package__
