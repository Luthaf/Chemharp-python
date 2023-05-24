.. _python-api:

Python interface reference
==========================

The Python interface is exposed in the :py:mod:`chemfiles` module, and this page
list all the classes and methods in this module.

Error handling
--------------

Chemfiles uses exceptions for error handling, throwing
:py:class:`ChemfilesException <chemfiles.errors.ChemfilesException>` when an
error occurs.

.. automodule:: chemfiles.errors
    :members:

Trajectory class
----------------

.. set current module to chemfiles
.. automodule:: chemfiles

.. autoclass:: Trajectory
    :members:

Frame class
-----------

.. autoclass:: Frame
    :members:

UnitCell class
--------------

.. autoclass:: CellShape
    :members:

.. autoclass:: UnitCell
    :members:

Topology class
--------------

.. autoclass:: Topology
    :members:

Atom class
----------

.. autoclass:: Atom
    :members:


Residue class
-------------

.. autoclass:: Residue
    :members:


Selection class
---------------

.. autoclass:: Selection
    :members:
