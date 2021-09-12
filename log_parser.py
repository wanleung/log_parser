#!/usr/bin/env python

# -*- coding: utf-8 -*-

import argparse
import sys
from log_parser.app import App


def main():
    argpr = argparse.ArgumentParser(description='Log Parser')
    argpr.add_argument(
        'logfile', metavar='log_file',
        type=str, help='log file'
    )
    argpr.add_argument(
        '--output', nargs='?',
        dest='outfile', type=str,
        help='output to a file'
    )
    argpr.add_argument(
        '--error', nargs='?',
        dest='errorfile', type=str,
        help='output error to a file'
    )
    argpr.add_argument(
        '--disable-ip-check',
        action="store_false",
        help='Disable IP check'
    )

    args = argpr.parse_args()
    try:
        app = App(
            args.logfile,
            enableIPCheck=args.disable_ip_check,
            outfile=args.outfile,
            errorfile=args.errorfile
        )
        app.run()
    except RuntimeError as ex:
        print("{0}\n".format(ex))


if __name__ == "__main__":
    sys.exit(main())
