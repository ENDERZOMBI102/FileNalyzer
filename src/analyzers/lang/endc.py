from pathlib import Path

from analyzers import LanguageData


_data = LanguageData(
	lang='EndC'
)


def getData() -> LanguageData:
	return _data


def getExtensions() -> tuple[str]:
	return '',


def supports( file: Path ) -> bool:
	return True


def analyze( path: Path ) -> None:
	pass


def getCategory() -> str:
	return __package__