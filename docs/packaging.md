# Packaging

We'll review here a few options to package your code and ship it around to other codes versions. 


## To create your own package...
https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/

Once you build a package, test it as:


### using pyenv....

1. Create a folder somewhere
2. activate an environment for testing. This should be python runtime you used to test your package (3.10 in the example below).
    ```sh
    pyenv virtualenv 3.10.8 3.10-test-inftools
    ```
3. Run
    ```sh
    pip install $PATH-TO-PACKAGE
    ```

### using pipenv...

1. Create a folder somewhere
2. pipenv install --python 3.10
3. pipenv install PATH-TO-PACKAGE



## Other stuff (more obscure, from past notes)...

### Packaging into a wheel
https://python101.pythonlibrary.org/chapter39_wheels.html

The cool thing of `wheel` is that it can be installed in a `virtualenv`.

### Egg files
https://python101.pythonlibrary.org/chapter38_eggs.html

This was the first mainstream packaging format. Egg files are simply a way to ship aroung python code. In fact, `egg` files are `zip` files, which contain your code inside.



