# implementation of https://gensimr.news-r.org/reference/model_word2vec.html
install.packages("remotes")
remotes::install_github("news-r/gensimr")
gensimr::install_dependencies()

library(tidyverse)
library(gensimr)



input_loc <- "/Users/bcritt/Documents/StanfordProjects/Corpora/Emerson/emerson"
files <- dir(input_loc, full.names = TRUE)
text <- c()
for (f in files) {
  text <- c(text, paste(readLines(f), collapse = "\n"))
}
docs <- prepare_documents(text)
word2vec <- model_word2vec(window = 5L, min_count = 1L)
word2vec$build_vocab(docs)
word2vec$train(docs, total_examples = word2vec$corpus_count, epochs = 20L)
word2vec$init_sims(replace = TRUE)
word2vec$wv$most_similar(positive = c("aristotle"))
word2vec$wv$doesnt_match(c("human", "interface", "trees"))
word2vec$wv$similarity("human", "trees")