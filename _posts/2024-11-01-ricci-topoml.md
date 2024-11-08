---
title: "asdb"
date: 2024-11-01
excerpt: ""
image: /assets/ricci-topoml/cover.gif
---

{% include cover.html url="/assets/ricci-topoml/cover.gif" description="" %}

## But first...

Let us take a quick look at some background.

Assume you have a Riemannian manifold \\(\mathcal{M}\\) with a metric \\(g_0\\). We will need derivatives of tensor field so we will denote \\( \nabla \\) as the Levi-Civita connection of the metric.

For vector fields \\(X,Y,W,Z \in \Gamma(T\mathcal{M})\\), the Riemann curvature tensor \\(\text{Rm}\\) is defined as:

$$\text{Rm}(X,Y) := \underbrace{\nabla_Y\nabla_X - \nabla_X\nabla_Y}_{\text{measure of non-commutativity}} + \overbrace{\nabla_{[X,Y]}}^{\text{correction term}}\tag{1}$$

The Ricci tensor \\(\text{Ric}\\) is then defined as the trace of \\(\text{Rm}\\) which is a \\( (0,2) \\) symmetric tensor field:

$$\text{Ric}(X,Y) := \underbrace{\text{tr}(\text{Rm}(X,\cdot,Y,\cdot))}_{\text{average of sectional curvatures}} \tag{2}$$

We can simply view \\(\text{Ric}\\) tensor as a measure of how the volume of a geodesic ball in the manifold deviates from that of the corresponding ball in Euclidean space.

In local coordinates \\((x^1,...,x^n)\\), this can be written as:

$$\text{Ric}_{jk} = \sum_{i=1}^n R^i_{jik} \tag{3}$$

where \\(R^i_{jkl}\\) are the components of the Riemann curvature tensor.
The scalar curvature \\(R\\) is the trace of the Ricci tensor:

$$R := \underbrace{\text{tr}(\text{Ric})}_{\text{total curvature}} = \overbrace{\sum_{i,j=1}^n g^{ij}\text{Ric}_{ij}}^{\text{metric contraction}} \tag{4}$$

where \\(g^{ij}\\) are the components of the inverse metric tensor.

The Ricci flow is a process that evolves the metric of a manifold according to the Ricci curvature. The Ricci flow is a PDE,

$$\frac{\partial g(t)}{\partial t} = \underbrace{-2\text{Ric}(g(t))}_{\text{geometric heat flow}} \quad\text{and}\quad \overbrace{g(0) = g_0}^{\text{initial metric}} \tag{5}$$

where \\(\text{Ric}(g(t))\\) is the Ricci curvature of the metric \\(g(t)\\).

## What is the Ricci flow doing?

I like the popular heat flow view. The Ricci flow is like a geometric heat equation that tries to smooth out these irregularities over time. Just as heat flows from hot regions to cold regions until temperature evens out, the Ricci flow works to even out the curvature of a space.

The main goal of Ricci flow is to deform an initial metric \\(g_0\\) towards a more canonical metric by smoothing out curvature irregularities. Under Ricci flow, regions of high positive curvature tend to shrink while regions of negative curvature tend to expand. This happens because positive Ricci curvature makes the right side of the equation negative, causing the metric to decrease and the negative Ricci curvature makes the right side positive, increasing the metric. This works towards homogenizing the curvature distribution.

{% include theorem_proof.html name="How does the curvature change?" content="$$\frac{\partial R}{\partial t} = \underbrace{\Delta R}_{\text{diffusion}} + \overbrace{2|\text{Ric}|^2}^{\text{positive reaction term}} \tag{6}$$

where \\(R\\) is the scalar curvature and \\(\Delta\\) is the Laplace-Beltrami operator."
proof="While I like the stochastic-like interpretation of this manifold curvature, we will not use that to prove this and I will take a turn from a popular way of proving this.

1) For a tensor \\(\alpha\\), the evolution of its trace is:

$$\frac{\partial}{\partial t}(\text{tr}\alpha) = -\langle h,\alpha \rangle + \text{tr}\frac{\partial \alpha}{\partial t}$$

2) The evolution of the Ricci tensor is:

$$\frac{\partial}{\partial t}\text{Ric} = \mathcal{L}(\text{Ric})$$

where $\mathcal{L}$ is the Lichnerowicz Laplacian:

$$(\mathcal{L}h)(X,W) = \underbrace{\Delta h(X,W)}_{\text{diffusion}} - \overbrace{h(X,\text{Ric}(W)) - h(W,\text{Ric}(X))}^{\text{curvature interaction}} + \underbrace{2\text{tr}h(R(X,\cdot)W,\cdot)}_{\text{full curvature coupling}}$$

We can now compute $\frac{\partial R}{\partial t}$:

$$\begin{aligned}\frac{\partial R}{\partial t} &= \frac{\partial}{\partial t}(\text{tr Ric})\\&= -\langle h,\text{Ric}\rangle + \text{tr}\frac{\partial \text{Ric}}{\partial t}\\&= 2\langle \text{Ric},\text{Ric}\rangle + \text{tr}(\mathcal{L}\text{Ric})\end{aligned}$$

