# Working with python venvs

### When installing on the venv

Installing smt on venv
```bash
pip install something
```
generate the list of everything installed and neccessary to run your program
```bash
pip freeze > requirements.txt
```
This becomes the official list for my projects dependencies

#### Freeze occacionnally: 
- *Freeze every once in a while* 
- *Freeze right after any install*
```bash
pip freeze > requirements.txt
```

### Restoring the venv
anyone including you can recreate the venv with all requirements using: 
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```