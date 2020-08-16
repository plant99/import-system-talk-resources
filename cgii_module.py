# sys_shelve_importer.py
import imp
import os
import shelve
import sys
import requests


class GithubFinder:

    def __init__(self, username, repository):
        self.url = 'https://raw.githubusercontent.com/{}/{}/master/'.format(username, repository)

    def find_module(self, fullname, path=None):
        print(fullname, path)
        if fullname.split('.')[0] != "testproject":
            return None
        print("Assuming project path is right")
        return GithubLoader(self.url, fullname.split('.')[1:])


class GithubLoader:
    """Load source for modules from shelve databases."""

    def __init__(self, url, path):
        self.path = "/".join(path)
        self.url = url + self.path + '.py'

    def get_source_for_path(self, path):
        
        r = requests.get(self.url)
        if r.status_code != 200:
            # ideally should treat this as module with __init__.py
            return ""
        else:
            return r.text

    def load_module(self, fullname):
        source = self.get_source_for_path(fullname)

        if fullname in sys.modules:
            mod = sys.modules[fullname]
        else:
            mod = sys.modules.setdefault(
                fullname,
                imp.new_module(fullname)
            )

        # Set a few properties required by PEP 302
        mod.__file__ = 'testproject'
        mod.__name__ = fullname
        mod.__path__ = '/dummy/path'
        mod.__loader__ = self
        mod.__package__ = fullname

        print('execing source...')
        exec(source, mod.__dict__)
        print('done')
        return mod