
import csv
import os #stands for operating system 

#udemy_csv = *./resources/web_starter.csv" #oldSchool way
udemy_csv=os.path.join(".", "resources","web_starter.csv") #BestWay

title=[]
price=[]
subscribers=[]
reviews=[]
reviews_percent=[]
length=[]

with open(udemy_csv, "r", encoding="UTF-8") as csvfile:
        csvreader = csv.reader(csvfile,delimiter=",")
        #test = next(csvreader)
        for row in csvreader:
            #addtitle
            title.append(row[1])
            price.append(row[4])
            subscribers.append(row[5])
            reviews.append(row[6])
            percent=round(int(row[6])/int(row[5]),2)
            reviews_percent.append(percent)
            new_length=row[9].split(" ")
            length.append(float(new_length[0]))

#print(reviews_percent)

cleanCsv= zip(title, price, subscribers, reviews, reviews_percent, length)
outputFile = os.path.join("webFinal.csv")

with open (outputFile, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Title","Course Price","Subscribers","Reviews","Percent of Reviews", "Length of Course"])
    writer.writerows(cleanCsv)