from invoke import task

@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)
from invoke import task

@task
def foo(ctx):
    print("bar")

