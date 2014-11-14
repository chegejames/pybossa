# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2014 SF Isle of Man Limited
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.
# Cache global variables for timeouts
"""
Exporter module for exporting tasks and tasks results out of PyBossa
"""

import zipfile


class Exporter(object):

    """Generic exporter class."""

    def _app_name_encoded(self, app):
        """app short name for later file system usage"""
        name = app.short_name.encode('utf-8', 'ignore').decode('latin-1') # used for latin filename later
        return name

    def _zip_factory(self, filename):
        """create a ZipFile Object with compression and allow big ZIP files (allowZip64)"""
        try:
            import zlib
            zip_compression= zipfile.ZIP_DEFLATED
        except:
            zip_compression= zipfile.ZIP_STORED
        zip = zipfile.ZipFile(file=filename, mode='w', compression=zip_compression, allowZip64=True)
        return zip

    def _make_zip(self, app, ty):
        """Generate a ZIP of a certain type and upload it"""
        pass

    def download_name(self, app, ty):
        """Get the filename (without) path of the file which should be downloaded.
           This function does not check if this filename actually exists!"""
        # TODO: Check if ty is valid
        pass

    def get_zip(self, app, ty):
        """Get a ZIP file directly from uploaded directory or generate one on the fly and upload it if not existing."""
        pass

    def response_zip(self, app, ty):
        pass

    def pregenerate_zip_files(self, app):
        """Cache and generate all types (tasks and task_run) of ZIP files"""
        pass



