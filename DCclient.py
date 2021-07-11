import git

print("Hello, i'm running!")
while True:
    id=1

def pull():
    repo = git.Repo('./')
    o = repo.remotes.origin
    o.pull()
