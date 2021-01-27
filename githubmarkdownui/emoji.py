from enum import Enum


class Emoji(Enum):
    # Use the actual emojis here instead of the shortcuts like :x: or :warning: because that text will show up inside
    # code blocks instead of the actual emoji.
    X = '❌'
    WARNING = '⚠️'
    CHECK_MARK = '✅'
    SQUARE = '⬜'
    HOURGLASS = '⏳'
    INFORMATION = 'ℹ️'
    PAGE = '📄'
    LOCK = '🔒'
    KEY = '🔑'
