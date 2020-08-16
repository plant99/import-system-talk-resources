"""
Stupid Python Trick - import modules over the web.
Author: Christian Wyglendowski
License: MIT (http://dowski.com/mit.txt)
"""

import requests
import imp
import sys
import os

def register_domain(name):
    WebImporter.registered_domains.add(name)
    parts = reversed(name.split('.'))
    whole = []
    for part in parts:
        whole.append(part)
        WebImporter.domain_modules.add(".".join(whole))

class WebImporter(object):
    domain_modules = set()
    registered_domains = set()

    def find_module(self, fullname, path=None):
        print(self.domain_modules)
        if fullname in self.domain_modules:
            return self
        if fullname.rsplit('.')[0] not in self.domain_modules:
            return None
        try:
            r = self._do_request(fullname, method="HEAD")
        except ValueError:
            return None
        else:
            if r.status == 200:
                return self
        return None

    def load_module(self, fullname):
        if fullname in sys.modules:
            return sys.modules[fullname]
        mod = imp.new_module(fullname)
        mod.__loader__ = self
        sys.modules[fullname] = mod
        print(fullname, self.domain_modules)
        if fullname not in self.domain_modules:
            url = "http://%s%s" % self._get_host_and_path(fullname)
            mod.__file__ = url
            r = self._do_request(fullname)
            code = r.read()
            assert r.status == 200
            for code in mod.__dict__:
                exec(code)
        else:
            mod.__file__ = "[fake module %r]" % fullname
            mod.__path__ = []
        return mod

    def _do_request(self, fullname, method="GET"):
        host, path = self._get_host_and_path(fullname)
        r = requests.get(os.path.join(host, path))
        return r.raw

    def _get_host_and_path(self, fullname):
        tld, domain, rest = fullname.split('.', 2)
        path = "/%s.py" % rest.replace('.', '/')
        return ".".join([domain, tld]), path

sys.meta_path = [WebImporter()]