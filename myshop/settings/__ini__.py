
from myshop.settings.production import *

try:
    from myshop.settings.local_settings import *
except ImportError:
    pass

