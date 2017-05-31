
Create and use virtual env

`
source ./conreg-env/bin/activate
`

Install Dependencies


`
pip install dbfpy
`


Test / dev

>>> from dbfpy import dbf
>>> db = dbf.Dbf('/Users/rpowell/dev/lasfs/conreg/databases/master.dbf', new=False)

for r in db:
  print r



# References

* http://dbfpy.sourceforge.net/ - Python dbfy

