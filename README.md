# AARUS

●Overview

AURS is a software designed to take and record attendance.It
allows the user to put the class list and the list of attendees
and display the output and also record the attendance data in
a csv format.

● Code Description

import csv
import pandas as pd
print('  '*25+"ARUS"+'  '*25)
def main():
>>>>>>>>>>DOCIFY-START - gihwzklptbfo >>>>>>>>>>
    """
     Main function for class. Increments number of classes and calls function nefi () to add students to class
    """
>>>>>>>>>>DOCIFY-END - gihwzklptbfo >>>>>>>>>>
    print('1.Enter NEW CLASS')
    print('2.Update or See EXISTING CLASS')
    print('3.EXIT')
    nfo=int(input('Enter your Choice::'))
>>>>>>>>>>DOCIFY-START - lsrlbqjsvqlq >>>>>>>>>>
    # This function is used to create a CSV file with the following options nfo 1. csv nfo 2. csv nfo 2. csv nfo 2. csv nfo 3. csv nfo 2. csv nfo 3. csv nfo 2. csv nfo 3. csv nfo 4. csv nfo 4. csv nfo 5. csv nfo 5. csv nfo 5. csv nfo 5. csv nfo 5. csv nfo 5. csv nfo 5. csv nfo 5. csv nfo 5. csv nfo 5. csv nfo 5. csv nfo 5. csv nfo
>>>>>>>>>>DOCIFY-END - lsrlbqjsvqlq >>>>>>>>>>
    if nfo==1:
        def nefi():
>>>>>>>>>>DOCIFY-START - fbeveoskjtmb >>>>>>>>>>
            """
             This function reads the class and attendences from csv file and writes it to csv file. It is called by nefi. py
             
             
             @return a tuple containing the name of the class and the attendence of the students in the class
            """
>>>>>>>>>>DOCIFY-END - fbeveoskjtmb >>>>>>>>>>
            nfn=input('Enter Class in Numeric Value::')
            nsn=input("Enter Class's Section::")
            nsn=nsn.upper()
            fn=nfn+' '+nsn+'.csv'
            a=input("Please enter full list of name of students in class::")
            header = ['Name', 'Attendence']
            r=a+".txt"
            gl = open(r, "r")
            m=[]
            l= []
            d=[]
            global fo
            fo=[]
            scl=1
>>>>>>>>>>DOCIFY-START - lrfodjwheedg >>>>>>>>>>
            # Add lines to the gl file
>>>>>>>>>>DOCIFY-END - lrfodjwheedg >>>>>>>>>>
            for line in gl:
              s = line.strip()
              lt = s.split('/n')
              l.append(lt)
>>>>>>>>>>DOCIFY-START - wxyeyuocqyjx >>>>>>>>>>
            # Appends the first letter of each string to the list of strings.
>>>>>>>>>>DOCIFY-END - wxyeyuocqyjx >>>>>>>>>>
            for i in l:
              ml=i[0].upper()
              m.append(ml)
            
            def extractDigits(lst):
>>>>>>>>>>DOCIFY-START - cxlnsfdvqgqd >>>>>>>>>>
                """
                 Extracts digits from a list. This is useful for converting numbers to strings in a way that's easier to read
                 
                 @param lst - list to extract digits from
                 
                 @return list of digits extracted from the input list >>> extractDigits ( ['0'' 1']
                """
>>>>>>>>>>DOCIFY-END - cxlnsfdvqgqd >>>>>>>>>>
                return [[el] for el in lst]
            
            
            j=extractDigits(m)
            
            def listToString(s):
>>>>>>>>>>DOCIFY-START - krniwbshaxat >>>>>>>>>>
              """
               Write list to file. This is used to create output files that are easier to read by humans
               
               @param s - list of strings to
              """
>>>>>>>>>>DOCIFY-END - krniwbshaxat >>>>>>>>>>
              global scl
>>>>>>>>>>DOCIFY-START - vinqvupiiytg >>>>>>>>>>
              # Append the vir to the output buffer
>>>>>>>>>>DOCIFY-END - vinqvupiiytg >>>>>>>>>>
              for e in j:
                  vir=e+[0]
                  d.append(vir)
                  writer.writerow(vir)
              
                 
            with open(fn, 'w', encoding='UTF8', newline='') as f:
              writer = csv.writer(f)
              writer.writerow(header)
              listToString(j)
            
            df = pd.read_csv(fn)
            
            df.to_csv(fn, index_label='Roll Number')
            print('New CSV FILE with name',nfn+' '+nsn,'Created')
        nefi()
        print()
        print()
        print('PLEASE SELLECT AS PER REQUIREMENT')
        print()
        print()
        main()
    elif nfo==2:
        def cl():
>>>>>>>>>>DOCIFY-START - suqnknqgseey >>>>>>>>>>
            """
             This function is called when user presses CTRL + C. The class is read from user input
            """
>>>>>>>>>>DOCIFY-END - suqnknqgseey >>>>>>>>>>
            back=input('Press B to go BACK and C to CONTINUE::')
            bc=back.upper()
>>>>>>>>>>DOCIFY-START - wsxxmiivpkht >>>>>>>>>>
            # Print out the test cases.
