# coding=utf-8

"""
File status tags
"""

from __future__ import unicode_literals

OLD_COMMON_STATUSES = dict(
    UNKNOWN=-1,  # should never happen

    WANTED=3,  # episodes we don't have but want to get
    ARCHIVED=6,  # episodes that you don't have locally (counts toward download completion stats)

    SKIPPED=5,  # episodes we don't want
    IGNORED=7,  # episodes that you don't want included in your download stats
    UNAIRED=1,  # episodes that haven't aired yet

    FAILED=11,  # episode downloaded or snatched we don't want

    SNATCHED=2,  # qualified with quality
    SNATCHED_BEST=12,  # episode re-downloaded using best quality
    SNATCHED_PROPER=9,  # qualified with quality

    DOWNLOADED=4,  # qualified with quality
    SUBTITLED=10,  # qualified with quality
)

status = (
    'Unknown',

    # Non-existent
    'Skipped',  # unwanted
    'Ignored',  # unwanted; don't include in download stats
    'Removed',  # removed from library, still counts towards stats

    # Action
    'Wanted',  # wanted, and do not have
    'Snatched',  # result found and awaiting download
    'Failed',  # snatched result failed to download
    'Replace',  # existing file should be replaced

    # Existent
    'Existing',  # pre-existing
    'Downloaded',  # downloaded and exists in library
    'Replaced',  # existing download was replaced
    'Archived',  # will not be replaced
)

qualifiers = (
    # SCENE TAGS
    'Nuke',  # Something is wrong with the release
    'Internal',  # Replaces previous release for minor reasons
    'Proper',  # Replaces poor quality release
    'Repack',  # Same as a 'Proper'
    'Real',  # Replaces a previous `Proper`

    # RESULT TAGS
    'Allowed',  # Continue searching for a preferred result
    'Preferred',  # Preferred result, will not be replaced by `Allowed`
    'Best',  # Best possible result, will not be replaced
)

resolutions = {
    '480p',
    '720p',
    '1080i',
    '1080p',
    '2160p',  # AKA 4K UHD
    '4320p',  # AKA 8K UHD, Full UHD
}
