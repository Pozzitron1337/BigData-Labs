import xml.etree.ElementTree as ET

# create the file structure
items = ET.Element('items')
item1 = ET.SubElement(items, 'item')
item2 = ET.SubElement(items, 'item')
item3 = ET.SubElement(items, 'item')

item1.text = 'item1abc'
item2.text = 'item2abc'
item3.text = 'item1abc'

#delete same elements
for i in range(len(items)):
    for j in range(i+1,len(items)):
        #print(f'{i} {j}')
        if items[i].text==items[j].text:
            items.remove(items[j])

tree=ET.parse("./items2.xml");
items=tree.getroot()
item3=ET.SubElement(items,"item")
item3.text='item3abc'
for i in items:
    print(i.text)



# create a new XML file with the results
mydata = ET.tostring(items, encoding='utf-8', method='xml').decode('utf-8')
myfile = open("items2.xml", "w")
myfile.write(mydata)







