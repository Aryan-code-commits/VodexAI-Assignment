import uvicorn

def main():
    """Run the FastAPI application."""
    uvicorn.run("vodex.main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()
