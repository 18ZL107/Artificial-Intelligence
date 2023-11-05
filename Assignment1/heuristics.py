# =============================
# Student Names:Irving Wu 20130998 Alisa Liu 20155349
# Group ID:117
# Date:2022.2.12
# =============================
# CISC 352 - W22
# heuristics.py
# desc:
#


#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete problem solution.

'''This file will contain different constraint propagators to be used within
   the propagators

var_ordering == a function with the following template
    var_ordering(csp)
        ==> returns Variable

    csp is a CSP object---the heuristic can use this to get access to the
    variables and constraints of the problem. The assigned variables can be
    accessed via methods, the values assigned can also be accessed.

    var_ordering returns the next Variable to be assigned, as per the definition
    of the heuristic it implements.
   '''

def ord_dh(csp):
    ''' return variables according to the Degree Heuristic '''
    ord_dh = []
    unasgnvar = csp.get_all_unasgn_vars()
    for unasgn in unasgnvar:
        ord_dh.append([unasgn,unasgn.domain_size()])
    insertionSort(ord_dh)
    return ord_dh[-1][0]

def ord_mrv(csp):
    ''' return variable according to the Minimum Remaining Values heuristic '''
    mrvorder=[]
    # find all unasgn vars
    unasgnvar=csp.get_all_unasgn_vars()
    for unasgn in unasgnvar:
    # append [variable, variable.domain_size] in mrvorder
        mrvorder.append([unasgn,unasgn.domain_size()])
    # sort the list by variable.domain_size
    insertionSort(mrvorder) 
    return mrvorder[0][0]

            

def insertionSort(arr): #insertionSort function
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key[1] < arr[j][1] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


