# Thanks ChatGPT

import os
import numpy as np


def parse_results(dir_path):
    for folder in os.listdir(dir_path):
        folder_path = os.path.join(dir_path, folder)
        if os.path.isdir(folder_path):
            values_files = [f for f in os.listdir(folder_path) if f.endswith('_values.csv')]
            for values_file in values_files:
                score_file = values_file.replace('_values.csv', '_values.csv_score.npy')
                variance_file = values_file.replace('_values.csv', '_values.csv_variance.npy')
                score_file = os.path.join(folder_path, score_file)
                variance_file = os.path.join(folder_path, variance_file)
                values_file = os.path.join(folder_path, values_file)
                if os.path.exists(score_file) and os.path.exists(variance_file):
                    row_names = np.genfromtxt(values_file, delimiter=',', dtype='str', usecols=(0,), skip_header=1)
                    score_data = np.load(score_file)
                    score_data = np.reshape(score_data, (-1, 1))
                    variance_data = np.load(variance_file)
                    variance_data = np.transpose(variance_data)
                    row_names_reshaped = np.reshape(row_names, (-1, 1))
                    print(row_names_reshaped.shape)
                    print(score_data.shape)
                    print(variance_data.shape)
                    score_data = np.concatenate((row_names_reshaped, score_data), axis=1)
                    variance_data = np.concatenate((row_names_reshaped, variance_data), axis=1)
                    output_score_file = os.path.join(folder_path, score_file.replace('_score.npy', '_score.csv'))
                    np.savetxt(output_score_file, score_data, delimiter=',', fmt='%s', comments='')
                    output_variance_file = os.path.join(folder_path, variance_file.replace('_variance.npy', '_variance.csv'))
                    np.savetxt(output_variance_file, variance_data, delimiter=',', fmt='%s', comments='')


parse_results(dir_path="/storage/htc/joshilab/Su_Li/Alg_development/svg/results/real_bsp/2D_MOB_grid_var_score/")
parse_results(dir_path="/storage/htc/joshilab/Su_Li/Alg_development/svg/results/real_bsp/2D_HBC_grid_var_score/")
parse_results(dir_path="/storage/htc/joshilab/Su_Li/Alg_development/svg/results/simu_bsp/3D_Standard_Sim_20230414_grid_var_score/")
