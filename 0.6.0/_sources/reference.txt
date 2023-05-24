.. _python-api:

Python interface reference
==========================

The Python interface is built on top of the C interface, using the `ctypes`_
standard module.

.. _ctypes: https://docs.python.org/3/library/ctypes.html

This interface is contained in the :py:mod:`chemfiles` module, and this page list all
the classes and methods in this module.

Logging functions
-----------------

All logging in chemfiles uses a global maximal logging level, of type
:py:class:`LogLevel <chemfiles.logging.LogLevel>`, which can be manipulated using
:py:func:`log_level <chemfiles.logging.log_level>` and
:py:func:`set_log_level <chemfiles.logging.set_log_level>`. The logging output is by
default redirected to the standard error stream, but this can be changed by using the
:py:func:`log_to_stderr <chemfiles.logging.log_to_stderr>`;
:py:func:`log_to_stdout <chemfiles.logging.log_to_stdout>`;
:py:func:`log_to_file <chemfiles.logging.log_to_file>`;
:py:func:`log_callback <chemfiles.logging.log_callback>` and
:py:func:`silent <chemfiles.logging.silent>` functions.

.. automodule:: chemfiles.logging
    :members:

Error classes
-------------

Chemfiles uses exceptions for error handling, and will only throw one of these
exceptions. The :py:class:`ChemfilesException <chemfiles.errors.ChemfilesException>`
base class can be used to catch all chemfiles related errors.

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

.. autoclass:: CellType
    :members:

.. autoclass:: UnitCell
    :members:

Topology class
--------------

.. autoclass:: Topology
    :members:

Atom class
----------

.. autoclass:: AtomType
    :members:

.. autoclass:: Atom
    :members:


Selection class
---------------

.. autoclass:: Selection
    :members:
