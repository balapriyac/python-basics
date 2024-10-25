## Unit Testing with PyTest

Install pytest in a virtual environment:

```
$ python3 -m venv v1
$ source v1/bin/activate
$ pip3 install pytest
```

The code for the TO-DO list app is in the `todo/` folder. And the unit tests are all in the `test_todo_manager.py` file in the `tests/` folder.

To run the tests, in the root directory, run:

```
$ pytest
```
