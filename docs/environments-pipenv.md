# Pipenv

`Pipenv` is the official recommended python packing tool is one of the easiest ways to create a virtual environment and install the python package together. In a nutshell, `pipenv` allows to create environments which support:
- **Their own `Python` version.** We not just define the required python packages: with `pipenv`, we can define which python version our codebase should execute with. Note that other environment managing tools, e.g. `pyenv`, only allow to manage python dependencies, typically through a `requirements.txt.

- **Add to your environment anything that can be `pip install`ed or cloned from `git`**. This allows to essentially add to your environment any other package, as long as it can be installed with pip or cloned from a git repository. 

- **Automatically separated between production and development environment**. When we install a new package, we can specify if this in only needed for development.

-  It creates a Pipfile to manage and record packages, so the overall project is easy to deploy.

The only requirement is to have pipenv installed on your development/testing machine. 


### **References**
1. https://pypi.org/project/pipenv/
2. https://pipenv-fork.readthedocs.io/en/latest/basics.html


---
## Install `pipenv`

- For Debian `sudo apt install pipenv` [1]
- For macOs, `brew install pipenv`, plus some extra [2].


**References:**
1. https://pypi.org/project/pipenv/
2. https://thinkdiff.net/how-to-use-python-pipenv-in-mac-and-windows-1c6dc87b403e


---
## Get started

**Note: all examples below can be seen also typing `pipenv --help`**.

- From your project folder, create a new project (e.g. one that uses Python 3.9) as:
    ```
    pipenv --python 3.9
    ```
    This will create a `Pipfile` into your project folder which specifies that we are using `Pyhton 3.9`. See `Pipfile` section for more info.

    **Tip**: pipenv installs the environments into a system folder. You can change this setting by exporting `export PIPENV_VENV_IN_PROJECT=1` in your `.zsh` or else file.



- To activate the environment into your shell, use:
    ```
    pipenv shell
    ```
    To check that the environment is active, try running `whereis python` or (equivalently) `pipenv --py`; the output should reference a `python` binary into the newly created virtual environment, which will have a format of this kind:
    ```sh
    [HOME FOLDER]/.local/share/virtualenvs/[PROJECT-FOLDER]-gXcgknWo/bin/activate
    ```
    You can deactivate the environment typing `exit` in the shell.



- With `pipenv` you can install:

    - from `git`. See [1] for examples.

    - from `pip`. Note that `pip install` is not limited to `python packages`; several tools, e.g. `dbt`, can be installed with `pip`. Here are a few examples:

        - Install the latest version of `numpy`: `pipenv install numpy`

        - Install `pytest`, but only for `dev`: `pipenv install pytest --dev`

        - Install `dbt` with postgres adapter:
        ```sh
        pipenv install dbt-core
        pipenv install dbt-postgres
        ```

        - You can also install from a requirement file as:
        ```sh
        pipenv install -r path/to/requirements.txt
        ```

        Note that in order to run `pipenv install` you **do not** need to first activate the environment in  the shell (namely, no need to run `pipenv shell` - in fact, thic could cause issues). Simply navigate to your project folder where the `Pipfile` is located. 

    After these steps, you should see the python packagest listed when running `pipenv shell; pip freeze`. You will also see them into your `Pipfile` (see `Pipfile` section).


- To ensure repeatability of your code (and deterministic build), the `Pipfile` alone is not enough. You'll need to create a `Pipfile.lock` file using:
    ```sh
    pipenv lock
    ```##
    The `Pipfile.lock` file  declares all dependencies (and sub-dependencies) of your project, their latest available versions, and the current hashes for the downloaded files. This ensures repeatable, and most importantly deterministic, builds.


- If you are **cloning a project which already has a `Pipfile`**, you can create this environment by simply typing 
    ```sh
    cd project-folder-where-pipfile-is
    pipenv install --dev
    ```
    where the (optional) `--dev` arguments will also install packages for development.


---
## Pipfile

A Pipfile looks like this:

```sh
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"

### add here packages.
# These are not just python packages, but also external programs/tools.
[packages]
numpy = "*"
dbt-core = "*"
dbt-bigquery = "*"

### add here extra development packages.
# They are installed with `pipenv install --dev`
[dev-packages]
pytest = "*"

### Python version
[requires]
python_version = "3.9"
```


