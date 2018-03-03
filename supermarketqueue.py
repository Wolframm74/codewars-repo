#https://github.com/Wolframm74/codewars-repo
#https://www.codewars.com/kata/the-supermarket-queue/train/python

#e.g.1 
# <== sum (5, 3, 4)=12

#e.g.2
# <== sum (10)
# <== sum (2,3,3)=8

#e.g.2
# <== sum (2)=2
# <== sum (3)=3
# <== sum (2+10)=12

class Till():
    def __init__(self):
        self.current_size=0
        self.absolute_time_ctr=0
        self.get_new_customer=False
        self.till_queuelist=[]

    def empty_queue(self):
        self.current_size=self.till_queuelist[0]
        self.till_queuelist.pop(0)

    def decrement_current_size(self, customers_to_serve_flag):

        if (self.current_size>0):
            self.current_size-=1
            self.absolute_time_ctr+=1
        if (self.current_size==0):
            if (customers_to_serve_flag):
                self.get_new_customer=True

def queue_time(customers, n):

    customers_to_serve=customers[:]

    if(customers==[]):
        return 0

    if (n==1):
        return sum(customers)

    if (len(customers)==1):
        return sum(customers)

    l=len(customers)
    
    print(customers)
    print("the number of customers is", l)
    print("customers[0] is", customers[0])

    print("the number of Tills is", n)

    my_objects = []

    n_target=min([n,l])

    if (n>l):
        return max(customers)

    for i in range(n):
        print("index is", i)
        my_objects.append(Till())
        my_objects[i].current_size=customers[i]
        print("current_size is", my_objects[i].current_size)
        #set the current size of the ith object to the ith queue element

    all_customers_served=False

    sum_current_size=0

    customers_to_serve_flag = True

    while_ctr=0

    if (n<l):
        customers_to_serve=customers[n:]

    while not(all_customers_served):

        #something wrong
        for i in range(n):

            #add it to the queuelist
            if ( my_objects[i].current_size == 0 ):

                #figure out the scenario in which we need to append
                if (customers_to_serve):
                    my_objects[i].till_queuelist.append(customers_to_serve[0])
                    my_objects[i].empty_queue()

            
            #if the ith queue is now empty, get the new queue of customers and add it to the ith Till.
            #if the list of customers is now empty then skip, we have no more queue's to add to our Tills.
            #if (my_objects[i].get_new_customer==True and not customers  ):
            if (my_objects[i].get_new_customer==True):

                #you don't want to get the ith element of customers. Need to create a so called customers_to_serve list, and pop the element off that.
                if (customers_to_serve):
                    my_objects[i].current_size=customers_to_serve[0]

                if (customers_to_serve):

                    customers_to_serve_flag = True
                    
                    #remove the first element
                    customers_to_serve.remove(customers_to_serve[0])        
                    my_objects[i].get_new_customer=False

            if not(customers_to_serve):
                customers_to_serve_flag = False

            my_objects[i].decrement_current_size(customers_to_serve_flag)

        if not(customers_to_serve_flag):

            sum_current_size=0       
            for i in range(n):
                sum_current_size=sum_current_size+my_objects[i].current_size

            if (sum_current_size==0):
                all_customers_served=True

        while_ctr+=1            
    
    print(my_objects[0].absolute_time_ctr)

    #Check which of the n tills is biggest
    till_list=[]

    if (n>1):
        for i in range(n):
            till_list.append(my_objects[i].absolute_time_ctr)
    else:
        return my_objects[0].absolute_time_ctr
   
    print(till_list)

    return max(till_list)


if _name_ == "_main_":

    x=queue_time([2,2,3,3,4,4], 2)
    #x=queue_time([1,2,3,4,5], 1)
    #x=queue_time([1,2,3,4,5], 100)
    #x=queue_time([47, 40, 3, 3, 4, 36, 10, 50, 4, 5, 23, 45, 3, 1, 43, 20, 41, 46], 6)


    print("the value of x is "+str(x))