import argparse
import os

import uvicorn

from config.env import ENVIRONMENT, EnvironmentType

if ENVIRONMENT == EnvironmentType.prod:
    # Specific code for DSLAB to run on expected port
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", help="Port on which to run")
    args = parser.parse_args()
    port = int(args.port)
    # End of specific code
else:
    port = 8001

if __name__ == '__main__':
    # WARNING : Being on 0.0.0.0 is a security issue according to bandit, we escaped the check in CI for now
    # but we should investigate it further.
    log_ini_path = os.path.join(os.path.dirname(__file__), 'log_config.ini')
    code_dir = os.path.dirname(__file__)
    uvicorn.run("source.api.main:app", host="127.0.0.1", port=port, reload=True, log_config=log_ini_path,
                reload_dirs=code_dir, reload_excludes="*.log")
