---
title: "Deriving a Generalized Kaiming Initialization"
date: 2026-02-07
excerpt: "A new general form of Kaiming initialization here which does not assume: that the weights and inputs have zero mean and that the inputs have variance $1$."
image:
tags: [training, machine-learning, learning-algorithms]
---

Kaiming initialization, also known as He initialization, is a very popular method for initializing the weights of neural networks. Kaiming initialization makes a few assumptions about the distribution of the weights and inputs which usually hold. I was going through the derivation of Kaiming initialization (once again) for a course I am taking at UofT, which led me to think about relaxing some of these assumptions. We derive a general form of Kaiming initialization here which does not assume: that the weights and inputs have zero mean and that the inputs have variance $1$.

I did not find something like this in existing literature so I thought to write it up here.

## A Preface on Practicality

It is worth asking if this is useful. To me it seems, perhaps not. Most modern architectures rely heavily on normalization layers. These layers explicitly re-center activations (driving $\mu \to 0$) and normalize variances. In such regimes, the standard Kaiming initialization approximations hold up very well because the data is effectively "whitened" at every stage.

However, this is interesting just because it's fun to understand these mechanics. And if for some reason (nothing that I can think of right now) you want to train without normalization layers, or constrain weights to be non-negative ($\mu_W > 0$), this might be useful.

## The Usual Setup

We focus on a single linear layer followed by a ReLU non-linearity.

$$
\begin{equation}
    \underbrace{z = Wx}_{\text{Linear Layer}}, \quad \underbrace{a = \text{ReLU}(z)}_{\text{Activation}},
\end{equation}
$$

where $x \in \mathbb{R}^{n_{in}}$ is the input vector, $W \in \mathbb{R}^{n_{out} \times n_{in}}$ is the weight matrix, and $z \in \mathbb{R}^{n_{out}}$ is the pre-activation output.

We usually assume data and weights are centered at zero.

$$
\begin{equation}
\begin{split}
    x_i &\sim \mathcal{N}(0, 1) \\
    W_{ji} &\sim \mathcal{N}(0, \sigma^2)
\end{split}
\label{eq:standard-assumptions}
\end{equation}
$$

The goal is to determine the variance of the weights $W$ such that we can keep activation scale constant after ReLU. Under these standard assumptions, standard Kaiming initialization gives us,

$$
\begin{equation}
    \sigma^2 = \frac{2}{n_{in}}.
\end{equation}
$$

## Our Setup

We consider the same linear transformation $z = Wx$ (or $o = Wx$) but with a more general set of assumptions. We assume the inputs $x$ and weights $W$ are independent random variables with non-zero means and arbitrary variances,

$$
\begin{equation}
\begin{split}
    x_i &\sim \mathcal{N}(\mu_x, \sigma_x^2) \\
    W_{ji} &\sim \mathcal{N}(\mu_W, \sigma_W^2).
\end{split}
\end{equation}
$$

In both the usual setup and our setup, we assume independence between weights and inputs, and across indices. In particular,
$$\mathbb{E}[W_{ji} x_i] = \mathbb{E}[W_{ji}]\,\mathbb{E}[x_i] = \mu_W \mu_x.$$
So we are relaxing the standard constraint where $\mu_x = 0$ and $\mu_W = 0$.

## A Less General Case

Before tackling the full derivation with non-zero means, let's look at a "less general" case: the standard Kaiming Initialization. Here, we maintain the zero-mean assumption ($\mathbb{E}[x] = 0, \mathbb{E}[W] = 0$) but allow the input variance $\sigma_x^2$ to be arbitrary (not necessarily $1$).

This is quite similar to the standard Kaiming derivation, but makes a small step towards the general case.

### $\operatorname{Var}$ Before Activation

Let $z = Wx$ be the pre-activation value, where $z_j = \sum_{i=1}^{n_{in}} W_{ji} x_i$. We assume $x_i$ and $W_{ji}$ are independent with zero means.

We calculate the variance of a single output unit $z_j$:

$$
\begin{equation}
Var(z_j) = Var\left(\sum_{i=1}^{n_{in}} W_{ji} x_i\right)
\end{equation}
$$

