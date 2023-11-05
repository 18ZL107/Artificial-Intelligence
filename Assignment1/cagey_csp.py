# =============================
# Student Names:Irving Wu 20130998 Alisa Liu 20155349
# Group ID:117
# Date:2022.2.12
# =============================
# CISC 352 - W22
# cagey_csp.py
# desc:
#

#Look for #IMPLEMENT tags in this file.
'''
All models need to return a CSP object, and a list of lists of Variable objects
representing the board. The returned list of lists is used to access the
solution.

For example, after these three lines of code

    csp, var_array = binary_ne_grid(board)
    solver = BT(csp)
    solver.bt_search(prop_FC, var_ord)

var_array is a list of all variables in the given csp. If you are returning an entire grid's worth of variables
they should be arranged in a linearly, where index 0 represents the top left grid cell, index n-1 represents
the top right grid cell, and index (n^2)-1 represents the bottom right grid cell. Any additional variables you use
should fall after that (i.e., the cage operand variables, if required).

1. binary_ne_grid (worth 10/100 marks)
    - A model of a Cagey grid (without cage constraints) built using only
      binary not-equal constraints for both the row and column constraints.

2. nary_ad_grid (worth 10/100 marks)
    - A model of a Cagey grid (without cage constraints) built using only n-ary
      all-different constraints for both the row and column constraints.

3. cagey_csp_model (worth 20/100 marks)
    - a model of a Cagey grid built using your choice of (1) binary not-equal, or
      (2) n-ary all-different constraints for the grid, together with Cagey cage
      constraints.


Cagey Grids are addressed as follows (top number represents how the grid cells are adressed in grid definition tuple);
(bottom number represents where the cell would fall in the var_array):
+-------+-------+-------+-------+
|  1,1  |  1,2  |  ...  |  1,n  |
|       |       |       |       |
|   0   |   1   |       |  n-1  |
+-------+-------+-------+-------+
|  2,1  |  2,2  |  ...  |  2,n  |
|       |       |       |       |
|   n   |  n+1  |       | 2n-1  |
+-------+-------+-------+-------+
|  ...  |  ...  |  ...  |  ...  |
|       |       |       |       |
|       |       |       |       |
+-------+-------+-------+-------+
|  n,1  |  n,2  |  ...  |  n,n  |
|       |       |       |       |
|n^2-n-1| n^2-n |       | n^2-1 |
+-------+-------+-------+-------+

Boards are given in the following format:
(n, [cages])

n - is the size of the grid,
cages - is a list of tuples defining all cage constraints on a given grid.


each cage has the following structure
(v, [c1, c2, ..., cm], op)

v - the value of the cage.
[c1, c2, ..., cm] - is a list containing the address of each grid-cell which goes into the cage (e.g [(1,2), (1,1)])
op - a flag containing the operation used in the cage (None if unknown)
      - '+' for addition
      - '-' for subtraction
      - '*' for multiplication
      - '/' for division
      - '?' for unknown/no operation given

An example of a 3x3 puzzle would be defined as:
(3, [(3,[(1,1), (2,1)],"+"),(1, [(1,2)], '?'), (8, [(1,3), (2,3), (2,2)], "+"), (3, [(3,1)], '?'), (3, [(3,2), (3,3)], "+")])

'''

from cspbase import *
from itertools import *

def binary_ne_grid(cagey_grid):
    n = cagey_grid[0]

    # create the variables' list to represent the board
    variables = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(Variable("Cell({},{})".format(i+1,j+1), domain = list(range(1, n+1))))
        variables.append(row)

    # create a complete list of satisfied tuples
    tuples = []
    for i in list(range(1, n+1)):
        for j in list(range(1, n+1)):
            if i != j:
                tuples.append((i,j))

    # create constraints
    constraints = []
    for i in range(n):
        for j in range(n):
            for k in range(j+1, n):
                # only check for two adjacent cells
                if (k == j+1):
                    # row constraints
                    row_constraint = Constraint("r{}c{}, r{}c{}".format(i+1,j+1,i+1,k+1), [variables[i][j], variables[i][k]])
                    row_constraint.add_satisfying_tuples(tuples)
                    constraints.append(row_constraint)

                    # column constraints
                    column_constraint = Constraint("r{}c{}, r{}c{}".format(j+1,i+1,k+1,i+1), [variables[j][i], variables[k][i]])
                    column_constraint.add_satisfying_tuples(tuples)
                    constraints.append(column_constraint)

    # create CSP object
    csp_list = []
    for rows in variables:
        for var in rows:
            csp_list.append(var)
    csp_object = CSP('binary_ne', csp_list)
    for con in constraints:
        csp_object.add_constraint(con)

    return csp_object,csp_list




