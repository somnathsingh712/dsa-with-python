class cwesar_cypher:
    def __init__(self,shift):
        encode=[None]*26
        decode=[None]*26

        for k in range(26):
            encode[k]=chr((k+shift)%26+ord('A'))
            decode[k]=chr((k-shift)%26+ord('A'))

        self._forward=''.join(encode)
        self._backward=''.join(decode)

    def encrypt(self,message):
        return self._transform(message,self._forward)
    
    def decrypt(self,message):
        return self._transform(message,self._backward)
    
    def _transform(self,original,code):
        msg=list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j=ord(msg[k])-ord('A')
                msg[k]=code[j]

        return ''.join(msg)



cipher=cwesar_cypher(5)
message="APPLE"
coded=cipher.encrypt(message)
print('coded'+coded)
answer=cipher.decrypt(coded)
print('decrypted'+answer)