## Python installation and environments

This file describes how to manage multiple python versions and environments within it.
For handling python versions, we'll use and external tool `pyenv`. This allows, in a nutshell, to have both python 3.10.14 and python 3.9.8 installed on your machine at the same time, and to choose which to use. A plugin on `venv`, `pyenv-virualenv`, is used to build versions of pythons with pre-installed packages; for e.g., we can build a `python 3.10-ml` environment, which will have a bunch of ML packages pre-installed on top of python 3.10 (e.g. for when we want to run a quick analysis or so). For development, instead, we can use virtual environments using `venv`, which is shipped by default with `python-3.3+`. Note that a better approach for development is to employ `pipenv`, which allows recording into a single setting file both the Python version and the packages required for our application.


## Best set-up

This section is a summary of the following, and describes the recommended set-up - this assumes `pyenv` is already installed and the latest python version is `3.9.0`.

```sh
# build pristine python installation. This will be starting point for projects environments
pyenv install -v 3.9.0

# build a pristine python with jupyter - and only jupyter. This will be used to start environments.
pyenv virtualenv 3.9.0 3.9.0-jupyter
pyenv shell 3.9.0-jupyter
pip install jupyter
pip install jupyterlab

# (optional)
pip install jupyterlab-spellchecker.  # for spell checker
```
This builds into `~/Library/Jupyter`. At this point, a Python 3 kernel is already available - but not shown in `~/Library/Jupyter/kernel`. This means, for eg, that notebooks form vscode will not work - cause vscode won't find a kernel. You can either add a kernel using the `python -m ipykernel ...` command, or also simply create your first notebook from `jupter notebook` and open it in `vscode` - VS code will pick the kernel from the notebook.

Next, we can build an environment for standard machine-learning tasks and with ipython. We will add the kernel of this environment to a location that `jupyter` knows. 
```sh
pyenv virtualenv 3.9.0 3.9.0-ml
pyenv shell 3.9.0-ml
pip install -r requirements-ml.txt
pip install ipykernel
python -m ipykernel install --user --name 3.9.0-ml --display-name 3.9.0-ml 
```

When building a new environment, if you want to use the notebook, simply add `ipykernel` to the requirements (or simply run) and export it to a location where `jupyter` can find it. **It is fundamental that you use a unique name. To automatise this, we run**:
```sh
ENV_NAME=env-dev
FOLDER_NAME=${$(pwd | tr "/" " ")[-1]}
KERNEL_NAME=${FOLDER_NAME}-${ENV_NAME}

python -m venv $ENV_NAME
source ${ENV_NAME}/bin/activate
pip install --upgrade pip
pip install -r requirements_dev.txt
pip install ipykernel

python -m ipykernel install --user --name $KERNEL_NAME --display-name $KERNEL_NAME 
```


## Python versions 

Managing python version is done independently from the environments management 

### pyenv

This is a tool to handle multiple python installations. Refer to `git` repo @:
https://github.com/pyenv/pyenv

- To install: you need to refer to the installation package repo https://github.com/pyenv/pyenv-installer. In both linux and Mac Os it was enough to run the installation script of the official repo:
    ```
    curl https://pyenv.run | bash
    ```
    add the following to your `~/.bashrc` (or `~./zshrc` if running `zsh` on Mac) to automatically start `pyenv`:
    ```sh
    export PATH="/home/smub/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    ```
    The installation builds a folder `.pyenv` in your home, where all `python` versions will be managed. 


- check: run `pyenv doctor` to see if there are issues. 


