# Python Debugging with VScode

This is a quick guide on python debugging in VScode. Refer to the [official documentation](https://code.visualstudio.com/docs/python/debugging) for more details.

1. start from a `main.py`, or a script, or a library in which you specified an entrypoint using `if __name__=="__main__": xxx` construct. This is the same as you'd be doing if you were, say, *print* debugging, or using `IPython` (`from IPython import embed; embed();`).

2. Open the file in editor. On top right, you'll see the *play* arrow. Select `Python Debugger: *`.

    - For the first time, choose to **Debug Pyhton File**, which will trigger the debugger. Unless your script is very simple, it will fail. There are a number of possible reasons:
        - your code requires environmental variables;
        - or input arguments;
        - a specific python environment;
        - or if the entry point is not correct - e.g. it can't find some custom library in the same folder. 
    
    - In this case, we'll need to manually update the `launch.json` settings. 
    
    - This may have been automatically created in `.vscode/launch.json` under the folder containing the python file debugged (or perhaps the project root, double check that).

    - If not, in the debugger window you can click `Add configuration`, which will add a new configuration - and should create the `.vscode/launch.json` above.

    - Modifying the `launch.json` you will be able to define the relevant aspects for executing your code. See ![]()
    

## `launch.json`

Here we highlight some key aspects of `launch.json`; refer to the [official documentation](https://code.visualstudio.com/docs/python/debugging#_justmycode) for a complete overview. 

It may be also handy to look at the vscode [Variable Reference], which shows key variables defined in VScode - e.g. the following are used in the example below:

- `${workspaceFolder}`: the path of the folder opened in VS Code.
- `${fileDirname}`: the current opened file's folder path.



```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug a file in local python environment from root folder",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",

            // python executable - environment.
            // This defaults to the interpreter selected for your workspace; to set this, go to 
            // `Python: Select Interpreter` command from the `Command Palette` [shift+cmd+P] and
            // select the python environment 
            // "python": "${command:python.interpreterPath}",
            // Alternatively, you can add the path to the python environemnt directly here - e.g.:
            "python": "${fileDirname}/venv/bin/python3",

            // folder from where the script is executes. Note that ${workspaceFolder} is the root 
            // folder opened in vscode.
            "cwd": "${workspaceFolder}", 

            // if true, will only debug your code. With false, it will dig also in libraries.
            "justMyCode": true, 

            // add environmental variables here or...
            "env": {
                "MY_ENV_1": "the-value-always-as-string",
                "MY_ENV_2": "12345",
            },
            // refer to a .env file
            // "envFile": "${workspaceFolder}/path-to-env-file/.env"

            // specify here arguments - e.g. if your script uses argparse and requires arguments to run.
            "args": [
                "--user=postgres", 
                "--password=password123"
            ],

            // with autoreload, when you change a module the debugger will automatically be reloaded.
            "autoReload": {
                "enable": false
            }

        },
        // you can have more configurations - and select the one you need at debug time.
        {
            "name": "Another configuration...",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
        }

    ]
}
```