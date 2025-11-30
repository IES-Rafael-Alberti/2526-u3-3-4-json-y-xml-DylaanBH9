import json
import xml.etree.ElementTree as ET

def cargar_json(nombre_fichero: str):
    try:
        with open(nombre_fichero, "r") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        print(f"*ERROR* El archivo {nombre_fichero} no existe.")

    except json.JSONDecodeError:
        print("*ERROR* El archivo JSON tiene un formato incorrecto.")

    except Exception as e:
        print(f"*ERROR* Problemas al cargar los datos {e}.")

    return None

def guardar_xml(arbol):
    try:
        arbol.write("otros/datos_usuarios_convertido.xml")
        print(f"Archivo XML guardado correctamente en: 'otros/datos_usuarios_convertido.xml'")
        return True

    except FileNotFoundError:
        print(f"*ERROR* La ruta especificada 'otros/datos_usuarios_convertido.xml' no existe (quizás la carpeta no existe).")

    except PermissionError:
        print(f"*ERROR* No tienes permisos para escribir en el archivo 'otros/datos_usuarios_convertido.xml'.")

    except Exception as e:
        print(f"*ERROR* Problemas al guardar el archivo XML: {e}")

    return False

def convertir_estructura_dict_a_xml(datos: dict):
    raiz = ET.Element("usuarios")

    lista_usuarios = datos.get("usuarios", [])

    for usuario_dic in lista_usuarios:
        
        usuario_xml = ET.SubElement(raiz, "usuario")

        ET.SubElement(usuario_xml, "id").text = str(usuario_dic.get("id", ""))
        ET.SubElement(usuario_xml, "nombre").text = usuario_dic.get("nombre", "")
        ET.SubElement(usuario_xml, "edad").text = str(usuario_dic.get("edad", ""))

    return ET.ElementTree(raiz)

def main():
    nombre_fichero = "otros/datos_usuarios_orig.json"

    print(f"Iniciando conversión de {nombre_fichero} a XML.")

    datos = cargar_json(nombre_fichero)

    if datos is not None:
        arbol_xml = convertir_estructura_dict_a_xml(datos)

        guardar_xml(arbol_xml)
    else:
        print("No se pudo realizar la conversión porque falló la carga del JSON.")

if __name__ == "__main__":
    main()