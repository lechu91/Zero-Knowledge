from zksk import Secret, DLRep
from zksk import utils

def ZK_equality(G,H):

    #Generate two El-Gamal ciphertexts (C1,C2) and (D1,D2)
    
    print(G)
    print(type(G))
    print(H)
    print(type(H))
    
    r1 = Secret()
    r2 = Secret()
    
    m = Secret()
    print(m)
    
    print(r1)
    print(r2)
        
    C1 = r1 * G
    C2 = r1 * H + m * G
    D1 = r2 * G
    D2 = r2 * H + m * G
    
    print(C1)
    print(C2)
    print(D1)
    print(D2)
    
    #Generate a NIZK proving equality of the plaintexts
    
    stmt = DLRep(C1,r1*G) & DLRep(C2,r1*H+m*G) & DLRep(D1,r2*G) & DLRep(D2,r2*H+m*G)
    zk_proof = stmt.prove()

    #Return two ciphertexts and the proof
    return (C1,C2), (D1,D2), zk_proof
