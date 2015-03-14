from lxml import etree


class Panel():
    def __init__(self, filename='newPanel.xml'):
        self.filename = filename
        self.tree = etree.parse(filename)
        self.key = ""
        self.elements = []
        self.root = self.tree.getroot()

    def __len__(self):
        if len(self.elements) != 0:
            return len(self.elements)
        else:
            self.set_elements()
            return len(self.elements)


    def set_key(self, key=''):
        if len(key) != 0:
            self.key = key
        else:
            self.key = 'TN_elems/Valve.pnl'  #change this

    def get_elements(self):
        for prop in self.root.findall("shapes/reference//prop/[@name='FileName']"):  #find all elements with key
            text = prop.text
            if text == self.key:
                yield prop

    def set_elements(self):
        for i in self.get_elements():
            self.elements.append(i)

    def change_elements_to(self, newKey="NewKey"):
        for i in self.get_elements():
            shapes = self.root.index(i.getparent().getparent().getparent())
            first_index = self.root[shapes].index(i.getparent().getparent())
            self.root[shapes][first_index][0][0].text = newKey

    def save_new_file(self):
        et = etree.ElementTree(self.root)
        et.write('New'+self.filename, pretty_print=True, xml_declaration=True, encoding='UTF-8')

if __name__ == '__main__':
    mypanel = Panel()
    mypanel.set_key()
    print(mypanel.key)
    mypanel.set_elements()
    print(mypanel.elements)
    print(len(mypanel))
    mypanel.change_elements_to()
    dd = Panel("LU_Kovali.xml")
    dd.set_key()
    print(dd.key)
    print(len(dd))
    dd.change_elements_to("TN_elems/KP_bar.pnl")
    dd.save_new_file()
