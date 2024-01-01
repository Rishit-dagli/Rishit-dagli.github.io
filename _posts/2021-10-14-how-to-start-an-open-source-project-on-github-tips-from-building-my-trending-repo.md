---
title: "How to Start an Open Source Project on GitHub – Tips from Building My Trending Repo"
date: 2021-10-14
excerpt: "Quite recently I ended up on the coveted GitHub Trending page. I was the #2 trending developer on all of GitHub – and for Python as well, which was a pleasant surprise for me. I will be sharing some tips in this article which you should be able to apply to all kinds of projects."
---

{% include cover.html url="/assets/how-to-start-an-open-source-project-on-github-tips-from-building-my-trending-repo/cover.png" description="" %}

<link rel="canonical" href="https://www.freecodecamp.org/news/graph-neural-networks-explained-with-examples/">

Developers around the world use GitHub to share their projects with the global developer community.

In this article, I'll give you some opinionated tips to help you build a great open-source project you can start using. You can also use these tips for building hackathon projects.

Quite recently I ended up on the coveted GitHub Trending page. I was the #2 trending developer on all of GitHub – and for Python as well, which was a pleasant surprise for me on the morning of 7 September. And it was based on code I wrote at 4am.

I was also featured on the GitHub daily newsletter, all after open-sourcing one of my projects.

I will be sharing some tips in this article which you should be able to apply to all kinds of projects and not just Python packages like my own.

