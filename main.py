#============================== Daxil edilmiş ədədin Armstrong ədədi olub olmadığını yoxlamaq =========================#
def Number_Armstrong(num):
    sum=0
    temp=num
    n=len(str(num))

    while(temp>0):
        sonuncu_eded=temp % 10 ## Sonuncu ədədin tapılması ->Məsələn:407->7, 1563->3
        sum +=sonuncu_eded**n
        temp //=10 ## Sonuncu ədədi silir qalan ifadəni ədəd kimi götürür ->Məsələn:407->40, 1563->156

    if(num==sum):
        return True
    else:
        return False

num=int(input('Ədədi daxil edin: '))

if(Number_Armstrong(num)):
    print(num, "bir Armstrong ədədidir.")
else:
    print(num, "bir Armstrong ədədi deyil.")