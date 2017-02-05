from google.appengine.ext import vendor

# workaround to make the application run on windows
import os
import sys

on_appengine = os.environ.get('SERVER_SOFTWARE', '').startswith('Development')
if on_appengine and os.name == 'nt':
    os.name = None
    sys.platform = ''

# Add any libraries installed in the "lib" folder.
vendor.add('lib')
