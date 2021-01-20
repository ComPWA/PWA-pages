# Introduction

```{warning}
These pages and are **under development**.
```

While the {term}`Standard Model` provides an incredibly accurate description of
the most fundamental constituents of matter, it remains difficult to describe
interactions at the level of bound states ({term}`hadrons <hadron>`). This is
because the fundamental force that dominates at this range―the
{term}`strong force`—is characterized by an {term}`asymptotic freedom`: it has
a strong coupling constant at low momentum transfer.

One the one hand, this asymptotic behavior of the strong force forces
{term}`quarks <quark>` to bound together in colorless groups
({term}`color confinement`), giving particle physicists an amazingly varied
spectrum of quark combinations to study. On the other, the asymptotic running
of the coupling constant makes it almost impossible to predict from first
principles how bound states of quarks interact at lower energies.

Theoreticians have developed several descriptive models and numerical tools
({term}`lattice QCD` most importantly), but these models often rest on several
assumptions or fail to describe larger systems. It therefore remains important
to study particle interactions at the lower energies.

Partial Wave Analysis is a collection of techniques that allows us to perform
these studies.

- Importance of decomposing interactions
- Strong QCD coupling constant at low momentum transfer
- Cannot compute intermediate states from theory
- Need to collect properties: mass, width, spin, parity

## Scattering theory

### Transition amplitude

- Amplitudes and intensities
- Scattering operator $S$ ({term}`S-matrix`)
- Lead-up to $T$-matrix ({term}`transition operator`)
- Distinction dynamical part and angular part

:::{dropdown} The old text

In general one is interested in gaining knowledge about the interaction of
particles. Therefore, particle reaction experiments are performed to validate
theoretical models and extract physical quantities and information (based on
those models). To validate and extract information a comparison of the data
from the experiment and the theoretical model is needed.

The probability amplitude {cite}`weinbergQuantumTheoryFields1995`, p.113 of an
initial state $Psi_i$ going to a final state $Psi_f$ is:

```{math}

S_{fi} = \left< \Psi_f \middle| S \middle| \Psi_i \right> = -2\pi i
\delta^4(p_i - p_f)M_{fi}.

```

This is a general formula, so the particle content of the initial and final
state is arbitrary.

Experimental physicists measure transition rates or cross sections instead of
the transition probability. There are two special cases of initial states,
since many experimental measurements fall under these two categories:

1. Single particles in the initial state ($N_I=1$)

   This is a single particle decaying into the final state particles. Here the
   decay rate {cite}`weinbergQuantumTheoryFields1995`, p.136 is

   ```{math}

   d\Gamma(i \rightarrow f) = 2\pi |M_{fi}|^2 \delta^4(p_f - p_i) d\Phi_f

   ```

   $dPhi_f$ is the phase space element of the final state, which is needed to
   make a comparison with data. More on this below.

2. Two particles in the initial state ($N_I=2$)

   The cross section of a two particle scattering/production process
   {cite}`weinbergQuantumTheoryFields1995`, p.137 is

   d\sigma(i \rightarrow f) = (2\pi)^4 u*i^{-1} |M*{fi}|^2 \delta^4(p_f - p_i)
   d\Phi_f with $u_i^{-1}$ the relative velocity of the initial state
   particles.

Describing multi body problems (more than 2) is a difficult task, since the
interaction of more than two particles is difficult to describe
{cite}`weinbergQuantumTheoryFields1995`, ch.4.

One can resort to a simplification to treat a many body interaction by
successive two body interactions. For N body particle decays (N > 2) this is
known as the isobar model. Here a particle into N final state particles is
modelled by a sequence of two particle decays. This is also also a assumption
of the helicity/canonical formalism.

:::

### Partial waves

Decomposition into partial waves ({cite}`petersPrimerPartialWave2004`, p.3):

> Consider an incident wave $\left|i\right> = Psi_i$. In an experimental
> setting, we can assume a vanishing potential at $t\rightarrow\infty$, which
> allows us to expand the incoming wave in terms of
> {wiki}`Legendre_polynomials` $P_l$, with $l$ the
> {dfn}`angular orbital momentum`:
>
> ```{math}
>
> \Psi_i(r,\theta) = \sum_{l=0}^\infty U_l(r) P_l(\theta)
>
> ```
>
> The $U_l$ factor can be parametrized further. At this stage, it is important
> to point that the angular orbital momentum of the incoming state is used to
> characterize specific systems. Here, it is common to use the labels used for
> [electron orbitals](https://scienceworld.wolfram.com/physics/ElectronOrbital.html):
>
> ```{eval-rst}
> ===  =====  ======================
> $l$  Label         Origin
> ===  =====  ======================
> 0    s      "sharp"
> 1    p      "principal"
> 2    d      "diffuse"
> 3    f      "fundamental"
> 4    g      *rest is alphabetical*
> ...  ...    ...
> ===  =====  ======================
> ```
>
> In PWA, it is therefore common to distinguish these wave contributions as
> $S$-wave, $P$-wave, etc.

- Separating out angular and radial wave functions using Legendre polynomials
- What we can see from this and how it relates to analysis techniques
- (?) Difference with amplitude analysis
- Possible initial states: 1, 2, and multi-body
- Suitable for propagation, not re-scattering

## Isobar model
