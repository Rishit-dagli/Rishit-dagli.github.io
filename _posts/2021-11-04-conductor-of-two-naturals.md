---
title: "What Is the Largest Integer Not of the Form mb+nc?"
date: 2021-11-04
excerpt: "What's the largest number that absolutely refuses to be written as mb+nc?"
tags: [number-theory]
---

<link rel="canonical" href="https://figshare.com/articles/preprint/A_Short_but_Interesting_Number_Theory_Theorem_pdf/16903252">

This note presents a simple yet non‑obvious number‑theory result I discovered while working on a related problem: for natural numbers $$b,c,m,n\in\mathbb N$$, the quantity $$bc-b-c$$ is the largest integer that cannot be written as $$mb+nc$$.[^assumptions] I first prove the statement and then show a direct application that considerably simplifies an Olympiad‑style problem.

By the “conductor” of two natural numbers we mean the product of the numbers minus their sum. In symbols,

$$
\operatorname{Conductor}(x, y) = xy - x - y
$$

The theorem below turns the original task into a short argument, and the same idea is useful in other settings as well.

## Main Theorem

{% include theorem.html name="Conductor of Two Naturals" content="The conductor of two natural numbers, $$bc - b - c$$, is the largest number which cannot be written as $$mb + nc$$, given all $$b, c, m$$ and $$n \in \mathbb{N}$$." %}

{% include proof.html proof="Without loss of generality let us assume $$b < c$$.

$$
0,\ c,\ 2c,\ 3c,\ 4c,\ \ldots,\ (b-2)c,\ (b-1)c
$$

is an exhaustive set of residues modulo $$b$$.[^residues-mod-b]

Let us take some $$r$$ for which

\begin{equation}
r > (b-1)c - b
\label{eq:r-bound}
\end{equation}

then

\begin{equation}
r \equiv nc \pmod b
\label{eq:r-equiv}
\end{equation}

for some $$n$$ such that $$0 \leq n \leq (b-1)$$.

Now it is obvious that any number larger than $$bc-b-c$$ cannot be written as $$mb+nc$$.

We are yet to prove that $$bc-b-c$$ itself cannot be written in this form.

Assume towards contradiction that

\begin{equation}
bc-b-c = mb+nc
\label{eq:contradiction}
\end{equation}

This implies $$n \geq b-1$$, and thus

\begin{equation}
mb+nc \geq nc \geq (b-1)\cdot c > bc-b-c
\label{eq:final-contradiction}
\end{equation}

which is a contradiction." %}

## Usage

We will now see a problem where using this theorem makes it significantly easier. This problem is from The International Mathematical Olympiad (IMO) 1983 Day 1 Problem 3 [^imo1983].

### Problem

Let $$a,b$$ and $$c$$ be positive integers, no two of which have a common divisor greater than $$1$$.[^pairwise-coprime-use] Show that $$2abc-ab-bc-ca$$ is the largest integer which cannot be expressed in the form $$xbc+yca+zab$$, where $$x,y,z$$ are non-negative integers.

Using the theorem, we use the same starting argument:

$$
0,\ bc,\ 2bc,\ 3bc,\ 4bc,\ \ldots,\ (a-2)bc,\ (a-1)bc
$$

is an exhaustive set of residues modulo $$a$$.

Given

\begin{equation}
N > 2abc - ab - bc - ca
\label{eq:N-bound}
\end{equation}

we may take

\begin{equation}
xbc \equiv N \pmod a,\quad 0 \leq x < a
\label{eq:x-equiv}
\end{equation}

Then

$$
\begin{equation}
\begin{aligned}
N - xbc &> 2abc - ab - bc - ca - (a-1)bc \\
&= abc - ab - ca \\
&= a\big( bc - b - c \big)
\end{aligned}
\label{eq:N-minus-xbc}
\end{equation}
$$

So

\begin{equation}
N - xbc = ka \quad \text{with} \quad k > bc - b - c
\label{eq:k-definition}
\end{equation}

Hence we can find non-negative $$y, z$$ so that

\begin{equation}
k = zb + yc
\label{eq:k-form}
\end{equation}

Therefore

\begin{equation}
N = xbc + yca + zab
\label{eq:N-final}
\end{equation}

Finally, we show that for $$N = 2abc - ab - bc - ca$$ we cannot find non-negative $$x, y, z$$ such that $$N = xbc + yca + zab$$. Indeed,

\begin{equation}
N \equiv -bc \pmod a
\label{eq:N-mod}
\end{equation}

so we must have $$x \equiv -1 \pmod a$$ and hence $$x \geq a-1$$. Similarly, $$y \geq b-1$$ and $$z \geq c-1$$.[^mod-analogues] Thus

\begin{equation}
xbc + yca + zab \geq 3abc - ab - bc - ca > N
\label{eq:usage-contradiction}
\end{equation}

which is a contradiction.

{% include bibtex.html %}

## References

[^imo1983]: International Mathematical Olympiad (IMO). The international mathematical olympiad (imo) 1983 problems, 1983. URL: https://www.imo-official.org/year_info.aspx?year=1983.

[^assumptions]: We interpret “written as $$mb+nc$$” with $$m,n\in\mathbb{Z}_{\ge 0}$$ (zero allowed). The coprimality condition $$\gcd(b,c)=1$$ is essential: if $$d=\gcd(b,c)>1$$, only multiples of $$d$$ are representable as $$mb+nc$$, so there is no finite “largest” non‑representable integer. This is the classical two‑variable case of the Frobenius coin problem, whose Frobenius number equals $$bc-b-c$$.

[^residues-mod-b]: Because $$\gcd(b,c)=1$$, the class of $$c$$ is invertible modulo $$b$$. Hence the set $$\{0,c,2c,\ldots,(b-1)c\}$$ hits every residue class mod $$b$$ exactly once; if $$\gcd(b,c)>1$$, it would hit only multiples of $$\gcd(b,c)$$.

[^pairwise-coprime-use]: “No two have a common divisor greater than 1” means $$\gcd(a,b)=\gcd(b,c)=\gcd(c,a)=1$$. This ensures that $$bc$$ is invertible modulo $$a$$, $$ca$$ is invertible modulo $$b$$, and $$ab$$ is invertible modulo $$c$$, which is used in the congruence arguments below.

[^mod-analogues]: From $$N\equiv -bc\pmod a$$ and $$\gcd(a,bc)=1$$ we infer $$xbc\equiv N\pmod a\Rightarrow x\equiv -1\pmod a$$, giving $$x\ge a-1$$. Reducing the same identity modulo $$b$$ and $$c$$ yields $$y\equiv -1\pmod b$$ and $$z\equiv -1\pmod c$$, hence $$y\ge b-1$$ and $$z\ge c-1$$.