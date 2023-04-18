install.packages("tokenizers", repos = "http://cran.us.r-project.org")
install.packages("rjson", repos = "http://cran.us.r-project.org")
library(tokenizers)
library(rjson)

path <-	file.path("scratch", "users")
corpus <- file.path("corpus")
outputs	<- file.path("outputs")
user <- Sys.getenv("LOGNAME")
input_loc <- file.path("/", path, user, corpus, "/")
output_loc = file.path("/", path, user, outputs, "/")

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

#output to json
jsonData <- toJSON(df)
write(jsonData,paste(output_loc, "tokens.json", sep =""))

#or csv
write.csv(df,paste(output_loc, "tokens.csv", sep =""))

