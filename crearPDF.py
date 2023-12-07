from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.graphics.barcode import code128
from PIL import Image
import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read())
        return encoded_image.decode("utf-8")

def create_pdf_with_image(file_path,  barcode_text, image_path):
    # Decodifica la imagen y guarda la imagen en un archivo temporal
    image_base64 = image_to_base64(image_path)

    # Crea un objeto canvas (lienzo) para dibujar en el PDF
    pdf_canvas = canvas.Canvas(file_path, pagesize=letter)

    #ñadd_header(pdf_canvas, "Encabezado del Documento")

    # Establece la fuente en negrita
    pdf_canvas.setFont("Times-Bold", 10)  
    pdf_canvas.drawString(50, 700, "Fecha :")
    pdf_canvas.setFont("Times-Roman", 10)  
    pdf_canvas.drawString(150, 700, "MARTES, 05 DE DICIEMBRE DE 2023")

    pdf_canvas.setFont("Times-Bold", 10)  
    pdf_canvas.drawString(50, 680, "Paciente : ")
    pdf_canvas.setFont("Times-Roman", 10) 
    pdf_canvas.drawString(150, 680, "DULCE MARIA DE LA PAZ PATERNO 3 MATERNO 3")

    pdf_canvas.setFont("Times-Bold", 10)  
    pdf_canvas.drawString(50, 660, "Edad :")

    pdf_canvas.setFont("Times-Roman", 10)  
    pdf_canvas.drawString(150, 660, "40 AÑOS")

    pdf_canvas.setFont("Times-Bold", 10)  
    pdf_canvas.drawString(400, 660, "Fecha de Nacimiento : ")
    

    pdf_canvas.setFont("Times-Roman", 10)  
    pdf_canvas.drawString(500, 660, "24/ENE./1983 ")

    pdf_canvas.setFont("Times-Bold", 10)  
    pdf_canvas.drawString(50, 640, "Sexo :")

    pdf_canvas.setFont("Times-Roman", 10)  
    pdf_canvas.drawString(150, 640, "FEMENINO")

    pdf_canvas.setFont("Times-Bold", 10)  
    pdf_canvas.drawString(400, 640, "Médico solicitante : ")

    pdf_canvas.setFont("Times-Roman", 10)  
    pdf_canvas.drawString(500, 640, "AQC ")

    pdf_canvas.setFont("Times-Bold", 10)  
    pdf_canvas.drawString(50, 620, "Sucursal :")

    pdf_canvas.setFont("Times-Roman", 10) 
    pdf_canvas.drawString(150, 620, "AV DR RUPERTO PALIZA 87, PRIMER CUADRO")

    pdf_canvas.setFont("Times-Bold", 10)  
    pdf_canvas.drawString(50, 600, "Nombre del estudio :")

    pdf_canvas.setFont("Times-Roman", 10) 
    pdf_canvas.drawString(150, 600, "DENSITOMETRIA OSEA DE COLUMNA Y FEMUR")

   
    draw_underlined_text(pdf_canvas, 50, 570, "Indicación del estudio")


    draw_underlined_text(pdf_canvas, 50, 540, "Técnica:")
    text_to_wrap = "Se realizó estudio ultrasonográfico vía abdominal con transductor convexo multifrecuencia de alta resolución en tiempo real observando lo siguiente:"
    draw_wrapped_text(pdf_canvas, 90, 540, text_to_wrap, max_width=450)

    draw_underlined_text(pdf_canvas, 50, 510, "Hallazgos:")

    pdf_canvas.setFont("Times-Bold", 10)  
    pdf_canvas.drawString(50, 490, "Vejiga urinaria")

    text_to_wrap = "se evalúa con repleción adecuada al momento del estudio. Muestra forma, contornos y patrón ecográfico normales. Pared delgada, de ___ mm de espesor, sin lesiones murales.  Anecogénica en su interior."
    draw_wrapped_text(pdf_canvas, 120, 490, text_to_wrap, max_width=450)
    

    pdf_canvas.setFont("Times-Bold", 10)  
    pdf_canvas.drawString(50, 460, "Evaluación dinámica:")


    pdf_canvas.setFont("Times-Roman", 10) 
    pdf_canvas.drawString(80, 440, "•      Volumen en fase de llenado de ___ cc")
    pdf_canvas.drawString(80, 430, "•      Volumen postmiccional: ___ cc")
    pdf_canvas.drawString(80, 420, "•      Porcentaje de orina residual postmiccional: ___ %")

    pdf_canvas.setFont("Times-Bold", 10)  
    pdf_canvas.drawString(50, 400, "Próstata")
    
    text_to_wrap = "de  localización,  forma,  contornos  y  patrón  ecográfico  normales,  mide ___ mm  en  su  diámetro  longitudinal,  anteroposterior y transversal respectivamente, con un volumen estimado de ___ cc. Protrusión prostática intravesical de ___ mm, grado ___."
    draw_wrapped_text(pdf_canvas, 90, 400, text_to_wrap, max_width=450)

    pdf_canvas.setFont("Times-Bold", 10)  
    pdf_canvas.drawString(50, 350, " Vesículas seminales")
   
    pdf_canvas.setFont("Times-Roman", 10) 
    pdf_canvas.drawString(140, 350, "simétricas, con aspecto ecográfico homogéneo.")


    pdf_canvas.setFont("Times-Bold", 10)  
    pdf_canvas.drawString(50, 340, " Riñones:")
   
    pdf_canvas.setFont("Times-Roman", 10) 
    pdf_canvas.drawString(93, 340, "dentro de lo valorado, no identifico dilatación del sistema colector.")
   
    draw_underlined_text(pdf_canvas, 50, 320, "Correlación con estudios previos:")
    pdf_canvas.setFont("Times-Roman", 10) 
    pdf_canvas.drawString(50, 310, "No se cuenta con estudios ecográficos previos para correlacionar.")

    draw_underlined_text(pdf_canvas, 50, 280, "Conclusión:")

    pdf_canvas.setFont("Times-Roman", 10) 
    pdf_canvas.drawString(50, 270, "Próstata con volumen aproximado de ___ mm y patrón ecográfico homogéneo")
    pdf_canvas.drawString(50, 260, "Protrusión prostática intravesical de ___ mm, grado ___.")
    pdf_canvas.drawString(50, 250, "Orina residual de ___ % en el estudio postmiccional inmediato.")


    draw_underlined_text(pdf_canvas, 50, 230, "Sugerencia: ")
    pdf_canvas.setFont("Times-Roman", 10) 
    pdf_canvas.drawString(50, 220, "Valoración por médico tratante.")


    pdf_canvas.setFont("Times-Bold", 10)  
    pdf_canvas.drawString(250, 150, "ATENTAMENTE:")
    pdf_canvas.drawString(210, 115, "ROSA IMELDA FLORES ONTIVEROS ")
    pdf_canvas.drawString(205, 100, "UNIVERSIDAD AUTÓNOMA DE SINALOA ")
    pdf_canvas.drawString(250, 85,  "CED.PROF. 4247840")
    pdf_canvas.drawString(240, 70,  "ULTRASONOGRAFISTA  ")






  
    # Crea un objeto Code128 para el código de barras
    barcode = code128.Code128(barcode_text)
    pdf_canvas.drawString(425, 693, f"{barcode_text}")
    # Dibuja el código de barras en el PDF
    barcode.drawOn(pdf_canvas, 400, 700)  # Cambia las coordenadas según tus necesidades



    #add_footer(pdf_canvas, "Pie de Pagina")
    ruta_firma = "C:\\PdfPython\\Imagenes\\firma.jpg"
    # Agrega la imagen al PDF
    image = ImageReader(ruta_firma)
    pdf_canvas.drawImage(image, 260, 125, width=50, height=25)  # Ajusta las coordenadas y el tamaño según tus necesidades

   

    # Guarda el PDF
    pdf_canvas.save()



