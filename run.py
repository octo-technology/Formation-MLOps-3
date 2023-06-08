import uvicorn

if __name__ == '__main__':
    # WARNING : Being on 0.0.0.0 is a security issue according to bandit, we escaped the check in CI for now
    # but we should investigate it further.
    uvicorn.run("source.api.main:app", host="0.0.0.0", port=8000)
