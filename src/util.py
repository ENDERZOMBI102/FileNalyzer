from pathlib import Path


def getExtension(path: Path) -> str:
	dotIndex = path.name.find('.')
	if dotIndex != -1:
		return path.name[ dotIndex: ]
	else:
		return ''
