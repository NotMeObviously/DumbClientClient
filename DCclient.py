import git



def pull():
    repo = git.Repo('./')
    o = repo.remotes.origin
    o.pull()
