import locale

from fpdf import FPDF
import urllib.request
import pandas as pd


locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')

url = 'https://docs.google.com/spreadsheets/d/1gLMD4knvGxssE9DDEq1rh-vpg2xeFFamyWgwV3lpovI/edit?usp=sharing'
name_excel = 'Catalogo Shainy.xlsx'
urllib.request.urlretrieve(url, name_excel)

class crearPdf():
    #scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

    pdf = FPDF(orientation='P', unit='mm', format=(216, 330))
    pdf.set_auto_page_break(auto=True, margin=5)
    pdf.add_page()
    pdf.image('C:/Users/ander/Downloads/fondo.png', x=0, y=0, w=216, h=330)
    pdf.add_font(family='MilkyNice-Clean', fname='C:/Users/ander/Proyectos/Catalogo Shainy/fuentes/MilkyNice-Clean.ttf', uni=True)
    pdf.set_font('MilkyNice-Clean', size=40)
    pdf.cell(216, 10, txt='SHAINY STORE', ln=1, align='C')
    df = pd.read_excel('C:/Users/ander/Desktop/Catalogo Shainy.xlsx')
    df = df.sort_values('categoria')

    contador = 1

    for index, row in df.iterrows():


        producto = row['producto']
        precio = row['precio']
        precio_formateado = locale.format_string('%d', precio, grouping=True)
        descripcion = row['descripcion']

        if contador == 1:
            #producto1
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

        if contador == 2:
            #producto 2
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

        if contador ==3:
            #producto 3
            pdf.image('C:/Users/ander/Proyectos/Catalogo Shainy/Imagenes/pngwing.com (2).png', x=40, y=260, w=50, h=50)
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


    '''credentials = ServiceAccountCredentials.from_json_keyfile_name('shainy-db-743877467d34.json', scope)
    client = gspread.authorize(credentials)
    spreadsheet = client.open('Catalogo Shainy')
    sheet = spreadsheet.worksheet('Hoja 1')
    values = sheet.get_all_records()'''

    '''pdf.image('C:/Users/ander/Downloads/fondo.png', x=0, y=0, w=216, h=330)
            pdf.image('C:/Users/ander/Proyectos/Catalogo Shainy/Imagenes/pngwing.com (2).png', x=bloque1[0], y=bloque1[0], w=50, h=50)
            pdf.set_font('MilkyNice-Clean', size=20)
            pdf.set_xy(bloque1[0], bloque1[1])
            pdf.cell(10, 10, txt=producto, ln=1, align='L')
            pdf.set_font('MilkyNice-Clean', size=14)
            pdf.set_xy(bloque1[2], bloque1[3])
            pdf.multi_cell(60, 5, txt=descripcion, align='C')
            pdf.set_font('MilkyNice-Clean', size=20)
            pdf.set_xy(40, -15)
            pdf.cell(50, 10, txt=f"${precio_formateado}", ln=1, align='C')
            pdf.set_draw_color(255, 153, 153)
            pdf.set_line_width(0.5)
            pdf.line(18.6, bloque1[4], 200, bloque1[4])'''

    pdf.output('output.pdf')
