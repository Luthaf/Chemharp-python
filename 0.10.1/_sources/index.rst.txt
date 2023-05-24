Python interface to chemfiles
=============================

This is the documentation for the Python interface to the `chemfiles`_ library.
This interface uses Numpy, and is compatible with Python 2.7 and 3.4+, and Numpy
1.8 to 1.10.

.. _chemfiles: https://github.com/chemfiles/chemfiles

Installation
^^^^^^^^^^^^

Pre-compiled packages
---------------------

Chemfiles is available as pre-compiled packages for the three main operating
systems, both on `PyPI`_ and `conda`_. You can install these pre-compiled
packages using

.. code-block:: bash

    # if you use pip
    pip install chemfiles

    # if you use conda
    conda install -c conda-forge chemfiles

In case there is no pre-compiled wheel for your platform available (currently 32
and 64-bit x86/Intel CPU on Linux and Windows are supported, as well as macOS
with Intel CPU); then the ``pip`` installation will try to build the latest
release from source on your machine. In this case, you will need to have a C++
compiler installed, as well as CMake.

.. _conda: https://conda.pydata.org/docs/
.. _PyPI: https://pypi.org/

Build from sources -- development version
-----------------------------------------

You can also install this python module from sources if you have all the
`dependencies`_ of the C++ library installed on your computer.

.. _dependencies: http://chemfiles.org/chemfiles/latest/installation.html#core-library-dependencies

.. code-block:: bash

    git clone https://github.com/chemfiles/chemfiles.py
    cd chemfiles.py
    git submodule update --init
    # Install development dependencies
    pip install -r dev-requirements.txt
    # Install chemfiles
    pip install .
    # Optionally run the test suite
    tox

User documentation
^^^^^^^^^^^^^^^^^^

This section contains example of how to use ``chemfiles``, and the complete
interface reference for all the types and subroutines in chemfiles.

.. toctree::
    :maxdepth: 2

    tutorials
    reference/index
    reference/atom
    reference/residue
    reference/topology
    reference/cell
    reference/frame
    reference/trajectory
    reference/selection
