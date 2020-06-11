Introduction
============


The importance of studying interactions
---------------------------------------

- Strong interactions at low momentum transfer
- Cannot predict intermediate states from QCD theory
- Study properties of intermediate states to derive descriptive models

Partial waves
-------------

- Schrödinger's equation
- Separating out angular and radial wave functions using Legendre polynomials
- What we can see from this and how it relates to analysis techniques

Transition amplitude
--------------------

- Distinction dynamical part and angular part

.. note::

   **The old text**

   In general one is interested in gaining knowledge about the interaction of particles. Therefore, particle reaction experiments are performed to validate theoretical models and extract physical quantities and information (based on those models). To validate and extract information a comparison of the data from the experiment and the theoretical model is needed.

   The probability amplitude :cite:`weinbergQuantumTheoryFields1995b`, p.113  of an initial state :math:`\Psi_i` going to a final state :math:`\Psi_f` is:

   .. math::

      S_{fi} = \left< \Psi_f \middle| S \middle| \Psi_i \right> = -2\pi i \delta^4(p_i - p_f)M_{fi}.

   This is a general formula, so the particle content of the initial and final state is arbitrary.

   Experimental physicists measure transition rates or cross sections instead of the transition probability. There are two special cases of initial states, since many experimental measurements fall under these two categories:

   1. Single particles in the initial state (:math:`N_I=1`)

      This is a single particle decaying into the final state particles. Here the decay rate :cite:`weinbergQuantumTheoryFields1995b`, p.136 is

      .. math::

         d\Gamma(i \rightarrow f) = 2\pi |M_{fi}|^2 \delta^4(p_f - p_i) d\Phi_f

      :math:`d\Phi_f` is the phase space element of the final state, which is needed to make a comparison with data. More on this below.

   2. Two particles in the initial state (:math:`N_I=2`)

      The cross section of a two particle scattering/production process :cite:`weinbergQuantumTheoryFields1995b`, p.137 is

      .. math::

         d\sigma(i \rightarrow f) = (2\pi)^4 u_i^{-1} |M_{fi}|^2 \delta^4(p_f - p_i) d\Phi_f

      with :math:`u_i^{-1}` the relative velocity of the initial state particles.

   Describing multi body problems (more than 2) is a difficult task, since the interaction of more than two particles is difficult to describe :cite:`weinbergQuantumTheoryFields1995b`, ch.4.

   One can resort to a simplification to treat a many body interaction by successive two body interactions. For N body particle decays (N > 2) this is known as the isobar model. Here a particle into N final state particles is modelled by a sequence of two particle decays. This is also also a assumption of the helicity/canonical formalism.

Isobar model
------------




References
----------

.. bibliography:: bibliography.bib
   :style: unsrtalpha
   :cited:
