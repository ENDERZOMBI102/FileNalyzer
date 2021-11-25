import sys
from dataclasses import dataclass
from typing import Any


@dataclass
class Data:
	fileCount: int = 0
	minSize: int = sys.maxsize
	maxSize: int = 0
	totalSize: int = 0

	def averageSize( self ) -> int:
		return self.totalSize // self.fileCount


class TextData(Data):
	rows: int = 0
	chars: int = 0
	emptyLines: int = 0
	totalLines: int = 0
	whitespaces: int = 0


@dataclass
class LanguageData(TextData):
	lang: str = ''
	commentLines: int = 0
	funcs: int = 0
	classes: int | str = 0
	interfaces: int | str = 0
	imports: int = 0


@dataclass
class HtmlData(TextData):
	tags: int = 0
	divs: int = 0
	scriptTags: int = 0
	commentLines: int = 0
	styleTags: int = 0
