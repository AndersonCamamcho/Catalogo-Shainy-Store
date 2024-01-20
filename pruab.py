import locale
from fpdf import FPDF
import urllib.request
import pandas as pd

locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')

url = 'https://docs.google.com/spreadsheets/d/1gLMD4knvGxssE9DDEq1rh-vpg2xeFFamyWgwV3lpovI/edit#gid=0'
name_excel = 'Catalogo Shainy.xlsx'
urllib.request.urlretrieve(url, name_excel)
contador = 1
n_pagi = 0

class crearPdf():
    pdf = FPDF(orientation='P', unit='mm', format=(216, 330))
    pdf.set_auto_page_break(auto=True, margin=5)
    pdf.add_page()
    pdf.image('C:/Users/ander/Downloads/fondo.png', x=0, y=0, w=216, h=330)
    pdf.add_font(family='MilkyNice-Clean', fname='C:/Users/ander/Proyectos/Catalogo Shainy/fuentes/MilkyNice-Clean.ttf', uni=True)
    pdf.set_font('MilkyNice-Clean', size=40)
    pdf.cell(216, 10, txt='SHAINY STORE', ln=1, align='C')
    df = pd.read_excel('C:/Users/ander/Desktop/Catalogo Shainy.xlsx')
    df = df.sort_values(['categoria', 'producto'])

    categorias = df['categoria'].unique()

    for categoria in categorias:
        pdf.add_page()
        pdf.image('C:/Users/ander/Proyectos/Catalogo Shainy/Imagenes/a.png', x=0, y=0, w=216, h=330)
        pdf.set_font('MilkyNice-Clean', size=40)
        pdf.set_xy(105, 130)
        pdf.set_font('MilkyNice-Clean', size=60)
        pdf.set_text_color(249, 232, 232)
        pdf.cell(10, 10, txt=categoria, ln=1, align='C')
        pdf.set_text_color(0, 0, 0)


        productos_categoria = df[df['categoria'] == categoria]

        contador = 1

        for index, row in productos_categoria.iterrows():
            producto = row['producto']
            precio = row['precio']
            precio_formateado = locale.format_string('%d', precio, grouping=True)
            descripcion = row['descripcion']


            if contador == 1:
                pdf.add_page()
                pdf.image('C:/Users/ander/Downloads/fondo.png', x=0, y=0, w=216, h=330)
                pdf.image('C:/Users/ander/Proyectos/Catalogo Shainy/Imagenes/pngwing.com.png', x=40, y=40, w=50, h=50)
                pdf.set_font('MilkyNice-Clean', size=20)
                pdf.set_xy(20, 20)
                pdf.cell(10, 10, txt=producto, ln=1, align='L')
                pdf.set_xy(40, 90)
                pdf.cell(50, 10, txt=f"${precio_formateado}", ln=1, align='C')
                pdf.set_font('MilkyNice-Clean', size=14)
                pdf.set_xy(100, 50)
                pdf.multi_cell(60, 5, txt=descripcion, align='C')
                pdf.set_draw_color(255, 153, 153)
                pdf.set_line_width(0.5)
                pdf.line(18.6, 110, 200, 110)
                pdf.set_xy(210, 320)
                #n_pagi += 1
                pdf.cell(60, 5, txt=f'pag.{n_pagi}', align='C')

            elif contador == 2:
                pdf.image('C:/Users/ander/Proyectos/Catalogo Shainy/Imagenes/pngwing.com (1).png', x=125, y=150, w=60, h=60)
                pdf.set_font('MilkyNice-Clean', size=20)
                pdf.set_xy(180, 120)
                pdf.cell(10, 10, txt=producto, ln=1, align='R')
                pdf.set_xy(130, 200)
                pdf.cell(50, 10, txt=f"${precio_formateado}", ln=1, align='C')
                pdf.set_font('MilkyNice-Clean', size=14)
                pdf.set_xy(30, 170)
                pdf.multi_cell(60, 5, txt=descripcion, align='C')
                pdf.line(18.6, 220, 200, 220)

            elif contador == 3:
                pdf.image('C:/Users/ander/Proyectos/Catalogo Shainy/Imagenes/pngwing.com (2).png', x=40, y=260, w=50,h=50)
                pdf.set_font('MilkyNice-Clean', size=20)
                pdf.set_xy(18, 225)
                pdf.cell(10, 10, txt=producto, ln=1, align='L')
                pdf.set_font('MilkyNice-Clean', size=14)
                pdf.set_xy(100, 280)
                pdf.multi_cell(60, 5, txt=descripcion, align='C')
                pdf.set_font('MilkyNice-Clean', size=20)
                pdf.set_xy(40, -15)
                pdf.cell(50, 10, txt=f"${precio_formateado}", ln=1, align='C')

            contador += 1
            if contador > 3:
                contador = 1

    pdf.output('output.pdf')
