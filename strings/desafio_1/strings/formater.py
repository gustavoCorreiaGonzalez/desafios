# -*- coding: utf-8 -*-

"""Formater.

Formater strings.

"""


class Formater(object):
    """Class Formater.

    Formater strings.

    """

    def __init__(self, text, width):
        """Init function.

        Args:
            text (string): text.
            width (string): width.

        """
        self.text = text
        self.width = width

    def format(self):
        """Format the text."""
        line = ""
        text = ""

        for character in self.text.split():
            if len(line) + len(character) >= self.width:
                text = "%s%s\n" % (text, line)
                line = ""

            if line:
                line += " "

            line += character

        text = "%s%s" % (text, line)

        return text
