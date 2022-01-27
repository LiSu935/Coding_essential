# sapply funciton:
#The sapply() function works like lapply(), but it tries to simplify the output to the most elementary data structure that is possible. And indeed, sapply() is a ‘wrapper’ function for lapply().
x <- c(sample(1:10, replace=F))
y <- c(sample(1:10, replace=F))
gene1 <- c(sample(1:20, 10, replace=F))

Input_Data = data.frame(x,y, gene1)
new_df = sapply(1:3, function(j) {
  return(Input_Data[sample(1:10, 
                           replace = FALSE), 
                    1 + 2])
})

> sample_list
# [1] "WT_mock_1"   "WT_mock_2"   "WT_mock_3"   "WT_Bc_1"     "WT_Bc_2"    
# [6] "ko33_mock_1" "ko33_mock_2" "ko33_mock_3" "ko33_Bc_1"   "ko33_Bc_2"  
#[11] "ko33_Bc_3"   "WT_Bc_3"   

treatment = sapply(sample_list,function(i){
  + return(strsplit(i, "_")[[1]][[2]])})
# WT_mock_1   WT_mock_2   WT_mock_3     WT_Bc_1     WT_Bc_2 ko33_mock_1 
#     "mock"      "mock"      "mock"        "Bc"        "Bc"      "mock" 
#ko33_mock_2 ko33_mock_3   ko33_Bc_1   ko33_Bc_2   ko33_Bc_3     WT_Bc_3 
#     "mock"      "mock"        "Bc"        "Bc"        "Bc"        "Bc" 

# ===================================================================================================================================== #
#  read table; group_by
# ===================================================================================================================================== #
df_ori_clu_Anno = read.table(paste(output_dir,prefix,"_df_ori_clu_Anno",".txt",sep=""),stringsAsFactors=F, header = T, row.names=1)
df_ori_clu_Anno = as.data.frame(df_ori_clu_Anno)

df_ori_clu = df_ori_clu_Anno %>% group_by(Sample,Cluster) %>% summarise(Number = sum(Number))
# when see the error of "Continuous value supplied to discrete scale", change the variable as factor.
df_ori_clu$Cluster = as.factor(df_ori_clu$Cluster)
