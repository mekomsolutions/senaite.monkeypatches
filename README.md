
=====================
senaite.monkeypatches
=====================

This is an add-on that provides monkey patches to override/customize existing senaite.core package api at runtime. 

Features
--------

- This add-on makes use of the collective.monkeypatches package in overriding/customizing SENAITE functionality.


Examples
--------

This add-on can be seen in action in the following contained files; [validators.py](src/senaite/monkeypatches/validators/validators.py) with [configure.zcml](src/senaite/monkeypatches/validators/configure.zcml), [__init__.py](src/senaite/monkeypatches/content/__init__.py).

Function calls are patched using the monkeypatches package as can be seen in the `configure.zcml` file, where as variables/constants are patched within the `__init__.py` file. The patches are conventionally organised in packages named relative/simillar to package names of their existing unpatched methods and variables.

All packages required at runtime are registered in the root [configure.zcml](src/senaite/monkeypatches/configure.zcml) file.

For further information please refer to the [collective.monkeypatcher](https://github.com/plone/collective.monkeypatcher/blob/master/README.rst) documentation for detailed usage of the package.



Installation
------------

Install senaite.monkeypatches by adding it to your buildout::

    [buildout]

    ...

    eggs =
        senaite.monkeypatches


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/mekomsolutions/senaite.monkeypatches/issues
- Source Code: https://github.com/mekomsolutions/senaite.monkeypatches


Support
-------

If you are having issues, please let us know by reportig it in the issues section of this project.
