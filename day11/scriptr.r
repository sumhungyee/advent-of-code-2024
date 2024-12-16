install.packages("stringr")
install.packages("hash")
library(stringr)
library(hash)

read_input <- function() {
  file <- file("day11/input.txt", "r")
  v <- c()
  index <- function(x, y) {
      return(substr(v[x], y, y))
  }
  while (TRUE) {
    line <- readLines(file, n = 1)
    if (length(line) == 0) break 
    v <- append(v, line)
  }
  close(file)
  v <- as.numeric(str_split_1(v, pattern = " "))
  return(v)

}

add_hashmap <- function(h, item, repeats) {
  if (is.null(h[[as.character(item)]])) {
    h[[as.character(item)]] <- repeats
  } else {
    h[[as.character(item)]] <- h[[as.character(item)]] + repeats
  }
}

remove_hashmap <- function(h, item, repeats) {

  if (h[[as.character(item)]] > repeats) {
    h[[as.character(item)]] <- h[[as.character(item)]] - repeats
  } else {
    h[[as.character(item)]] <- NULL
  }
}

data <- read_input()
h <- hash()
for (d in data) {
  h[[as.character(d)]] <- 1
}
steps <- as.numeric(readline("Steps: "))

for (i in 1:steps) { # 1-based indexing is crazy
  key <- keys(h)
  items <- unname(sapply(keys(h), \(k) h[[k]]))
  
  for (j in 1:length(key)) {
    k <- key[j]
    v <- items[j]

    remove_hashmap(h, k, v)
    if (as.numeric(k) == 0) {
      add_hashmap(h, "1", v)
    } else if (nchar(k) %% 2 == 0) {

      k1 <- substring(k, 1, nchar(k) / 2)
      k2 <- substring(k, nchar(k) / 2 + 1, nchar(k))
      add_hashmap(h, as.numeric(k1), v) # its fine already converted in the fn
      add_hashmap(h, as.numeric(k2), v)
    } else {
      add_hashmap(h, as.numeric(k) * 2024, v) 
    } 
  }
}
print(sum(values(h)))