# [ADR-0000] Write overview of Partial Wave Analysis

Status: **proposed**

Deciders: @redeboer

## Context and Problem Statement

Existing literature on Partial Wave Analysis (PWA) theory is often dry and hard
to get into, while the theory cannot be ignored when doing PWA research. This is
a problem for a specialized and narrow field that is limited on manpower. In
addition, while much of PWA research itself relies heavily on specific analysis
frameworks, PWA publications hardly ever expand on the use or development of
those frameworks.

## Considered Options

1. Limit to a list of references.
2. Write specific theory in the codebase API.
3. Build a Sphinx webpage that summarizes and bundles existing literature.

## Decision Outcome

### Option 1 [rejected]: Limit to a list of references.

- **Positive**:
  - Don't have to spend time on rewriting
  - Good old academic style
- **Negative**:
  - Hard to link to specific pages
  - Less interactive (no 'navigating around' through sources)
  - Prone to become outdated

### Option 2 [rejected]: Write in codebase

- **Positive**:
  - Explanation right next to the code in one repository
  - [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
    works best within one webpage + API
  - Kept in sync per commit
- **Negative**:
  - No bundled overview for the user
  - Quickly becomes out-of-sync with the code

### Option 3 [accepted]: New PWA webpage

- **Positive**:
  - Neutral, not specific to one framework
  - Provides a bundled overview
  - Easy to keep up to date
  - Don't have to repeat oneself in each of the code repositories
  - Does not have to be academic (add disclaimer: do not use as your source, but
    carefully study the references we provide)
- **Negative**:
  - Have to link by URL to this external webpage from the APIs
  - API links become invalid once the structure of this theory webpage changes

## Specification

The theory pages consist of a few sub-pages (**bold**), each covering the
following topics. Each of them can be ticked off in follow-up PRs or ADRs.

Note that the pages should be condense and serve as an evolving guide to more
specific literature. In addition, the intended audience is experimental
physicists, so we should emphasize the advantages and limitations of the
different techniques.

- [ ] **General Introduction**: The Aim of Partial Wave Analysis
  - [ ] Importance of decomposing interactions
  - [ ] Strong QCD coupling constant at low momentum transfer
  - [ ] Cannot compute intermediate states from theory
  - [ ] Need to collect properties: mass, width, spin, parity
- [ ] **Decay description**
  - [ ] Decomposition into partial waves
  - [ ] Scattering theory
    - Complex energy plane
  - [ ] (?) Lead-up to _T_-matrix
  - [ ] Amplitudes and intensities
    - From transition matrix to partial waves
    - (?) Difference with amplitude analysis
  - [ ] Initial states: 1, 2, and multi-body
  - [ ] Isobar model
    - Suitable for propagation, not rescattering
- [ ] **Common formalisms**
  - [ ] Helicity
    - [ ] Lorentz-invariance of helicity operator
    - [ ] Types
      - Two-body decay amplitude
      - Sequential two-body decay amplitude
    - [ ] Definition of angles
      - Production angle
      - Helicity angle
      - Treiman-Yang angle
      - Overview of kinematic variables
    - [ ] Dynamics:
      - Wigner-D functions
      - Clebsch-Gordan coefficients
    - [ ] Kinematic variables
    - [ ] An example
  - [ ] Canonical
  - [ ] Lorentz-invariant: Rarita-Schwinger
  - [ ] Other spin formalisms
    - (Covariant) tensor formalisms
    - Spin-projection formalisms
- [ ] **Dynamics**
  - [ ] _K_-matrix
  - [ ] Special cases of _K_-matrix:
    - Breit-Wigner
    - Flatté
  - [ ] Note on unitarity
  - [ ] Poles versus resonances
- [ ] **Experimental data**
  - [ ] Experiment types: formation vs production
  - [ ] Input data: momentum tuples
    - Why are only initial 4-momenta sufficient?
    - How to determine initial 4-momentum?
  - [ ] Observables and variables we want to compute
    - Luminosity
    - Cross-section
    - Branching fraction
    - (?) Fit fractions
- [ ] **Overview of latest insights**
  - [ ] Exotic states
- [ ] _Other concepts_ [*re-categorize!*]
  - [ ] Phase-space
  - [ ] Coherent vs incoherent
  - [ ] _P_-vector
  - [ ] (?) _S_-matrix
  - [ ] (?) Spin density
  - [ ] Constituent Quark Model
    - Asymptotic freedom and color confinement
    - _J^CP(I^G)_
    - Multiplets categorization
    - Importance of experimental data
- [ ] _Challenges_ [*Move to separate analysis sub-page?*]
  - [ ] Overlapping resonances
  - [ ] Coupled channels
