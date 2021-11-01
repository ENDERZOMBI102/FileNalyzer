from argparse import ArgumentParser
from pathlib import Path
from sys import argv

import analyzers
import util


class Arguments:
	directory: Path


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

	for path in args.directory.rglob('*.*'):
		for analyzer in analyzers.getAnalyzerForExtension( util.getExtension(path) ):
			if analyzer.supports( path ):
				analyzer.analyze( path )


main()
