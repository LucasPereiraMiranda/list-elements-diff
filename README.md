<h1 align="center"> List Elements Diff </h1>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/LucasPereiraMiranda/list-elements-diff">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/LucasPereiraMiranda/list-elements-diff">
  
  <a href="https://github.com/LucasPereiraMiranda/list-elements-diff/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/LucasPereiraMiranda/list-elements-diff">
  </a>

  <a href="https://github.com/LucasPereiraMiranda/list-elements-diff/issues">
    <img alt="Repository issues" src="https://img.shields.io/github/issues/LucasPereiraMiranda/list-elements-diff">
  </a>

  <a href="https://github.com/LucasPereiraMiranda/list-elements-diff/issues">
    <img alt="GitHub license" src="https://img.shields.io/github/license/LucasPereiraMiranda/list-elements-diff">
  </a>
</p>

## 💻 Objectives

Project helper to obtain the different elements between two lists

### Execution preview:

<div align="center">
  <img src=".github/img/execution.png" alt="Execution preview">
</div>

## 🚀 Techs

The analysis is being performed with the following technologies:

- [Python3](https://www.python.org/)
- [UnitTest](https://docs.python.org/3/library/unittest.html)

## :boom: How to run the application?

- We can activate the virtual environment by running:

```shell
  source /venv/bin/activate # Linux or Mac
```

- After defining the contents of the lists in the `handle` file `list_1` and `list_2`, we can run:

```shell
  python src/handle.py
```

## :heavy_check_mark: How to run project unit tests?

We can run it from the root of the project:

```shell
  python -m unittest discover -s src -v -p "test_*.py"
```

### License

[MIT](https://choosealicense.com/licenses/mit/)
