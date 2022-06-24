# ---------------------------- Functions ------------------------------ #
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
    new_input.name = descriptive_label.cget("text")
    return new_input


def create_check_boxes(descriptive_label):
    new_check_box = tkinter.Checkbutton()
    new_check_box.grid(column=descriptive_label.grid_info()["column"] - 1, row=descriptive_label.grid_info()["row"])
    return new_check_box


def check_box_clicked(k_e_check_box, input_list, k_e_motor, engine_dimensions_check_box):
    # ----------------------------- ke Value ------------------------------ #
    k_e_input_position = 0
    k_e_input_position_list = [list_position for list_position, input in enumerate(input_list) if
                               input.name == "ke:"]
    k_e_input_position = k_e_input_position_list[0]

    if k_e_check_box.get() == 1 and input_list[k_e_input_position].get() == "":
        input_list[k_e_input_position].insert(0, f"{k_e_motor}")
    elif k_e_check_box.get() == 0:
        input_list[k_e_input_position].delete(0,"end")

    # ----------------------------- Engine dimensions ------------------------------ #
    def empty_input():
        for input in input_list[4:8]:
            if input.get() != "":
                return False
            else:
                return True

    engine_dimensions_list_positions = [list_position for list_position, input in enumerate(input_list)
                                        if input.name in ["a:","b:","c:","d:","e:" ] ]
    engine_dimensions_list_values = [8.7, 2.9, 6.0, 3.0, 20.5]

    if engine_dimensions_check_box.get() == 1 and empty_input():
        for i, position in enumerate(engine_dimensions_list_positions):
            input_list[position].insert(0, f"{engine_dimensions_list_values[i]}")
    elif engine_dimensions_check_box.get() == 0:
        for i, position in enumerate(engine_dimensions_list_positions):
            input_list[position].delete(0,"end")