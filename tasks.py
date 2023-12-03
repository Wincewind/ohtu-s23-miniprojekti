import os
from invoke import task

"""All tasks require a running PostegreSQL server."""


@task
def build_frontend(ctx):
    os.chdir('frontend')
    ctx.run('npm ci')
    ctx.run('npm run build')
    os.chdir('..')


@task
def build_backend(ctx):
    ctx.run("poetry install")


@task
def start(ctx):
    ctx.run("flask --app src/app.py run")


@task
def init_db(ctx):
    ctx.run("psql < schema.sql")


@task(build_frontend, build_backend)
def build_full(ctx):
    pass


@task(init_db, build_frontend, build_backend)
def build_full_init_db(ctx):
    """CAUTION: Will delete any and all existing data!"""
    pass
