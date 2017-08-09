val <- c(1,2,3,4,5,6)
mean(val)


myfun <- function(a,b,c){
 sum <- a+b+2*c
 foobar <- 0
 return(sum)
}

print(paste("myfun:",myfun(1,2,3)))