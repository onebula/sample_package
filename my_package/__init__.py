# import sys
# sys.path.append('my_package/src')

# import sys
# from os.path import abspath, join, dirname
# sys.path.insert(0, join(abspath(dirname(__file__)), 'src'))

import sys
from os.path import abspath, join, dirname
my_path = join(abspath(dirname(__file__)), 'src')
if my_path not in sys.path:
   sys.path.insert(0, my_path)

from .src import Foo2
#from .src import Foo1