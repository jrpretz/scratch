# list
a <- list(aa=1,bb=2,cc=3)
print (a)
a$dd = 4
print(paste("a$dd:",a$dd))
a <- list(foo=c(1,2,3))
print(a)

# vector
v <- c(98, 99, 100)
print(v)

v <- c(1:10)
print(paste("length of v:",length(v)))
v[length(v)+1] <- 44

print(v)


#matrix 
data <- c(1:12)
m <- matrix(data,nrow=3,ncol=4)

print(m)
print(paste(m[2,3],"should be 8"))
print(m[1,])
print("^-- should be 1 4 7 10")



# data frame
years <- c(1980,1985,1990)
scores <- c(34,44,83)
df <- data.frame(years,scores)

typeof(df)