>>>>>>>>>>DOCIFY-END - wsxxmiivpkht >>>>>>>>>>
            if bc=='B':
                print()
                print()
                print('PLEASE SELLECT AS PER REQUIREMENT')
                print()
                print()
                main() 
            elif bc=='C':
                global un
                un=input('Enter Class in Numeric Value::')                
                global se
                se=input("Enter Class's Section::")
                
                se=se.upper()
                global fi
                fi=un+' '+se+'.csv'
            else:
                print()
                print()
                print('PLEASE INPUT VALID OPTION')
                print()
                print()
                cl() 
        cl()    
        def fi():
>>>>>>>>>>DOCIFY-START - bwhegzrecfts >>>>>>>>>>
            """
             This is a test for the fi command. It does nothing but print the status of the program to stdout
            """
>>>>>>>>>>DOCIFY-END - bwhegzrecfts >>>>>>>>>>
            fi() 
        def primary():
>>>>>>>>>>DOCIFY-START - zxrfglegfbon >>>>>>>>>>
            """
             Primary function for MENU. Input : 1. User chooses to input todays attendence 2. User asks for file name of students present today in class
            """
>>>>>>>>>>DOCIFY-END - zxrfglegfbon >>>>>>>>>>
            print('MENU for CLASS',un+' '+se)
            print('1.INPUT TODAYS ATTENDENCE')
            print('2.GO BACK')
            print('3.EXIT')
            ui=int(input('Enter your Choice::'))            
>>>>>>>>>>DOCIFY-START - ahxlnmloqmhk >>>>>>>>>>
            # This function is used to display the user input
>>>>>>>>>>DOCIFY-END - ahxlnmloqmhk >>>>>>>>>>
            if ui==1:
                print('INPUT TODAYS ATTENDENCE')
                a=input("Please enter file with name of students present today in class::")
                r=a+".txt"
                gl = open(r, "r")
                m=[]
                l=[]
                fo=[]
>>>>>>>>>>DOCIFY-START - uurbkbovhyqy >>>>>>>>>>
                # Add lines to the gl file
>>>>>>>>>>DOCIFY-END - uurbkbovhyqy >>>>>>>>>>
                for line in gl:
                    s = line.strip()
                    lt = s.split('/n')
                    l.append(lt)
>>>>>>>>>>DOCIFY-START - kesgvmriggce >>>>>>>>>>
                # Appends the first letter of each string to the list of strings.
>>>>>>>>>>DOCIFY-END - kesgvmriggce >>>>>>>>>>
                for i in l:
                    ml=i[0].upper()
                    m.append(ml)
>>>>>>>>>>DOCIFY-START - gzvrtqxshakd >>>>>>>>>>
                # Append the items in m to fo.
>>>>>>>>>>DOCIFY-END - gzvrtqxshakd >>>>>>>>>>
                for i in m:
                    fo.append(i)
                y=input("Enter todays date :: ")
                z=input("Enter month :: ")
                k=input("Enter Year :: ")
                f=y+"/"+z+"/"+k
                L1=fo
                n=0                                                               
                df = pd.read_csv(un+' '+se+".csv")
                df[f] = ""
                df.to_csv(un+' '+se+".csv", index=False)
>>>>>>>>>>DOCIFY-START - avbebwwirfie >>>>>>>>>>
                # This function is used to determine whether the column n is present or absent.
>>>>>>>>>>DOCIFY-END - avbebwwirfie >>>>>>>>>>
                while n<57:
>>>>>>>>>>DOCIFY-START - piwuzydrknjv >>>>>>>>>>
                    # This function is used to set the location of the column in the dataframe.
>>>>>>>>>>DOCIFY-END - piwuzydrknjv >>>>>>>>>>
                    if df.loc[n,'Name',] in  L1:                                           
                        df.loc[n, 'Attendance']+=1                                      
                        df.loc[n, f] ='Present'
                        df.to_csv(un+' '+se+".csv", index=False)  
                        n+=1
                        print(n,"Present")
                    elif df.loc[n,'Name',] not in  L1:
                        df.loc[n, f] ='Absent'
                        df.to_csv(un+' '+se+".csv", index=False)
                        n+=1
                        print(n,"absent")
            elif ui==2:
                print()
                print('PLEASE SELLECT AS PER REQUIREMENT')
                print()
                main() 
            elif ui==4:
                print('Thanks for using ARUS (・∀・)')                    
            else:
                print()
                print()
                print('Please choose a numberfrom the menu ('-')')
                print()
                print()
                primary()
        primary()
    elif nfo==3:
        print('Thanks for using ARUS (・∀・)')
    else:
        print()
        print()
        print('Please choose a numberfrom the menu ('-')')
        print()
        print()
        main()            
main()

● Workings

It takes the attendance in any format and converts it into
txt format where it converts it finally to list.
It goes through all the name in the list with the provided
class list and at last gives the names that do not match i.e.
The absentees and then it uses csv to append the
attendance in csv as +1 for present and +0 for absent.

#Hardware Requirements

● Processor

1. Intel Core 2 duo or higher
2.AMD Athlon 5350 APU OR higher

● GPU

1. Intel Iris Graphics
2.Intel Xe
3.AMD Vega 1 or higher
4.GTX 750 or higher

#Software Requirements

● Operating system
1. Debian GNU/linux or any distro based on it
2.Ubuntu version 3.5 or higher
3.Arch GNU/linux or any distro based on it
4.Windows 7 or higher

● Integrated development environment
1. Python 3.x
2.VS code
3.Pycharm etc.
