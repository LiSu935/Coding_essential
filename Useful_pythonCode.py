# To remove the rows with column c startswith 'l'
df = df[~df['c'].astype(str).str.startswith('1')]


# numpy array np.sum
array1  = np.array([[0,1], [0,5], [1,4])
array1
#array([[0, 1],
#       [0, 5],
#       [1, 4]])
                    
# so slide with the direction of the first axis, which is row's direction, so it is column-wised                    
np.sum(array1 , axis=0)
#array([ 1, 10])
                    
# column-wised, how many rows, at which the element is larger than 0. ====> 1, 3      
np.sum(array1>0 , axis=0)
#array([1, 3])
np.sum(array1>0 , axis=1)
# array([1, 1, 2])
                    
                    
# In pandas dataframe, if one column is null, set another column to be some value (here is 'No', or set the value to be the value from another column. ex. `df['Middle']`;
                    # if the column is not null, then set the value to be 'Yes')
# super useful!
merge_df['Is_TF'] = np.where(merge_df['TF_ID'].isnull(), 'No', 'Yes')

                    
# ============================================================================================ #
# merge several tables into a excel file:
# ============================================================================================ #
                    
import pandas as pd
import os
#import openpyxl
import xlsxwriter

input_dir = '/Users/lisu/Documents/DrDongXu/Guoquan_UTSA_immune/per_modality_clu_clean/with_clean/' \
            'immunarch/'

prefix = 'CD8_T'
dic = {}
sample_name_list = []
for filename in os.listdir(input_dir):
    if (filename.startswith(prefix)) & (filename.endswith("frequencyTable.txt")):
        sample_name_list.append(filename)

for samplename in sample_name_list:
    df = pd.read_table(input_dir+samplename, header=0)
    dic[samplename.split('_')[2]] = df

writer = pd.ExcelWriter(input_dir+prefix+'_geneUsage_summary.xlsx', engine='xlsxwriter')

for sheet, frame in dic.items(): # .use .items for python 3.X
    frame.to_excel(writer, sheet_name=sheet)

#critical last step
writer.save()
