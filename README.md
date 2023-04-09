# poker-hands-tester

Testing poker hand outcomes in OOP Python.

## Usage
```python
from main import *

protagonist = Hand(set((Card(...), Card(...), ...)))
antagonist = ...

print(Judge.judge(protagonist, antagonist))
# 'win' | 'loss' | 'tie'
```
Check the tests for details on usage.

## Test (unix)
```sh
cd poker-hands-tester 

# make virtual environment
python -m venv .venv

# activate virtual environment (source it)
. .venv/bin/activate

# install testing framework
pip install pytest

# run tests (collects all test_* files)
pytest

# want to leave the virtual environment? 
deactivate
````