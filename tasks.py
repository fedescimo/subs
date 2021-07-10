from invoke import task
from pyavsubs.Prj import Prj

# -------------
# Project tasks
# -------------
@task(default = True)
def test(c):
    Prj(id = 'test', yt_id = 'Lox6tAor5Xo').menu()

@task
def gymix(c):
    Prj(id = 'gymix', yt_id = 'Lox6tAor5Xo').menu()


# @task
# def hnva20(c):
#     Prj(id = 'hnva20', yt_id = 'Jaok_8MNntQ').menu()

@task
def hnva25(c):
    Prj(id = 'hnva25', yt_id = 'GHGRkgF-JXQ').menu()

@task
def arav(c):
    Prj(id = 'arav', yt_id = 'ZTlx0I4qDoo').menu()
    

# -----
# Utils
# -----
@task
def autocomplete(c):
    c.run("source <(inv --print-completion-script bash)")

@task
def download_video(c):
    url = input('Input YT video url: ')
    cmd = "cd /tmp && youtube-dl -f 18 " + "'" + url + "'"
    c.run(cmd)
    print("Video downloaded in /tmp/")

@task
def download_subs(c):
    url = input('Input YT video url: ')
    cmd = "cd /tmp && youtube-dl --skip-download --all-subs --sub-format srt " + "'" + url + "'"
    c.run(cmd)
    print("Subs downloaded in /tmp/")
