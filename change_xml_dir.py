from lxml import etree
import os


def change_dir(file, change_path):
    tree = etree.parse(file)
    root = tree.getroot()
    root.find('path').text = change_path
    tree.write(file)


def init(base_path):
    xml_path = os.path.join(base_path, 'annotations')
    img_path = os.path.join(base_path, 'images')
    xmls = os.listdir(xml_path)
    for xml in xmls:
        change_dir(os.path.join(xml_path, xml), os.path.join(img_path, xml.replace('xml', 'jpg')))


if __name__ == '__main__':
    init(r'E:\opencv3\python3x\ship_training\ship\train')
    init(r'E:\opencv3\python3x\ship_training\ship\validation')
