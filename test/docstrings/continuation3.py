# not a docstring
a = \
r'>>> print(42)a[wer]'

b = \
# docstring
r'>>> print()a[wer]'



#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 not a docstring : comment.line.number-sign.python, source.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
\             : separator.continuation.line.python, source.python
              : source.python
r             : source.python, storage.type.string.python, string.regexp.quoted.python
'             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.python
>>> print     : source.python, string.regexp.quoted.python
(             : punctuation.parenthesis.begin.regexp, source.python, string.regexp.quoted.python, support.other.parenthesis.regexp
42            : source.python, string.regexp.quoted.python
)             : punctuation.parenthesis.end.regexp, source.python, string.regexp.quoted.python, support.other.parenthesis.regexp
a             : source.python, string.regexp.quoted.python
[             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.begin.regexp, source.python, string.regexp.quoted.python
w             : constant.character.set.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.python
e             : constant.character.set.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.python
r             : constant.character.set.regexp, meta.character.set.regexp, source.python, string.regexp.quoted.python
]             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.end.regexp, source.python, string.regexp.quoted.python
'             : punctuation.definition.string.end.python, source.python, string.regexp.quoted.python
              : source.python
b             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
\             : separator.continuation.line.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 docstring    : comment.line.number-sign.python, source.python
r             : source.python, storage.type.string.python, string.quoted.docstring.raw.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.raw.python
>>> print()a[wer] : source.python, string.quoted.docstring.raw.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.docstring.raw.python