def nary_ad_grid(cagey_grid):
    namelist=[]#build a list for pass name to Variable(name,domain)
    varlist=[]#build a list for collecting variables
    n=cagey_grid[0]#get Cagey row,column grids' numbers
    row=1
    while row<=n:#add name to name list
        column=1
        while column<=n:
            namelist.append("Cell("+str(row)+","+str(column)+")")
            column=column+1
        row=row+1
    for name in namelist:#build Variable_list for pass vars to Variable(name,vars)
        varlist.append(Variable(name,list(range(1,n+1))))
    CSPins=CSP(str(n*n),varlist)#instantiate CSP 
    rowlist=[]
    columnlist=[]
    index=0
    while index<n*n: # add n-ary all-different constraints for column
        rowlist.append(varlist[index:index+n])
        index=index+n
    for index2 in range(n):# add n-ary all-different constraints for column
        column=[]
        while index2<len(varlist):
            column.append(varlist[index2])
            index2=index2+n
        columnlist.append(column)
    Constraintlist=[]
    cagelist=rowlist+columnlist
    for scope in cagelist: #add constraint list
        Constraintlist.append(Constraint("nary_ad_grid",scope))

    for Constrain in Constraintlist:# add add_satisfying_tuples for constraint
        Constraintuple=[]
        do=[]
        for i in range(n):
            do.append(i+1)
        for Constu in permutations(do):
            Constraintuple.append(Constu)
        Constrain.add_satisfying_tuples(Constraintuple)
    for Constrain in Constraintlist:
        CSPins.add_constraint(Constrain)
                
    return CSPins,varlist

    




def cagey_csp_model(cagey_grid):
    CSPins,varlist=nary_ad_grid(cagey_grid) #call nary_ad_grid
    rowlist=[]
    n=cagey_grid[0]
    index=0
    while index<n*n: #build a rowlist for order the variables
        rowlist.append(varlist[index:index+n])
        index=index+n
    for cages in cagey_grid[1]: 
        a,b,c=cages
        scopelist=[]
        for pairs in b:
            e,f=pairs
            scopelist.append(rowlist[e-1][f-1])
        Constraints=Constraint("cage",scopelist)
        domainlist=[]
        domainlists=[]
        tuplelists=[]
        answerlists=[]
        #build lists use for itertools.product([])
        for i in range(n):
            domainlist.append(i+1)
        varnum=len(b)
        for i in range(varnum):
            domainlists.append(domainlist)
        for i in product(*domainlists): #find all possiable combination of numbers under cage constraints
            tuplelists.append(i)
        for dom in tuplelists:#check cage constraints
            if (c=="+"):
                if (sum(list(dom))==a):
                    answerlists.append(dom)
            elif (c=="*"):
                prod=1
                for num in dom:
                    prod=prod*num
                if (prod==a):
                    answerlists.append(dom)
            elif (c=="-"):
                for num in permutations(dom):
                    sub=num[0]
                    for n in range(1,len(num)):
                        sub=sub-num[n]
                    if (sub==a):
                        answerlists.append(dom)
            elif (c=="/"):
                for num in permutations(dom):
                    div=num[0]
                    for n in range(1,len(num)):
                        div=sub-div[n]
                    if (div==a):
                        answerlists.append(dom)
            else:
                if (sum(list(dom))==a):
                    answerlists.append(dom)
                prod=1
                for num in dom:
                    prod=prod*num
                if (prod==a):
                    answerlists.append(dom)
                for num in permutations(dom):
                    sub=num[0]
                    for n in range(1,len(num)):
                        sub=sub-num[n]
                    if (sub==a):
                        answerlists.append(dom)
                for num in permutations(dom):
                    div=num[0]
                    for n in range(1,len(num)):
                        div=sub-div[n]
                    if (div==a):
                        answerlists.append(dom)
        Constraints.add_satisfying_tuples(answerlists)
        CSPins.add_constraint(Constraints)

    for cages in cagey_grid[1]:#add cage variable
        a,b,c=cages
        tupstringlist=[]
        for tup in b:
            tupstringlist.append(str(tup).replace(" ",""))
        String=""
        for i in tupstringlist:
            String=String+"Var-Cell"+i+", "
        Stringcut=String[0:len(String)-2]
        cagename="Cage_op("+str(a)+":"+c+":"+"["+Stringcut+"])"
        if cages[2]=="+":
            scopelist=["+"]
        elif cages[2]=="-":
            scopelist=["-"]
        elif cages[2]=="*":
            scopelist=["*"]
        elif cages[2]=="/":
            scopelist=["/"]
        else:
            scopelist=["+","-","*","/"]
        CSPins.add_var(Variable(cagename,scopelist))
    return CSPins,CSPins.get_all_vars()





