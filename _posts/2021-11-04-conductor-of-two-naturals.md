---
title: "The Conductor of Two Naturals is the largest number which cannot be written as mb+nc"
date: 2021-11-04
excerpt: "What's the largest number that absolutely refuses to be written as mb+nc?"
tags: [number-theory]
---

<link rel="canonical" href="https://figshare.com/articles/preprint/A_Short_but_Interesting_Number_Theory_Theorem_pdf/16903252">

This paper presents a short but non-obvious and interesting theorem in Number Theory that I originally discovered while working on a problem. This theorem states that $$bc - b - c$$ is the largest number which _cannot_ be written as $$mb + nc$$. Given all $$b, c, m$$ and $$n \in \mathbb{N}$$. In this article I prove the above statement and also show a problem where this theorem could be directly applied to considerably make the problem easier.

## Introduction And Statement Of Result

I created the theorem I will present below while working on a problem involving conductors of natural numbers. Here we refer to the "conductor" of two natural numbers as computing the product of the two numbers and subtracting each of the original numbers from it. Simply enough, in a mathematical form we say:

$$
Conductor(x, y) = xy - x - y
$$

Using the below theorem which I originally created just to solve the problem made the problem significantly easier for me and in this paper I also show how this also proved to be super useful for other problems too. I hope seeing this to be used for a wide variety of problems.

## Theorem 1

The conductor of two natural numbers, $$bc - b - c$$, is the largest number which cannot be written as $$mb + nc$$. Given all $$b, c, m$$ and $$n \in \mathbb{N}$$.

_Proof._ Without loss of generality let us assume $$b < c$$

$$
0, c, 2c, 3c, 4c \ldots (b-2)c, (b-1)c
$$

is an exhaustive set of residues for modulo $$b$$

Let us take some $$r$$ for which:

$$
r > (b-1)c-b
$$

then,

$$
r \equiv nc \mid b
$$

for some $$n$$ such that $$0 \leq n \leq (b-1)$$

Now it is obvious that a number larger than $$bc-b-c$$ can not be written as $$mb +nc$$

**Note:** We are yet to prove that $$bc-b-c$$ can not be written in this form, we have only proved for numbers larger than $$bc-b-c$$ .

Let us now see for the number $$bc-b-c$$ itself.

If $$bc-b-c = mb+nc$$

this $$\implies n \geq b-1$$

And this leads to:

$$
mb+nc \geq nc \geq (b-1) \cdot c > bc-b-c
$$

Which is a contradiction.

## Usage

We will now see a problem  where using this theorem makes it significantly easier. This problem is from The International Mathematical Olympiad (IMO) 1983 Day 1 Problem 3 [^imo1983].

### Problem

Let $$a,b$$ and $$c$$ be positive integers, no two of which have a common divisor greater than $$1$$. Show that $$2abc-ab-bc-ca$$ is the largest integer which cannot be expressed in the form $$xbc+yca+zab$$, where $$x,y,z$$ are non-negative integers.

Using Theorem 1 we use the same starting argument:

$$
0, bc, 2bc, 3bc, 4bc \ldots (a-2)bc, (a-1)bc
$$

is an exhaustive set of residues for modulo $$a$$

Given $$ N > 2abc - ab - bc - ca $$

we may take

$$
xbc = N \pmod a
$$

with $$0 \leq x < a $$

But:

$$
\begin{align*} 
N - xbc &> 2abc - ab - bc - ca - (a-1)bc \\ 
 &= abc - ab - ca \\
 &= a(bc - b - c)
\end{align*}
$$

So,

$$
N - xbc = ka \text{ with }  k > bc - b - c
$$

Hence we can find non-negative $$y, z$$ so that:

$$
k = zb + yc
$$

So, 

$$
N = xbc + yca + zab
$$

Finally, we show that for $$N = 2abc - ab - bc - ca$$ we cannot find non-negative $$x, y, z$$

so that $$N = xbc + yca + zab$$

$$
N \equiv -bc \pmod a   
$$

so we must have $$x \equiv -1 \pmod a$$ and hence $$x \geq a-1$$

Similarly, $$y => b-1$$, and $$z \geq c-1$$

Hence,

$$
xbc + yca + zab \geq 3abc - ab - bc - ca > N
$$

Contradiction.

## Data availability

Data sharing not applicable to this article as no datasets were generated or analysed during the current study.

{% include bibtex.html %}

## References

[^imo1983]: International Mathematical Olympiad (IMO). The international mathematical olympiad (imo) 1983 problems, 1983. URL: https://www.imo-official.org/year_info.aspx?year=1983.
