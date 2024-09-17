from openpyxl.drawing.spreadsheet_drawing import AnchorMarker, TwoCellAnchor
import os
from openpyxl.drawing.image import Image as OpenPyXLImage
from io import BytesIO

def add_image_to_cell(sheet, image_data, col, row, col_span, row_span):
    # Cria uma imagem OpenPyXL a partir dos dados da imagem em memória (image_data)
    img = OpenPyXLImage(BytesIO(image_data))
    
    offset = 30000  # Ajuste para o posicionamento da imagem
    _from = AnchorMarker(col=col, row=row, colOff=offset, rowOff=offset)
    to = AnchorMarker(col=col + col_span, row=row + row_span, colOff=-offset, rowOff=-offset)

    # Define a ancoragem da imagem
    img.anchor = TwoCellAnchor(editAs="twoCell", _from=_from, to=to)

    # Adiciona a imagem à planilha
    sheet.add_image(img)

# Exemplo de como usar:
# add_image_to_cell(sheet, img_data, col=2, row=2, col_span=2, row_span=2)
