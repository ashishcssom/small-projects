import string
import random
if __name__=="__main__":
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    getInputSize=int(input("Enter password length:"))
    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    print("Your password is","".join(random.sample(s,getInputSize)))
