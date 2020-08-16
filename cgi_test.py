from cgii import GithubFinder
import sys
gf = GithubFinder("https://gist.githubusercontent.com/plant99/eed61fb134ea335bc94e31fb642789b5/raw/2debf50f991bd148145a58fa088328cd99806a84/importcheck.py")
sys.meta_path.append(gf)

import importcheck
import os
importcheck.print_dummy(5)
