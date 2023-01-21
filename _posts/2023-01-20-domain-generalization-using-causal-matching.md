---
title: "Review of Domain Generalization using Causal Matching: Causal Learning Series"
date: 2023-01-20
excerpt: "In this part of the causal learning series I will review the paper Domain Generalization using Causal Matching. This was also submitted as an assignment at the University of Toronto."
---

This is the first part of the causal learning blog series. I am taking the course CSC 2545: Advanced Topics in Machine Learning by Professor [Igor Gilitschenski](https://www.gilitschenski.org/igor/). I really love the way this course is structured, every week we are given three papers to read and review. We need to write a NeurIPS/ ICML/ ICLR style review for the paper and four people also have to engage in a debate on the pros and cons of the paper, one of which also gives a fifteen-minute talk on the paper. Having absolutely loved the format of this course and just in the first week I learned quite a lot.

So, I thought I would share my reviews of the papers I read as a blog series. These might not be perfect but I have put in quite some work in writing the reviews.

## Review

Here, I review the paper Domain Generalization using Causal Matching [^review].

### Summary

In this paper, the authors examine the task of domain generalization, in which the goal is to train a machine learning model that can perform well on new, unseen data distributions. The authors propose a new algorithm $$MatchDG$$ which is a contrastive learning method that tries to approximately identify the object from which the input had been derived. The paper refers to this as a match. The paper relies on trying to have the same representation for inputs across domains if they are derived from the same object.

They first introduce the perfect match approach which involves learning representations that satisfy the invariance criteria and are informative of a label across domains. The perfect match case is applicable when we have self augmentations in which case we get a perfect base object. As expected the authors report strong performance of Rotated MNIST with perfect matching.
    
However, in most cases, we do not know the perfect matches across domains in which case the authors propose finding approximate matches without known objects. To learn this matching function, $$MatchDG$$ optimizes a contrastive representation learning loss. Positive matches here mean data points from a different domain that share the same class label as the anchor. The key difference in the training of this algorithm is updating positive matches: after every $$t$$ epochs, the positive matches inferred using the learned matching function are updated during training based on the nearest same-class data points in the representation space. The intuition for this could be thought of as accounting for the intra-class variance across domains. After this, the learned matching function is substituted in the perfect macth loss function.

### Strengths

- One way to improve the effectiveness of augmentations is to use causal models. The key is to focus on altering spurious features which can help disrupt any patterns of correlation that may exist. The authors demonstrate that this approach leads to the best outcomes when it comes to generalizing to out-of-distribution examples.
- A new two-phase, iterative algorithm to approximate object-based matches, is useful since no past algorithms tacked cases when objects are unobserved.
- Presents sufficient reasoning to show that the class-conditional invariant is not sufficient for generalizing to unseen domains.
- State of the Art for Domain Generalization on Rotated Fashion-MNIST with $$82.8$$ % top-1 accuracy. Presents good results on Domain Generalization on PACS with MDG-Hybrid achieving $$87.52$$ % average accuracy.
- Provide a great motivation and intuition at each stage for their approaches.

### Weaknesses

- Expected experiments on Domain generalization on ImageNet-C.
- A few vagaries in mathematics (see questions).
- The results on Chest-Xrays dataset which is a hard real-world dataset are quite mixed results.

### Questions

- The paper mentions:
        
For a finite number of domains $$m$$, as the number of examples in each domain $$n_d\rightarrow \infty$$
        
1. The set of representations that satisfy the condition $$\sum_{\Omega(j,k)=1; d\neq d'} dist(\phi(x_j^{(d)}), \phi(x_k^{(d')})) =0$$ contains the optimal $$\phi(x)=X_C$$ that minimizes the domain generalization loss.
        
2. Assuming that $$P(X_a|O, D)<1$$ for every high-level feature $$X_a$$ that is directly caused by domain, and for P-admissible loss functions whose minimization is conditional expectation (e.g., $$\ell_2$$ or cross-entropy), %the true function $$f^*$$ is one of the optimal solutions, a loss-minimizing classifier for the  following loss is the true function $$f^*$$, for some value of $$\lambda$$ provided that $$f^* \in F_c\subseteq F$$.

$$
f_{perfectmatch} = \arg \min_{h, \phi} \sum_{d=1}^{m} L_d(h(\phi(X)), Y) + \lambda \sum_{\Omega(j,k)=1; d\neq d'} dist(\phi(x_j^{(d)}), \phi(x_k^{(d')}))
$$

However, this might not always be true. You can theoretically generate data such that you can learn the specific transformations and minimize the objective to be 0. For example, this statement will most certainly not hold true if we are given the liberty to choose a subset of the data from Rotated-MNIST. However, in most cases minimizing for $$C(\phi)$$ does imply better generalizability.

- The intuition for using a two-phase approach for $$MatchDG$$ is well motivated and contrasted with previous approaches as well as backed by experiments. It might be very helpful to signify the use of a two-phase approach with some more ablation studies.

- Might be helpful to investigate more on the poor performance of Chest X-Rays dataset and experiments on some other large datasets.

### Concerns

Found this work by Jiles et al. [^jiles2022re] that showed some disrepancies in evaluation.

### Soundness:

4 excellent

### Contribution:

4 excellent

### Overall:
7: Accept: Technically solid paper, with high impact on at least one sub-area of AI or moderate-to-high impact on more than one area of AI, with good-to-excellent evaluation, resources, reproducibility, and no unaddressed ethical considerations.\

### Confidence:

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

## References

[^review]: Mahajan, Divyat, Shruti Tople, and Amit Sharma. "Domain generalization using causal matching." International Conference on Machine Learning. PMLR, 2021.

[^jiles2022re]: D JILES, R. I. C. H. A. R. D., and Mohna Chakraborty. "[Re] Domain Generalization using Causal Matching." ML Reproducibility Challenge 2021 (Fall Edition). 2022.