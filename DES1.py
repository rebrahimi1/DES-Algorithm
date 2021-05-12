{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "########################################\n",
      "#############  Encryption  #############\n",
      "########################################\n",
      "\n",
      "Original Text: 341289576BAECD71\n",
      "After inital permutation D88B69DC64B1743A\n",
      "\n",
      "Key for round 1 : 7832A5BFE86C\n",
      "-0.012978400000065449\n",
      "After Round 1 : 64B1743A1B173371\n",
      "\n",
      "Key for round 2 : 69BC64434E2F\n",
      "-0.009418299999992996\n",
      "After Round 2 : 1B17337156674B02\n",
      "\n",
      "Key for round 3 : C0ECDADE3998\n",
      "-0.005356800000072326\n",
      "After Round 3 : 56674B02728E1400\n",
      "\n",
      "Key for round 4 : 74E732A1537D\n",
      "-0.0008160999999518026\n",
      "After Round 4 : 728E1400A5689976\n",
      "\n",
      "Key for round 5 : E69D0353BAA2\n",
      "0.016134900000110974\n",
      "After Round 5 : A568997673E3312A\n",
      "\n",
      "Key for round 6 : 6BA257F40D3D\n",
      "0.015034299999911127\n",
      "After Round 6 : 73E3312AD4514E5B\n",
      "\n",
      "Key for round 7 : 2DD49A0B3ADE\n",
      "-0.005409399999962261\n",
      "After Round 7 : D4514E5BA4C7E09C\n",
      "\n",
      "Key for round 8 : 7601FA75F1B1\n",
      "-0.011696200000073986\n",
      "After Round 8 : A4C7E09C23E3BCFB\n",
      "\n",
      "Key for round 9 : 12DBF1BEEA0D\n",
      "-0.0015768999999181688\n",
      "After Round 9 : 23E3BCFB97B37DE5\n",
      "\n",
      "Key for round 10 : 9D79437257D2\n",
      "0.030156299999930525\n",
      "After Round 10 : 97B37DE5104F597A\n",
      "\n",
      "Key for round 11 : 2367CD9DA12B\n",
      "-0.008740299999999479\n",
      "After Round 11 : 104F597A3248AF73\n",
      "\n",
      "Key for round 12 : 595585E67E40\n",
      "0.00033329999996567494\n",
      "After Round 12 : 3248AF7374F393B1\n",
      "\n",
      "Key for round 13 : 5189F978A37E\n",
      "-0.012699099999963437\n",
      "After Round 13 : 74F393B1CEA4D89F\n",
      "\n",
      "Key for round 14 : 95E0A7B5DC8A\n",
      "-0.010407999999983986\n",
      "After Round 14 : CEA4D89FC8EECFED\n",
      "\n",
      "Key for round 15 : B30F864C3673\n",
      "0.01017740000008871\n",
      "After Round 15 : C8EECFEDC56C3542\n",
      "\n",
      "Key for round 16 : 623E0BF8D1B1\n",
      "0.05184489999999187\n",
      "After Round 16 : C56C354214391964\n",
      "\n",
      "Cipher Text :  9C02E9345C39A380\n",
      "0.03546440000002349\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "########################################\n",
      "#############  Decryption  #############\n",
      "########################################\n",
      "\n",
      "Cipher Text: 9C02E9345C39A380\n",
      "After inital permutation 14391964C56C3542\n",
      "\n",
      "Key for round 1 : 623E0BF8D1B1\n",
      "-0.00984619999996994\n",
      "After Round 1 : C56C3542C8EECFED\n",
      "\n",
      "Key for round 2 : B30F864C3673\n",
      "-0.017601899999931447\n",
      "After Round 2 : C8EECFEDCEA4D89F\n",
      "\n",
      "Key for round 3 : 95E0A7B5DC8A\n",
      "-0.009737500000028376\n",
      "After Round 3 : CEA4D89F74F393B1\n",
      "\n",
      "Key for round 4 : 5189F978A37E\n",
      "-0.010097200000018347\n",
      "After Round 4 : 74F393B13248AF73\n",
      "\n",
      "Key for round 5 : 595585E67E40\n",
      "0.010807199999931072\n",
      "After Round 5 : 3248AF73104F597A\n",
      "\n",
      "Key for round 6 : 2367CD9DA12B\n",
      "-0.02201900000011392\n",
      "After Round 6 : 104F597A97B37DE5\n",
      "\n",
      "Key for round 7 : 9D79437257D2\n",
      "-0.008182400000009693\n",
      "After Round 7 : 97B37DE523E3BCFB\n",
      "\n",
      "Key for round 8 : 12DBF1BEEA0D\n",
      "-0.0066276999999672626\n",
      "After Round 8 : 23E3BCFBA4C7E09C\n",
      "\n",
      "Key for round 9 : 7601FA75F1B1\n",
      "-0.0067262999999684325\n",
      "After Round 9 : A4C7E09CD4514E5B\n",
      "\n",
      "Key for round 10 : 2DD49A0B3ADE\n",
      "-0.03103289999990011\n",
      "After Round 10 : D4514E5B73E3312A\n",
      "\n",
      "Key for round 11 : 6BA257F40D3D\n",
      "0.019641499999920597\n",
      "After Round 11 : 73E3312AA5689976\n",
      "\n",
      "Key for round 12 : E69D0353BAA2\n",
      "-0.007696000000123604\n",
      "After Round 12 : A5689976728E1400\n",
      "\n",
      "Key for round 13 : 74E732A1537D\n",
      "-0.017072899999902802\n",
      "After Round 13 : 728E140056674B02\n",
      "\n",
      "Key for round 14 : C0ECDADE3998\n",
      "-0.039925900000071124\n",
      "After Round 14 : 56674B021B173371\n",
      "\n",
      "Key for round 15 : 69BC64434E2F\n",
      "-0.006690499999990607\n",
      "After Round 15 : 1B17337164B1743A\n",
      "\n",
      "Key for round 16 : 7832A5BFE86C\n",
      "-0.0038792999999941458\n",
      "After Round 16 : 64B1743AD88B69DC\n",
      "\n",
      "Plain Text :  341289576BAECD71\n",
      "-0.02287599999988288\n",
      "01100000011110001110111010100011010011001100111100110101\n",
      "\n",
      "Run Time for Key: -0.0012381000000232234\n"
     ]
    }
   ],
   "source": [
    "import timeit\n",
    "# convert hex to 4 bit binary\n",
    "def hex2bin(s):\n",
    "  return ''.join([format(int(c, 16), '04b') for c in s])\n",
    "\t\n",
    "import time\n",
    "# convert binary string to hex string\n",
    "def bin2hex(s):\n",
    "  return ''.join([format(int(s[i:i+4], 2), '01x').upper() for i in range(0,len(s),4)])\n",
    "\n",
    "\n",
    "# convert binary number to decimal number\n",
    "def bin2dec(binary):\n",
    "  # binary is a integer but in form 10, 110 etc.\n",
    "\treturn int(str(binary), 2)\n",
    "\n",
    "\n",
    "# convert decimal to binary conversion\n",
    "def dec2bin(num):\n",
    "\treturn format(num, '04b')\n",
    "\n",
    "\n",
    "# This method rearrange the bits as per the given order on the bitMap\n",
    "def rearrangeBits(bits, bitMap, n):\n",
    "\treturn ''.join([bits[bitMap[i] - 1] for i in range(0, n)])\n",
    "\n",
    "\n",
    "# shifting the bits towards left by nth shifts\n",
    "def shiftLeft(k, nBits):\n",
    "\treturn k[nBits:]\t+ k[:nBits]\n",
    "\n",
    "\n",
    "# calculating xow of two strings of binary number a and b\n",
    "def xor(a, b):\n",
    "  l = max(len(a), len(b))\n",
    "  return format(int(a, 2) ^ int(b, 2), '0' + str(l) + 'b')\n",
    "\n",
    "\n",
    "# This method performs the initial permutation on the provided input text\n",
    "def performInitialPermutation(inputText):\n",
    "  # BitMap on basis of which bits need to be rearranged.\n",
    "  initialPermTable = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54,\n",
    "              46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33,\n",
    "              25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21,\n",
    "              13, 5, 63, 55, 47, 39, 31, 23, 15, 7]\n",
    "  return rearrangeBits(inputText, initialPermTable, 64)\n",
    "\n",
    "\n",
    "# This method performs the final permutation on the provided input text\n",
    "def performFinalPermutation(inputText):\n",
    "  # Final Permutaion Table\n",
    "  finalPermTable = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, \n",
    "              38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, \n",
    "              4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, \n",
    "              42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]\n",
    "  return rearrangeBits(inputText, finalPermTable, 64)\n",
    "  \n",
    "\n",
    "# This method performs the expansion on the provided text of 32 bits and converts\n",
    "# it to 48 bits. Known as DBox expansion.\n",
    "def performaExpansionPermutation(inputText):\n",
    "  bitRearrangingMap = [32, 1, 2 , 3 , 4 , 5 , 4 , 5, 6 , 7 , 8 , 9 , 8 , 9 , 10, 11, 12,\n",
    "              13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23,\n",
    "              24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]\n",
    "  return rearrangeBits(inputText, bitRearrangingMap, 48)\n",
    "\n",
    "\n",
    "# This method takes a 64 bit and geerates a 56 bit key out of it.\n",
    "def generate56BitKey(key64Bit):\n",
    "  bitRearrangingMap = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, \n",
    "              51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, \n",
    "              15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13,\n",
    "              5, 28, 20, 12, 4]\n",
    "  return rearrangeBits(key64Bit, bitRearrangingMap, 56)\n",
    "\n",
    "\n",
    "# This method compresses the 56 bit key for a given round into 48 bit keys.\n",
    "def performKeyTransformation(key56Bit, roundIndex):\n",
    "  bitRearrangingMap = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8,\n",
    "              16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,\n",
    "              44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]\n",
    "\n",
    "  # Shifting the bits for left and right part and then join them back\n",
    "  for round in range(roundIndex + 1):\n",
    "    left = shiftLeft(key56Bit[:28], 1 if round in [0, 1, 8, 15] else 2)\n",
    "    right = shiftLeft(key56Bit[28:56], 1 if round in [0, 1, 8, 15] else 2)\n",
    "    key56Bit = left + right\n",
    "  return rearrangeBits(key56Bit, bitRearrangingMap, 48)\n",
    "\n",
    "\n",
    "# This method performs PBox permutation so that 32 bits are rearranged.\n",
    "def performPBoxPermutation(sboxText):\n",
    "  bitRearrangingMap = [ 16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,\n",
    "                        2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]\n",
    "  return rearrangeBits(sboxText, bitRearrangingMap, 32)\n",
    "\n",
    "\n",
    "# This method performs SBox substitution to generate a 32 bit text from a 48bit text\n",
    "def performSBoxSubstitution(xorText):\n",
    "  sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],\n",
    "\t\t  [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],\n",
    "\t\t  [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],\n",
    "\t\t  [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],\n",
    "\t\t\t\n",
    "\t\t[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],\n",
    "\t\t\t[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],\n",
    "\t\t\t[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],\n",
    "\t\t  [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],\n",
    "\t\n",
    "\t\t[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],\n",
    "\t\t  [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],\n",
    "\t\t  [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],\n",
    "\t\t\t[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],\n",
    "\t\t\n",
    "\t\t[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],\n",
    "\t\t  [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],\n",
    "\t\t  [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],\n",
    "\t\t\t[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],\n",
    "\t\t\n",
    "\t\t[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],\n",
    "\t\t  [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],\n",
    "\t\t\t[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],\n",
    "\t\t  [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],\n",
    "\t\t\n",
    "\t\t[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],\n",
    "\t\t  [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],\n",
    "\t\t\t[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],\n",
    "\t\t\t[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],\n",
    "\t\t\n",
    "\t\t[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],\n",
    "\t\t  [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],\n",
    "\t\t\t[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],\n",
    "\t\t\t[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],\n",
    "\t\t\n",
    "\t\t[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],\n",
    "\t\t\t[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],\n",
    "\t\t\t[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],\n",
    "\t\t\t[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]\n",
    "\n",
    "  result = \"\"\n",
    "  for j in range(0, 8):\n",
    "    section = xorText[j*6: j*6+6]\n",
    "    row = bin2dec(int(section[0] + section[5]))\n",
    "    col = bin2dec(int(section[1: 5]))\n",
    "    val = sbox[j][row][col]\n",
    "    result += dec2bin(val)\n",
    "  return result\n",
    "\n",
    "# This method runs the algorithm for 16 rounds using the provided inputText and 56BitKey.\n",
    "# This method can be used to encrypt or decrypt the inputText\n",
    "def runAlgorithm(inputText, key56Bit, decrypt=False):\n",
    "  \n",
    "\t# Perform Initial Permutation\n",
    "\tinputText = performInitialPermutation(hex2bin(inputText))\n",
    "\t\n",
    "\tprint(\"After inital permutation\", bin2hex(inputText))\n",
    "\t\n",
    "\t# Split left and right section\n",
    "\tleft, right = inputText[:32], inputText[32:64]\n",
    "\n",
    "  # Running 16 rounds.\n",
    "\tfor i in range(0, 16):\n",
    "    # Find key for current round\n",
    "\t\troundKey = performKeyTransformation(key56Bit, (15 - i) if decrypt else i)\n",
    "\t\tstt = timeit.timeit()\n",
    "\t\tprint(\"\\nKey for round\", i + 1, \":\", bin2hex(roundKey))\n",
    "\t\tendr = timeit.timeit()\n",
    "\t\tprint(endr - stt)\n",
    "\n",
    "\n",
    "\t\t# We are trying to expand the 32 bit of right Plain text into 48 bits.\n",
    "\t\trightExpanded = performaExpansionPermutation(right)\n",
    "\t\t\n",
    "\t\t# XOR 48bit RoundKey with 48bit right text\n",
    "\t\txorText = xor(rightExpanded, roundKey)\n",
    "\n",
    "\t\tsboxText = performSBoxSubstitution(xorText)\n",
    "\t\tpboxText = performPBoxPermutation(sboxText)\n",
    "\t\t\n",
    "\t\tleft = xor(left, pboxText)\n",
    "\t\t\n",
    "\t\t# Swap left and right part\n",
    "\t\tleft, right = right, left\n",
    "\t\tprint(\"After Round\", i + 1, \":\", bin2hex(left + right))\n",
    "\t\t\n",
    "\t# perform final permutation to get the result. Note that because of last swap\n",
    "  # Left and right section are swapped. So right section comes first now.\n",
    "\tprint()\n",
    "\treturn performFinalPermutation(right + left)\n",
    "\n",
    "\n",
    "def main():\n",
    "  # Both Key and plainText are 16 characters in hex, which means 64 bit values.\n",
    "  plainText = \"341289576BAECD71\"\n",
    "  key = \"192837654BFAED3C\"\n",
    "\n",
    "  # Convert key to binary 64 bits.\n",
    "  key = hex2bin(key)\n",
    "  \n",
    "  # Generate 56 bits key from 64 bits key\n",
    "  key56Bit = generate56BitKey(key)\n",
    "\n",
    "  # Perform encryption\n",
    "  start = timeit.timeit()  \n",
    "  print(\"#\" * 40)\n",
    "  print(\"#############  Encryption  #############\")\n",
    "  print(\"#\" * 40, end='\\n\\n')\n",
    "  print('Original Text:', plainText)\n",
    "  cipherText = bin2hex(runAlgorithm(plainText, key56Bit))\n",
    "  print(\"Cipher Text : \",cipherText)\n",
    "  end = timeit.timeit()\n",
    "  print(end - start)\n",
    "  print('\\n\\n\\n\\n')\n",
    "\n",
    "    \n",
    "  # Perform decryption\n",
    "  st = timeit.timeit()\n",
    "  print(\"#\" * 40)\n",
    "  print(\"#############  Decryption  #############\")\n",
    "  print(\"#\" * 40, end='\\n\\n')\n",
    "  print('Cipher Text:', cipherText)\n",
    "  text = bin2hex(runAlgorithm(cipherText, key56Bit, decrypt=True))\n",
    "  print(\"Plain Text : \",text)\n",
    "  en = timeit.timeit()\n",
    "  print(en - st)\n",
    "  stk = timeit.timeit()\n",
    "  print(key56Bit)\n",
    "  enk = timeit.timeit()\n",
    "  print(\"\\nRun Time for Key:\", enk - stk)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "  main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}