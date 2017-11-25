inFileName  = 'file1.txt'
outFileName = 'file2.txt'

with open(inFileName) as ifile, open(outFileName,'w') as ofile:
    beforeTax = ifile.read().splitlines()
    # or we could use   beforeTax = ifile.read().split('\n')
    for one in beforeTax:
        if one.count(';') != 1: # ensure valid
            continue
        
        namePart,salaryPart = one.split(';')   
        # name Part like  name: Jack  |  salaryPart like    salary:  12000]
        
        if namePart.count(':') != 1: # ensure valid
            continue
        if salaryPart.count(':') != 1: # ensure valid
            continue
            
        name   = namePart.split(':')[1].strip()
        salary = int(salaryPart.split(':')[1].strip())
        
        income = int(salary*0.9)
        tax    = int(salary*0.1)
        
        outPutStr = 'name: {:10}   ;    salary:  {:6} ;  tax: {:6} ; income:  {:6}'.format(name,salary,tax,income)
        
        print outPutStr
        
        ofile.write(outPutStr + '\n')
    
