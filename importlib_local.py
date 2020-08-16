# sys_shelve_importer.py
import importlib
import os
import shelve
import sys
import requests
from types import ModuleType

session = requests.Session()
session.auth = ("admin", "12345")

class RemoteDirFinder:

    def __init__(self, url, subdir):
        self.url = '{}/{}'.format(url, subdir)
        self.subdir = subdir

    # find_module is deprecated, use find_spec instead
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split('.')[0] != self.subdir:
            return None
        print("Found module {}".format(fullname))
        return importlib.machinery.ModuleSpec(fullname, RemoteDirLoader(self.url, fullname.split('.')[1:]))


class RemoteDirLoader:
    """Load source for modules from shelve databases."""

    def __init__(self, url, path):
        self.path = "/".join(path)
        self.url = url + '/' + self.path + '.py'

    def get_source_for_path(self, path):
        
        r = session.get(self.url)
        if r.status_code != 200:
            # ideally should treat this as module with __init__.py
            return ""
        else:
            return r.text

    def create_module(self, spec, install=True):
        """Create a built-in module"""
        if spec.name in sys.modules:
            mod = sys.modules[spec.name]
            return mod

        print(f'create_module {spec.name}')
        mod = ModuleType(spec.name)
        mod.__file__ = "testproject"
        mod.__name__ = spec.name
        mod.__loader__ = self
        mod.__spec__ = spec
        mod.__path__ = '/dummy/path'

        if install:
            print(f'Installing module {spec.name}')
            sys.modules[spec.name] = mod

        return mod

    def exec_module(self, mod):
        source = self.get_source_for_path(mod.__name__)
        print(f'execing source for {mod.__name__} \n')
        try:
            # print(mod.__dict__)
            # print("\n\n\n")
            exec(source, mod.__dict__)
            # print(mod.__dict__)
            # print("\n\n\n")
        except:
            raise ImportError("Bad code")
        return None # it doesn't care what you import