Because $x_i$ and $W_{ji}$ are independent across $i$, the variance of the sum is the sum of the variances:

$$
\begin{equation}
Var(z_j) = \sum_{i=1}^{n_{in}} Var(W_{ji} x_i)
\end{equation}
$$

Using the variance product identity, $Var(AB) = \mathbb{E}[A^2]\mathbb{E}[B^2] - (\mathbb{E}[A]\mathbb{E}[B])^2$:

$$
\begin{equation}
Var(W_{ji} x_i) = \mathbb{E}[W_{ji}^2]\mathbb{E}[x_i^2] - (\mathbb{E}[W_{ji}]\mathbb{E}[x_i])^2
\end{equation}
$$

Since means are zero ($\mathbb{E}[W]=0, \mathbb{E}[x]=0$), this simplifies to:

$$
\begin{equation}
Var(W_{ji} x_i) = Var(W_{ji}) Var(x_i) = \sigma_W^2 \sigma_x^2
\end{equation}
$$

Substituting this back into the sum:

$$
\begin{equation}
Var(z_j) = \sum_{i=1}^{n_{in}} \sigma_W^2 \sigma_x^2 = n_{in} \sigma_W^2 \sigma_x^2
\end{equation}
$$

### $\operatorname{Var}$ After ReLU

Let $a = ReLU(z) = \max(0, z)$. The ReLU function sets all negative values to zero. Assuming $z_j$ has a symmetric distribution around zero (which tends to be true given zero-mean weights and inputs):
1.  Half the values become 0.
2.  The other half remain unchanged ($z^2$).

We calculate the expected squared value (the second moment):

$$
\begin{equation}
\mathbb{E}[a^2] = \frac{1}{2} \mathbb{E}[z^2]
\end{equation}
$$

Since $z$ has zero mean, $\mathbb{E}[z^2] = Var(z)$. The standard derivation uses the approximation that the variance is effectively halved by the ReLU:

$$
\begin{equation}
Var(a_j) \approx \frac{1}{2} Var(z_j)
\end{equation}
$$

### Solving for $\operatorname{Var}$

Substituting the pre-activation variance into the ReLU equation:

$$
\begin{equation}
Var(a_j) = \frac{1}{2} (n_{in} \sigma_W^2 \sigma_x^2)
\end{equation}
$$

**Constraint:** We want to preserve the variance scale, so we set $Var(a_j) = \sigma_x^2$:

$$
\begin{equation}
\frac{1}{2} n_{in} \sigma_W^2 \sigma_x^2 = \sigma_x^2
\end{equation}
$$

Solving for $\sigma_W^2$:

$$
\begin{equation}
\frac{1}{2} n_{in} \sigma_W^2 = 1 \implies \sigma_W^2 = \frac{2}{n_{in}}
\end{equation}
$$

Notice that $\sigma_x^2$ cancels out! This explains why Kaiming initialization works robustly even if earlier layers scale the variance, as long as the mean stays zero.

## The General Case

Now we move to the general case where we relax the zero-mean assumption. We assume inputs $x$ and weights $W$ have non-zero means $\mu_x, \mu_W$ and variances $\sigma_x^2, \sigma_W^2$.

### General Variance

First, we need to determine how the variance propagates through a linear layer when means are non-zero.

{% include lemma_proof.html name="Variance of a Product" content="For independent random variables $w$ and $x$, the variance of their product is: $$ \begin{equation} Var(wx) = \sigma_W^2 \sigma_x^2 + \sigma_W^2 \mu_x^2 + \mu_W^2 \sigma_x^2 \label{eq:general-variance-lemma} \end{equation} $$" proof="$$ \begin{aligned} Var(wx) &= \mathbb{E}[(wx)^2] - (\mathbb{E}[wx])^2 \\ &= \mathbb{E}[w^2]\mathbb{E}[x^2] - (\mathbb{E}[w]\mathbb{E}[x])^2 \\ &= (\sigma_W^2 + \mu_W^2)(\sigma_x^2 + \mu_x^2) - (\mu_W \mu_x)^2 \\ &= \sigma_W^2 \sigma_x^2 + \sigma_W^2 \mu_x^2 + \mu_W^2 \sigma_x^2 + \mu_W^2 \mu_x^2 - \mu_W^2 \mu_x^2 \\ &= \sigma_W^2 \sigma_x^2 + \sigma_W^2 \mu_x^2 + \mu_W^2 \sigma_x^2 \end{aligned} $$" %}

