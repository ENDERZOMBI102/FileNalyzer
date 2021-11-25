from pathlib import Path

import util
from analyzers import LanguageData


_data = LanguageData(
	lang=Path(__file__).name[:-3].capitalize()
)
changed: bool = False


def getData() -> LanguageData:
	return _data


def getExtensions() -> tuple[str]:
	return '',


def supports( file: Path ) -> bool:
	return util.getExtension(file) in getExtensions()


def analyze( path: Path ) -> None:
	pass


def getCategory() -> str:
	return __package__
