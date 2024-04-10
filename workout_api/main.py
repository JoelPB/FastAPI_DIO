from fastapi import FastAPI

app = FastAPI(title="workoutApi")


if __name__ == "__main__":
    import unicorn

    unicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)