Using this lemma, for a layer with $n_{in}$ inputs, the total variance of the pre-activation $z_j = \sum_{i=1}^{n_{in}} W_{ji}x_i$ is simply the sum of the variances (since terms are independent),

$$
\begin{equation}
    Var(z) = \sum_{i=1}^{n_{in}} Var(W_{ji} x_i) = n_{in} \left( \sigma_W^2 (\sigma_x^2 + \mu_x^2) + \mu_W^2 \sigma_x^2 \right).
\label{eq:layer-variance}
\end{equation}
$$

### General Xavier / Glorot Initialization

To start, let us consider the case without any activation function (or a linear activation). This allows us to derive a generalization of Xavier (Glorot) Initialization.

#### Forward Pass Constraint

For the forward pass, we require the output variance $Var(z)$ to roughly equal the input variance $\sigma_x^2$. If $Var(z) > \sigma_x^2$, the signal explodes; if $Var(z) < \sigma_x^2$, it vanishes.

Using our result from Equation \eqref{eq:layer-variance}, we set $Var(z) = \sigma_x^2$ and solve for the weight variance $\sigma_W^2$:

$$
\begin{equation}
\begin{split}
    n_{in} \left[ \sigma_W^2 (\sigma_x^2 + \mu_x^2) + \mu_W^2 \sigma_x^2 \right] &= \sigma_x^2 \\
    n_{in} \sigma_W^2 (\sigma_x^2 + \mu_x^2) &= \sigma_x^2 - n_{in} \mu_W^2 \sigma_x^2 \\
    \sigma_W^2 &= \frac{\sigma_x^2 (1 - n_{in} \mu_W^2)}{n_{in} (\sigma_x^2 + \mu_x^2)} \\
    &= \frac{1 - n_{in} \mu_W^2}{n_{in} (1 + \frac{\mu_x^2}{\sigma_x^2})}
\end{split}
\end{equation}
$$

#### Backward Pass Constraint

For the backward pass, we want to preserve the variance of the gradients flowing backwards. Due to the symmetry of linear layers, the derivation is identical, but we sum over the $n_{out}$ output units instead of $n_{in}$ inputs. We also replace input statistics ($x$) with gradient statistics ($g$, e.g., $\mu_g, \sigma_g^2$).

Thus, we require:

$$
\begin{equation}
    \sigma_W^2 = \frac{1 - n_{out} \mu_W^2}{n_{out} (1 + \frac{\mu_g^2}{\sigma_g^2})}.
\end{equation}
$$

#### The Xavier Solution

We now have two candidate weight variances: one that preserves variance in the forward direction, and one that preserves variance in the backward direction. Following the same motivation as standard Xavier/Glorot initialization, we combine these two constraints into a single choice of $(\sigma_W^2)$ by taking the harmonic mean.

From the forward-pass constraint \(Var(z)=\sigma_x^2\), we derived \eqref{eq:sigmaW_fwd}. From the backward-pass constraint (same derivation with \(n_{out}\) and gradient statistics), we derived \eqref{eq:sigmaW_bwd}.

Let's start by defining the harmonic mean,

$$
\begin{equation}
\sigma_W^2
=
\mathrm{HM}\!\left(\sigma_{W,\text{fwd}}^2,\sigma_{W,\text{bwd}}^2\right)
=
\frac{2}{\frac{1}{\sigma_{W,\text{fwd}}^2}+\frac{1}{\sigma_{W,\text{bwd}}^2}}.
\label{eq:harmonic_mean_def}
\end{equation}
$$

Now, make the reciprocals from Equation \eqref{eq:harmonic_mean_def} a bit easier to work with,

