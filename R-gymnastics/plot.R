library("RSQLite")
mydb <- dbConnect(RSQLite::SQLite(), "data.db")
dbListTables(mydb)
data <- dbGetQuery(mydb, 'SELECT * FROM xvy')
plot(data$x,data$y)

dev.copy(png,'data.png')
dev.off()