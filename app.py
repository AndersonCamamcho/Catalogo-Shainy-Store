


import PyPDF2

def cambiar_orden_paginas(ruta_archivo_original, output_path):
    with open(ruta_archivo_original, 'rb') as input_file, open(output_path, 'wb') as output_file:
        reader = PyPDF2.PdfReader(input_file)
        writer = PyPDF2.PdfWriter()

        # Agregar la última página primero
        last_page = reader.pages[-1]
        writer.add_page(last_page)

        # Agregar las páginas restantes en el orden original
        for page in reader.pages[:-1]:
            writer.add_page(page)

        writer.write(output_file)

