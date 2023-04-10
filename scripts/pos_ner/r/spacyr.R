# implementation of https://cran.r-project.org/web/packages#/spacyr/vignettes/using_spacyr.html
# recommended for use in sdev or OnDemand due to complicated set-up
#ml load r/4.2.0
#ml load python/3.9.0

install.packages("reticulate", repos = "http://cran.us.r-project.org")
#worked without library(reticulate). I know there can be a python version error
#when reticulate is loaded vs miniconda python vs system python
reticulate::virtualenv_create(envname = 'python_environment', 
                              python= 'python3')
#reticulate::virtualenv_install("python_environment") #py_install on sherlock R
#interactive here for installing miniconda. Can be pipped or install.packages()?
reticulate::use_virtualenv("python_environment",required = TRUE)

install.packages("spacyr", repos = "http://cran.us.r-project.org")
library(spacyr)

#use_python("/usr/local/bin/python3")
spacy_initialize(model = "en_core_web_sm")

input_loc <- "/home/users/bcritt/corpus/"
files <- dir(input_loc, full.names = TRUE)
text <- c()
for (f in files) {
  text <- c(text, paste(readLines(f), collapse = "\n"))
}

parsedtxt <- spacy_parse(text)
write.csv(parsedtxt, "/home/users/bcritt/Rpos_ner.csv")