$$
\begin{equation}
\frac{1}{\sigma_{W,\text{fwd}}^2}
=
\frac{n_{in}\left(1+\frac{\mu_x^2}{\sigma_x^2}\right)}{1-n_{in}\mu_W^2},
\qquad
\frac{1}{\sigma_{W,\text{bwd}}^2}
=
\frac{n_{out}\left(1+\frac{\mu_g^2}{\sigma_g^2}\right)}{1-n_{out}\mu_W^2}.
\label{eq:reciprocals}
\end{equation}
$$

Substitute Equation \eqref{eq:reciprocals} into \eqref{eq:harmonic_mean_def},

$$
\begin{equation}
\boxed{
\sigma_W^2
=
\frac{2}{
\frac{n_{in}\left(1+\frac{\mu_x^2}{\sigma_x^2}\right)}{1-n_{in}\mu_W^2}
+
\frac{n_{out}\left(1+\frac{\mu_g^2}{\sigma_g^2}\right)}{1-n_{out}\mu_W^2}
}.
}
\label{eq:general_xavier_harmonic}
\end{equation}
$$

Let's do a little bit of algebraic manipulation to make this look a bit nicer. We can multiply numerator and denominator by $\left(1-n_{in}\mu_W^2\right)\left(1-n_{out}\mu_W^2\right)$,

$$
\begin{equation}
\boxed{
\sigma_W^2
=
\frac{
2\left(1-n_{in}\mu_W^2\right)\left(1-n_{out}\mu_W^2\right)
}{
n_{in}\left(1+\frac{\mu_x^2}{\sigma_x^2}\right)\left(1-n_{out}\mu_W^2\right)
+
n_{out}\left(1+\frac{\mu_g^2}{\sigma_g^2}\right)\left(1-n_{in}\mu_W^2\right)
}.
}
\label{eq:general_xavier_harmonic_rational}
\end{equation}
$$

Let us try to plug in standard Xavier into Equation \eqref{eq:general_xavier_harmonic_rational} to see if we can recover Xavier. Under the standard Xavier assumptions,

$$
\mu_W = 0,\quad \mu_x = 0,\quad \mu_g = 0.
$$

Lets us work through the substitutions. First we have the ratio terms,

$$
\begin{equation}
\begin{split}
1+\frac{\mu_x^2}{\sigma_x^2} &= 1+\frac{0}{\sigma_x^2} = 1,\\
1+\frac{\mu_g^2}{\sigma_g^2} &= 1+\frac{0}{\sigma_g^2} = 1.
\end{split}
\label{eq:xavier_numerator_substitutions}
\end{equation}
$$

Then the denominators,

$$
\begin{equation}
\begin{split}
1-n_{in}\mu_W^2 &= 1-n_{in}\cdot 0^2 = 1,\\
1-n_{out}\mu_W^2 &= 1-n_{out}\cdot 0^2 = 1.
\end{split}
\label{eq:xavier_substitutions}
\end{equation}
$$

Now substitute Equation \eqref{eq:xavier_substitutions}\eqref{eq:xavier_numerator_substitutions} into \eqref{eq:general_xavier_harmonic},

$$
\begin{equation}
\sigma_W^2
=
\frac{2}{
\frac{n_{in}\cdot 1}{1}
+
\frac{n_{out}\cdot 1}{1}
}
=
\frac{2}{n_{in}+n_{out}}.
\end{equation}
$$

This exactly recovers the usual Xavier/Glorot variance!

