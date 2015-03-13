# Usage #

This page covers the basic functionalities of the extension.

## Basic spell checking ##

```
>>> import hunspell
>>> hobj = hunspell.HunSpell('/usr/share/myspell/en_US.dic', '/usr/share/myspell/en_US.aff')
>>> hobj.spell('spookie')
False
>>> hobj.suggest('spookie')
['spookier', 'spookiness', 'spooky', 'spook', 'spoonbill']
>>> hobj.spell('spooky')
True
>>>
```

## More fun ##

```
>>> import hunspell
>>> hobj = hunspell.HunSpell('/usr/share/myspell/en_US.dic', '/usr/share/myspell/en_US.aff')
>>> hobj.analyze('linked')
[' st:link fl:D']
>>> hobj.stem('linked')
['link']
>>> 
```