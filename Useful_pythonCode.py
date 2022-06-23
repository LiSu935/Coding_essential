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
