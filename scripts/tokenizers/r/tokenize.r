install.packages("tokenizers", repos = "http://cran.us.r-project.org")
install.packages("tidyverse", repos = "http://cran.us.r-project.org")
install.packages("rjson", repos = "http://cran.us.r-project.org")
library(tokenizers)
library(tidyverse)
library(rjson)



input_loc <- "/scratch/users/bcritt/corpus/"
files <- dir(input_loc, full.names = TRUE)
text <- c()
for (f in files) {
  text <- c(text, paste(readLines(f), collapse = "\n"))
}

#tokenize to list of tokens, no metadata
tokens <- tokenize_words(text)

#create df with file names and tokenize text with tokenizers
test <- cbind(files,text)
df <- data.frame(test)
df$tokens <- tokenize_words(df[,2])

jsonData <- toJSON(df)

write(jsonData, "/scratch/users/bcritt/outputs/tokens.json")

