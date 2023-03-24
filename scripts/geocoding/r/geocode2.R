# implementation of https://cran.r-project.org/web/packages/spacyr/vignettes/using_spacyr.html
#remove.packages("reticulate")
install.packages("reticulate")
reticulate::virtualenv_create(envname = 'python_environment', 
                              python= 'python3')
#reticulate::virtualenv_install("python_environment")
reticulate::use_virtualenv("python_environment",required = TRUE)

install.packages("spacyr")
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
write.csv(parsedtxt, "pos_ner.csv")

install.packages("sf")
install.packages("rgdal")
install.packages("tmaptools")
library(sf)
library(rgdal)
library(tmaptools)

# geocoding only GPEs
places_tmaptools <- geocode_OSM(paste(parsedtxt$entity, "GPE", sep = " "),
                              details = TRUE, as.data.frame = TRUE)

# extracting from the result only coordinates and address
places_tmaptools <- places_tmaptools[, c("lat", "lon", "display_name")]
places_tmaptools <- cbind(Places = parsedtxt$token, places_tmaptools)

# print the results
write.csv(places_tmaptools,"places.csv")