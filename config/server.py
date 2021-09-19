import uvicorn


# Config Server
def application_run():
    return uvicorn.run(
        "config:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        debug=True,
    )






