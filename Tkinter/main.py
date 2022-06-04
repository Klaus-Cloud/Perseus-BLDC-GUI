import tkinter

STANDARD_FONT = ("Arial", 10)

# Functions


# Window Definition
window = tkinter.Tk()
window.title("BLDC Software")
window.wm_minsize(width=500, height=500)
window.config(padx=50, pady=50)

# # Labels
mainRow = 0
mainColumn = 0
# Descriptive Labels
position_lists = [["toInput", "AWG:",                        STANDARD_FONT, mainColumn, mainRow + 1],
                  ["toInput", "Corrente(A):",                STANDARD_FONT, mainColumn, mainRow + 2],
                  ["toInput", "ke:",                         STANDARD_FONT, mainColumn, mainRow + 3],
                  ["toCheckBox", "Usar valor anterior",      ("Arial", 7), mainColumn + 1, mainRow + 4],
                  ["toInput", "Medidas(mm):",                STANDARD_FONT, mainColumn, mainRow + 5],
                  ["toCheckBox", "Usar medidas anteriores",  ("Arial", 7),  mainColumn + 1, mainRow + 6],
                  ["toInput", "a:",                          STANDARD_FONT, mainColumn, mainRow + 7],
                  ["toInput", "b:",                          STANDARD_FONT, mainColumn, mainRow + 8],
                  ["toInput", "c:",                          STANDARD_FONT, mainColumn, mainRow + 9],
                  ["toInput", "d:",                          STANDARD_FONT, mainColumn, mainRow + 10],
                  ["toInput", "e:",                          STANDARD_FONT, mainColumn, mainRow + 11],
                  ["toInput", "Torque desejado:",            STANDARD_FONT, mainColumn+2, mainRow + 2],
                  ["toAnswer", "Número de fios em paralelo:", STANDARD_FONT, mainColumn+2, mainRow + 6],
                  ["toAnswer", "Número de voltas por slot:",  STANDARD_FONT, mainColumn+2, mainRow + 7],
                  ["toAnswer", "Comprimento do fio(m):",      STANDARD_FONT, mainColumn+2, mainRow + 8],
                  ]
descriptive_labels_list = []


def create_descriptive_label(list):
    model = list[0]
    label_text = list[1]
    label_font = list[2]
    label_column = list[3]
    label_row = list[4]
    newLabel = tkinter.Label(text=label_text, font=label_font)
    newLabel.model = model
    newLabel.grid(column=label_column, row=label_row)
    descriptive_labels_list.append(newLabel)


for position_list in position_lists:
    create_descriptive_label(position_list)

# Inputs


def create_input(descriptive_label):
    pass


input_list = [create_input(descriptive_label) for descriptive_label in descriptive_labels_list if descriptive_label.model =="toInput"]


# Buttons


# Start the program
window.mainloop()
