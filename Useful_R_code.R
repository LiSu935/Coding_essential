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