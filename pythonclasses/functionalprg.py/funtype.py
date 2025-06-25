#kwargs= keyword arguments

def add(**args):
    print(args)
    # to print values
    res=0 
    for k,v in args.items():
        res+=v
    print(res)

add(n1=19,n2=45,n3=46)
# when the add is called values are stored in key value pair
# o/p=>{'n1': 19, 'n2': 45, 'n3': 46}
