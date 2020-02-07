
# Flow

## proc ReplaceTex

replace text:
* search value (?s:^.*$)  ## matches whole line

repacement value:
* a,b,c,d,


## Proc ExractText

property: cvs
* regex (.+),(.+),(.+),(.+)

NB: rout unmatched -> LogAttribute

## Proc ReplaceText
search value
* regex (?s:^.*$)   ## matches whole line
* regex (?s)(^.*$)


replacement value:
    * value:
```
{"field1" : "${csv.1}",
 "field2" : "${csv.2}",
 "field3" : "${csv.3}",
 "field4" : "${csv.4}",
 "field5" : "${uuid}",
 "field6" : "${filename}"}

```




