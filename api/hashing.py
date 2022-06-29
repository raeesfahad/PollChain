from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



class Hash():

    def HashPassword(password : str):

        return password_context.hash(password)
    
    
    def DeHashPassword(plaintext,hashed):
        
        return password_context.verify(plaintext, hashed)
