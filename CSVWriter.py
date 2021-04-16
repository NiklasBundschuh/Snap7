import csv



def HeaderParser(fileLine, Header):

    
    Header.append(fileLine + "\n")
    return Header

def FooterParser(fileLine, Footer):
   
    Footer.append(fileLine + "\n")
    return Footer
      

def DataParser(fileLine, Data):
    
    Data.append(fileLine+ "\n")
    return Data

def Writer(Header, Footer, Data):
    CSVList = []
    CSVList = Header + Footer + Data
    

    with open('CSVCopy.csv', 'w', newline='')as copy:
        writer = csv.writer(copy)
        writer.writerows([CSVList])
        copy.close
