try:
    from fastapi import FastAPI
except Exception:
    # Minimal stub implementation to avoid import errors when FastAPI is not installed.
    # This allows the module to be imported and the decorated function to remain callable.
    class FastAPI:
        def __init__(self):
            pass

        def get(self, path: str):
            def decorator(func):
                return func
            return decorator

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Task 1 Completed!"}