
senaite.monkeypatches
=====================

This is an add-on that provides monkey patches to override/customize existing senaite.core and other plone add-on package `api`s at runtime. 

Features
--------

- This add-on uses the collective.monkeypatches package to override/customize SENAITE functionality.


Examples
--------

This add-on can be seen in action in the following contained scripts/files; [validators.py](src/senaite/monkeypatches/validators/validators.py) together with [configure.zcml](src/senaite/monkeypatches/validators/configure.zcml), [__init__.py](src/senaite/monkeypatches/content/__init__.py).

Function calls are patched using the monkeypatches package as can be seen in the `configure.zcml` file, where as variables/constants are patched within the `__init__.py` file. The patches are conventionally organised in packages named relative/simillarly to package names of their existing unpatched methods and/or variables.

All packages required at runtime are registered in the root [configure.zcml](src/senaite/monkeypatches/configure.zcml) file.

For details on how the patches are applied please refer to the following [collective.monkeypatcher](https://github.com/plone/collective.monkeypatcher/blob/master/README.rst) documentation.

List of all packaged patches
----------------------------

* `bika.lims.content.abstractbaseanalysis.ResultOptions` replacement with a different variable/config that allows for greater field `maxlength` and `size` of the `ResultValue` field for the `ResultOptions` widget.
* `bika.lims.content.abstractbaseanalysis.schema` updation with the new `ResultOptions` config.
* `bika.lims.validators.ResultOptionsValueValidator.__call__()` replacement with a validator function that allows for non-numeric result option values.



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
