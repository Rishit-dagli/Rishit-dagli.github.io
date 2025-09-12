---
title: "Compression Unlocks Statistical Learning Secrets"
date: 2023-03-06
excerpt: "Characterizing the sample complexity of different machine learning tasks is an important question in learning theory. This article reviews the less conventional approach of using compression schemes for proving sample complexity upper bounds, with specific applications in learning under adversarial perturbations and learning Gaussian mixture models."
tags: [statistical-learning, compression, machine-learning]
---

Characterizing sample complexity across learning tasks is a core goal in learning theory. Classic Vapnik-Chervonenkis (VC) theory[^devroye1996vapnik] explains binary classification, but many other settings—like density estimation and adversarially robust learning—remain subtler. This note reviews a complementary approach: compression schemes for proving sample‑complexity upper bounds, with applications to robust learning and Gaussian mixture models. I mainly started looking into this class of techniques after a rabbit hole I went down after reading *Adversarially Robust Learning with Tolerance* [^ashtiani23a].

## Setup and Assumptions

Let’s fix the basic objects once so we don’t keep repeating them. We have a domain $$Z$$ and a data distribution $$D_Z$$ over it. A training set is an i.i.d. sample $$S\sim D_Z^m$$ of size $$m$$. We pick a hypothesis class $$H$$ and a task‑specific risk functional $$L(D_Z,h)$$ (for example, total variation distance in density estimation, or misclassification error in classification). Think of $L$ as measuring mismatch between the world ($D_Z$) and a model’s predictions.

Given a learner $$A_{Z,H}: Z^*\to H$$ that maps a sample to a hypothesis, we’ll compare its risk against the in‑class optimum $$OPT = \inf_{h\in H} L(D_Z,h)$$. You might wonder why we benchmark against $$OPT$$ instead of the Bayes optimal; this keeps the discussion model‑agnostic and lets us focus on sample complexity rather than approximation power. In other words: we ask “how many samples suffice to get close to the best member of $H$?” rather than “is $H$ rich enough to approximate ground truth?”[^opt-vs-bayes]

## Density Estimation

Goal: for every $$D_Z$$, the output $$A_{Z,H}(S)$$ should be close to $$OPT$$ with high probability. But you might ask: close in what sense? We’ll use total variation distance as a running example: $$L(D_Z,h) = d_{\mathrm{TV}}(D_Z,h)$$.

We say $$A_{Z,H}$$ PAC‑learns $$H$$ with $$m(\epsilon,\delta)$$ samples if for all $$D_Z$$, for all $$\epsilon>0$$ and $$\delta\in(0,1)$$, when $$S\sim D_Z^{m(\epsilon,\delta)}$$ then

$$
\begin{equation}
\Pr_S\left[\color{blue}{L(D_Z,A_{Z,H}(S))} > \underbrace{\color{orange}{\epsilon}}_{\text{target}} + \underbrace{\color{purple}{C\cdot OPT}}_{\text{approx. to best in }H}\right] < \color{green}{\delta}
\label{eq:pac-density}
\end{equation}
$$

**Theorem (Single Gaussian density estimation).** For $$H$$ the class of all Gaussians in $$\mathbb{R}^d$$ and any constant $$C=2$$,
\begin{equation}
 \color{blue}{m(\epsilon,\delta)} = O\!\left(\frac{\color{purple}{d^2} + \log\!\left(\tfrac{1}{\color{green}{\delta}}\right)}{\color{orange}{\epsilon^2}}\right).
\label{eq:gaussian-density-bound}
\end{equation}

Fixing a constant confidence (say $$\delta=0.01$$) gives

\begin{equation}
\Pr_S\big[\,\color{blue}{L(D_Z,A_{Z,H}(S))} > \color{orange}{\epsilon} + \color{purple}{C\cdot OPT}\,\big] < \color{green}{0.01},
\label{eq:pac-density-fixed}
\end{equation}

with sample complexity

\begin{equation}
 m(\epsilon) = O\!\left(\frac{d^2}{\epsilon^2}\right).
\label{eq:gaussian-density-bound-fixed}
\end{equation}

If you’re thinking “why $$d^2$$?”, a quick intuition is that estimating a Gaussian in $$\mathbb{R}^d$$ involves a mean ($$d$$ parameters) and a covariance ($$\approx d^2$$ parameters), so sample needs scale with the number of effective degrees of freedom.

## Binary Classification (with adversarial perturbations)

