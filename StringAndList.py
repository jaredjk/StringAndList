
words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
print words.replace('day', 'month',1)

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello", 2,54,-2,7,12,98,"world"]
print x[0]
print x[-1]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x.sort() # so this sort from low number to high. and print.
def split_list(x):  # make function and new var(split_list(x) just a new name.can be anything.a)
    half = len(x)/2 # i divid it in half which is divid by 2 . not the number but the whole []
    return x[:half],x[half:] #this shows the output of after dividing the [] so : before half and : after half shows that its first half and second half.

a, b = split_list(x) # new var a, b. which automatically directs to :half and half:
b.insert(0,a)   # so we need to have the half go into the first index in array. so we use the insert function. and put x.insert. i put b since my half is set to b.
print (b) #and (0,a) means insert in index 0.(it doesnt replace the index 0 like javascript. in python it makes space at 0 and push other index back.)
# so make 0 index in a which is another half. so 
# (0,a) means make index 0 in a array(other half i split)
# that insert into b. since i have set b.insert. so b in 0index of a array. we need to get use to the python language since its different. i googled a lot to write how i want.
# i dont know what + hold does. 
# len = length
