replace = {'"' : R'\"',
           "'" : R'\'',
           '\\': R'\\'}



replace       : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
{             : punctuation.definition.dict.begin.python, source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
"             : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
 :            : source.python
R             : source.python, storage.type.string.python, string.quoted.raw.single.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.raw.single.python
\"            : source.python, string.quoted.raw.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.raw.single.python
,             : source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
'             : source.python, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
 :            : source.python
R             : source.python, storage.type.string.python, string.quoted.raw.single.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.raw.single.python
\'            : source.python, string.quoted.raw.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.raw.single.python
,             : source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
\\            : constant.character.python, source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
:             : source.python
R             : source.python, storage.type.string.python, string.quoted.raw.single.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.raw.single.python
\\            : source.python, string.quoted.raw.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.raw.single.python
}             : punctuation.definition.dict.end.python, source.python
