from cgii_module import GithubFinder
import sys
gf = GithubFinder("vulb", "testproject")
sys.meta_path.append(gf)

from testproject.two import three
import os
three.print_dummy(4)
print(sys.modules["testproject"].__name__, sys.modules["testproject.two"].__name__, sys.modules["testproject.two.three"].__name__)
