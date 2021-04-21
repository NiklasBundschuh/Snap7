import csv
 
def ReadAndWrite(CSVData):
    with open('text_2DateiÖffnen.csv') as file:
            for fileLine in file:
                fileLine = fileLine[:-1]
                CSVData.append(fileLine + "\n")
                return CSVData
                
    with open('CSVCopy.csv', 'w', newline='')as copy:
        writer = csv.writer(copy)
        writer.writerows([CSVData])
        copy.close


def main():
    CSVData = []
    CSVData = ReadAndWrite(CSVData)



if __name__ == '__main__':
    main()
