import hashlib

def read_dictionary(file_path):
      with open(file_path, 'r') as dictionary_file:
            return [line.strip()for line in dictionary_file]
      
def password_hash(password):
      return hashlib.sha256(password.encode()).hexdigest()

def crack_password(target_hash, dictionary):
      for word in dictionary:
            hashed_word = password_hash(word)
            if hashed_word == target_hash:
                  return word
      return None

if __name__ == "__main__":
      target_hash = "e06e309b66b35433fd311e9bab12a9843671de60cb122636d43ebd87754ded62"
      dictionary_file = "dictionary.txt"  #path to our dictionary file
      dictionary = read_dictionary("dictionary.txt")
      cracked_password = crack_password(target_hash, dictionary)

      if cracked_password:
            print("Password Cracked, Your password is:", (cracked_password))
      else:
            print("Password not found in the dictionary.")