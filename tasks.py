from invoke import task
import os


@task
def start(c):
    """
    Start the Uvicorn server.
    """
    c.run("uvicorn workout_api.main:app --reload")


@task
def create_migrations(c, d):
    """
    Create database migrations.
    """
    pythonpath = os.getcwd()
    c.run(f"set PYTHONPATH={pythonpath} && alembic revision --autogenerate -m '{d}'")


@task
def run_migrations(c):
    """
    Run database migrations.
    """
    pythonpath = os.getcwd()
    c.run(f"set PYTHONPATH={pythonpath} && alembic upgrade head")
