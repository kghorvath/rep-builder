#Testing functions
from lib.build_header import build_header
from lib.add_product import add_product

#Global variables
projid='1001'
#Testing build_header
repfile = open('examples/testing.xml','w')
build_header(repfile,'2018.05',projid,'19EX999','Example Project',)

#Testing add_product
repfile = open('examples/testing.xml','a')

#Item 1
pid = '001'
tag = 'ITEM-1'
pn = '123-1'
desc = 'Example Item 1'
mult = '1.0'
quantity = '1'
price = '1000.00'

add_product(repfile,pid,projid,tag,pn,desc,mult,quantity,price)

#Item 2
pid = '002'
tag = 'ITEM-2'
pn = '123-2'
desc = 'Example Item 2'
mult = '1.5'
quantity = '8'
price = '2878.00'

add_product(repfile,pid,projid,tag,pn,desc,mult,quantity,price)