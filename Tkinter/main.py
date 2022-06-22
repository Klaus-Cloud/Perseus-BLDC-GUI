import tkinter
from functions import *
from PIL import Image, ImageTk
import json
STANDARD_FONT = ("Arial", 10)
mainRow = 0
mainColumn = 0
GREY = "#EEEDDE"
# ---------------------------- Window Definition ------------------------------- #
window = tkinter.Tk()
window.title("BLDC Software")
window.wm_minsize(width=500, height=500)
window.config(padx=50, pady=50)

canvas1 = tkinter.Canvas(width=100, height=100, highlightthickness=0, bg=GREY)
engine_image = Image.open("Engine.png")
engine_image_resized = engine_image.resize((100, 100))
image1 = ImageTk.PhotoImage(engine_image_resized)
canvas1.create_image(50, 50, image=image1)
canvas1.grid(column=mainColumn + 2, row=mainRow)

canvas2 = tkinter.Canvas(width=100, height=100, highlightthickness=0, bg=GREY)
wr_image = Image.open("WR.png")
wr_image_resized = wr_image.resize((100, 100))
image2 = ImageTk.PhotoImage(wr_image_resized)
canvas2.create_image(50, 50, image=image2)
canvas2.grid(column=mainColumn + 4, row=mainRow + 12)
# ---------------------------- Labels ------------------------------- #

# Descriptive Labels
position_lists = [["toInput", "AWG:", STANDARD_FONT, mainColumn, mainRow + 1],
                  ["toInput", "Corrente(A):", STANDARD_FONT, mainColumn, mainRow + 2],
                  ["toInput", "ke:", STANDARD_FONT, mainColumn, mainRow + 3],
                  ["toCheckBox", "Usar valor anterior", ("Arial", 7), mainColumn + 1, mainRow + 4],
                  ["toInput", "Medidas(mm):", STANDARD_FONT, mainColumn, mainRow + 5],
                  ["toCheckBox", "Usar medidas anteriores", ("Arial", 7), mainColumn + 1, mainRow + 6],
                  ["toInput", "a:", STANDARD_FONT, mainColumn, mainRow + 7],
                  ["toInput", "b:", STANDARD_FONT, mainColumn, mainRow + 8],
                  ["toInput", "c:", STANDARD_FONT, mainColumn, mainRow + 9],
                  ["toInput", "d:", STANDARD_FONT, mainColumn, mainRow + 10],
                  ["toInput", "e:", STANDARD_FONT, mainColumn, mainRow + 11],
                  ["toInput", "Torque desejado:", STANDARD_FONT, mainColumn + 3, mainRow + 2],
                  ["toAnswer", "Número de fios em paralelo:", STANDARD_FONT, mainColumn + 3, mainRow + 6],
                  ["toAnswer", "Número de voltas por slot:", STANDARD_FONT, mainColumn + 3, mainRow + 7],
                  ["toAnswer", "Comprimento do fio(m):", STANDARD_FONT, mainColumn + 3, mainRow + 8],
                  ]

descriptive_labels_list = [create_descriptive_label(position_list) for position_list in position_lists]

# Answer Labels
answer_label_list = [create_answer_label(descriptive_label) for descriptive_label in descriptive_labels_list if
                     descriptive_label.model == "toAnswer"]

# ---------------------------- Inputs ------------------------------- #
input_list = [create_input(descriptive_label) for descriptive_label in descriptive_labels_list if
              descriptive_label.model == "toInput"]

# ---------------------------- Buttons ------------------------------- #
solution_button = tkinter.Button(text="Solução!")
solution_button.grid(column=mainColumn + 3, row=mainRow + 4)

# ---------------------------- CheckBoxes ------------------------------- #
check_box_list = [create_check_boxes(descriptive_label) for descriptive_label in descriptive_labels_list if
                  descriptive_label.model == "toCheckBox"]


# ---------------------------- Data files ------------------------------- #
with open("tabelaAWG.json", 'r') as file:
    # Writing New file
    file_data= json.load(file)
file_data_dict = json.loads(file_data)
k_e_motor = 0.002007 # Valor medido no laboratório


# ---------------------------- Start the program ------------------------------ #
window.mainloop()