{% include remark.html content="For $\sigma_{W,\text{fwd}}^2$ and $\sigma_{W,\text{bwd}}^2$ to be positive (and for the harmonic mean to be well-defined), we require,

$$
1-n_{in}\mu_W^2>0
\quad\text{and}\quad
1-n_{out}\mu_W^2>0.
$$" %}

### General Kaiming / He Initialization

Our goal now is to maintain variance after the ReLU activation $a = \max(0, z)$. We require $Var(a) = \sigma_x^2$. Since $z$ is a sum of many independent random variables ($n_{in}$ is typically large), by the Central Limit Theorem (CLT), we can approximate the pre-activation $z$ as a Gaussian variable:

$$
\begin{equation}
z \sim \mathcal{N}(\mu_z, \sigma_z^2)
\end{equation}
$$

First, we calculate the mean $\mu_z$. Since expectation is linear and weights/inputs are independent:

$$
\begin{equation}
\mu_z = \mathbb{E}\left[\sum_{i=1}^{n_{in}} W_{ji} x_i\right] = \sum_{i=1}^{n_{in}} \mathbb{E}[W_{ji}]\mathbb{E}[x_i] = n_{in} \mu_W \mu_x
\end{equation}
$$

For the variance $\sigma_z^2$, we use Equation \eqref{eq:layer-variance} derived earlier:

$$
\begin{equation}
\sigma_z^2 = Var(z) = n_{in} \left( \sigma_W^2 (\sigma_x^2 + \mu_x^2) + \mu_W^2 \sigma_x^2 \right)
\end{equation}
$$

Now, we must calculate the variance of this distribution after it passes through the ReLU function.

#### Variance of a Rectified Gaussian

Let $\phi(\cdot)$ be the standard normal PDF and $\Phi(\cdot)$ be the standard normal CDF. We define the standardized mean shift $\alpha$ as:

$$
\begin{equation}
\alpha = \frac{\mu_z}{\sigma_z}
\end{equation}
$$

Using standard results for truncated/rectified Gaussians, we can derive the moments of the output $a$. The expectation involves integrating over the positive part of the Gaussian distribution (since ReLU zeros out the negative part). We denote the integration variable for the pre-activation values as $\zeta$, and $p(\zeta)$ as the probability density function of $z \sim \mathcal{N}(\mu_z, \sigma_z^2)$.

The expected value is:

$$
\begin{equation}
\begin{aligned} 
\mathbb{E}[a] &= \int_{-\infty}^{\infty} \max(0, \zeta) p(\zeta) d\zeta \\
&= \int_{0}^{\infty} \zeta \frac{1}{\sigma_z \sqrt{2\pi}} \exp\left(-\frac{(\zeta - \mu_z)^2}{2\sigma_z^2}\right) d\zeta \\
&= \sigma_z \phi(\alpha) + \mu_z \Phi(\alpha)
\end{aligned}
\end{equation}
$$

Similarly, the second moment is:

$$
\begin{equation}
\begin{aligned} 
\mathbb{E}[a^2] &= \int_{0}^{\infty} \zeta^2 p(\zeta) d\zeta \\
&= (\sigma_z^2 + \mu_z^2)\Phi(\alpha) + \mu_z \sigma_z \phi(\alpha)
\end{aligned}
\end{equation}
$$

The variance is $Var(a) = \mathbb{E}[a^2] - (\mathbb{E}[a])^2$. To simplify this, we substitute $\mu_z = \alpha \sigma_z$ and factor out $\sigma_z^2$:

$$
\begin{equation}
\begin{split}
Var(a) &= \sigma_z^2 \left[ (\alpha^2 + 1)\Phi(\alpha) + \alpha \phi(\alpha) \right] - \sigma_z^2 \left[ \alpha \Phi(\alpha) + \phi(\alpha) \right]^2 \\
&= \sigma_z^2 \left( (1 + \alpha^2)\Phi(\alpha) + \alpha \phi(\alpha) - (\phi(\alpha) + \alpha \Phi(\alpha))^2 \right)
\end{split}
\end{equation}
$$

Thus, we can express the variance as a scaled version of the pre-activation variance:

$$
\begin{equation}
    Var(a) = \sigma_z^2 \cdot K(\alpha)
\end{equation}
$$

where $K(\alpha)$ is the Variance Reduction Factor:

$$
\begin{equation}
    K(\alpha) = (1+\alpha^2)\Phi(\alpha) + \alpha\phi(\alpha) - (\phi(\alpha) + \alpha\Phi(\alpha))^2
\end{equation}
$$

*Note: $\Phi(\alpha)$ is related to the error function by $\Phi(\alpha) = \frac{1}{2}\left[ 1 + \text{erf}\left(\frac{\alpha}{\sqrt{2}}\right) \right]$.*

#### The General Solution

We start again with our goal: output variance equals input variance.

$$
\begin{equation}
\begin{split}
    Var(a) &= \sigma_x^2 \\
    \sigma_z^2 \cdot K(\alpha) &= \sigma_x^2
\end{split}
\end{equation}
$$

Substitute the expression for $\sigma_z^2$ (from Equation \eqref{eq:layer-variance}):

$$
\begin{equation}
    n_{in} \left[ \sigma_W^2 (\sigma_x^2 + \mu_x^2) + \mu_W^2 \sigma_x^2 \right] \cdot K(\alpha) = \sigma_x^2
\end{equation}
$$

Dividing by $\sigma_x^2$ and solving for $\sigma_W^2$:

$$
\begin{equation}
    n_{in} \left[ \sigma_W^2 \left(1 + \frac{\mu_x^2}{\sigma_x^2}\right) + \mu_W^2 \right] = \frac{1}{K(\alpha)}
\end{equation}
$$

$$
\begin{equation}
\boxed{
    \sigma_W^2 = \frac{\frac{1}{n_{in} K(\alpha)} - \mu_W^2}{1 + \frac{\mu_x^2}{\sigma_x^2}}
}
\end{equation}
$$

This equation gives us the generalized variance $\sigma_W^2$. However, note that $\alpha = \frac{\mu_z}{\sigma_z}$ itself depends on $\sigma_W^2$ (via $\sigma_z$), making this an implicit equation that must generally be solved numerically.

#### A Numeric Note

It is commonly known that for the zero-mean case, the variance is halved, implying $K(0) = 0.5$. This is actually an approximation.

If we calculate $K(0)$ exactly using the formula above with $\alpha=0$:
*   $\Phi(0) = 0.5$
*   $\phi(0) = \frac{1}{\sqrt{2\pi}} \approx 0.3989$

$$
\begin{equation}
K(0) \approx 0.3408
\label{eq:K0}
\end{equation}
$$

The key subtlety is that the ReLU output does not have zero mean even when $z$ is centered. In fact, for $z \sim \mathcal{N}(0,\sigma_z^2)$,
$$
\mathbb{E}[a^2] = \frac{1}{2}\sigma_z^2 \quad \text{but} \quad Var(a) = \left(\frac{1}{2} - \frac{1}{2\pi}\right)\sigma_z^2 \approx 0.3408\,\sigma_z^2.
$$
Standard Kaiming/He initialization targets preservation of the second moment (or makes the approximation $Var(a)\approx \mathbb{E}[a^2]$), which is why it yields the familiar $2/n_{in}$.

#### Feasibility Constraints

For a valid solution to exist, the calculated variance must be positive ($\sigma_W^2 > 0$). Looking at the numerator of our general formula, this implies:

$$
\begin{equation}
\frac{1}{n_{in} K(\alpha)} > \mu_W^2 \implies n_{in} \mu_W^2 K(\alpha) < 1
\end{equation}
$$

If the mean of the weights $\mu_W$ is too large, it may be impossible to initialize the network to preserve variance, regardless of $\sigma_W^2$. This provides a bound on how far we can shift the weight distribution from zero before initialization breaks down.

## Solving the Implicit Equation

As noted, the final equation is transcendental because $\sigma_W^2$ appears on the LHS and also inside the $K(\alpha)$ term on the RHS (since $\alpha = \mu_z/\sigma_z$ depends on $\sigma_W$).

$$
\begin{equation}
\sigma_W^2 = \text{RHS}(\sigma_W^2)
\end{equation}
$$

To find the correct initialization variance it should be straightforward to use a numerical root-finding method. We define the residual function:

$$
\begin{equation}
f(\sigma_W^2) = \sigma_W^2 - \frac{\frac{1}{n_{in} K(\alpha(\sigma_W^2))} - \mu_W^2}{1 + \frac{\mu_x^2}{\sigma_x^2}}
\end{equation}
$$

We can solve $f(\sigma_W^2) = 0$ using methods like Newton-Raphson.
