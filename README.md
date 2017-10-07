# chcbot
Script to generate automated responses based on input text

This script will take an input string and generate an automated response based on
given predetermined input.

The code works using primary and secondary key words. If a primary keyword is found,
it will then search for a secondary key word and output a response if found.

If the keyword "@chainbot" is found, then the secondary keyword search is skipped
and a response is generated based on the primary keyword alone.

EXAMPLE:
> primary key = updates
> secondary key = new,any,chc
> response = Hi, here are the updates!
>
> chcbot('Are there any new updates?')
> "Hi, here are the updates!"
> chcbot('@chainbot updates')
> "Hi, here are the updates!"
> chcbot('my computer keeps getting updates')
> ""
