from PIL import Image
import os

downloads_folder = "/Users/mac/Downloads"
folder_pictures = "/Users/mac/Pictures"

if __name__ == "__main__":
    for filname in os.listdir(downloads_folder):

        # Comprueba si el archivo es un archivo regular
        if os.path.isfile(os.path.join(downloads_folder, filname)):

            # Divide el nombre del archivo en el nombre del archivo y la extensión
            name, extension = os.path.splitext(
                os.path.join(downloads_folder, filname))

            # Comprueba si la extensión del archivo es una de las siguientes: .png, .jpg o .jpeg
            if extension in [".png", ".jpg", ".jpeg", ".PNG"]:

                # Abre el archivo de imagen
                with Image.open(os.path.join(downloads_folder, filname)) as picture:

                    # Guarda la imagen comprimida en la carpeta Descargas con el nombre `compressed__` prefijado
                    picture.save(os.path.join(
                        folder_pictures, "compressed__" + filname), optimize=True, quality=60)

                    # Elimina el archivo original
                    os.remove(os.path.join(downloads_folder, filname))


    
