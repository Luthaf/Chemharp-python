Python interface to chemfiles
=============================

This is the documentation for the Python interface to the `chemfiles`_ library.
This interface uses Numpy, and is compatible with Python 2.7 and 3.4+, and Numpy
1.8 to 1.10.

.. _chemfiles: https://github.com/chemfiles/chemfiles

Installation
^^^^^^^^^^^^

Pre-built binaries
------------------

The easiest way to install this interface is to use the the `conda`_ package
manager. It is part of the Anaconda Python distribution, and can be installed
separatly using the Miniconda distribution. The command to install the chemfiles
Python module with conda is:

.. _conda: http://conda.pydata.org/docs/

.. code-block:: bash

    conda install -c conda-forge chemfiles

Build from sources
------------------

You can also install this python module from sources if you have all the
`dependencies`_ of the C++ library installed on your computer.

.. _dependencies: http://chemfiles.org/chemfiles/latest/installation.html#core-library-dependencies

.. code-block:: bash

    git clone https://github.com/chemfiles/chemfiles.py
    cd chemfiles.py
    git submodule update --init
    mkdir build
    cd build
    cmake <CMAKE_OPTIONS> ..
    make
    make install

The cmake options are the same one as the c++ library, you can find them `here
<build-options_>`_. Additionally, there are some options to configure the Python
interface:

+------------------------------------------+---------------------+------------------------------+
| Option                                   | Default value       | Effect/Informations          |
+==========================================+=====================+==============================+
| ``-DCHFL_PY_BUILD_DOCUMENTATION=ON|OFF`` | ``OFF``             | Build the python docs.       |
+------------------------------------------+---------------------+------------------------------+
| ``-DCHFL_PY_INTERNAL_CHEMFILES=ON|OFF``  | ``OFF``             | Force usage of the internal  |
|                                          |                     | chemfiles instead of the     |
|                                          |                     | system one.                  |
+------------------------------------------+---------------------+------------------------------+

.. _build-options: http://chemfiles.org/chemfiles/latest/installation.html#build-steps

User documentation
^^^^^^^^^^^^^^^^^^

This section contains example of how to use ``chemfiles``, and the complete
interface reference for all the types and subroutines in chemfiles.

.. toctree::
   :maxdepth: 2

   examples
   reference
