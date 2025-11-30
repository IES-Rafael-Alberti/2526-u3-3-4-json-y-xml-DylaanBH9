import json
import xml.etree.ElementTree as ET

def cargar_xml(nombre_fichero: str):
    try:
        return ET.parse(nombre_fichero)

    except FileNotFoundError:
        print(f"*ERROR* El archivo {nombre_fichero} no existe.")

    except ET.ParseError:
        print("*ERROR* El archivo XML tiene un formato incorrecto.")

    except Exception as e:
        print(f"*ERROR* Problemas al cargar el XML: {e}")

    return None

def convertir_estructura_xml_a_dict(raiz):
    lista_usuarios = []

    for usuario_xml in raiz.findall("usuario"):

        id = usuario_xml.find("id")
        nombre = usuario_xml.find("nombre")
        edad = usuario_xml.find("edad")

        datos_completos = id is not None and nombre is not None and edad is not None

        if datos_completos:
            usuario_dict = {
                "id": int(id.text),
                "nombre": nombre.text,
                "edad": int(edad.text)
            }
            lista_usuarios.append(usuario_dict)
        else:
            print("Usuario con datos incompletos encontrado en el XML.")

    return {"usuarios": lista_usuarios}

def guardar_json(datos: dict):
    try:
        with open("otros/datos_usuarios_convertido.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)
        print(f"Archivo JSON guardado correctamente en: {"otros/datos_usuarios_convertido.json"}")

    except FileNotFoundError:
        print(f"*ERROR* La ruta o carpeta para 'otros/datos_usuarios_convertido.json' no existe.")

    except PermissionError:
        print(f"*ERROR* No tienes permisos para escribir en el archivo 'otros/datos_usuarios_convertido.json'.")

    except Exception as e:
        print(f"*ERROR* Problemas al guardar los datos: {e}")

def main():
    nombre_fichero = "otros/datos_usuarios_orig.xml"

    print(f"Iniciando conversión de {nombre_fichero} a JSON.")

    arbol = cargar_xml(nombre_fichero)

    if arbol:
        raiz = arbol.getroot()

        datos_json = convertir_estructura_xml_a_dict(raiz)

        guardar_json(datos_json)
    else:
        print("No se pudo realizar la conversión porque falló la carga del XML.")

if __name__ == "__main__":
    main()