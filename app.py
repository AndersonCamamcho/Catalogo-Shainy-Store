import PyPDF2

def cambiar_orden_paginas(input_path, output_path, posicion_deseada):
    with open(input_path, 'rb') as file:
        pdf_merger = PyPDF2.PdfMerger()
        pdf_merger.append(file)

        # Obtener la última página
        last_page = pdf_merger.pages[-1]

        # Insertar la última página en la posición deseada
        pdf_merger.pages.insert(posicion_deseada, last_page)

        # Guardar el nuevo PDF
        with open(output_path, 'wb') as new_file:
            pdf_merger.write(new_file)
