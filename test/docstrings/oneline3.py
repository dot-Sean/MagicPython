def foo():
    '>>> print("docstring")'
def foo():
    ">>> print('docstring')"



def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.python
>>> print("docstring") : source.python, string.quoted.docstring.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.docstring.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.python
>>> print('docstring') : source.python, string.quoted.docstring.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.docstring.python
