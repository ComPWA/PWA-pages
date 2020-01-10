Helicity Formalism
------------------

Two particle states are the key element here. With these one can construct
states of total spin :math:`J` and projection :math:`M`.

The probability amplitude of a state with spin J and projection M decaying into
two particles 1 and 2 with helicities :math:`\lambda_i` and momentum
:math:`\vec{p}` in the cms frame is given by :cite:`chung2006spin`, p.16.

.. math::

  two body decay amplitude here

In the helicity formalism sequential two body decays are easy to handle

.. math::

  seq two body decay amplitude here

Then show explicitly what ComPWA implements and which components correspond to
what part in the equation. So we would refer in the Doxygen docs to

- the Wigner D functions

- the Kinematics class

- the IntensityBuilderXML with the two functions createSequentialAmplitudeFT
  createHelicityDecayFT

- the dynamical functions

- the phase space element calculations?

https://compwa.github.io/ComPWA/classComPWA_1_1Physics_1_1IntensityBuilderXML.html


Canonical Formalism
-------------------

The canonical formalism gives access to the orbital angular momentum :math:`L`
and the coupled Spin :math:`S` arising from a two particle state.

There is a simple connection between the two formalism. Show that here

This expression is simply inserted into equation () and that is it!

The choice of the formalism depends on the physics process being analyzed. Give
an example here.
