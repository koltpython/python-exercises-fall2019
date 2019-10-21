
street1 = 'street1cacaaacatdogdodogggoddogcatgoddocat'
street2 = 'street2dogggdocadocacatdogdogdogcdodcdogca'
street3 = 'street3catcatccttaaddogdogdogdogcatdogdogcat'
street4 = 'street4catdogogogggddoocogdatddactogdogca'

streets = [street1, street2, street3, street4]

# Your code starts here
for street in streets:
  name = street[:7]
  count = 0
  while ('dogcat' in street ):
    count += 1 
    ind = street.index('dogcat')
    street = street[ind+1:]
  print (f'Dog has left {count} marks on {name}')
