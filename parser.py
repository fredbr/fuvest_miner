import argparse
import sys

class DefaultHelpParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

def parse():
	parser = DefaultHelpParser(description="Bixão Miner")

	parser.add_argument('pdf', type=str, help='PDF dos aprovados')
	parser.add_argument('codigo', type=str, help='Código do Curso')
	parser.add_argument('-o', type=str, metavar='output_file',
				        dest='output_file',
		                help='Output file (default: stdout)')

	args = parser.parse_args()

	return (args.pdf, args.codigo, args.output_file)