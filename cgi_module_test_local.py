from cgii_module_local import LocalDirFinder
import sys
gf = LocalDirFinder("http://localhost:8333", "testproject")
sys.meta_path.append(gf)

from testproject.two import three
import os
three.print_dummy(4)
