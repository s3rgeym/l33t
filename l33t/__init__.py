"""Leet Speak Generator"""
import sys
from argparse import ArgumentParser
from typing import Dict

from .version import __version__

__all__ = ('l33t',)

TRANSLATE_TABLE: Dict[int, str] = str.maketrans(
    {
        'o': '0',
        'l': '1',
        'z': '2',
        'e': '3',
        'a': '4',
        's': '5',
        'g': '6',  # or 9
        't': '7',
        'b': '8',
    }
)


def l33t(text: str) -> str:
    return text.lower().translate(TRANSLATE_TABLE)


def main() -> None:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('text', help='text to be translated', nargs='+')
    parser.add_argument(
        '-v', '--version', action='version', version=f'v{__version__}',
    )
    # parser.add_argument(
    #     '-a',
    #     '--advanced',
    #     action='store_true',
    #     default=False,
    #     help='advanced mode',
    # )
    try:
        args = parser.parse_args()
        text = ' '.join(args.text)
        print(l33t(text))
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)
