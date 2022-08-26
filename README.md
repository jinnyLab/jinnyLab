# jinnyLab Python setup

jinnyLab Core Python packages

## Python Environment Setup
00. install miniconda or anaconda
01. install conda packages
    ```bash
    # create new environment
    conda env remove -n jinnylab -y
    conda env create --name recoveredenv --file environment.yml
    # install conda packages
    conda activate jinnylab
    conda update --all -y
    conda clean --all -y

02. pip install package
    ```bash
    pip install -e .
    ```



## Git Setup
Check https://rogerdudler.github.io/git-guide/index.ko.html
01. Make a folder and initialize git
    ```bash
    # Initialize git
    git init
    ```
02. Git pull and and remote repository
    ```bash
    # Pull from remote
    git pull https://github.com/jinnyLab/jinnyLab.git
    # Add remote repository as origin
    git remote add origin https://github.com/jinnyLab/jinnyLab.git
    ```
03. Update the progess
    ```bash
    # check which files have been updated
    git status
    # add files you want to update
    # add . will update all files you have changed
    git add .
    # commit with note
    git commit -m "Test message"
    # push to remote repository
    git push origin master
