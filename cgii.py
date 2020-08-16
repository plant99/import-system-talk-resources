# sys_shelve_importer.py
import imp
import os
import shelve
import sys
import requests


class GithubFinder:

    def __init__(self, url):
        self.url = url

    def find_module(self, fullname, path=None):
        if fullname != "importcheck":
            return None
        r = requests.get(self.url)
        if r.status_code == 200:
            return GithubLoader(self.url)
        else:
            return None


class GithubLoader:
    """Load source for modules from shelve databases."""

    def __init__(self, url):
        self.url = url

    def get_source(self):
        r = requests.get(self.url)
        return r.text

    def load_module(self, fullname):
        source = self.get_source()

        if fullname in sys.modules:
            mod = sys.modules[fullname]
        else:
            print("importcheck" in sys.modules.keys())
            mod = sys.modules.setdefault(
                fullname,
                imp.new_module(fullname)
            )
            print("importcheck" in sys.modules.keys())

        # Set a few properties required by PEP 302
        mod.__file__ = 'importcheck'
        mod.__name__ = fullname
        mod.__path__ = '/dummy/path'
        mod.__loader__ = self
        mod.__package__ = fullname

        print('execing source...')
        exec(source, mod.__dict__)
        print(sys.modules["importcheck"])
        print('done')
        return mod