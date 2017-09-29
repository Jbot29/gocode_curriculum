'''Introduction To Git

Working on complex software projects involves many files. When work is done on the project, these files are in a state of flux: some change frequently, some rarely. Some have strong interdependencies, and others do not.

Because all these changes are taking place, the problem of understanding what changes are taking place is enormous without tools to help. Git is one such tool, and arguably the most important of all of them in a developer's toolkit.

Even in an environment where only one developer is working, these changes are challenging to track. When files come in to conflict, it can be hard to remember what you changed where. And more often, more than one person is working on the project, often on the same file, and at worst, on the same files at the same time. Without a management tool, there would be chaos.

Git is a repository that saves versioned states of a project, and allows collaborations between multiple contributors. You'll be introduced to Git as a simple repository at first. In later units, we'll add features as our projects demand it.

Complete git_intro exercise here: https://gist.github.com/jhylau/2caebb1e77a9af96f1d7

'''



'''Git Checkouts

Checkouts are the inverse of commits in some ways, so a word about committing is useful.

When Git manages the changes in a project, it relies on the developers creating periodic commits that act as a "snapshot" of the project at that time. Each of these commits carries a message that describes the changes that the commit contains. While Git provides ways of examining the actual changes, the most frequent way that developers will determine what happened when in the development path of the project, is by examining the commit messages that were provided.

For this reason, emphasis should be put on the way commit messages are composed. They should be terse and informative: if major changes are taking place, then commits should be made frequently, and the messages focused on the change. Too many changes in one commit make it very hard to encapsulate for other developers the nature of the changes in a single short message.

With that said, the other thing to keep in mind is that each commit represents a place that we can go back to, and restore the project to its previous state. Each commit is provided with a long, alphanumeric code that identifies it uniquely. The checkout command can use this as an argument, to restore the project to the point it was at that commit. Any subsequent changes will be preserved in the Git repo, and we can return to them: checkouts using digital signatures (or hashes as they are known) provides a way to get back to things that worked.


Branching and Checkouts

The use of checkouts is more frequently associated with moving between branches, however. A branch is an isolated thread where changes to the project can be made, without affecting the main thread. Git provides us with a default branch, called master that we generally use as the reference for the project. A developer working on, say, the emailing functions of the app might create a branch called email, and by checking that branch out, all commits she makes to the project will be confined to the email branch. Development and commits can continue in the master (or other) branches; the branches don't affect each other.

There is a relationship between branching and retrospective checkouts: it's often the case that we will checkout an older commit of the project, and then immediately branch from that. This might arise when we know that the project was working at a certain expected level at a commit a few days back: since then, a feature has been added that will make the development we want to do more complicated. Rather than coping with the complication, we can go back to before that feature was added, and then branch: our work will now be in a version of the project from before the feature was put in.

Other than this, simply returning to an older version of the project and continuing to make changes and commit them creates problems in Git. These will be dealt with later


'''


'''Git Branching

Git Branching and Inheritance:

Git branches allow the creation of isolated work threads. A repository always has at least one branch, but in the course of development, you'll create many branches, each of which will be derived from an existing branch.

Understanding how this branch inheritance works is important. In many cases, simply taking the current state of the master branch is all that needs to be done. But in some cases this may not be the best way to do so.

As a hypothetical example, you might be creating a project where two parts of the project will share access to a database. One developer has created a branch that has focused on creating the core database functionality. This is not in the master branch, so when the developers want to start working on the two new features, it will make sense to branch from the branch containing the work already done on the database.

Retrograde Branches:

You already explored how to checkout an earlier version of the project, via the digital signature of the commit. This carries risks of creating conflicts between the later state of the branch and the changes that you make to the rolled-back version. As soon as you change, add and commit changes in the rolled-back version, conflict is impossible to avoid.

The way around this is to immediately branch the retrograde version. By doing so, you're free to use an older version of the project as a starting point for new work that you want to add.

Merging:
The integration of changes in different branches requires a merging process. This is in a future unit, but until that is the case, branches represent diverging threads of a project. Learning good branching practice and understanding the consequences of branching is the basis for easy and effective merging.
'''

# Complete git_branching.md