---
 title: "#BIS-Hard but Not Impossible: Ferromagnetic Potts Model on Expanders"
 date: 2023-03-07
 excerpt: "How do you efficiently sample from a distribution that's algorithmically #BIS-hard? The ferromagnetic Potts model is a canonical Markov random field where monochromatic edges win the popularity contest. This article is about how polymer methods and extremal graph theory crack the sampling puzzle on d-regular weakly expanding graphs."
 image: /assets/ferromagnetic-potts/sample-graph.png
 tags: [statistical-physics, learning-algorithms, graph-theory]
---

The ferromagnetic Potts model is a canonical example of a Markov random field from statistical physics that is of great probabilistic and algorithmic interest. This is a distribution over all $$1$$-colorings of the vertices of a graph where monochromatic edges are favored. The algorithmic problem of efficiently sampling approximately from this model is known to be #BIS-hard, and has seen a lot of recent interest. This blog outlines some recently developed algorithms for approximately sampling from the ferromagnetic Potts model on d-regular weakly expanding graphs. This is achieved by a significantly sharper analysis of standard "polymer methods" using extremal graph theory and applications of Karger's algorithm to count cuts that may be of independent interest. This article is mostly about a rabbit hole I went down while reading the paper *Algorithms for the ferromagnetic Potts model on expanders* [^carlson2022algorithms].

## The Ferromagnetic Potts Model

Let’s pin down notation (and keep it light):

- $$G=(V,E)$$: finite graph
- $$q\in \mathbb{N}$$: number of colors; a coloring is $$\chi: V\to [q]$$
- $$m(\chi)$$: number of monochromatic edges under $$\chi$$
- $$\beta\in \mathbb{R}$$: inverse temperature

Define the Potts distribution

\begin{equation}
 p(\chi) \propto \exp\big(\beta\, m(\chi)\big),
\label{eq:potts-def}
\end{equation}

so for $$\beta>0$$ (ferromagnetic) matching edges are favored, and for $$\beta<0$$ (antiferromagnetic) they are discouraged. The normalized form is

\begin{equation}
 p(\chi) 
 = \frac{\exp\big(\beta\, m(\chi)\big)}{\underbrace{\sum_{\chi'} \exp(\beta\, m(\chi'))}_{\text{partition function}~Z_G(q,\beta)}}.
\label{eq:potts-p}
\end{equation}

When $$\beta=0$$ this is the uniform distribution over all $$q$$-colorings; as $$\beta\to -\infty$$ it concentrates on proper colorings.

## The Problem

We want to sample (approximately) from $$p(\chi)$$ in time polynomial in the graph size and the accuracy parameter.

A standard reduction says: it is enough to approximate $$Z_G(q,\beta)$$, since we can then turn partition-function approximations into samplers.

**Goal (approximate sampling).** Given $$G$$ and $$\beta$$, sample from a law $$q$$ such that the total variation distance is small:

\begin{equation}
 \lVert p-q \rVert_{\mathrm{TVD}} \le \epsilon, \qquad \lVert p-q \rVert_{\mathrm{TVD}} := \frac{1}{2}\sum_{\chi} \big|p(\chi)-q(\chi)\big|.
\label{eq:tvd}
\end{equation}

A Fully Polynomial Almost Uniform Sampler (FPAUS) produces an $$\epsilon$$-approximate sample in $$\mathrm{poly}(\mid G\mid,1/\epsilon)$$ time. A Fully Polynomial Time Approximation Scheme (FPTAS) returns a $$(1\pm\epsilon)$$-approximation to $$Z$$ in similar time. Conveniently, in these settings one typically has

\begin{equation}
 \text{FPTAS} \iff \text{FPAUS}.
\label{eq:fptas-fpaus}
\end{equation}

## Antiferromagnetic Potts model

For $$\beta<0$$, the same definition applies,

\begin{equation}
 p(\chi) \propto \exp\big(\beta\, m(\chi)\big), \qquad \beta<0.
\label{eq:anti}
\end{equation}

The algorithmic target is an FPTAS for $$Z_G(q,\beta)$$, which is equivalent (in the sense above) to an FPAUS for the distribution. Prior work shows there is a threshold $$\beta_c$$ with two regimes:

- For $$\beta < \beta_c$$, an FPTAS exists
- For $$\beta > \beta_c$$, no FPTAS unless $$\mathrm{NP} = \mathrm{RP}$$

This is where #BIS-hardness (counting independent sets in bipartite graphs) enters: approximating the Potts partition function is at least as hard as that, and without bipartiteness the problem is NP-hard.

To make things concrete, one proxy problem is: given a bipartite graph $$G$$, design an FPTAS for the number of independent sets in $$G$$. This already captures the complexity of counting proper $$q$$-colorings for $$q\ge 3$$, the number of stable matchings, and the number of antichains in posets.

## Main Results

Assume throughout that $$G$$ is $$d$$-regular on $$n$$ vertices. For a subset $$S\subseteq V$$, define its edge boundary

\begin{equation}
 \nabla(S) := \\# \{\,uv\in E ~:\; u\in S, v\notin S\,\}.
\label{eq:edge-boundary}
\end{equation}

The graph $$G$$ is an $$\eta$$-expander if every $$S\subseteq V$$ of size at most $$n/2$$ satisfies

\begin{equation}
 |\nabla(S)| \ge \eta\,|S|.
\label{eq:expander}
\end{equation}

