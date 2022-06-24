# ---------------------------- Functions ------------------------------ #
import tkinter
from tkinter import messagebox
import math
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
    new_answer_label.name = descriptive_label.cget("text")
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
        input_list[k_e_input_position].delete(0, "end")

    # ----------------------------- Engine dimensions ------------------------------ #
    def empty_input():
        for input in input_list[4:8]:
            if input.get() != "":
                return False
            else:
                return True

    engine_dimensions_list_positions = [list_position for list_position, input in enumerate(input_list)
                                        if input.name in ["a:", "b:", "c:", "d:", "e:"]]
    engine_dimensions_list_values = [8.7, 2.9, 6.0, 3.0, 20.5]

    if engine_dimensions_check_box.get() == 1 and empty_input():
        for i, position in enumerate(engine_dimensions_list_positions):
            input_list[position].insert(0, f"{engine_dimensions_list_values[i]}")
    elif engine_dimensions_check_box.get() == 0:
        for i, position in enumerate(engine_dimensions_list_positions):
            input_list[position].delete(0, "end")


def get_inputs(input_list, k_e_motor, file_data_dict, answer_label_list):
    # ----------------------------- Input Process ------------------------------ #
    desired_input_list = [float(input.get()) for input in input_list
                          if input.name in ["AWG:", "Corrente(A):", "Torque desejado:", "a:", "b:", "c:", "d:", "e:"]]
    if "" in desired_input_list:
        messagebox.showerror(title="Erro", message="Sem valor atribuido as entradas")
    else:
        AWG_Cable = desired_input_list[0]
        I_rms_motor = desired_input_list[1]
        T_Desejado = desired_input_list[2]
        a_dim_motor = desired_input_list[3] * 0.001
        b_dim_motor = desired_input_list[4] * 0.001
        c_dim_motor = desired_input_list[5] * 0.001
        d_dim_motor = desired_input_list[6] * 0.001
        e_dim_motor = desired_input_list[7] * 0.001
        # ----------------------------- Equations ------------------------------ #
        N_antigo = 10  # Numero de voltas usado pelo Warthog antes do estudo
        N_imas = 16  # Numero de imas
        T_final = T_Desejado * 1.1
        N_novo = T_final / (2 * k_e_motor * N_imas * I_rms_motor / N_antigo)

        Diametro_fio = file_data_dict["Diametro do fio esmaltado em mm:"][str(int(AWG_Cable))] * 1e-3
        raio_fio = Diametro_fio / 2

        # Numero de fios em paralelo
        Tab_I_Max = file_data_dict['Corrente máxima em Ampéres:'][str(int(AWG_Cable))]
        N_fios_Paralelo = I_rms_motor / Tab_I_Max

        # -----Distribuicao 1 -----#
        # Camadas
        N_cable_Layer = math.floor(a_dim_motor / Diametro_fio) # Numero de cabos por camada, floor aproxima o valor
        # real para o menor inteiro
        N_Layers_complete = math.floor(N_novo * N_fios_Paralelo / N_cable_Layer) # Numero de camadas completas

        # Comprimento completo
        Comprimento_1 = 0
        for n in range(1, N_Layers_complete + 1):
            Comprimento_1 = Comprimento_1 + (2 * (e_dim_motor + d_dim_motor) + 4 * (n - 1) * Diametro_fio) * N_cable_Layer

        # Comprimento incompleto
        Comprimento_2 = (2 * (e_dim_motor + d_dim_motor) + 4 * (N_Layers_complete - 1) * Diametro_fio) * (
                    N_novo * N_fios_Paralelo - N_Layers_complete * N_cable_Layer)
        # Comprimento Final
        Comprimento_Final = 4 * Comprimento_1 + 4 * Comprimento_2 + 7 * b_dim_motor + 5 * d_dim_motor + 0.1

        # ----------------------------- Results ------------------------------ #
        output_list_positions = [list_position for list_position, input in enumerate(answer_label_list)
                                            if input.name in ["Número de fios em paralelo:",
                                                              "Número de voltas por slot:","Comprimento do fio(m):"]]
        answer_label_list[output_list_positions[0]].config(text=f"{N_fios_Paralelo}")
        answer_label_list[output_list_positions[1]].config(text=f"{N_novo}")
        answer_label_list[output_list_positions[2]].config(text=f"{Comprimento_Final}")


