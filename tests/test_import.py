# -*- coding: utf-8 -*-

import pytest


def test():
    import light_emoji

    _ = light_emoji.emojis.cat
    _ = light_emoji.common.succeeded


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
