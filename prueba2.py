import locale
import gspread
from fpdf import FPDF
from PIL import Image
import requests
import pandas as pd
from rembg import remove
import re
from oauth2client.service_account import ServiceAccountCredentials
from app import cambiar_orden_paginas
from descargarImagenes import descargar_imagen

urls_imagenes = [
    'https://www.canva.com/design/DAF6WeNQNQg/Mulc3tZpdR5ulTRt41H8Sw/watch',
    'https://www.canva.com/design/DAF6WeNQNQg/Mulc3tZpdR5ulTRt41H8Sw/watch',
    'https://www.canva.com/design/DAF6WeNQNQg/Mulc3tZpdR5ulTRt41H8Sw/watch'
]
nombres_archivos = ['categoria.jpg', 'portada.jpg', 'cuerpo.jpg']
for url, nombre_archivo in zip(urls_imagenes, nombres_archivos):
    descargar_imagen(url, nombre_archivo)

locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('shainy-store-db-815beb877278.json', scope)
client = gspread.authorize(credentials)
spreadsheet = client.open('Catalogo Shainy')
sheet = spreadsheet.worksheet('Hoja 1')
values = sheet.get_all_records()
df = pd.DataFrame(values)
df = df.sort_values(['categoria', 'producto'])
contador = 1
n_pagi = 0
id_image = 1
indice = {}
ejey = 80


class crearPdf(FPDF):
    # @staticmethod
    def quitar_fondo(imagen_url, QuitarFondo):
        if QuitarFondo == 1:
            imagen = Image.open(requests.get(imagen_url, stream=True).raw)
            sin_fondo = remove(imagen)
            imagen_url_limpio = re.sub(r'[\/:*?"<>|]', '_', imagen_url)
            nombre_archivo = f"{imagen_url_limpio}.png"
            sin_fondo.save(nombre_archivo)
            return nombre_archivo
        else:
            imagen = Image.open(requests.get(imagen_url, stream=True).raw)
            imagen_url_limpio = re.sub(r'[\/:*?"<>|]', '_', imagen_url)
            nombre_archivo = f"{imagen_url_limpio}.png"
            imagen.save(nombre_archivo)
            return nombre_archivo

    # Portada/indice
    pdf = FPDF(orientation='P', unit='mm', format=(216, 330))
    pdf.set_auto_page_break(auto=True, margin=5)
    pdf.add_font(family='MilkyNice-Clean', fname='C:/Users/ander/Proyectos/Catalogo Shainy/fuentes/MilkyNice-Clean.ttf')

    categorias = df['categoria'].unique()

    for categoria in categorias:
        pdf.add_page()
        pdf.image('C:/Users/ander/Proyectos/Catalogo Shainy/Imagenes/a.png', x=0, y=0, w=216, h=330)
        pdf.set_xy(105, 130)
        pdf.set_font('MilkyNice-Clean', size=75)
        pdf.set_text_color(249, 232, 232)
        pdf.cell(10, 10, text=categoria, align='C')
        pdf.set_text_color(96, 96, 96)
        pdf.set_font('MilkyNice-Clean', size=14)
        pdf.set_xy(175, 320)
        n_pagi += 1
        pdf.cell(60, 5, text=f'pag.{n_pagi}', align='C')

        productos_categoria = df[df['categoria'] == categoria]
        indice[categoria] = n_pagi

        contador = 1

        for index, row in productos_categoria.iterrows():
            producto = row['producto']
            precio = row['precio']
            precio_formateado = locale.format_string('%d', precio, grouping=True)
            descripcion = row['descripcion']
            imagen_exc = row['img']
            val_fondo = row['QuitarFondo']

            imagen_procesada = quitar_fondo(imagen_exc, val_fondo)

            if contador == 1:
                pdf.add_page()
                pdf.image('C:/Users/ander/Downloads/fondo.png', x=0, y=0, w=216, h=330)
                pdf.image(imagen_procesada, x=35, y=35, w=60, h=60)
                pdf.set_font('MilkyNice-Clean', size=16)
                pdf.set_text_color(96, 96, 96)
                pdf.set_xy(20, 20)
                pdf.multi_cell(180, 8, text=producto, align='L')
                pdf.set_xy(40, 90)
                pdf.cell(50, 10, text=f"${precio_formateado}", align='C')
                pdf.set_font('MilkyNice-Clean', size=14)
                pdf.set_xy(100, 50)
                pdf.multi_cell(60, 5, text=descripcion, align='C')
                pdf.set_draw_color(255, 153, 153)
                pdf.set_line_width(0.5)
                pdf.set_xy(175, 320)
                n_pagi += 1
                pdf.cell(60, 5, text=f'pag.{n_pagi}', align='C')

            elif contador == 2:
                pdf.image(imagen_procesada, x=120, y=138, w=60, h=60)
                pdf.set_font('MilkyNice-Clean', size=16)
                pdf.set_xy(18, 120)
                pdf.multi_cell(180, 8, text=producto, align='L')
                pdf.set_xy(127, 200)
                pdf.cell(50, 10, text=f"${precio_formateado}", align='C')
                pdf.set_font('MilkyNice-Clean', size=14)
                pdf.set_xy(30, 170)
                pdf.multi_cell(60, 5, text=descripcion, align='C')

            elif contador == 3:
                pdf.image(imagen_procesada, x=35, y=255, w=60, h=60)
                pdf.set_font('MilkyNice-Clean', size=16)
                pdf.set_xy(18, 225)
                pdf.multi_cell(180, 8, text=producto, align='L')
                pdf.set_font('MilkyNice-Clean', size=14)
                pdf.set_xy(100, 280)
                pdf.multi_cell(60, 5, text=descripcion, align='C')
                pdf.set_font('MilkyNice-Clean', size=16)
                pdf.set_xy(40, -15)
                pdf.cell(50, 10, text=f"${precio_formateado}", align='C')

            contador += 1
            if contador > 3:
                contador = 1

    # *******************    portada/Indices     ********************
    pdf.add_page()
    pdf.image('C:/Users/ander/Proyectos/Catalogo Shainy/Imagenes/portada.png', x=0, y=0, w=216, h=330)
    pdf.set_font('MilkyNice-Clean', size=50)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 40)
    pdf.cell(216, 10, text='SHAINY STORE', align='C')
    pdf.set_xy(50, 185)
    pdf.set_font('MilkyNice-Clean', size=18)
    pdf.cell(0, 10, text='Distribuidores de TRENDY, ELAYA & ANI-K', align='L')
    pdf.set_xy(50, 201)
    pdf.cell(0, 10, text='instagram.com/shainy.store/', link="https://www.instagram.com/shainy.store/", align='L')
    pdf.set_xy(50, 219)
    pdf.cell(0, 10, text='300 9069301 ', link='wa.link/i9elhd', align='L')

    for categoria, num_pagina in indice.items():
        pdf.set_font('MilkyNice-Clean', size=18)
        link = pdf.add_link(page=num_pagina)
        pdf.set_xy(50, ejey)
        pdf.cell(0, 5, text=f'{categoria}', align='L', link=link)
        pdf.set_xy(0, ejey)
        pdf.cell(160, 5, text=f'............................. pag. {num_pagina}', align='R', link=link)
        ejey += 20

    pdf.output('output.pdf')

    cambiar_orden_paginas('output.pdf', 'catalogo shainy v1.pdf')