Binary robustness replaces pointwise loss with worst‑case loss over a neighborhood $\color{orange}{U(x)}$. This enlarges the “felt” hypothesis class, which explains why naive ERM can fail even when standard learning succeeds.

Binary classification: $$Z = X \times \{0,1\}$$, hypotheses $$h: X \to \{0,1\}$$. Define the 0/1 loss $$\ell^{0/1}(h,x,y) = \mathbf{1}\{h(x)\ne y\}$$ and risk $$L(D_Z,h) = \mathbb{E}_{(x,y)\sim D_Z}\,\ell^{0/1}(h,x,y)$$. For halfspaces in $$\mathbb{R}^d$$,

\begin{equation}
 \color{blue}{m(\epsilon)} = O\!\left(\frac{\color{purple}{d}}{\color{orange}{\epsilon^2}}\right).
\label{eq:halfspace-bound}
\end{equation}

Adversarial risk: given a perturbation set $$U(x)\subseteq X$$, define

\begin{equation}
 \ell^{U}(h,x,y) = \sup_{\bar{x}\in \overbrace{\color{orange}{U(x)}}^{\text{allowed perturbations}}} 
 \underbrace{\color{blue}{\ell^{0/1}(h,\bar{x},y)}}_{\text{0/1 loss}},
\label{eq:adv-loss}
\end{equation}

and

\begin{equation}
 \color{blue}{L^{U}(D_Z,h)} = \mathbb{E}_{(x,y)\sim \color{purple}{D_Z}}\,\color{blue}{\ell^{U}(h,x,y)}.
\label{eq:adv-risk}
\end{equation}

A PAC statement mirrors the standard one (for fixed confidence):

\begin{equation}
 \Pr_S\big[\,L^U(D_Z, A_{Z,H}(S)) > \epsilon + C\cdot OPT\,\big] < 0.01.
\label{eq:pac-adv}
\end{equation}

Richer hypothesis classes can both fit better and be harder to learn. And here’s the twist: in the adversarial world the neighborhood $$U(x)$$ effectively enlarges the hypothesis complexity the learner “feels”, which is why robust ERM can fail; uniform convergence bounds can break down when you must be correct on an entire ball around each point.

In the standard (non‑adversarial) case, VC dimension quantifies complexity:

**Theorem (VC dimension sample complexity).** For any class $$H$$ with VC dimension $$VC(H)$$,
\begin{equation}
 \color{blue}{m(\epsilon)} = \Theta\!\left(\frac{\color{purple}{VC(H)}}{\color{orange}{\epsilon^2}}\right).
\label{eq:vc-sample}
\end{equation}

Empirical risk minimization (ERM) and uniform convergence:

\begin{equation}
 \color{blue}{L(S,h)} = \frac{1}{\color{green}{|S|}} \sum_{(x,y)\in \color{purple}{S}} \color{blue}{\ell^{0/1}(h,x,y)}, \qquad h \in \arg\min_{h\in H} \color{blue}{L(S,h)},
\label{eq:erm}
\end{equation}

and

\begin{equation}
 \sup_{h\in H} \big|\color{blue}{L(S,h)} - \color{blue}{L(D_Z,h)}\big| = O\!\left(\sqrt{\frac{\color{purple}{VC(H)}}{\color{green}{|S|}}}\right) \;\text{w.p.}>0.99.
\label{eq:uniform-conv}
\end{equation}

**Remark.** In the adversarial world the neighborhood $$U(x)$$ effectively enlarges the hypothesis complexity the learner “feels”, which is why robust ERM can fail. Uniform convergence may break: $$\sup_{h\in H} \mid L^U(S,h) - L^U(D_Z,h)\mid$$ can be unbounded.

## Sample Compression

Compression asks: how can we compress a training set into a few labeled examples so that a decoder reconstructs a good hypothesis? For simple linear classification, the number of bits can be unbounded (sample‑dependent), but compression by examples is often feasible.

**Theorem (Compression implies learnability).** If a class $$H$$ admits a sample compression scheme of size $$k$$, then for some universal constant and ignoring polylog factors,
\begin{equation}
 \color{blue}{m(\epsilon)} = \tilde{O}\!\left(\frac{\color{purple}{k}}{\color{orange}{\epsilon^2}}\right).
\label{eq:comp-learn}
\end{equation}

**Theorem (Learnability implies compressibility).** If $$H$$ is PAC learnable with VC dimension $$VC(H)$$, then it admits a compression scheme of size
\begin{equation}
 \color{purple}{k} = 2^{O(\color{purple}{VC(H)})}.
