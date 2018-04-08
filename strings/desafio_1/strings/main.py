# -*- coding: utf-8 -*-

"""App.

File containing the api routes.

"""

import sys

from formater import Formater


if __name__ == "__main__":
    text = sys.argv[1]
    width = int(sys.argv[2])
    formater = Formater(text, width)

    if len(sys.argv) == 3:
        text_transformed = formater.format()

        print(text_transformed)
    else:
        print("docker run -t -i strings_formatter \"text\" width")
