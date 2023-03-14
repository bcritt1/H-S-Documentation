install.packages("spacyr")
library(spacyr)
library(reticulate)

reticulate::virtualenv_create(envname = 'python_environment', 
                              python= 'python3')
reticulate::virtualenv_install("python_environment")
reticulate::use_virtualenv("python_environment",required = TRUE)

use_python("/usr/local/bin/python3")
spacy_initialize(model = "en_core_web_sm")

input_loc <- "/Users/bcritt/Documents/StanfordProjects/Corpora/Emerson/emerson"
files <- dir(input_loc, full.names = TRUE)
text <- c()
for (f in files) {
  text <- c(text, paste(readLines(f), collapse = "\n"))
}

parsedtxt <- spacy_parse(text)
write.csv(parsedtxt, "pos_ner.csv")