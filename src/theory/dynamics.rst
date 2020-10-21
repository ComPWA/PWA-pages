Dynamics
========

.. warning::
  These pages and are **under development**.

$K$-matrix
----------

.. todo::

  Since :term:`scattering operator` ($S$-matrix) formulates the transition
  amplitude from initial state :math:`\left|i\right>` to final state
  :math:`\left|f\right>` through :math:`\left<i\right|S\left|f\right>`, it is a
  **unitary** operator—probability is conserved, meaning $SS^* = I$. Now,
  :ref:`having defined the transition operator <theory/introduction:Transition
  amplitude>` through $S = I + iT$, we can introduce another operator: $K^{-1}
  = T^{-1} + iI$ :cite:`chungPartialWaveAnalysis1995`.

  Why is this new matrix interesting?

- Definition in terms of $T$-matrix

Special cases of the $K$-matrix
-------------------------------

Breit-Wigner
""""""""""""

.. todo:: Derive from $K$-matrix instead/as well.

A quantum mechanical state at rest with energy $E_0$ can be described in terms
of the wave function:

.. math::
  \psi(t) = \psi_0 e^{-iE_0t}

Now, if we assume that the state has a decay width of $\Gamma$, the probability
density $\psi^*\psi$ of this state can be described as:

.. math::
  \psi^*\psi = \psi_0^*\psi_0 e^{-\Gamma t}.

The wave function itself then becomes:

.. math::

  \psi(t) = \psi_0 e^{-iE_0t} e^{-\frac{\Gamma}{2} t} = \psi_0 e^{-i
  \left(E_0-\tfrac{i}{2}\Gamma\right) t}.

A particle with a finite decay width can therefore be described as a particle
with **complex energy**:

.. math::
  E' = E_0 - \frac{i}{2}\Gamma

Now, as an experimental physicist, one is interested in predicting the
probability of observing the particle at energy $E$ (we want to describe the
observed invariant mass distributions). This can be achieved by applying a
:wiki:`Fourier_transform`, so that $\psi$ is described in terms of energy $E$
(or frequency $\omega$) instead of time $t$:

.. math::

  \psi(E)
  & \propto \psi_0 \int_0^\infty e^{i\left(E-E_0+\tfrac{i}{2}\Gamma\right)t}\,\mathrm{d}t

  & \propto \frac{1}{\left(E-E_0\right) - \tfrac{i}{2}\Gamma}

The probability to observe the particle at energy $E$ is therefore:

.. math::
  \psi^*(E)\psi(E) \propto
  \frac{\frac{\Gamma^2}{4}}{\left(E-E_0\right)^2 - \frac{\Gamma^2}{4}}

.. todo:: Describe relation between $\psi(E)$ and transition amplitude $M$

From this, one can see that the transition amplitude $M$ is described by:

.. math::
  M(E) \propto
  \frac{\frac{\Gamma}{2}}{\left(E-E_0\right) - i\frac{\Gamma}{2}}

because $|\psi|^2\propto|M|$. This is called **non-relativistic Breit-Wigner
parametrization**.

.. todo::

  Describe how the **relativistic Breit-Wigner formula**:

  .. math::

    M(E) \propto
    \frac{m_0\Gamma}{m_0^2 - m_{ab}^2 - im_0\Gamma}

  is derived and why this is important in case of $\Gamma \gg m_0$.


Flatté
""""""

The importance of Unitarity
---------------------------

What's the difference between Poles and Resonances?
---------------------------------------------------
