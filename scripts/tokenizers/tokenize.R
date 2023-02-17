install.packages("tokenizers")
install.packages("tidyverse")
install.packages("tidytext")

library(tokenizers)
library(tidyverse)
library(tidytext)

input_loc <- "</Users/your/file/path/>"
files <- dir(input_loc, full.names = TRUE)
text <- c()
for (f in files) {
  text <- c(text, paste(readLines(f), collapse = "\n"))
}

#tokenize with tokenizers
words <- tokenize_words(text)

#adds file names, but puts every word as a row
#words2 <- do.call(rbind, Map(data.frame, work=files, text=words))

#tokenize with tidytext: also puts every word as own row. Can connect to file 
#names with simple merge of numbered "files" list
text2 <- enframe(text)
tidyText <- text2 %>%
  unnest_tokens(word, value)
