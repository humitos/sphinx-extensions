# myst-parser[sphinx]

* **Homepage**: [https://github.com/ExecutableBookProject/MyST-Parser](https://github.com/ExecutableBookProject/MyST-Parser)
* **Documentation**: [https://myst-parser.readthedocs.io/en/latest/](https://myst-parser.readthedocs.io/en/latest/)

`myst-parser[sphinx]` is a Markdown parser (`.md` files) that allows you to
combine all the power of Markdown with all the potential of
Sphinx. All at once!


```{note} This whole page is written in Markdown (see [Show Source](https://sphinx-extensions.readthedocs.io/en/latest/_sources/myst-parser.md.txt)).

As you can see, Sphinx extensions keep working without changes (e.g. `sphinx-prompt` and `sphinx-copybutton`)
```

% I had to add an absolute link, because I didn't find how to make it relative


## Installation

```bash
pip install myst-parser[sphinx]
```


## Configuration


```python
# conf.py
extesions = [
    '...',
    'myst_parser',
]
```