Notice, we used \\(h = -2\text{Ric}\\) from Equation (5).

The trace of the Lichnerowicz Laplacian acting on \\(\text{Ric}\\) gives us:

$$\text{tr}(\mathcal{L}\text{Ric}) = \Delta R$$

This works because:

- The trace of \\(\Delta \text{Ric}\\) is \\(\Delta R\\)
- The trace of the lower order terms gives us extra terms that are quadratic in \\(\text{Ric}\\)

Thus, we have:

$$\frac{\partial R}{\partial t} = \Delta R + 2|\text{Ric}|^2$$

From this, we can derive a useful inequality. Since we can decompose \\(\text{Ric}\\) into its traceless part and trace part:

$$\text{Ric} = \underbrace{\stackrel{\circ}{\text{Ric}}}_{\text{traceless part}} + \overbrace{\frac{R}{n}g}^{\text{trace part}}$$

We get:

$$|\text{Ric}|^2 = |\stackrel{\circ}{\text{Ric}}|^2 + \frac{R^2}{n}$$

Therefore:

$$\frac{\partial R}{\partial t} \geq \underbrace{\Delta R}_{\text{spreads curvature}} + \overbrace{\frac{2}{n}R^2}^{\text{amplifies curvature}}\tag{7}$$" %}

I like to think of Theorem (1) in a stochastic manner. The \\(\Delta R\\) term is like a diffusion term that spreads out curvature and the \\(\lvert\text{Ric}\rvert^2\\) term is always positive, which tends to increase the scalar curvature. A very useful conclusion which becomes somewhat more straightforward when you think of the stochastic interpretation is to understand what happens we start with positive Ricci curvature, it becomes singular in finite time. Since the Ricci curvature is positive, the scalar curvature \\(R\\) is also positive.

<div style="padding: 0.75em; border: 1px solid black;" markdown="1">
**Aside (Some bits of maximum principle):**

The main idea is to see if we can track the extremes of solutions and constrain them.

Let \\((M,g(t))\\) be a closed manifold with a time-dependent Riemannian metric. Suppose \\(u: M \times \left[\right.0,T\left.\right) \to \mathbb{R}\\) satisfies:

$$\frac{\partial u}{\partial t} \leq \Delta_{g(t)}u + \langle X(t), \nabla u \rangle + F(u)$$

where \(F: \mathbb{R} \to \mathbb{R}\) is locally Lipschitz, and there exists some constant \(C\) such that the initial condition satisfies, \\(u(x, 0) \leq \forall x \in M\\) and if \\(\phi(t)\\) solves the ODE:

$$\frac{d\phi}{dt} = F(\phi)\quad \text{and} \quad\phi(0) = C$$

for all \(x \in M\) and \(t \in [0,T)\) for which \(\phi(t)\) exists.

Then,

$$u(x,t) \leq \phi(t)$$

Given we already know From Equation (6) that,

$$\frac{\partial R}{\partial t} = \Delta R + 2|\text{Ric}|^2 \geq \Delta R + \frac{2}{n}R^2$$

</div>

Using the maximum principle, we can show that if \\(R\\) starts positive, it must blow up in finite time, forcing the space to collapse. To do so, let us make some substitutions:

- \\(\Delta R\\) is the Laplacian term
- \\(X(t)=0\\)
- \\(F(R) = \frac{2}{n}R^2\\) is our reaction term

Then the ODE is:
   
$$\frac{d\phi}{dt} = \frac{2}{n}\phi^2$$

$$\phi(0) = \min_{x \in M} R(x,0) = r_0 > 0$$

The solution to this ODE is:

$$\phi(t) = \frac{r_0}{1 - \frac{2r_0t}{n}}$$

By the maximum principle, 
   
$$R(x,t) \geq \phi(t)$$

And now since \\(\phi(t)\\) becomes infinite in finite time \\(T = \frac{n}{2r_0}\\), the scalar curvature must also become infinite by this time!

But we want to understand the shape just before it collapses? To do so we can rescale the metric to keep the volume constant:

$$\tilde{g}(t) = \overbrace{\frac{\text{Vol}(g_0)}{\text{Vol}(g(t))}}^{\text{volume preserving factor}} \underbrace{g(t)}_{\text{evolving metric}}$$

This normalized flow lets us see the limiting shape. Under our setting, the rescaled flow will converge to a round sphere or similar constant curvature space. Thus, the Ricci flow takes some random complicated geometric spaces and tries to deform them into simpler, more symmetric ones! (Well there are also "pinches" that might happen when getting into these better geometric spaces but let us leave this for later).

{% include theorem.html name="What does the metric converge to?" content="In ideal circumstances, the flow evolves the metric towards one with constant sectional curvature, making the manifold rounder. For a compact manifold, if the flow exists for all time and converges, the limit metric \\(g_{\infty}\\) satisfies:

$$\text{Ric}(g_{\infty}) = \underbrace{\lambda g_{\infty}}_{\text{Einstein condition}}$$

for some constant \\(\lambda\\), making \\(g_{\infty}\\) an Einstein metric." %}