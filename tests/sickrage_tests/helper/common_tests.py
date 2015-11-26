# This file is part of SickRage.
#
# URL: https://sickrage.github.io
# Git: https://github.com/SickRage/SickRage.git
#
# SickRage is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SickRage is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SickRage.  If not, see <http://www.gnu.org/licenses/>.

from unittest import TestCase, TestLoader, TextTestRunner

import os
import sys

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../lib')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from sickrage.helper.common import remove_extension


class CommonTests(TestCase):
    def test_remove_extension(self):
        tests = {
            None: None,
            '': '',
            u'': u'',
            '.': '.',
            u'.': u'.',
            'filename': 'filename',
            u'filename': u'filename',
            '.bashrc': '.bashrc',
            u'.bashrc': u'.bashrc',
            '.nzb': '.nzb',
            u'.nzb': u'.nzb',
            'file.nzb': 'file',
            u'file.nzb': u'file',
            'file.name.nzb': 'file.name',
            u'file.name.nzb': u'file.name',
            '.torrent': '.torrent',
            u'.torrent': u'.torrent',
            'file.torrent': 'file',
            u'file.torrent': u'file',
            'file.name.torrent': 'file.name',
            u'file.name.torrent': u'file.name',
            '.avi': '.avi',
            u'.avi': u'.avi',
            'file.avi': 'file',
            u'file.avi': u'file',
            'file.name.avi': 'file.name',
            u'file.name.avi': u'file.name',
        }

        for (extension, result) in tests.iteritems():
            self.assertEqual(remove_extension(extension), result)


if __name__ == '__main__':
    print('=====> Testing %s' % __file__)

    suite = TestLoader().loadTestsFromTestCase(CommonTests)
    TextTestRunner(verbosity=2).run(suite)