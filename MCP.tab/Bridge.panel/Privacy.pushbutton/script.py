# -*- coding: utf-8 -*-
"""Open the privacy information shipped with this extension."""
import os
from pyrevit import script
extension_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
script.get_output().print_md(open(os.path.join(extension_root, "PRIVACY.md")).read())
