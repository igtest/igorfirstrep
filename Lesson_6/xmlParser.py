# __author__ = 'i.brikin'

from lxml import etree
# temp = []
# temp1 = []
def read_xml():
    elements = []  # list для элементов которые будем заменять
    elements_value = []  # для значений этих элементов
    key = 'TN_elems/Valve.pnl'  # ключь для замены
    tree = etree.parse('newPanel.xml')
    root = tree.getroot()
    # *************** тут мы нашли все вложения текста в chapes/reference и там же в prop
    for prop in root.findall("shapes/reference//prop/[@name='FileName']"):  # для каждого тега prop
        text = prop.text
        if text == key:
            elements.append(prop.getparent().getparent())  # получаем дважды родителя
    print(elements, len(elements))

    for each in elements:
        for elem in each.findall(".//prop"):
            if elem.attrib['name'] == 'Location':
                temp = elem.text.split()
            if elem.attrib['name'] == 'Geometry':
                temp1 = elem.text.split()
        if float(temp1[0]) < 1.0 and len(temp1) == 6:
            temp1.append(0)
        if float(temp1[0]) == 1.0 and len(temp1) == 6:
            temp1.append(1)
        if len(elements_value) > 0:         # ставим нули элементам у которых нет атрибута Geometry
            if temp1[-3] == elements_value[-1][3] and temp1[-2] == elements_value[-1][4]:
                if temp1[-1] == 0:
                    temp1 = [0, 0, 0, 0, 0, 0, 0]
                else:
                    temp1 = [0, 0, 0, 0, 0, 0, 1.0]
        elements_value.append((each.attrib['Name'], temp[0], temp[1], temp1[-3], temp1[-2], temp1[-1]))
    print(elements_value, len(elements_value))
# Удаление ненужных элементов------------------
    for all in elements:
        root[1].remove(all)
#----------------------------------------------
    for all in elements_value:
        root[1].append(make_xml(all))

    et = etree.ElementTree(root)
    et.write('myPanel.xml', pretty_print=True, xml_declaration=True, encoding='UTF-8')

def make_xml(value):
    name = value[0]

    if float(value[-1]) == 1:
        location1 = float(value[1]) + float(value[3])
        location2 = float(value[2]) + float(value[4])
        root = etree.Element('shape')  # создаю начала дерева
        root.set('shapeType', 'GENERIC')
        root.set('layerId', '0')
        root.set('Name', name)
        # root.append(etree.Element('root'))
        properties = etree.Element('properties')
        root.append(properties)
        prop = etree.Element('prop')
        prop.set('name', "serialId")
        prop.text = '1581'
        properties.append(prop)
        prop2 = etree.Element('prop')
        prop2.set('name', 'RefPoint')
        properties.append(prop2)
        prop3 = etree.Element('prop')
        prop3.set('name', 'Enable')
        prop3.text = 'True'
        properties.append(prop3)
        prop4 = etree.Element('prop')
        prop4.set('name', 'Visible')
        prop4.text = 'True'
        properties.append(prop4)
        prop5 = etree.Element('prop')
        prop5.set('name', 'ForeColor')
        prop5.text = '_3DText'
        properties.append(prop5)
        prop6 = etree.Element('prop')
        prop6.set('name', 'BackColor')
        prop6.text = '_3DFace'
        properties.append(prop6)
        prop7 = etree.Element('prop')
        prop7.set('name', 'TabOrder')
        prop7.text = '79'
        properties.append(prop7)
        prop8 = etree.Element('prop')
        prop8.set('name', 'BorderStyle')
        prop8.text = 'Normal'
        properties.append(prop8)
        prop9 = etree.Element('prop')
        prop9.set('name', 'Font')
        properties.append(prop9)
        inprop1 = etree.Element('prop')
        inprop1.set('name', 'ru_RU.utf8')
        inprop1.text = 'Arial,10,-1,5,50,0,0,0,0,0'
        inprop2 = etree.Element('prop')
        inprop2.set('name', 'en_US.utf8')
        inprop2.text = 'Arial,10,-1,5,50,0,0,0,0,0'
        prop9.append(inprop1)
        prop9.append(inprop2)
        prop10 = etree.Element('prop')
        prop10.set('name', 'Location')
        prop10.text = str(location1) + " " + str(location2)
        properties.append(prop10)
        prop11 = etree.Element('prop')
        prop11.set('name', 'Size')
        prop11.text = '48 95'
        properties.append(prop11)
        prop12 = etree.Element('prop')
        prop12.set('name', 'ObjectType')
        prop12.text = 'sw.ewo'
        properties.append(prop12)
        # Создание файла
        return root
    else:
        location1 = float(value[1]) - float(value[3])
        location2 = float(value[2]) - float(value[4])
        root = etree.Element('shape')  # создаю начала дерева
        root.set('shapeType', 'GENERIC')
        root.set('layerId', '0')
        root.set('Name', name)
        # root.append(etree.Element('root'))
        properties = etree.Element('properties')
        root.append(properties)
        prop = etree.Element('prop')
        prop.set('name', "serialId")
        prop.text = '1581'
        properties.append(prop)
        prop2 = etree.Element('prop')
        prop2.set('name', 'RefPoint')
        properties.append(prop2)
        prop3 = etree.Element('prop')
        prop3.set('name', 'Enable')
        prop3.text = 'True'
        properties.append(prop3)
        prop4 = etree.Element('prop')
        prop4.set('name', 'Visible')
        prop4.text = 'True'
        properties.append(prop4)
        prop5 = etree.Element('prop')
        prop5.set('name', 'ForeColor')
        prop5.text = '_3DText'
        properties.append(prop5)
        prop6 = etree.Element('prop')
        prop6.set('name', 'BackColor')
        prop6.text = '_3DFace'
        properties.append(prop6)
        prop7 = etree.Element('prop')
        prop7.set('name', 'TabOrder')
        prop7.text = '79'
        properties.append(prop7)
        prop8 = etree.Element('prop')
        prop8.set('name', 'BorderStyle')
        prop8.text = 'Normal'
        properties.append(prop8)
        prop9 = etree.Element('prop')
        prop9.set('name', 'Font')
        properties.append(prop9)
        inprop1 = etree.Element('prop')
        inprop1.set('name', 'ru_RU.utf8')
        inprop1.text = 'Arial,10,-1,5,50,0,0,0,0,0'
        inprop2 = etree.Element('prop')
        inprop2.set('name', 'en_US.utf8')
        inprop2.text = 'Arial,10,-1,5,50,0,0,0,0,0'
        prop9.append(inprop1)
        prop9.append(inprop2)
        prop10 = etree.Element('prop')
        prop10.set('name', 'Location')
        prop10.text = str(location1) + " " + str(location2)
        properties.append(prop10)
        prop11 = etree.Element('prop')
        prop11.set('name', 'Size')
        prop11.text = '153 93'
        properties.append(prop11)
        prop12 = etree.Element('prop')
        prop12.set('name', 'ObjectType')
        prop12.text = 'swv.ewo'
        properties.append(prop12)
        # Создание файла
        return root

read_xml()