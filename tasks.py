import os
from invoke import task

"""All tasks require a running PostegreSQL server."""


@task
def build_frontend(ctx):
    os.chdir('frontend')
    ctx.run('npm ci', pty=True)
    ctx.run('npm run build', pty=True)
    os.chdir('..')


@task
def build_backend(ctx):
    ctx.run("poetry install && \
            poetry shell",
            pty=True)


@task
def start(ctx):
    ctx.run("flask --app src/app.py run", pty=True)


@task
def init_db(ctx):
    ctx.run("psql < schema.sql", pty=True)


@task(build_frontend, build_backend)
def build_full(ctx):
    pass


@task(init_db, build_frontend, build_backend)
def build_full_init_db(ctx):
    """CAUTION: Will delete any and all existing data!"""
    pass
