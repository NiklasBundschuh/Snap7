
from os import name
from CSVWriter import HeaderParser
from CSVWriter import FooterParser
from CSVWriter import DataParser
from CSVWriter import Writer

def parseFile(Header, Footer, Data):
    headerSection = False
    footerSection = False
    dataSection = False

    with open('text_2DateiÖffnen.csv') as file:
        for fileLine in file:
            fileLine = fileLine[:-1]
            
            fileLine, headerSection, footerSection, dataSection = checkForSection(fileLine, headerSection, footerSection, dataSection)
            
            if headerSection == True:
                HeaderParser(fileLine, Header)
                if fileLine == "Kopfzeilen ENDE":
                    headerSection = False

            elif footerSection == True:
                FooterParser(fileLine, Footer)
                if fileLine == "Fusszeilen ENDE":
                    footerSection = False
            
            elif dataSection == True:
                DataParser(fileLine, Data)

        Writer(Header, Footer, Data)

    return Header, Footer, Data


    
def checkForSection(fileLine, headerState, footerState, dataState):
    HEADER_START = "Kopfzeilen START"
    HEADER_END   = "Kopfzeilen ENDE"
    FOOTER_START = "Fusszeilen START"
    FOOTER_END   = "Fusszeilen ENDE"
    Data_Start = "Zeittakt"




    # check the Header Start
    if fileLine[0:len(HEADER_START)] == HEADER_START:
        headerState = True
        fileLine = HEADER_START
           

    # check the Header End
    elif fileLine[0:len(HEADER_END)] == HEADER_END:
        fileLine = HEADER_END
               
            
    # check the Footer Start
    elif fileLine[0:len(FOOTER_START)] == FOOTER_START:
        footerState = True
        fileLine = FOOTER_START
       
           
     # check the Footer End
    elif fileLine[0:len(FOOTER_END)] == FOOTER_END:
        fileLine = FOOTER_END
        

    elif fileLine[0:len(Data_Start)] == Data_Start:
        dataState = True
        # don't remove trigger info    
    

    return fileLine, headerState, footerState, dataState,

def main():
    Header = []
    Footer = []
    Data = []
    Header, Footer, Data = parseFile(Header, Footer, Data)



if __name__ == '__main__':
    main()