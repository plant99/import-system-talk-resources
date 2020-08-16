from importlib_local import RemoteDirFinder
import sys
lf = RemoteDirFinder("http://localhost:8333", "testproject")
sys.meta_path.append(lf)

from testproject.two import three
import os
three.print_dummy(5)

# print(three.__dict__)