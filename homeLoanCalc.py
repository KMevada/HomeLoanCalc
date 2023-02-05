# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# INPUT
LOAN_AMT_INR        = 3*1000*1000
INTREST_RATE_YEAR   = 8.55
NO_OF_YEARS         = 30
INCR_EMI_BY_RATE    = 0.1
EMI_CAP             = -1

INTREST_RATE_MNTH   = INTREST_RATE_YEAR/12/100
NO_OF_MONTH         = NO_OF_YEARS * 12
EMI_TO_BE_PAID      = LOAN_AMT_INR * INTREST_RATE_MNTH * pow((1 + INTREST_RATE_MNTH), NO_OF_MONTH) / (pow((1 + INTREST_RATE_MNTH), NO_OF_MONTH) - 1)


OPEN_BAL = LOAN_AMT_INR;

def getClosBalMonthly(openBal, emi, monthlyInterestRate):
    interestPaid    = openBal * monthlyInterestRate
    principalPaid   = emi - interestPaid
    closeBal        = openBal - principalPaid
    return(closeBal, interestPaid, principalPaid)

def getClosBalYearly(openBal, emi, monthlyInterestRate):
    temp_openBal                = openBal
    interestPaid                = 0
    principalPaid               = 0
    for i in range(1, 13):
        
        closeBal, temp_interestPaid, temp_principalPaid = getClosBalMonthly(temp_openBal, emi, monthlyInterestRate)
        temp_openBal = closeBal
        interestPaid += temp_interestPaid    
        principalPaid += temp_principalPaid    
        
        if(temp_openBal < 0.0):
            break;
    print("Open Bal:%.3f EMI:%.3f Interest Paid:%.3f Principal Paid:%.3f Close Bal:%.3f"%(openBal, emi, interestPaid, principalPaid, closeBal))
    return(closeBal, interestPaid, principalPaid, i)

temp_openBal                = LOAN_AMT_INR    
temp_emi                    = EMI_TO_BE_PAID   
total_interestPaid                = 0
total_principalPaid               = 0 
total_noOfMonths                  = 0 
for i in range(1, NO_OF_YEARS+1):
    print("Year", i)
    closeBal, temp_interestPaid, temp_principalPaid, noOfMonths = getClosBalYearly(temp_openBal, temp_emi, INTREST_RATE_MNTH)
    temp_openBal = closeBal
    
    new_emi = temp_emi*(1 + INCR_EMI_BY_RATE)
    if(EMI_CAP > new_emi) or (EMI_CAP == -1) :
        temp_emi = new_emi
    else:
        temp_emi = temp_emi
    
    total_interestPaid += temp_interestPaid    
    total_noOfMonths += noOfMonths 
    if(temp_openBal < 0.0):
        break;
        

print("TOTAL Interest Paid:",total_interestPaid)
print("TOTAL time to Pay Loan:",int(total_noOfMonths/12),"Years", total_noOfMonths%12, "months")
