
#Flow


### after split

contents:

[1580882400000,30.23]

## attributes

$fragment.count, $fragment.index

$frequency,$lastmod,$oid,$oname,$tz

## extract text



prop: tstamp
* ^[(d+),.*]$
* ^\[(\d+),.+\]$

prop: numvalue 
* ^.*,(.+)]$


## proc replace text
search value:
* (s?)(^.*$)  ## matches whole line

replacement value:  ## $1  is a default value referencing group1

```
insert into tbl(oid,tstamp,tz,price) values (${oid},${tstamp},${tz},${numvalue});
insert into tbl(oid,tstamp,tz,price) values (${oid},${tstamp},${tz},${numvalue});${literal('\n')
```

## proc mergeContent

$fragment.identifier : e3fb98e9-b577-4fd8-bf1c-503b75ae0c9e
$fragment.index  : 2
$fragment.count   : 96
$uuid:  4dce1355-df15-410e-8958-6b2b711c0236


$fragment.identifier: e3fb98e9-b577-4fd8-bf1c-503b75ae0c9e
$fragment.index  : 5
$fragment.count   : 96
$uuid: fc7796bf-7a4c-4dac-bbde-70d6ba4db941


$ofilename=${oid}.sql


