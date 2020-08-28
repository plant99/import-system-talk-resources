# import-system-talk-resources
Code and presentation used for 'What happens behind execution of an import statement?'

# declaration

Most of the code here are not written by me. I created `cgi_*` files, `importlib*` files, and files at `package-test/`. I'll be adding authors of respective files as comments soon, until then one can check the source by looking up the custom finder's/loader's class name.

# usage

- Run an [sauth](https://pypi.org/project/sauth/) server in `./package-test/` directory.
- Set credentials in https://github.com/plant99/import-system-talk-resources/blob/master/importlib_local.py
- Install [rich](https://pypi.org/project/rich/) to be used in `package-test/testproject/two/three.py`
- In the home directory of the project run `python importlib_local_test.py`

# references

Also most of the code examples are taken from these references.

- https://www.youtube.com/watch?v=0oTh1CXRaQ0
- https://docs.python.org/3/reference/import.html 
- https://snarky.ca/why-you-should-use-python-m-pip/
- http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html
- https://dev.to/dangerontheranger/dependency-injection-with-import-hooks-in-python-3-5hap
- https://pymotw.com/3/sys/imports.html
- https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/sys/imports.html
- https://xion.org.pl/2012/05/06/hacking-python-imports/
- http://blog.dowski.com/2008/07/31/customizing-the-python-import-system/
