#!/usr/bin/env python3
import argparse
import download_exe

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'url',
        help="URL which leads to the page containing files to download"
    )
    parser.add_argument(
        'pattern',
        help="phrase(or regex pattern) which all addresses must contain"
    )
    parser.add_argument(
        '-d',
        '--download',
        help="Download instead of just listing",
        action="store_true"
    )

    args = parser.parse_args()

    download_exe.download_from_url(args.url, args.pattern, args.download)
