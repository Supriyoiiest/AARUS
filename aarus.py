import csv
import pandas as pd
print('  '*25+"ARUS"+'  '*25)
def main():
    print('1.Enter NEW CLASS')
    print('2.Update or See EXISTING CLASS')
    print('3.EXIT')
    nfo=int(input('Enter your Choice::'))
    if nfo==1:
        def nefi():
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
            for line in gl:
              s = line.strip()
              lt = s.split('/n')
              l.append(lt)
            for i in l:
              ml=i[0].upper()
              m.append(ml)
            
            def extractDigits(lst):
                return [[el] for el in lst]
            
            
            j=extractDigits(m)
            
            def listToString(s):
              global scl
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
            back=input('Press B to go BACK and C to CONTINUE::')
            bc=back.upper()
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
            fi() 
        def primary():
            print('MENU for CLASS',un+' '+se)
            print('1.INPUT TODAYS ATTENDENCE')
            print('2.GO BACK')
            print('3.EXIT')
            ui=int(input('Enter your Choice::'))            
            if ui==1:
                print('INPUT TODAYS ATTENDENCE')
                a=input("Please enter file with name of students present today in class::")
                r=a+".txt"
                gl = open(r, "r")
                m=[]
                l=[]
                fo=[]
                for line in gl:
                    s = line.strip()
                    lt = s.split('/n')
                    l.append(lt)
                for i in l:
                    ml=i[0].upper()
                    m.append(ml)
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
                while n<57:
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
