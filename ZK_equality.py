from zksk import Secret, DLRep
from zksk import utils

def ZK_equality(G,H):


  


    #Generate two El-Gamal ciphertexts (C1,C2) and (D1,D2)

    r1 = random.randrange(2,p)
    c1 = pow(g, r1, p)
    d1 = (m * pow(pk, r, p)) % p

    r2 = random.randrange(2,p)
    c2 = pow(G, r2, p)
    d2 = (m * pow(pk, r, p)) % p
    
    

    #Generate a NIZK proving equality of the plaintexts

    #Return two ciphertexts and the proof
    return (C1,C2), (D1,D2), zk_proof

