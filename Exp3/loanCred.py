def LoanCrdts(age,incm,othrLoan,year,asstval):
    if othrLoan>0 and year>0:
      return (100-age)*((incm-(othrLoan/(year*12)))/100000)*(asstval/100000)
    return (100-age)*(incm/100000)*(asstval/100000)
    
age=int(input("Enter your Age:"))
incm=int(input("Enter your Income:"))
othrloan=0
othrLoan=int(input("Enter Other loan Amount (If not enter 0):"))
year=0
if othrLoan>0:
    year=int(input("Enter Year remaining for previous loan to pay:"))
asstval=int(input("Enter your Assets value(Ex.Equity Stocks value/other investments):"))
print("Your Creadit Score:",round(LoanCrdts(age,incm,othrLoan,year,asstval),4))
#print (round(a,3)) 