\label{eq:learn-comp}
\end{equation}

A commonly held conjecture is that the right scale is $$k = \Theta(VC(H))$$. If true, it would tie together the combinatorial and algorithmic views of learnability quite tightly.

Why does compression help? A $k$‑example compression is a short certificate for a hypothesis. Short descriptions generalize: the decoder is deterministic, so the effective hypothesis class has description length $\tilde O(k)$, yielding bounds like (\ref{eq:comp-learn}). This intuition survives robust settings when the compressed core encodes local geometry (e.g., margins or certified neighborhoods).

In adversarial settings, the intuition is similar but the stakes are higher: you want the compressed set to carry not just labels, but also local robustness information. A naïve robust compression can blow up sample complexity ($$m^U(\epsilon)=O(2^{VC(H)}/\epsilon^2)$$), which motivates the tolerant variants below.

For adversarial classification, we had

\begin{equation}
 \ell^{0/1}(h,x,y) = \mathbf{1}\{h(x)\ne y\}, \quad \ell^{U}(h,x,y) = \sup_{\bar{x}\in U(x)} \ell^{0/1}(h,\bar{x},y),
\label{eq:adv-loss-restated}
\end{equation}

so

\begin{equation}
 L^{U}(D_Z,h) = \mathbb{E}_{(x,y)\sim D_Z}\,\ell^{U}(h,x,y).
\label{eq:adv-risk-restated}
\end{equation}

A direct compression approach that forces the decoder to recover training labels (and their neighbors) yields, for some classes,

\begin{equation}
 \color{blue}{m^{U}(\epsilon)} = O\!\left(\frac{2^{\color{purple}{VC(H)}}}{\color{orange}{\epsilon^2}}\right),
\label{eq:robust-compression}
\end{equation}

exhibiting exponential dependence on $$VC(H)$$.

## Tolerant Adversarial Learning

Essentially, we benchmark against the best $h$ that is robust under a friendlier neighborhood $V$ (not necessarily $U$). This relaxes the target and restores learnability while keeping robustness in view.

[^ashtiani23a] introduced tolerant adversarial learning: $$A_{Z,H}$$ PAC‑learns $$H$$ with $$m(\epsilon)$$ samples if $$\forall D_Z,\, \forall \epsilon\in(0,1)$$, for $$S\sim D_Z^{m(\epsilon)}$$,

\begin{equation}
 \Pr_S\Big[\,\color{blue}{L^U(D_Z,A_{Z,H}(S))} > \color{orange}{\epsilon} + \inf_{h\in H} \color{blue}{L^V(D_Z,h)}\,\Big] < \color{green}{0.01}.
\label{eq:tolerant-pac}
\end{equation}

\begin{equation}
 \color{blue}{m^{U,V}(\epsilon)} = \tilde{O}\!\left( \frac{\color{purple}{VC(H)}\, \color{green}{d}\, \log\!\big(1+\tfrac{1}{\color{green}{\gamma}}\big)}{\color{orange}{\epsilon^2}} \right).
\label{eq:tolerant-bound}
\end{equation}

What changes conceptually? Instead of forcing correctness on every point in a (possibly infinite) neighborhood, we define a noisy empirical distribution using $$V(x)$$, boost weak learners to drive error small under that distribution, encode the few samples used by boosting, and let the decoder smooth the hypothesis. This avoids compressing an infinite set while still targeting robustness. If you’re thinking “couldn’t we just cap the adversary?”, yes, that’s another relaxation (bounded adversary, limited black‑box queries, certification), but tolerant learning offers a principled, data‑driven route.

Other relaxations to avoid the $$2^{O(VC)}$$ barrier include: bounded adversary, limited black‑box query access, and certification‑style guarantees.

## Gaussian Mixture Models

Gaussian mixture models (GMMs) are universal density approximators and building blocks for richer classes. A 3‑component GMM has density

\begin{equation}
 \color{blue}{f(x)} = \color{green}{w_1}\,\mathcal{N}(x\mid \color{purple}{\mu_1},\color{purple}{\Sigma_1}) + \color{green}{w_2}\,\mathcal{N}(x\mid \color{purple}{\mu_2},\color{purple}{\Sigma_2}) + \color{green}{w_3}\,\mathcal{N}(x\mid \color{purple}{\mu_3},\color{purple}{\Sigma_3}).
