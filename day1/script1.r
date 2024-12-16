install.packages("tidyverse")
library(tidyverse)


read_input <- function() {
  data <- read.table("day1/input.txt", header = F, sep = "")
  return(data)
}

data <- read_input()
data$V1 <- sort(data$V1, decreasing = F)
data$V2 <- sort(data$V2, decreasing = F)

data <- mutate(data, diff=abs(V1-V2))
print(sum(data$diff))