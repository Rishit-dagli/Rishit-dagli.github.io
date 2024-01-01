---
title: "My Journey – How I got into research and AI"
date: 2021-07-28
excerpt: "Hello 👋. In this article, I will share my journey about how I got into Artificial Intelligence (AI) and related research as a high school student and consequently, a couple of things I have learned that might help you as well. However, do note that this blog is not one about getting started with AI or research."
---

<link rel="canonical" href="https://raisingamathematician.wordpress.com/2021/07/28/student-diaries-my-journey-how-i-got-into-research-and-ai/">

{% include cover.html url="/assets/my-journey-how-i-got-into-research-and-ai/cover.png" description="" %}

Hello 👋. In this article, I will share my journey about how I got into Artificial Intelligence (AI) and related research as a high school student and consequently, a couple of things I have learned that might help you as well. However, do note that this blog is not one about getting started with AI or research.

During my middle school and high school math and computer science studies, I noticed that a lot of focus was on rote learning. I found it quite unsatisfactory that there was no talk about intuition or reasoning behind any concepts. One such example in my high school studies was about bitwise operators: I was simply taught to remember that bitwise operators are faster, to check if a number is even i++ & 1 is faster than i % 2. However, there was no talk about the intuition behind it.

This certainly did not work for me and I started to explore robotics out of my school curriculum. Soon enough, I started participating in competitions and hackathons and most of what I learned was through these events. I advocate participating in such events because these were what pushed me out of my comfort zone and helped me grow. These were also major steps for me since I was quite shy and these events allow you to get a taste of the entrepreneurship side:

I made my first business plan for a project in a hackathon…

I made my first project pitch in a hackathon…

I worked in a team for the first time in a hackathon…

I got my first project funding through a hackathon…

And a lot more! There is indeed so much that I learned through the community around me. If you learned any of these you are already a winner.

{% include image.html url="/assets/my-journey-how-i-got-into-research-and-ai/hackathon.png" description="Me winning my first hackathon" %}

Somewhere down the line, I got more interested in writing code and soon left working with hardware. But knowledge is never wasted. I certainly got so much help working with robotics while working with software. Another thing I noticed with my friends was that they practiced their passion when they got free time from their school studies. I feel it just does not work that way. You need to be dedicated to working on your passion and not be stuck in excuses. (Although I do not advocate dropping out of school.) In fact, I strongly feel I was able to do all my work with Machine Learning because I had studied high school math. It does sound difficult but you need to find a way that works for you.

Computer Science is also quite an open field, most of the research work in this field is often publicly available. Almost all of the most used frameworks or programming languages are open-sourced. There are a ton of communities and even more free content to help you learn almost anything by yourself. I learned nearly everything in CS through the open content present on the internet and through the community around me.

{% include image.html url="/assets/my-journey-how-i-got-into-research-and-ai/learning.png" description="" %}

I strongly advocate working on open-source code, contributing to the codebase of some large project, or creating your own open-source projects. I always aimed to make a positive impact on the world and open-source could easily enable me to do so. At the start, I was a bit skeptical about creating open-source projects. I wondered if I should do so much work on making a project and then just make it public for all? Nevertheless, I did make some of my work open-source. One of them was a simple developer tool I had built for myself. Quite some people started using my work and also started contributing towards making my project better! After a couple of months, I received a thank you email from a company that had used my project (of course there are legal licenses).

