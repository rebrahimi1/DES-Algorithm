import time
# convert hex to 4 bit binary
def hex2bin(s):
  return ''.join([format(int(c, 16), '04b') for c in s])
  
import time
# convert binary string to hex string
def bin2hex(s):
  return ''.join([format(int(s[i:i+4], 2), '01x').upper() for i in range(0,len(s),4)])


# convert binary number to decimal number
def bin2dec(binary):
  # binary is a integer but in form 10, 110 etc.
  return int(str(binary), 2)


# convert decimal to binary conversion
def dec2bin(num):
  return format(num, '04b')


# This method rearrange the bits as per the given order on the bitMap
def rearrangeBits(bits, bitMap, n):
  return ''.join([bits[bitMap[i] - 1] for i in range(0, n)])


# shifting the bits towards left by nth shifts
def shiftLeft(k, nBits):
  return k[nBits:]  + k[:nBits]


# calculating xow of two strings of binary number a and b
def xor(a, b):
  l = max(len(a), len(b))
  return format(int(a, 2) ^ int(b, 2), '0' + str(l) + 'b')


# This method performs the initial permutation on the provided input text
def performInitialPermutation(inputText):
  # BitMap on basis of which bits need to be rearranged.
  initialPermTable = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54,
              46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33,
              25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21,
              13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
  return rearrangeBits(inputText, initialPermTable, 64)


# This method performs the final permutation on the provided input text
def performFinalPermutation(inputText):
  # Final Permutaion Table
  finalPermTable = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 
              38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 
              4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 
              42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
  return rearrangeBits(inputText, finalPermTable, 64)
  

# This method performs the expansion on the provided text of 32 bits and converts
# it to 48 bits. Known as DBox expansion.
def performaExpansionPermutation(inputText):
  bitRearrangingMap = [32, 1, 2 , 3 , 4 , 5 , 4 , 5, 6 , 7 , 8 , 9 , 8 , 9 , 10, 11, 12,
              13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23,
              24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
  return rearrangeBits(inputText, bitRearrangingMap, 48)


# This method takes a 64 bit and geerates a 56 bit key out of it.
def generate56BitKey(key64Bit):
  bitRearrangingMap = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 
              51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 
              15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13,
              5, 28, 20, 12, 4]
  return rearrangeBits(key64Bit, bitRearrangingMap, 56)


# This method compresses the 56 bit key for a given round into 48 bit keys.
def performKeyTransformation(key56Bit, roundIndex):
  bitRearrangingMap = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8,
              16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
              44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

  # Shifting the bits for left and right part and then join them back
  for round in range(roundIndex + 1):
    left = shiftLeft(key56Bit[:28], 1 if round in [0, 1, 8, 15] else 2)
    right = shiftLeft(key56Bit[28:56], 1 if round in [0, 1, 8, 15] else 2)
    key56Bit = left + right
  return rearrangeBits(key56Bit, bitRearrangingMap, 48)


# This method performs PBox permutation so that 32 bits are rearranged.
def performPBoxPermutation(sboxText):
  bitRearrangingMap = [ 16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
                        2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
  return rearrangeBits(sboxText, bitRearrangingMap, 32)


# This method performs SBox substitution to generate a 32 bit text from a 48bit text
def performSBoxSubstitution(xorText):
  sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
      
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
  
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

  result = ""
  for j in range(0, 8):
    section = xorText[j*6: j*6+6]
    row = bin2dec(int(section[0] + section[5]))
    col = bin2dec(int(section[1: 5]))
    val = sbox[j][row][col]
    result += dec2bin(val)
  return result

# This method runs the algorithm for 16 rounds using the provided inputText and 56BitKey.
# This method can be used to encrypt or decrypt the inputText
sub_key_gen_time = 0
sub_key_gen_count = 0

def runAlgorithm(inputText, key56Bit, decrypt=False):
  
  # Perform Initial Permutation
  inputText = performInitialPermutation(hex2bin(inputText))
  
#   print("After inital permutation", bin2hex(inputText))
  
  # Split left and right section
  left, right = inputText[:32], inputText[32:64]

  # Running 16 rounds.
  for i in range(0, 16):
    global sub_key_gen_time
    global sub_key_gen_count
    # Find key for current round
    st = time.time()
    roundKey = performKeyTransformation(key56Bit, (15 - i) if decrypt else i)
    en = time.time()

    sub_key_gen_time += (en - st)
    sub_key_gen_count += 1

#     stt = time.time()
    print("\nKey for round", i + 1, ":", bin2hex(roundKey))
#     endr = time.time()
#     print(endr - stt)


    # We are trying to expand the 32 bit of right Plain text into 48 bits.
    rightExpanded = performaExpansionPermutation(right)
    
    # XOR 48bit RoundKey with 48bit right text
    xorText = xor(rightExpanded, roundKey)

    sboxText = performSBoxSubstitution(xorText)
    pboxText = performPBoxPermutation(sboxText)
    
    left = xor(left, pboxText)
    
    # Swap left and right part
    left, right = right, left
    print("After Round", i + 1, ":", bin2hex(left + right))
    
  # perform final permutation to get the result. Note that because of last swap
  # Left and right section are swapped. So right section comes first now.
#   print()
  return performFinalPermutation(right + left)


def main():
  # Both Key and plainText are 16 characters in hex, which means 64 bit values.
  plainText = "341289576BAECD71"
  key = "192837654BFAED3C"

  # Convert key to binary 64 bits.
  key = hex2bin(key)
  
  # Generate 56 bits key from 64 bits key
  key56Bit = generate56BitKey(key)

  # Perform encryption
  print("#" * 40)
  print("#############  Encryption  #############")
  print("#" * 40, end='\n\n')
  print('Original Text:', plainText)
  st = time.time()
  cipherText = bin2hex(runAlgorithm(plainText, key56Bit))
  en = time.time()
  print("Cipher Text : ",cipherText)
  print("Encryption Run Time : ", str(en - st), "seconds")
  print("Subkey Generation Time (Avg.) : ", str(sub_key_gen_time/sub_key_gen_count), "seconds")
  print('\n\n\n\n')

    
  # Perform decryption
  
  print("#" * 40)
  print("#############  Decryption  #############")
  print("#" * 40, end='\n\n')
  print('Cipher Text:', cipherText)
  st = time.time()
  text = bin2hex(runAlgorithm(cipherText, key56Bit, decrypt=True))
  en = time.time()
  print("Plain Text : ", text)
  print("Decryption Run Time : ", str(en - st), "seconds")
  print("Subkey Generation Time (Avg.) : ", str(sub_key_gen_time/sub_key_gen_count), "seconds")

if __name__ == '__main__':
  main()