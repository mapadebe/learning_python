# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:01:19 2020

@author: Martin
"""
#I commented out the user prompt crap because it is very annoying. 
"Part A: House Hunting"
#annual_salary=120000#float(input("What is your annual salary (in $)?:"))
#portion_saved=0.10#float(input("What percentge of your salary would you like to save?"))/100
#total_cost=1000000#float(input("What is the total cost of your dream home (in $)?:"))
#portion_down_payment=0.25
#initial_savings=0
#rate_of_return=0.04
#
#number_of_months=0
#
##I think it's best to define a function here which takes in all those things and outputs the amount of interest after a certain amount of time
#
#def savings(annual_salary, portion_saved, total_cost, initial_savings):
#    current_savings = initial_savings
#    number_of_months=0
#    while current_savings < portion_down_payment*total_cost:
#        interest=current_savings*rate_of_return/12
#        monthly_savings=portion_saved*annual_salary/12
#        current_savings=current_savings+monthly_savings+interest
#        number_of_months += 1
#    return number_of_months
#
#print(savings(annual_salary, portion_saved, total_cost, initial_savings))
#
"Part B: Saving, with a Raise"
#annual_salary=80000#float(input("What is your annual salary (in $)?:"))
#portion_saved=0.1#float(input("What percentge of your salary would you like to save?"))/100
#total_cost=800000#float(input("What is the total cost of your dream home (in $)?:"))
#semi_annual_raise=0.03#float(input("percentage raise?"))/100
#portion_down_payment=0.25
#initial_savings=0
#rate_of_return=0.04
#
#number_of_months=0
#
##I think it's best to define a function here which takes in all those things and outputs the amount of interest after a certain amount of time
#
#def savings(annual_salary, portion_saved, total_cost, initial_savings, semi_annual_raise):
#    current_savings = initial_savings
#    number_of_months=0
#    while current_savings < portion_down_payment*total_cost:
#        interest=current_savings*rate_of_return/12
#        monthly_savings=portion_saved*annual_salary/12
#        current_savings=current_savings+monthly_savings+interest
#        number_of_months += 1
#        if number_of_months % 6 ==0:
#            annual_salary=annual_salary*(1+semi_annual_raise)
#    return number_of_months
#
#print(savings(annual_salary, portion_saved, total_cost, initial_savings, semi_annual_raise))


"Part C: Finding the Right amount to save"
#In this section you need to modify the savings function to return how much you deviate from the amount and run the bisection method on that "departure function"

annual_salary=10000#float(input("What is your annual salary (in $)?:"))
#float(input("What percentge of your salary would you like to save?"))/100
total_cost=1000000#float(input("What is the total cost of your dream home (in $)?:"))
semi_annual_raise=0.03#float(input("percentage raise?"))/100
P_DP=0.25

    
def function(annual_salary, portion_saved,total_cost, portion_down_payment):
    '''Returns the difference between your savings and the down payment on your house '''
    initial_savings=0
    semi_annual_raise=0.07
    saving_duration=36
    current_savings = initial_savings
    number_of_months=0
    rate_of_return=0.04
    while number_of_months < saving_duration:
        interest=current_savings*rate_of_return/12
        monthly_savings=portion_saved*annual_salary/12
        current_savings=current_savings+monthly_savings+interest
        number_of_months += 1
        departure = current_savings-portion_down_payment*total_cost
        if number_of_months % 6 ==0:
            annual_salary=annual_salary*(1+semi_annual_raise)
    return departure

PS_UB=1
PS_LB=0
N=100
count=0
error=100

if function(annual_salary, PS_LB,total_cost, P_DP)*function(annual_salary, PS_UB,total_cost, P_DP)>=0:
    print("Its not possible to make the downpayment in 3 years")
for n in range(1,N+1):
    PS_m = (PS_UB+PS_LB)/2
    count += 1
    if function(annual_salary, PS_LB,total_cost, P_DP)*function(annual_salary, PS_m,total_cost, P_DP)<0:
        PS_LB=PS_LB
        PS_UB=PS_m
    elif function(annual_salary, PS_m,total_cost, P_DP)*function(annual_salary, PS_UB,total_cost, P_DP)<0:
        PS_LB=PS_m
        PS_UB=PS_UB
    if abs(function(annual_salary, PS_m,total_cost, P_DP))<error:
        print(PS_m,count)
        break

        
