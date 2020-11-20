

def printArray(arr):
    for i in range(0,len(arr)):
        print (arr[i])

def reverseArray(arr,start,end):
    while(start < end):
        if end <= len(arr)-1:
            tmp = arr[start]
            arr[start] = arr[end]
            arr[end]=tmp
            start+=1
            end=end-1
        else:
            print("enter end value equal or less than total length of array");
            break;
        print(len(arr))
    for i in range(0,len(arr)):
        print(arr[i])


def leftRotate(arr,d):
    n = len(arr)
    reverseArray(arr,0,d-1)
    reverseArray(arr,d,n-1)
    reverseArray(arr,0,n-1)


def Fibonacci(n):

    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)



def fibo(n):
    if (n<0):
        print ("FIB not a valid no:")
    elif (n==1):
        print ("FIB:", 0)
    elif(n==2):
        print ("FIB:", 1)
    else:
        a = 0;
        b = 1;
        for i in range(1,n):
            c=a+b;
            b=a;
            a=c;
            print("fib", b);
        print ('fibno.', a)

a_d = {"a":1}
a_d.update({"b":2})






if __name__ == '__main__':
 print ('Hi, This is Python 3.8');
 #print_p();
 #reverseArray([1,2,3,4,5],1,4);
 #printArray([1,2,3,4,5]);
 #leftRotate([1,2,3,4,5],5)
 print(Fibonacci(20))
 fibo(20)
 print (a_d)
 list_m = [1, 2, 3, 4, 5, "A", "b", "c", "d", 6, 7, 8]
 list_n=[]
 xx = 0
 for i in list_m:
     if isinstance(i, int):
         print(i)
         list_n.append(i)
         list_m.pop(xx)
         print(list_m)
     xx += 1
     print(list_n)
     print(list_m)