You can check out my repo [here](https://github.com/Rishit-dagli/Fast-Transformer).

{% include image.html url="/assets/how-to-start-an-open-source-project-on-github-tips-from-building-my-trending-repo/trending-page.png" description="My project on the GitHub Trending page" %}

## Find Your Motivation

It is almost impossible to game the GitHub Trending section:

> GitHub’s definition (of trending) takes into account a longer term definition of trending and uses more complex measurement than sheer number of stars which helps to keep people from farming the system.

Founders often create startups based on problems they have personally encountered. With open-sourced code, you will likely be trying to solve problems that **developers commonly have**.

And since gaming the GitHub Trending section is almost impossible, you need a strong motivation – a big, common developer problem – to work on. So how do you stumble onto a developer problem?

Well, for starters you can participate in hackathons, build projects, and experiment with other projects. And you will soon find something which could be made into a library, something you could make a utility out of, and so on.

Your motivation for building your project could come from anywhere. In my case, I explore new Machine Learning papers daily on arXiv (an open-access archive for papers) and read the ones I find interesting. One such paper I read motivated me to build my Python package.

Another time, I was in a hackathon training a Machine Learning model and wanted to participate in other festivities. Our team then decided to build another open-source project called [TF-Watcher](https://www.freecodecamp.org/news/how-to-monitor-ml-projects-on-mobile-devices/).

So you see, you'll likely find all sorts of issues you can work on when you're building a project.

And just to note – when I say you should have a strong motivation, I do not mean the project should be really huge or really complex. It could certainly be a simple project that could make developers' lives easier.

Think about it this way: if there was a project like the one you want to develop, **would you use it?** If the answer is yes, you have enough motivation to build the project, regardless of the size or complexity.

> A man in Oakland, California, disrupted web development around the world last week by deleting 11 lines of code. —Keith Collins in [How one programmer broke the internet by deleting a tiny piece of code](https://qz.com/646467/how-one-programmer-broke-the-internet-by-deleting-a-tiny-piece-of-code/)

You might know about `left-pad` , a very small open-source npm package with just 11 lines of straightforward code. But it was used by tons of developers around the world, which just reinforces what I was talking about above.

## Research Your Idea

Once you find a developer problem you want to solve and have enough motivation to start working on it, you'll ideally want to spend quite a bit of time doing your research.

I believe it is a good practice to try and answer these questions through your research:

### Does a similar project or tool already exist?

If it has not been done yet, and there's a need for it, go ahead and start building it.

If something similar exists, is well developed, and is heavily used too, you might want to move on.

There are a huge number of open-source projects out there already, and it is quite common to find a repository doing similar stuff (more common than you would think). But you can still work on your project and make it better.

### If something similar does exist, can your project make it better?

If something similar exists, your goals could be to make it more modular or more efficient. You could try implementing it in some other language or improve it in any other number of ways.

A great way to do so is to take a look at the issues for the existing repository. Try doing your research with existing solutions (if there are any) and find out what aspect of the project could possibly be improved. Your work could even be a derivative of the other project.

In my case, as I mentioned, I took inspiration from an interesting research paper I read (Fastformer: Additive Attention Can Be All You Need). I also discovered an official code implementation and a community implementation of the paper, both in PyTorch.

In the end, my repository, though a derivative of the research papers, _was quite different from existing code implementations_.

### Can you explain your project like I'm 5?

ELI5, or explain it like I'm five, is a great exercise that I like doing as soon as I have an idea for a repository.

I try to explain what the project aims to achieve or how it works or why it is better than similar repositories – to a friend who doesn't know a lot about the subject. Often with some helpful analogies.

By doing this, it helps me develop or get a clear understanding of what I want to do in my projects. Trying to explain the project to a friend often also helps me spot any flaws in my plan or assumptions I may have made while ideating on the project.

This process really helps me when I start the development phase of the project. This is also when I start creating a project board. You can make a project board on GitHub itself, or you can use Trello, JetBrains Spaces, and so on.

I love using GitHub Projects and Issue checklists at this stage to help me manage, prioritize, and have a clear high-level idea of what I need to do.

{% include image.html url="/assets/how-to-start-an-open-source-project-on-github-tips-from-building-my-trending-repo/gh-projects.png" description="GitHub Projects and Issue checklists" %}

### What can you learn from great repositories in similar categories?

You can often take inspiration and learn from repositories belonging to similar categories. Check out how their code is structured. You should try scouting other great repositories and read through their well-written code.

In my case, I really loved the way [reformer-pytorch](https://github.com/lucidrains/reformer-pytorch) was written. It's easy to use in your projects as a Python library, it expects you to ideally care about only a single class abstracting a lot of the model building process, and returns an instance of `torch.nn.Module` (in Pytorch, a base class for all neural network modules) which you can pretty much do anything with. I ended up building [Fast-Transformer](https://github.com/Rishit-dagli/Fast-Transformer) in a quite similar way.

## How to Develop Your Project's Repo

You might have heard the popular quote:

> Any fool can write code that a computer can understand. Good programmers write code that humans can understand. —Martin Fowler

If people can not understand your code, they will not use it.

I've noticed in my own repositories that, when I spend more time trying to make things simple and easy to use, those projects end up getting more traction. So try to spend the extra time making your project more usable and intuitive.

As a general rule of thumb while developing your repo:

- You should include a license when you launch an open-source project. This allows people to use, copy, modify, and contribute back to your project while you retain the copyright. You can easily find a license suitable for your project at https://choosealicense.com/.
- Create a good README: there's a whole section about this next because it is super important.
- Use consistent code conventions and clear function/method/variable names. You can often use some static code analysis tool like [black](https://github.com/psf/black), [ktlint](https://ktlint.github.io/), and so on.
- Make sure your code is clearly commented, document your thoughts, and include edge cases.
- Make sure there are no sensitive materials in the revision history, issues, or pull requests (for example, API keys, passwords, or other non-public information).
- If you are developing an app/library, I would recommend that you use GitHub releases. Try maintaining clear release notes and changelogs each time you make a new release so the community can track what is new. Record what bugs were fixed, and so on. Here is a [great repo](https://github.com/PatilShreyas/NotyKT/releases) showing this.
- Finally, you should also include contributing guidelines in the repository that tells your audience how to participate in your project. You can include information on the types of contributions you are expecting or how to suggest a feature request or bug report and so on.

## How to Write a Good README

A good README is undoubtedly one of the most important components of the repository. It's displayed on the repository's homepage.

Potential contributors usually first check out the README, and only then if they find it interesting will they look at the code or even consider using the project.

Also, this is not a definitive guide to writing a README. Just play around with it and experiment with what works for your project.

Generally, you'll want to include these components in your README:

### Explain what the project does

Try to describe the project in just 3-4 lines. Don't worry about including too many minute details or features – you can add them in later sections. This is also the first thing visitors to your repository would be reading, so be sure to make it interesting.

### Have a great project cover image or logo

If you have a logo or a cover image for your project, include it here. It helps contributors to have some sort of visual.

### Share your badges

{% include image.html url="/assets/how-to-start-an-open-source-project-on-github-tips-from-building-my-trending-repo/badges.png" description="Badges in README" %}

You will often see small badges at the top of the README that convey metadata, such as whether or not all the tests are passing for the project.

You can use [shields.io](http://shields.io/) to add some to your README. These will often give your project a lot of credibility without visitors having to go through all of your code.

### Include visuals

You should always try to include visuals in your README. These could be a gif showing your project in action or a screenshot of your project.

Good graphics in the README can really help convince other developers to use your project.

### Explain how to install or set up your project

You should also include specific installation guidelines. Include all the required dependencies and anything else other devs need to install in order to use your project.

If you faced any problems while setting up your project or installing a dependency, it is quite likely users will face that too, make sure you talk about it.

These can be super straightforward:

{% include image.html url="/assets/how-to-start-an-open-source-project-on-github-tips-from-building-my-trending-repo/installation.png" description="My Installation section" %}

### Give clear and reproducible usage examples

I think this is super important to have in your README. You should not expect other developers to do a lot of homework or read your code – make it as easy as you can for them.

Always make sure and double-check that your code examples or a "How To" section are easily reproducible. Also, make sure it's understandable for a wide range of users, and don't leave out any required instructions for reproducing it.

Since my project is a Python package, I created an accompanying Colab Notebook to demonstrate the use of the package. This lets people easily try it out on their browsers without having to install anything on their own machines.

There are quite a few products that let you do this like repl.it, Glitch, Codepen, and so on.

### Explain what you can do with the project

It is often helpful to list out features your project has and problems it can help solve. You don't have to cover all the features you have worked on, but share the main ones.

This will help developers understand what your project can do and why they should use it.

### Share how people can get help or contribute to the project

Finally, you should clearly state if you are open to contributions and what your requirements are for accepting them. You should also document commands to lint the code or run tests.

These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something.

### External Documentation

Suppose you think your README gets too long. In that case, you can create an additional documentation website and link to it in the README rather than omitting any important information.

Since I work a lot with Python, I generally use [Sphinx](https://www.sphinx-doc.org/en/master/) to generate my documentation from Python docstrings. I find Sphinx quite flexible and easy to set up.

There are quite a lot of options to generate your documentation out there: [mkdocs](https://www.mkdocs.org/), [Docsaurus](https://docusaurus.io/), [docsify](https://docusaurus.io/), and more. For my project which started trending, however, I didn't need an external documentation website.

Here is an example of what I feel might be a good start to a README from one of my own projects. This is not the complete README, but just how much I could get in a single image:

{% include image.html url="/assets/how-to-start-an-open-source-project-on-github-tips-from-building-my-trending-repo/readme.png" description="Example of what I add in a README" %}

Finally, for more inspiration, I would suggest that you try using the [“Make a README” guide](https://www.makeareadme.com/).

## How to Drive Visitors to Your GitHub Page

Once you have created a beautiful README and made the project public, you need to think about bringing people to the GitHub page.

First, make sure you add relevant tags to your GitHub repo. These tags will make it much easier for the project to get discovered by people exploring GitHub.

### Share your project on Hacker News, Twitter, and Reddit

Great places to post about your project are Hacker News and Reddit. Just keep in mind that getting your post to be the top story or the top post on either of these platforms is a difficult task.

When one of my repositories became the top story, it got more than a hundred stars in a couple of hours.

But when I originally posted my repo on Hacker News, I didn't have a single upvote. It wasn't until someone else from the community noticed my project and posted it on Hacker News that it went on to be the top story. So it often takes a good amount of planning and a little help from your friends to get your project to the top.

In my case, Twitter was a really great place to get the very first visitors for my project and reach out to an external audience.

This often serves as a great way to allow people to quickly see if they might be interested in checking out your project. And you just have a limited number of characters to sell your repository to people.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Here is my implementation of the &quot;Fastformer: Additive Attention is All You Need&quot; paper<br><br>It is a Transformer variant based on additive attention<br>that can handle long sequences efficiently with linear complexity<a href="https://t.co/jBfyCNGlcN">https://t.co/jBfyCNGlcN</a><a href="https://twitter.com/hashtag/MachineLearning?src=hash&amp;ref_src=twsrc%5Etfw">#MachineLearning</a></p>&mdash; Rishit Dagli (@rishit_dagli) <a href="https://twitter.com/rishit_dagli/status/1433795914888482822?ref_src=twsrc%5Etfw">September 3, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Also, make that you don't overdo posting about your project on any platform because it might get flagged as spam.

### Shoutouts matter but not in the way you think

I often get emails or messages about shouting out a project or a book. But I strongly believe that this does not make a lot of sense.

If you want someone to shout out your project, then you would want them to have used your project and found it useful before shouting it out. So an easier way to do so is by just adding a "tweet this project" button to the README. Then people who like the project can naturally shout it out.

Also, keep in mind that shoutouts don't directly bring you stars. People coming from shoutouts will only star your project if they like it.

This most certainly does not mean that you should not ask people for help or feedback or code reviews. Indeed, you should always try to address all kinds of feedbacks: improvements, bugs, inconsistencies, and so on.

Always be ready to embrace negative feedback and think about how you can improve on it. You might end up learning a couple new things :)

In my case, I noticed an unusually high number of visitors coming to the project from Twitter. My project was implemented with TensorFlow and Keras, and a couple of days later (after I got shouted out) I discovered that the creator of Keras himself shouted out my project!

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">A TensorFlow/Keras implementation of the additive attention Transformer paper (Wu et al) that was released a few days ago <a href="https://t.co/nxYHGlzYDS">https://t.co/nxYHGlzYDS</a></p>&mdash; François Chollet (@fchollet) <a href="https://twitter.com/fchollet/status/1434214348650475522?ref_src=twsrc%5Etfw">September 4, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

This was most probably because I added a "Tweet this project" at the top of my README and let the discoveries come in on their own.

## Tips from the Developer Community about Creating a Project on GitHub

As an interesting exercise, I tried asking the community on Twitter for any tips they might have for me to include in this blog. Here are a few of them:

> (You should add) 1. Documentation 2. Decision logs —Shreyas Patil

> Good issue and PR templates. You could also use the GitHub issue forms. —Burhanuddin Rangwala

> Documentation (should be complete and) include app architecture, packaging, style guide, coding conversation, links of technology framework library used, pre requisite tokens, etc. —Chetan Gupta

## Conclusion

Thank you for sticking with me until the end. I hope that you take back a thing or two for your own open-source projects and build better ones. By incorporating these tips and experimenting – and by putting in a lot of hard work – you can create a great project.

If you learned something new or enjoyed reading this article, please share it so that others can see it. Until then, see you in the next post!

Many thanks to [Santosh Yadav](https://www.santoshyadav.dev/) and [Shreyas Patil](https://shreyaspatil.dev/) for helping me make this article better.

You can also find me on Twitter [@rishit_dagli](https://twitter.com/rishit_dagli), where I tweet about open-source, machine learning, and a bit of android.