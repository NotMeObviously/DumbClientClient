import git
git_repository = "DumbClientClient"

repo = git.Repo('./')
o = repo.remotes.origin
o.pull()
