# Notes

Steps:

1. Clone the repo
2. set up venv environment (please use `.venv` directory as it the .gitignore is already configured for it):

   ``` bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Run `get_openvino_repo.sh`
4. Run `install_dependencies.sh`
5. Run `build_doxygen.sh`
6. Run `sphinx-build -b html . _build/html`
7. Leave venv environment: `deactivate`