def draw_wrapped_text(canvas, x, y, text, max_width, font_name="Times-Roman", font_size=10):
    # Establece la fuente y tamaño del texto
    canvas.setFont(font_name, font_size)

    # Divide el texto en palabras
    words = text.split()

    # Inicializa la línea de texto
    line = ""

    # Itera sobre las palabras y agrega a la línea hasta alcanzar el ancho máximo
    for word in words:
        if canvas.stringWidth(line + word, font_name, font_size) < max_width:
            line += word + " "
        else:
            # Dibuja la línea actual y reinicia para la siguiente línea
            canvas.drawString(x, y, line.strip())
            y -= font_size * 1.2  # Puedes ajustar el espaciado entre líneas según tus necesidades
            line = word + " "

    # Dibuja la última línea
    canvas.drawString(x, y, line.strip())
def draw_underlined_text(canvas, x, y, text, font_name="Times-Bold", font_size=10):
    # Establece la fuente y tamaño del texto
    canvas.setFont(font_name, font_size)

    # Dibuja el texto
    canvas.drawString(x, y, text)

    # Calcula la longitud del texto en el lienzo
    text_width = canvas.stringWidth(text, font_name, font_size)

    # Dibuja una línea debajo del texto para simular el subrayado
    canvas.line(x, y - 2, x + text_width, y - 2)
def add_header(canvas, text):
    # Establece la fuente y tamaño del encabezado
    canvas.setFont("Times-Bold", 12)

    # Alinea el texto al centro
    width, height = letter
    text_width = canvas.stringWidth(text, "Times-Bold", 12)
    x = (width - text_width) / 2

    # Agrega el encabezado en la parte superior de la página
    canvas.drawString(x, height - 20, text)

def add_footer(canvas, text):
    # Establece la fuente y tamaño del pie de página
    canvas.setFont("Times-Roman", 10)  # Puedes cambiar la fuente y el tamaño según tus necesidades

    # Alinea el texto al centro
    width, height = letter
    text_width = canvas.stringWidth(text, "Times-Roman", 10)
    x = (width - text_width) / 2

    # Agrega el texto del pie de página
    page_number = canvas.getPageNumber()
    footer_text = f"{text} - Página {page_number}"

    # Agrega el pie de página en la parte inferior de la página
    canvas.drawString(x, 50, footer_text)

if __name__ == "__main__":
    # Especifica la ruta del archivo PDF que quieres crear
    pdf_path = "documento_con_imagen.pdf"

    # Texto para el código de barras
    texto_codigo_barras = "*RSV123456789*"

    # Ruta de la imagen
    ruta_imagen = "C:\\PdfPython\\Imagenes\\Spearker.png"
    


    # Llama a la función para crear el PDF con texto, código de barras e imagen
    create_pdf_with_image(pdf_path, texto_codigo_barras, ruta_imagen)

    print(f"Se ha creado el archivo PDF con imagen en el pie de página en: {pdf_path}")
