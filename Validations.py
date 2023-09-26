def isMobileValid(mobile_number):
    if len(mobile_number)==10:
        if mobile_number.isdigit():
            return True
        else:
            return False
    else:
        return  False


def isNameValid(name):
    l=name.split()

    if len(l) !=3:
        return False
    
    for i in l:
        if not i[0].isupper():
            return False
    
    return True

def isPanValid(pan_number):
    if len(pan_number)!=10:
        return False
    if not pan_number[:5].isalpha()or not pan_number[:5].isupper():
        return False
    if not pan_number[5:9].isdigit():
        return False
    if not pan_number[9].isalpha()or not pan_number[9].isupper():
        return False
    else:
        return True
        
def isDOBValid(dob):
    day,month,year=map(int,dob.split('-'))
    min_year=1900
    max_year=2023
    min_month=1
    max_month=12
    min_day=1
    max_day=31
    if(min_year<=year<=max_year and min_month <= month <= max_month and min_day <=day <= max_day):
        if(year%4==0 and month==2 and day<=29):
            return True
        else:
            return True
    else:
        return False
    
def isAadharValid(aadhar_number):
    if not aadhar_number.isdigit() or len(aadhar_number)!=12:
        return False
    else:
        return True

def isDOJValid(doj):
    day,month,year=map(int,doj.split('-'))
    min_year=1900
    max_year=2023
    min_month=1
    max_month=12
    min_day=1
    max_day=31
    if(min_year<=year<=max_year and min_month <= month <= max_month and min_day <=day <= max_day):
        if(year%4==0 and month==2 and day<=29):
            return True
        else:
            return True
    else:
        return False
    
def isAgeValid(age):
    if(int(age)>18 and age.isdigit() and len(age)==2):
        return True
    else:
        return False

def isSalValid(sal):
    if(sal.isdigit() and int(sal)>0):
        return True
    else:
        return False
    
def isIDValid(id):
    if(id.isdigit()):
        return True
    else:
        return False
    
def isGenderValid(gender):
    if(gender=='M' or gender=='Male' or gender=='F' or gender=='Female'):
        return True
    else:
        return False

def isDnameValid(name):
    l=name.split()
    
    for i in l:
        if not i[0].isupper():
            return False
    
    return True

def isAddressValid(name):
    l=name.split()
    
    for i in l:
        if not i[0].isupper():
            return False
    
    return True

def isCityValid(name):
    l=name.split()
    
    for i in l:
        if not i[0].isupper():
            return False
    
    return True

def isdesivalid(name):
    l=name.split()
    
    for i in l:
        if not i[0].isupper():
            return False
    
    return True
