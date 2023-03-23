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

input_loc <- "/Users/bcritt/Documents/StanfordProjects/Corpora/Emerson/emerson/"
files <- dir(input_loc, full.names = TRUE)
text <- c()
for (f in files) {
  text <- c(text, paste(readLines(f), collapse = "\n"))
}

library(tidyverse)

parsedtxt <- spacy_parse(text)

#workflow to keep only rows with entities if desired
#parsedtxt$entity[parsedtxt$entity==""] <- NA
#onlyEntities <- parsedtxt %>% 
#  filter(!is.na(parsedtxt$entity))

#workflow to keep only places. can be used for people, etc. by swapping search term to different type of entity
onlyPlaces <- parsedtxt %>%
  filter(str_detect(entity, "GPE"))
#write out. variable can be changed depending on if you want full dataset, only entities, only places, etc.
#write.csv(parsedtxt, "pos_ner.csv")

install.packages("sf")
install.packages("rgdal")
install.packages("tmaptools")
library(sf)
library(rgdal)
library(tmaptools)

# geocoding only GPEs in dataset
places_tmaptools <- geocode_OSM(onlyPlaces$token, details = TRUE, as.data.frame = TRUE)

# extracting from the result only coordinates and query. You can adjust this as needed by inspecting places_tmaptools
places_tmaptools <- places_tmaptools[, c("lat", "lon", "display_name", "query")]


# print the results
write.csv(places_tmaptools,"places.csv")