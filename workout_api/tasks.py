from invoke import task

@task
def start(c):
    """
    Start the Uvicorn server.
    """
    c.run("uvicorn main:app --reload")
