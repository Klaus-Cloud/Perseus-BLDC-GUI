import tkinter

STANDARD_FONT = ("Arial", 10)


def create_descriptive_label(position_list):
    model = position_list[0]
    label_text = position_list[1]
    label_font = position_list[2]
    label_column = position_list[3]
    label_row = position_list[4]
    newLabel = tkinter.Label(text=label_text, font=label_font)
    newLabel.model = model
    newLabel.grid(column=label_column, row=label_row)
    return newLabel


def create_answer_label(descriptive_label):
    new_answer_label = tkinter.Label(text="", font=STANDARD_FONT)
    new_answer_label.grid(column=descriptive_label.grid_info()["column"] + 1, row=descriptive_label.grid_info()["row"])
    return new_answer_label


def create_input(descriptive_label):
    new_input = tkinter.Entry(width=15)
    new_input.grid(column=descriptive_label.grid_info()["column"] + 1, row=descriptive_label.grid_info()["row"])
    return new_input
