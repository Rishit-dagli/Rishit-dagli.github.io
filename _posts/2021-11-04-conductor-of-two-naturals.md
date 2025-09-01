---
title: "What Is the Largest Integer Not of the Form mb+nc?"
date: 2021-11-04
excerpt: "What's the largest number that absolutely refuses to be written as mb+nc?"
tags: [number-theory]
---

<link rel="canonical" href="https://figshare.com/articles/preprint/A_Short_but_Interesting_Number_Theory_Theorem_pdf/16903252">

This note presents a simple yet non‑obvious number‑theoretic result I discovered while working on a related problem: for natural numbers $$b,c,m,n\in\mathbb N$$, the quantity $$bc-b-c$$ is the largest integer that cannot be written as $$mb+nc$$. I first prove the statement and then show a direct application that considerably simplifies an Olympiad‑style problem.

By the “conductor” of two natural numbers we mean the product of the numbers minus their sum. In symbols,

$$
\operatorname{Conductor}(x, y) = xy - x - y
$$

The theorem below turns the original task into a short argument, and the same idea is useful in other settings as well.

## Main Theorem

{% include theorem.html name="Conductor of Two Naturals" content="The conductor of two natural numbers, $$bc - b - c$$, is the largest number which cannot be written as $$mb + nc$$, given all $$b, c, m$$ and $$n \in \mathbb{N}$$." %}

## Proof

{% include proof.html proof="Without loss of generality let us assume $$b < c$$.

$$
0,\ c,\ 2c,\ 3c,\ 4c,\ \ldots,\ (b-2)c,\ (b-1)c
$$

is an exhaustive set of residues modulo $$b$$.

Let us take some $$r$$ for which

$$
\tag{1}
r > (b-1)c - b
$$

then

$$
\tag{2}
r \equiv nc \pmod b
$$

for some $$n$$ such that $$0 \leq n \leq (b-1)$$.

Now it is obvious that any number larger than $$bc-b-c$$ cannot be written as $$mb+nc$$.

We are yet to prove that $$bc-b-c$$ itself cannot be written in this form.

Assume towards contradiction that

$$
\tag{3}
bc-b-c = mb+nc
$$

This implies $$n \geq b-1$$, and thus

$$
\tag{4}
mb+nc \geq nc \geq (b-1)\cdot c > bc-b-c
$$

which is a contradiction." %}

## Usage

We will now see a problem where using this theorem makes it significantly easier. This problem is from The International Mathematical Olympiad (IMO) 1983 Day 1 Problem 3 [^imo1983].

### Problem

Let $$a,b$$ and $$c$$ be positive integers, no two of which have a common divisor greater than $$1$$. Show that $$2abc-ab-bc-ca$$ is the largest integer which cannot be expressed in the form $$xbc+yca+zab$$, where $$x,y,z$$ are non-negative integers.

Using the theorem, we use the same starting argument:

$$
\tag{5}
0,\ bc,\ 2bc,\ 3bc,\ 4bc,\ \ldots,\ (a-2)bc,\ (a-1)bc
$$

is an exhaustive set of residues modulo $$a$$.

Given

$$
\tag{6}
N > 2abc - ab - bc - ca
$$

we may take

$$
\tag{7}
xbc \equiv N \pmod a,\quad 0 \leq x < a
$$

Then

$$
\begin{align}
\tag{8}
N - xbc &> 2abc - ab - bc - ca - (a-1)bc \\
&= abc - ab - ca \\
&= a\big( bc - b - c \big)
\end{align}
$$

So

$$
\tag{9}
N - xbc = ka \quad \text{with} \quad k > bc - b - c
$$

Hence we can find non-negative $$y, z$$ so that

$$
\tag{10}
k = zb + yc
$$

Therefore

$$
\tag{11}
N = xbc + yca + zab
$$

Finally, we show that for $$N = 2abc - ab - bc - ca$$ we cannot find non-negative $$x, y, z$$ such that $$N = xbc + yca + zab$$. Indeed,

$$
\tag{12}
N \equiv -bc \pmod a
$$

so we must have $$x \equiv -1 \pmod a$$ and hence $$x \geq a-1$$. Similarly, $$y \geq b-1$$ and $$z \geq c-1$$. Thus

$$
\tag{13}
xbc + yca + zab \geq 3abc - ab - bc - ca > N
$$

which is a contradiction.

{% include bibtex.html %}

## References

[^imo1983]: International Mathematical Olympiad (IMO). The international mathematical olympiad (imo) 1983 problems, 1983. URL: https://www.imo-official.org/year_info.aspx?year=1983.
