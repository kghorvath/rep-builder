import xml.etree.ElementTree as ET

#Import the REP file
tree = ET.ElementTree(file='examples/example.rep')
print tree.getroot()
root = tree.getroot()

for header in root.attrib('Header'):
    print header.attrib