- Usage (https://realpython.com/intro-to-pyenv/):
    ```sh
    # list all versions available to install...
    pyenv install --list
    # maybe shorten th eoutput - e.g. only python 3.7 to 3.8
    pyenv install --list | grep 3\.[7,8]
    # once you are happy, install one from the list
    pyenv install -v 3.8.6

    # all your versions are stored in:
    ls ~/.pyenv/versions/
    # but you can list them with
    pyenv versions
    # see current version
    python --version
    # change default version 
    pyenv global ANY-PYTHON-INSTALLED

    # chenge default python version in FOLDER (creates a .python-version file)
    pyenv local 2.7.15
    # change python in shell
    pyenv shell 3.9.0

    # check all ins good with your installation
    python -m test
    # remove a version
    pyenv uninstall 3.8.6
    ```

### about IPython, jupyter & co...
*https://medium.com/@henriquebastos/the-definitive-guide-to-setup-my-python-workspace-628d68552e14*

There may be other packages that you may want by default on your system - e.g. `IPython` or `jupyter`, to quickly test code not necessarely within a project. Other examples are packages for making coding easy (eg `pylint`).

In order to have these packages handy without messing up the original installation of python, you can use the plugin `pyenv-virtualenv`. This can create a globally available virtual environment which is seen by `pyenv` as a python version. This virtual environment that lives inside your home `.pyenv` folder as if it was a different python installation - or similarly to a `conda` environment that is available *globally*.

To do this, for your favourite or latest (or whatever) python version, you can build a new environment with extra packages. E.g.:
```
pyenv virtualenv 3.9.0 3.9.0-jupyther
```

You can now augment this version with extra packages. A common set-up is to have `jupyter` and `IPython`. *Note that, having `jupyter` means having (type `jupyter --version`): `jupyter core` a `jupyter client`, `ipython` and `ipykernel`. But `jupyter-notebook` or `jupyter lab` will not be there and you should add them using pip (https://jupyter.org/install), e.g. `pip install jupyterlab` or `pip install notebook` - **upon creation of an environment**.* Following from previous example:
```sh
pyenv global 3.9.0-jupyther
pip install jupyter
pip install jupyterlab
# this builds into ~/Library/Jupyter . At this point, a Python 3 kernel is already available - but not shown in ~/Library/Jupyter/kernel.
```
This python version can, for instance, be used by default in vscode. As `jupyter` supports many kernel, this installation can be used to manage all notebooks environments - rather than installing `jupyter` in each project environment, add instead the project environment to the kernel of this `jupyter` installation.
Other packages that may be worth including in this installation may be `pyyaml`, `pylint` etc. To remove all packages from a python version, you can run `pip freeze | xargs pip uninstall -y`.



## Python environment

For how to write requirement files, refer to: https://pip.pypa.io/en/stable/reference/pip_install/.


### venv
This is the official package, which ships with python `3.3+` -so it is an ideal solution, as it does not require installations. It works precisely as `virtualenv` Usage:

- Build and install packages
    ```
    python -m venv env_prod
    source env_prod/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
    If you want to make sure people are using the same identical version pf python (not just `3`, but `3.6` for eg), replace the first line with 
    `python3.6 -m venv env_prod`. Note that this command will work whether people have `3.6.1` or `3.6.4` installed.

- deactivate `deactivate`

- remove 'rm -r ./env_prod'


### virtualenv

This works like `venv` but does not ship automatically with python - however can be used with older pythons. The execution is as per `venv`, with the exception that we may need to install `virtualenv` itself: 

```
pip install virtualenv
virtualenv env_prod
pip install --upgrade pip
source env_prod/bin/activate
pip install -r requirements.txt
```


## Local environmental variables
You can use `direnv` https://direnv.net/ . 

0. Install as: `curl -sfL https://direnv.net/install.sh | bash`. **Note that `direnv` is installed as a plugin under your `pyenv` installation**.

1. Create a `.envrc` file as: `echo export FOO=foo > .envrc`.

2. Load env variable to `.envrc` as: `echo export FOO=foo > .envrc`.


## Working with notebooks and environment

While one can install `jupyter{lab}` in a local environment, having multiple `jupyter` installations can be confusing - and is **useless**. One cause of confusion (which can be solved) arises from the fact that all `Jupyter` installations would build environment **kernels** (which is just a `json` with some metadata) in the same global locations (e.g. on MacOs `~/Library/Jupyter` or `/usr/local/share/jupyter/kernels/ENV-NAME`). Also, there is no advantage/need to have multiple `jupyter` installations. 

What `jupyter` does, in fact, is to create `kernels` (with the module `ipykernel`). These `kernels` are effectively a bunch of metadata that can point to **any** python installation on your system. In fact, when you create a kernel with `python -m ipykernel` this will by default refer to the python version you are using when issuing the command. what `jupyter` does, therefore, is simply to read the `kernel` and start whichever `python` exdecutable is pointed to in that kernel. 

In summary:
- when you create a new environment, you need to `pip install ipykernel` as this will allow you to issue a command `python -m ipykernel --PLUS-OPTIONS` that builds the `kernel` (a pointer to the `python` executable)

Hence, it becomes complicated to maintain different `jupyter` unless one is extra careful not to duplicate names. *Note that this issue arises even if you have a single `jupyter` installation (e.g. if you build two kernels for different projects with same name, they may overwrite each other). However, having multiple `jupyter` does not solve it and, on the ocntrary, may make things more confusing*
Also, this effort is totally non-sense as, by default, jupyter can load any kernel. Therefore, the best practice is to have a pristine python installation with only `jupyter` and use this to start jupyterlab. 

When building a new environment, instead, we will export the kernel for this environment, either:

1. to a location where `jupyter` looks for kernels. **The key here is to ensure that the current environment name won't override an environment previously built for another project**. 

2. locally. In this case, we should not worry about the naming. However, we may have issues locating the kernel. 

The following code, in which we pre-fix the current folder name to the environment, should do the trick.
```sh
ENV_NAME=env-dev
FOLDER_NAME=${$(pwd | tr "/" " ")[-1]}
KERNEL_NAME=${FOLDER_NAME}-${ENV_NAME}

python -m venv $ENV_NAME
source ${ENV_NAME}/bin/activate
pip install --upgrade pip
pip install -r requirements_dev.txt
pip install ipykernel

# export to global location ( on MacOs `~/Library/Jupyter` or `/usr/local/share/jupyter/kernels/ENV-NAME` if not used the `--user` option - see below)
python -m ipykernel install --user --name $KERNEL_NAME --display-name $KERNEL_NAME 

# export locally (to ./${KERNEL_NAME}/share/jupyter/kernels/env-dev)
python -m ipykernel install --name $KERNEL_NAME --display-name $KERNEL_NAME --sys-prefix
cp ./${ENV_NAME}/share/jupyter/kernels/${KERNEL_NAME}/kernel.json kernel-${KERNEL_NAME}.json
```
In both examples, we will have built the same kernel of type:

```json
{
 "argv": [
  "..../ENV-FOLDER/bin/python",
  "-m",
  "ipykernel_launcher",
  "-f",
  "{connection_file}"
 ],
 "display_name": "DISPLAY-NAME",
 "language": "python"
}
```
what changes is the location of the kernel. I'm still unsure on how to tell `jupyter` to read the kernel. There is an option
```
jupyter noteook --notebook-dir .
```
but if does noy seem to identify the kernel.


Note that you can also create a kernel on the fly without having to export etc by typing in terminal:
```sh 
ENV_NAME=env-dev
source ${ENV_NAME}/bin/activate
python -m ipykernel 
```
See also `python -m ipykernel --help` for more options. You can also view a list of your kernels (at least those that are in `jupyter` default path) through `jupyer kernelspec list`.


## Working with notebooks in VScode

1. https://code.visualstudio.com/docs/python/environments

- When launching a notebook in VScode, VScode will generally see local virtual environments (those inside your workspace root folder) and proposed them to you for use. So the steps defined in the previous sections are not needed. This may be an advantage, to keep things tider. VS code should also be able to see global environments. In my experience it sees the `pyenv` environments, but not all kernels. You can change the folders where vs code looks for environment if needed - see ref.[1] of this section.

- Enviromental variables are more tricky.

    - add an `.env` file to your workspace root folder (i.e. the fodler you open in vs code). This must have format
        ```sh
        # API endpoint
        MYPROJECT_APIENDPOINT=https://my.domain.com/api/dev/
        # Variables for the database
        MYPROJECT_DBURL=https://my.domain.com/db/dev
        MYPROJECT_DBUSER=devadmin
        MYPROJECT_DBPASSWORD=!dfka**213=
        ```
   
        You can control the file name in `Settings->` "python.envFile": "${workspaceFolder}/.env". You can even have a productionand debug configuration (if you set-up the debug environment).
    

    - You can make a start-up script to execute at notbook launch. 

        ```
        "jupyter.runStartupCommands": [
            "import os",
            "env_vars = !cat .env",
            "os.environ['TEST']='1'"
        ]
        ```
