import shapefile

shape = shapefile.Reader("cb_2016_us_county_20m.shp")

print(shape.shapeType)

n = len(shape.shapeRecords())
records = shape.shapeRecords()
#for i in range(n):
#  print(i,records[i].record[5])

print(2224,records[2224].record)
