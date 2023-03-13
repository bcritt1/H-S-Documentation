install.packages("tokenizers")
install.packages("tidyverse")

library(tokenizers)
library(tidyverse)

task_id <- Sys.getenv("SLURM_ARRAY_TASK_ID")

input_loc <- "/Users/bcritt/Documents/StanfordProjects/Corpora/Emerson/emerson"
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