**Theorem (informal).** For each $$\epsilon>0$$ there exist functions $$d(\epsilon)$$ and $$q(\epsilon)$$ such that there is an FPTAS for $$Z_G(q,\beta)$$ whenever $$G$$ is a $$d$$-regular 2-expander and the following conditions hold: $$q=\mathrm{poly}(d)$$ and $$\beta \notin (2\pm\epsilon)\, \tfrac{\ln q}{d}.$$

A sharper result proved in the referenced work is:

**Theorem (main).** For each $$\epsilon>0$$ and sufficiently large $$d$$, there is an FPTAS for $$Z_G(q,\beta)$$ for the class of $$d$$-regular triangle-free 1-expanders, provided $$q\ge \mathrm{poly}(d)$$ and $$\beta \notin (2\pm\epsilon)\, \tfrac{\ln q}{d}.$$

Previously, similar statements required stronger expansion with $$d = q^{\Omega(d)}$$ or higher temperature with $$q = d^{\Omega(d)}$$. It is plausible that the condition $$q\ge \mathrm{poly}(d)$$ is not actually necessary.

## Potts Distribution

The order-disorder threshold for the ferromagnetic model is

\begin{equation}
 \beta_0 := \ln\!\left(\frac{q-2}{(q-1)^{1-2/d} - 1}\right) = 2\, \frac{\ln q}{d}\,\Big(1+O\!\big(\tfrac{1}{q}\big)\Big).
\label{eq:beta0}
\end{equation}

We care about the regimes $$\beta < (1-\epsilon)\beta_0$$ and $$\beta > (1+\epsilon)\beta_0$$.

## Results

**Theorem (typical color class sizes).** Let $$\epsilon>0$$, $$d$$ large enough, $$q\ge \mathrm{poly}(d)$$, and let $$G$$ be a $$d$$-regular 2-expander on $$n$$ vertices. Then:

- If $$\beta < (1-\epsilon)\beta_0$$, every color class has size $$\tfrac{n}{q}\,(1\pm o(1))$$ with high probability
- If $$\beta > (1+\epsilon)\beta_0$$, there is a color class of size $$n - o(n)$$ with high probability

## Strategy (why it works)

- Pass to the random cluster model: a distribution on edge subsets

\begin{equation}
 p(A) \propto q^{k(A)}\, \big(e^{\beta}-1\big)^{|A|}, \qquad Z_G^{\mathrm{RC}}(q,\beta) = Z_G^{\mathrm{Potts}}(q,\beta),
\label{eq:rc}
\end{equation}

and sample by first drawing a random-cluster configuration and then giving each connected component a uniform color.

- Use standard polymer methods with sharper counting via extremal graph theory (Karger-style cut counting enters here) to control contributions of defects.

## Polymer Methods (at a glance)

At low temperature (large $$\beta$$), it is helpful to visualize a typical configuration as

\begin{equation}
 \text{coloring} = \underbrace{\text{ground state}}_{\text{one dominant color}} + \underbrace{\text{defects}}_{\text{small regions}}.
\label{eq:polymer-picture}
\end{equation}

Let the defect graph $$G$$ encode these regions as polymers. Then for a reference color (say “red”), one writes

\begin{equation}
 Z_{\text{red}}\, e^{-\beta n d /2} 
 = \sum_{I\subset V(G)}\; \prod_{\gamma\in I} w_\gamma,
\label{eq:polymer-sum}
\end{equation}

where $$w_\gamma$$ is the weight of a polymer $$\gamma$$. The cluster expansion is the multivariate Taylor expansion in the $$w_\gamma$$ of

\begin{equation}
 \ln\!\left( \sum_{I\subset V(G)} \prod_{\gamma\in I} w_\gamma \right),
\label{eq:cluster}
\end{equation}

and convergence is established by the Kotecký–Preiss criterion under the expansion conditions. A key combinatorial input is bounding how many connected vertex subsets have a given edge boundary in an $$\eta$$-expander.

**Theorem (counting connected subsets).** In an $$\eta$$-expander, the number of connected subsets containing a fixed vertex and with edge boundary at most $$b$$ is at most $$d^{O((1+1/\eta)b/d)}.$$

A companion question: how many $$q$$-colorings of an $$\eta$$-expander induce at most $$k$$ non-monochromatic edges? A crude but effective upper bound colors all but about $$k/d$$ vertices with the same color (the remaining set is likely independent) and colors the rest arbitrarily, giving

\begin{equation}
 \binom{n}{k/d} \; q^{\,k/d + 1}
\label{eq:color-count}
\end{equation}

candidates. In particular, for $$\eta$$-expanders and $$q\ge \mathrm{poly}(d)$$ there are at most $$n^4\, q^{O(k/d)}$$ such colorings.

Finally, the maximum of $$Z_G(q,\beta)$$ over all graphs with $$n$$ vertices, $$m$$ edges, and maximum degree $$d$$ is achieved by the disjoint union of $$K_{d+1}$$ and isolated vertices, giving useful benchmarks for the analysis.

{% include bibtex.html %}

## References

[^carlson2022algorithms]: Carlson, Charlie, et al. "Algorithms for the ferromagnetic Potts model on expanders." 2022 IEEE 63rd Annual Symposium on Foundations of Computer Science (FOCS). IEEE, 2022.

[^coulson_et_al]: Coulson, Matthew, et al. "Statistical physics approaches to Unique Games." arXiv preprint arXiv:1911.01504 (2019).

[^helmuth2019]: Helmuth, Tyler, Will Perkins, and Guus Regts. "Algorithmic pirogov-sinai theory." Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing. 2019.

[^frankl1981short]: Frankl, Peter, and Zoltán Füredi. "A short proof for a theorem of Harper about Hamming-spheres." Discrete Mathematics 34.3 (1981): 311-313.