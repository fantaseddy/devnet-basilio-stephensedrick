# Module 1 — Git & GitHub

**Student:** Stephen Sedrick C. Basilio
**Date:** September 23, 2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Git is version control, in the sense that it lets us track and save different versions of our work. It's basically a tool that tracks our changes of the files in a project. GitHub is the website platform that we have used in this subject to store, create, and access repositories online. We often have them on public and have added group members and instructor as a contributor.

---

## Key vocabulary (in your own words)

- repository: project folder tracked by Git
- commit: messaged checkpoint of changes one made in a project
- branch: a separate version that doesn't directly change the main branch
- push / pull: push sends from local commits to remote repo, while pull is the reverse
- pull request: a review to merge the changes from other branches to main
- merge conflict: Git cannot emrge changes coz different branches changed the same parts of a file

---

## Walking through what I did

For this activity, I used the template in the given GitHub repository using the link. I renamed it as per the instructions, made it public, and read the README. I made branches for each file inside the folders. I opened Visual Studio Code, updated it, restarted it, and checked my version. Then, I cloned it to my local Visual Studio Code application in my laptop, double checked, and then tested my local connectivity to the remote repository. I make changes to the files, commit those changes, push the branch to GitHub, and then create a pull request.

```
git --version
Ctrl + Shift + P
Git: Clone
https://github.com/fantaseddy/devnet-basilio-stephensedrick.git
git pull
git status
git add .
git commit -m "Message"
git push
```

---

## A mistake I made (or one I want to avoid)

Don't be mad, but after cloning I forgot to save using Ctrl + S hahahah XD
I made changes to the file, then I added, committed, and pushed those files. I was wondering why they're not causing a pull request. It turns out I simply forgot to save the file first after cloning it. D:

---

## How this connects to something else

We used Git and GitHub for our previous group activities, since we have to use branches then push it on main as we work on different parts of the system without conflicting each other. And that was only for this subject. This is relevant for us as we most definitely will still use this as IT students in the future.