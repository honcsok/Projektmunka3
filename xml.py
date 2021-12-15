import xml.etree.ElementTree as et
import pandavro as pdx
import pandas as pd

def readxml(path):
    tree = et.parse(path)
    root = tree.getroot()
    data = {}
    i = 0
    for child in root:
        data[i] = []
        for ch in child:
            data[i].append(ch.text)
        i+=1
    return data
dictData = readxml(r"D:\\Desktop\\Szakirany\adat.xml")

OUTPUT_PATH = "D:\\Desktop\\Szakirany\example.avro"
pdx.to_avro(OUTPUT_PATH, pd.DataFrame.from_dict(dictData[0]))
saved = pdx.read_avro(OUTPUT_PATH)
print(saved)
