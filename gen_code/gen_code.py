# -*- coding: utf-8 -*-

"""
Generate code based on https://github.com/carpedm20/emoji/blob/master/emoji/unicode_codes/data_dict.py
"""

import typing as T
from pathlib import Path
from jinja2 import Template
from data_dict import EMOJI_DATA, fully_qualified

var_name_unfriendly_chars = "-()’.!@#$%^&*()"

identifier_and_emoji_list: T.List[T.Tuple[str, str]] = list()
for emoji, data in EMOJI_DATA.items():
    length = len(emoji)
    if length > 1:
        continue
    if data["status"] == fully_qualified is False:
        continue
    identifier = data["en"].replace(":", "")
    for char in var_name_unfriendly_chars:
        identifier = identifier.replace(char, "_")
    if identifier[0].isdigit():
        identifier = "d" + identifier
    identifier_and_emoji_list.append((identifier, emoji[0]))

dir_here = Path(__file__).absolute().parent
path_emoji_template = dir_here / "emojis.py.jinja"
path_emoji_py = dir_here / "emojis.py"

template = Template(path_emoji_template.read_text())
path_emoji_py.write_text(template.render(identifier_and_emoji_list=identifier_and_emoji_list))
