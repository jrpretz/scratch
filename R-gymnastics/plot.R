library("RSQLite")
mydb <- dbConnect(RSQLite::SQLite(), "data.db")
dbListTables(mydb)
data <- dbGetQuery(mydb, 'SELECT * FROM xvy')


png('data.png')
plot(data$x,data$y)

