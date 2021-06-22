from invoke import task
from pyavsubs.Prj import Prj

@task(default = True)
def test(c):
    Prj(id = 'test', yt_id = 'Lox6tAor5Xo').menu()

@task
def gymix(c):
    Prj(id = 'gymix', yt_id = 'Lox6tAor5Xo').menu()

@task
def arav(c):
    Prj(id = 'arav', yt_id = 'ZTlx0I4qDoo').menu()

@task
def hnva2(c):
    Prj(id = 'hnva2', yt_id = 'Jaok_8MNntQ').menu()
    
@task
def autocomplete(c):
    c.run("source <(inv --print-completion-script bash)")
