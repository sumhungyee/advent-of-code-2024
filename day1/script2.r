
read_input <- function() {
  data <- read.table("day1/input.txt", header = F, sep = "")
  return(data)
}
data <- read_input()
data$V1 <- sort(data$V1, decreasing = F)
data$V2 <- sort(data$V2, decreasing = F)
print(sum(sapply(data$V1, \(x) x * length(data$V2[data$V2 == x]))))