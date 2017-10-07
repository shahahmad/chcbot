# chcbot
This script will take an input string and generate an automated response based on
given predetermined input.

The code works using primary and secondary key words. If a primary keyword is found,
it will then search for a secondary key word and output a response if found.

If the keyword "@chainbot" is found, then the secondary keyword search is skipped
and a response is generated based on the primary keyword alone.

EXAMPLE:
```
$ Python
> primary key = "updates"
> secondary key = "new,any,chc"
> response = "Hi, here are the updates!"
> chcbot('Are there any new updates?')
> "Hi, here are the updates!"
>
> chcbot('@chainbot updates')
> "Hi, here are the updates!"
>
> chcbot('my computer keeps getting updates')
>
```

The outputs are generated using a tab delimited file. The file contains no header
and three columns separated by "\t". The fist column is the primary key, the
second column contains the the secondary keys and the last column is the response.

Here are some criteria the input data must follow:

1. For the time being only a single primary key can be given, but multiple secondary
keys can be given separated by commas.

2. The primary and secondary keys cannot contain any punctuation (it is stripped
off if given).

3. The secondary key field can be left blank


EXAMPLE (please also refer to the "input.txt" file):
```
$TXT
update\tnew,any,dev,development,chaincoin,chc\tHi, here is the new update
hi\t\thello!
```

#TODO:
1. Use nltk stemmer package available for python to get stem words from input_list
such as plurals (so they do not need their own row in input.txt)

2. If needed, add functionality to allow for unlimited "layers" of keys after
primary keys (not just secondary keys)

3. Use natural language processing to utilize word order and sentence structure
to generate more accurate responses