I then saw a podcast by Lex Fridman and Ian Goodfellow on [Generative Adversarial Networks](https://youtu.be/Z6rxFNMGdn0) which got me quite interested in exploring AI. Being exposed to some quite novel ideas in AI, I started loving it and learning more about it, yet again everything from open-source content.

I also think it would be worth mentioning that I believe it is quite important to “learn on your own” or simply saying that trying to explore things yourself helps you understand them a lot better. 

As an example, one of the initial exercises I tried was building a simple neural network without using any libraries and while doing so I faced quite a lot of problems. But guess what, I reinvented an idea, though not exactly the same, called [Gradient Checking](http://deeplearning.stanford.edu/tutorial/supervised/DebuggingGradientChecking/) (which simply uses two-sided derivatives to make approximations) which helped me debug my back propagation algorithm. I later also tried explaining my version of this concept (I used graphs to develop the intuition unlike how it was explained earlier) to the community through [an article](https://towardsdatascience.com/debugging-your-neural-nets-and-checking-your-gradients-f4d7f55da167) that forced me to put things in a structural way. In my opinion, this would be a single step: a great way to learn a concept.

Another exercise that I often do is sort out a couple of research papers I read that are, in my opinion, really interesting. I then try to implement the algorithms they introduce in their paper which I find  quite fun and often it is a huge learning experience. This also pushed me to divert some interest in research.

{% include image.html url="/assets/my-journey-how-i-got-into-research-and-ai/a-robot.png" description="" %}

I then started working on ML research projects and the only tip I would give for someone planning to publish a research paper is to read a lot of existing papers. One of the main things when picking up a research topic to work on is identifying a research problem, the motivation for which comes often from an existing paper. I was once trying out a paper that proposed a framework for text summarization and I came across seeing their algorithm using a “generalized embedding algorithm” (Simply enough this is what converts text to vectors for the computers which convey information about the meaning of a word). This paper motivated me to think about making a new task-specific algorithm that might perform better and later published this as a research paper.

Machine Learning is just a fancy name given to a subset of math. You often need a ton of results to publish a Machine Learning research work which is super costly in terms of hardware and makes it really difficult for individual researchers to publish a Machine Learning paper.  Training a single Machine Learning algorithm with a couple of expensive GPUs could take weeks. 

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Here is a rant about why AI paper review system is broken for students . This is based on my previous paper rejections. You may agree or disagree.<a href="https://twitter.com/hashtag/MachineLearning?src=hash&amp;ref_src=twsrc%5Etfw">#MachineLearning</a> <a href="https://twitter.com/hashtag/AI?src=hash&amp;ref_src=twsrc%5Etfw">#AI</a> <a href="https://twitter.com/hashtag/AcademicChatter?src=hash&amp;ref_src=twsrc%5Etfw">#AcademicChatter</a> <a href="https://twitter.com/hashtag/AcademicChatter?src=hash&amp;ref_src=twsrc%5Etfw">#AcademicChatter</a></p>&mdash; Awais Hussain (@MAwaisHussain6) <a href="https://twitter.com/MAwaisHussain6/status/1395751799416524814?ref_src=twsrc%5Etfw">May 21, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

In my case, I had to reach out for any sponsorship opportunities for this project. Fortunately, my research proposal got selected for a Cloud TPU sponsorship by Google. Cloud TPU resources accelerate the performance of linear algebra computation, which is used heavily in machine learning applications. TPUs minimize the time-to-accuracy when you train large, complex neural network models. Models that previously took weeks to train on other hardware platforms can converge in hours on TPUs and consequently are super expensive. Fortunately, we had this sponsorship from Google to cover all our costs and I would advise looking for more such research grants in case you have an idea but don’t have the means to implement it.

{% include image.html url="/assets/my-journey-how-i-got-into-research-and-ai/tpu.png" description="A screenshot from my paper" %}

In Machine Learning, a huge chunk of research is often published at conferences and you could yet again find sponsorships with your paper proposal for a conference. As an example the conference paper I had presented was sponsored by IEEE and you could easily find grants. As you might have understood, sharing your research idea in a good way through a proposal is really important. I believe all your proposal should contain is:

- what you hope to accomplish
- why those objectives are important to your field
- how you intend to achieve your objectives

{% include image.html url="/assets/my-journey-how-i-got-into-research-and-ai/code.png" description="" %}

You also most probably would be having a mentor to guide you through performing your experiments which is often quite important. I have learned so much about doing the research and also about other things like how do you convey your ideas in a good manner on the paper or write a novel paper or how to address feedback by reviewers. You could reach out to a university professor with work in a similar subfield whose work you have followed to work under. In my case, I had met a university professor through open-source and then wrote a paper with him. I cannot highlight how much I learned just by writing a single paper under a mentor.

This may seem quite difficult and overwhelming but is indeed quite fun and interesting. You would also feel a great sense of accomplishment once you solve a problem which no one in the world has made; making all the related hardships worth it! Also getting published in a reputed Scopus Indexed journal or a reputed conference often brings quite some publicity. This was a bit about my journey and I have tried to also share some tips along the way that might help you.