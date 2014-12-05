import argparse
import http.server

from spaegg.server import SpaeggHandler


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bind', '-b', default='', metavar='ADDRESS',
                        help='Specify alternate bind address '
                             '[default: all interfaces]')
    parser.add_argument('port', action='store',
                        default=8000, type=int,
                        nargs='?',
                        help='Specify alternate port [default: 8000]')
    args = parser.parse_args()
    http.server.test(HandlerClass=SpaeggHandler, port=args.port, bind=args.bind)
