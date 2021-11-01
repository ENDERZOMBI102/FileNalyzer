from dataclasses import dataclass


@dataclass
class LanguageData:
	lang: str
	count: int = 0
	rows: int = 0
	comments: int = 0
	funcs: int = 0
	classes: int | str = 0
	interfaces: int | str = 0


class TextData:
	pass


class Total


class ImgData:
	pass


class AudioData:
	pass


class BinData:
	pass