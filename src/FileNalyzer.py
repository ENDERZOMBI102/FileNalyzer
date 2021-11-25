from argparse import ArgumentParser
from pathlib import Path
from pprint import pprint
from sys import argv

import analyzers
import util


class Arguments:
	directory: Path
	excludePaths: list[Path]


parser = ArgumentParser(
	prog='FileNalyzer',
	description='Analyzes directories and gathers file infos and stats'
)
parser.add_argument(
	'directory',
	default=Path('.'),
	type=Path,
	nargs='?'
)


def main() -> None:
	# noinspection PyTypeChecker
	args: Arguments = parser.parse_args( argv[1:] )

	analyzers.initAnalyzers()

	for path in args.directory.rglob('*.*'):
		if 'test' in path.parts:
			continue
		for analyzer in analyzers.getAnalyzersForExtension( util.getExtension( path ) ):
			if analyzer.supports( path ):
				# print(f'{path = }')
				analyzer.analyze( path )
				size = path.lstat().st_size
				data = analyzer.getData()
				data.totalSize += size
				if data.maxSize < size:
					data.maxSize = size
				if data.minSize > size:
					data.minSize = size
				data.fileCount += 1

	for analyzer in analyzers.getChangedAnalyzers():
		print( analyzer.__name__, end=': ' )
		pprint( analyzer.getData().__dict__ )


main()
