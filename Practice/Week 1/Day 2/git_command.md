# Practice_Week1_Day2 (2022-03-23)
* * * 
+ git main commands

	1. clone, init / what's the difference
		- init : create new repository or initialize original one
		- clone : clone <url>, clone the repository and take it to local

	2. add, commit, push, pull
		- add : ready to staging area
		- commit : similar to save but not equal
		- push : to remote repository (github)
		- pull : from remote to local
		- _git commit -m "Change history"_
	3. log 
		- call commit history
		- _git log_
	4. status 
		- load and list the object to add & commit
		- _git status_

	5. checkout 
		- shift to another branch
		- _git checkout -b <branch>_ : create & change branch

	6. branch
		- master branch / develop branch : main branch, develop branch usually derived from master branch
		- feature branch (=topic branch) : not to share in public
		- release branch : work well?
		- hotfix branch : needed to modify in urgent, in the head of master branch
		- _git branch <branchname>_
		
	7. revert - remove specific commit
	
	8. stash - temporary repository, before commit when do checkout (modified), prevent conflict

	9. merge 
		- XXX branch is merge to develop
		- _git merge <commit>_
