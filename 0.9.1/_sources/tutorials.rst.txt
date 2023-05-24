.. py:currentmodule:: chemfiles

Tutorials
=========

This section present some hand-on tutorials to the chemfiles Python module. All
the code here is under the `CC-0 Universal Licence`_ which means that you are
free to do whatever you want with it (*i.e.* it is Public Domain code)

.. _CC-0 Universal Licence: https://creativecommons.org/publicdomain/zero/1.0/

Read a single frame
-------------------

In this tutorials we will read a frame from a trajectory, and print the indexes
of all the atom in the half-space ``x < 5``.

We start by importing the classes we need from chemfiles, here only the
:py:class:`Trajectory` class.

.. literalinclude:: ../examples/indexes.py
   :language: python
   :lines: 4-5

Then we open a Trajectory and read the first frame:

.. literalinclude:: ../examples/indexes.py
   :language: python
   :lines: 7-8

We can now create a list to store the indices of the atoms with ``x < 5``, and
get the positions of the atoms in the frame with the :py:func:`Frame.positions`
function

.. literalinclude:: ../examples/indexes.py
   :language: python
   :lines: 10-11

Iterating through the atoms in the frame, we get the ones matching our
condition. ``len(frame)`` gives the number of atoms in the frame, which is also
the size of the ``positions`` array. This array is a numpy array which shape is
``(len(frame), 3)``.

.. literalinclude:: ../examples/indexes.py
   :language: python
   :lines: 13-15

And finally we can print our results

.. literalinclude:: ../examples/indexes.py
   :language: python
   :lines: 17-19

.. htmlhidden::
    :toggle: Click here to see the whole program
    :before-not-html: The whole code looks like this

    .. literalinclude:: ../examples/indexes.py
       :language: python
       :lines: 4-

For more information about reading frame in a trajectory, see the following
functions:

- :py:func:`Trajectory.nsteps` gives the number of frame in a Trajectory.
- :py:func:`Trajectory.read_step` to directlty read a given step.
- :py:func:`Trajectory.set_cell` and :py:func:`Trajectory.set_topology` to
  specify an unit cell or a topology for all frames in a trajectory.

Generating a structure
----------------------

Now that we know how to read frames from a trajectory, let's try to create a new
structure and write it to a file. As previsouly, we start by importing the
clases we need, as well as numpy:

.. literalinclude:: ../examples/generate.py
   :language: python
   :lines: 4-6

Everything starts in a :py:class:`Topology`. This is the class that defines the
atoms and the connectivity in a system. Here, we add three :py:class:`Atom` and
two bonds to create a water molecule.

.. literalinclude:: ../examples/generate.py
   :language: python
   :lines: 8-14

We can then create a :py:class:`Frame` corresponding to this topology. We resize
the frame to ensure that the frame and the topology contains the same number of
atoms.

.. literalinclude:: ../examples/generate.py
   :language: python
   :lines: 16-18

We can then set the atomic positions:

.. literalinclude:: ../examples/generate.py
   :language: python
   :lines: 20-23

Another possibility is to directly add atoms to the frame. Here we define a
second molecule representing carbon dioxyde. :py:func:`Frame.add_atom` takes
two arguments: the atom, and the position of the atom as a 3-element list

.. literalinclude:: ../examples/generate.py
   :language: python
   :lines: 25-29

Finally, we can set the :py:class:`UnitCell` associated with this frame.

.. literalinclude:: ../examples/generate.py
   :language: python
   :lines: 31

Now that our frame is constructed, it is time to write it to a file. For that,
we open a trajectory in write (``'w'``) mode, and write to it.

.. literalinclude:: ../examples/generate.py
   :language: python
   :lines: 33-34

.. htmlhidden::
    :toggle: Click here to see the whole program
    :before-not-html: Wrapping everything up, the whole code looks like this:

    .. literalinclude:: ../examples/generate.py
       :language: python
       :lines: 4-

Using selections
----------------

Now that we know how to read and write frame from trajectories, how about we do
a bit a filtering? In this tutorial, we will read all the frames from a file,
and use selections to filter which atoms we will write back to another file.
This example will also show how chemfiles can be used to convert from a file
format to another one.


Here, we will need two of chemfiles classes: :py:class`Trajectory` and
:py:class`Selection`.

.. literalinclude:: ../examples/select.py
   :language: python
   :lines: 4-5

We start by opening the two trajectories we will need

.. literalinclude:: ../examples/select.py
   :language: python
   :lines: 7-8

And we create a :py:class:`Selection` object to filter the atoms we want to
remove.

.. literalinclude:: ../examples/select.py
   :language: python
   :lines: 10

Then we can iterate over all the frames in the trajectory, and use the selection
to get the list of atoms to remove. The result of :py:func:`Selection.evaluate`
is a list containing the atoms matching the selection.

.. literalinclude:: ../examples/select.py
   :language: python
   :lines: 12-13

In order to remove the atoms from the frame, we need to sort the ``to_remove``
list in descending order: removing the atom at index i will shift the index of
all the atoms after i. So we start from the end and work toward the start of the
frame.

.. literalinclude:: ../examples/select.py
   :language: python
   :lines: 14-15

Finally, we can write the cleaned frame to the output file, and start the next
iteration.

.. literalinclude:: ../examples/select.py
   :language: python
   :lines: 16

.. htmlhidden::
    :toggle: Click here to see the whole program
    :before-not-html: The whole program look like this:

    .. literalinclude:: ../examples/select.py
       :language: python
       :lines: 4-
