import xml.etree.ElementTree as ET
import csv


def xml_to_csv(xml_file, csv_file):
    # Definir los espacios de nombres
    namespaces = {  # Cambia este URI según tu XML
        'cfdi': 'http://www.sat.gob.mx/cfd/4'  # Cambia este URI según tu XML
    }
    
    # Cargar y parsear el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Crear y abrir el archivo CSV
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Escribir los encabezados en el archivo CSV
        headers = ["Parte", "Cantidad", "Descripcion", "Costo"]  # Cambia estos nombres según la estructura de tu XML
        writer.writerow(headers)
        
        # Extraer información y escribir cada fila en el CSV
        for conceptos in root.findall('.//cfdi:Conceptos', namespaces):
            for concepto in conceptos.findall('.//cfdi:Concepto', namespaces):
                parte = concepto.get('NoIdentificacion', '')
                cantidad = float(concepto.get('Cantidad', ''))
                descripcion = concepto.get('Descripcion', '')
                costo = float(concepto.get('ValorUnitario', ''))
                writer.writerow([parte, cantidad, descripcion, costo])


if __name__ == '__main__':
    xml_to_csv('GE136232.xml', 'GE136232.csv')
    xml_to_csv("CFD303192.xml", "CFD303192.csv")
