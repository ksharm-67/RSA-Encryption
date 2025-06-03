import argparse

def generate_private_key(e, p, q):                                            #Generate private key (d)  
    p, q = q, p 

    phiN = (p - 1) * (q - 1)                                                  #Calculate phi(N)

    a = phiN                                                                  #Set a to phiN
    b = e                                                                     #Set b to e

    run = True

    x0, x1 = 1, 0                                                             #Initialise coefficients of d = ap + bq
    y0, y1 = 0, 1

    while (run == True):
        quo = a//b                                                            #Keep track of the quotient
        rem = a % b                                                           #Keep track of the remainder
    
        if rem == 0:
            d = y1 % phiN                                                     #If remainder is 0, set d to the previous quotient y1
            run = False                                                       #Exit the loop
        else:
            a, b = b, rem                                                     #Set a and b to the new b and remainder
            x0, x1 = x1, (x0 - quo*x1)                                        #Set x0 and x1 to the new x1 and x0 - quotient * x1
            y0, y1 = y1, (y0 - quo*y1)                                        #Set y0 and y1 to the new y1 and y0 - quotient * x1
 
    #print("e * d mod phi(N): ", (e * d) % phiN)
    return d

def decrypt(ciphertext, key, N):

    plaintext = pow(ciphertext, key, N)                                       #Decrypt using plaintext = ciphertext ^ key % N

    return plaintext;


def encrypt(plaintext, key, N):
    
    ciphertext = pow(plaintext, key, N)                                       #Encrypt using ciphertext = plaintext ^ key % N
     
    return ciphertext;

parser = argparse.ArgumentParser(description="RSA")                           #Parse the given arguments
parser.add_argument("--p_e", type=int)
parser.add_argument("--p_c", type=int)
parser.add_argument("--q_e", type=int)
parser.add_argument("--q_c", type=int)
parser.add_argument("--e_e", type=int)
parser.add_argument("--e_c", type=int)
parser.add_argument("--ciphertext", type=int)
parser.add_argument("--plaintext", type=int)
    
args = parser.parse_args()

p = pow(2, args.p_e) - args.p_c
q = pow(2, args.q_e) - args.q_c
e = pow(2, args.e_e) - args.e_c

#print("p: ", p)
#print("q: ", q)
#print("e: ", e)

d = generate_private_key(e, p, q)
#print("d: ", d)

N = p*q
print(decrypt(args.ciphertext, d, N), encrypt(args.plaintext, e, N), sep=",")


