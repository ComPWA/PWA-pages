Formalisms
==========

.. warning::
  These pages and are **under development**.

Helicity Formalism
------------------

- Lorentz-invariance of helicity operator

- Types

  - Two-body decay amplitude
  - Sequential two-body decay amplitude

- Definition of angles

  - Production angle
  - Helicity angle
  - Treiman-Yang angle
  - Overview of kinematic variables

- Dynamics:

  - Wigner-D functions
  - Clebsch-Gordan coefficients

- Kinematic variables
- An example

.. note::
  **The old text**

  Two particle states are the key element here. With these one can construct
  states of total spin :math:`J` and projection :math:`M`.

  The probability amplitude of a state with spin J and projection M decaying
  into two particles 1 and 2 with helicities :math:`\lambda_i` and momentum
  :math:`\vec{p}` in the cms frame is given by
  :cite:`chungSpinFormalismsUpdated2014`, p.16.

  .. math::

    two body decay amplitude here

  In the helicity formalism sequential two body decays are easy to handle

  .. math::

    seq two body decay amplitude here

  Then show explicitly what ComPWA implements and which components correspond
  to what part in the equation. So we would refer in the Doxygen docs to

  - the Wigner D functions

  - the Kinematics class

  - the IntensityBuilderXML with the two functions createSequentialAmplitudeFT
    createHelicityDecayFT

  - the dynamical functions

  - the phase space element calculations?

  https://compwa.github.io/ComPWA/classComPWA_1_1Physics_1_1IntensityBuilderXML.html


Canonical Formalism
-------------------

.. note::
  **The old text**
  The canonical formalism gives access to the orbital angular momentum
  :math:`L` and the coupled Spin :math:`S` arising from a two particle state.

  There is a simple connection between the two formalism. Show that here

  This expression is simply inserted into equation () and that is it!

  The choice of the formalism depends on the physics process being analyzed.
  Give an example here.


Lorentz-invariant Formalisms
----------------------------

Rarita-Schwinger
""""""""""""""""


Other Spin Formalisms
---------------------

(Covariant) Tensor Formalisms
"""""""""""""""""""""""""""""

Spin-projection formalisms
""""""""""""""""""""""""""