\label{eq:gmm-density}
\end{equation}

We say $$F$$ is the class of GMMs with $$k$$ components in $$\mathbb{R}^d$$. How many samples suffice to learn $$f\in F$$ within $$L_1$$ error $$\epsilon$$? For a single Gaussian in $$\mathbb{R}^d$$,

\begin{equation}
 O\!\left(\frac{\color{purple}{d^2}}{\color{orange}{\epsilon^2}}\right) = O\!\left(\frac{\text{parameters}}{\color{orange}{\epsilon^2}}\right)
\label{eq:gmm-single}
\end{equation}

samples are sufficient (and necessary). For $$k$$ Gaussians, a natural question is whether

\begin{equation}
 O\!\left(\frac{\color{purple}{k d^2}}{\color{orange}{\epsilon^2}}\right) = O\!\left(\frac{\text{parameters}}{\color{orange}{\epsilon^2}}\right)
\label{eq:gmm-k}
\end{equation}

suffices. You might think of the classification view here: the induced decision boundaries are quadratic, and the capacity (e.g., VC dimension) scales accordingly.

## Compression Framework

Let $$F$$ be a class of distributions (e.g., Gaussians). If an encoder sends $$t$$ points (from $$m$$ points) and a decoder reconstructs an approximation to $$D$$, then we say $$F$$ admits a $$(t,m)$$ compression scheme.

**Theorem (Generalization from distribution compression).** If $$F$$ has a distribution compression scheme of size $$(t,m)$$, then the sample complexity of learning $$F$$ is

$$
\begin{equation}
 \tilde{O}\!\left( \underbrace{\color{blue}{\frac{t}{\epsilon^2}}}_{\text{statistical term}} + \underbrace{\color{purple}{m}}_{\text{covering term}} \right).
\label{eq:compression-sample}
\end{equation}
$$

<b>Proof (idea):</b> Compressing to $$t$$ examples bounds the effective description length; standard generalization from compressed samples yields the stated dependence on $$t$$ and $$m$$ up to polylog factors.

**Theorem (Mixtures preserve compression).** If $$F$$ has a compression scheme of size $$(t,m)$$ then mixtures of $$k$$ members of $$F$$ admit $$(kt,km)$$ compression. Intuition: encode each component with its own $(t,m)$ code and concatenate; decoding applies component‑wise.

\begin{equation}
 (t,m)\;\Rightarrow\;(kt,km).
\label{eq:mixture-compression}
\end{equation}

<b>Proof (sketch):</b> Encode each component using $$(t,m)$$; concatenating encodings and decodings preserves reconstruction error, giving linear scaling in $$k$$ for both tokens and sample budget.

Thus distribution compression schemes extend naturally to mixtures. For GMMs in $$\mathbb{R}^d$$ it suffices to design a good scheme for a single Gaussian: encode the center and principal axes of the ellipsoid to recover $$\mathcal{N}(\mu,\Sigma)$$, which gives roughly $$(t,m)=\tilde{O}(d^2, 1/\epsilon)$$. The main technical hurdle is encoding the $$d$$ eigenvectors accurately using only $$d^2$$ points when the condition number $$\sigma_{\max}/\sigma_{\min}$$ is large.

## Conclusion

Compression gives us a second lens on learnability. Instead of bounding the capacity of an entire hypothesis class directly, we ask whether good hypotheses can be reconstructed from a tiny, stable core of examples. When the answer is “yes,” we get clean sample bounds ($$\tilde{O}(t/\epsilon^2)+m$$), and more importantly an algorithmic blueprint: pick the right anchors, and let the decoder do the rest. This perspective explains why compression can keep working when uniform convergence fails (robust learning) and why it scales gracefully to mixture models.

{% include bibtex.html %}

## References

[^devroye1996vapnik]: Devroye, Luc, et al. "Vapnik-Chervonenkis Theory." A probabilistic theory of pattern recognition (1996): 187–213.

[^ashtiani23a]: Ashtiani, Hassan, Vinayak Pathak, and Ruth Urner. "Adversarially robust learning with tolerance." International Conference on Algorithmic Learning Theory. PMLR, 2023.

[^littlestone1986relating]: Littlestone, Nick, and Manfred Warmuth. "Relating data compression and learnability." (1986).

[^moran2016sample]: Moran, Shay, and Amir Yehudayoff. "Sample compression schemes for VC classes." Journal of the ACM (JACM) 63.3 (2016): 1–10.
