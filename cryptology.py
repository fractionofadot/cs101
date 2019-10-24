import string

def letterFQ(phrase):
	phrase = str(phrase)
	letter_count = {}
	for c in phrase:
		if c in string.ascii_letters:
			try:
				letter_count[c] += 1
			except:
				letter_count[c] = 1
	return letter_count

def siftc(phrase, key):
	letters = string.ascii_lowercase
	e = ''
	for c in phrase:
		if c not in letters:
			e = e + c
		else:
			e = e + letters[ (letters.find(c) + key) % 26 ]
	return e

def siftd(phrase, key):
	letters = string.ascii_lowercase
	d = ''
	for c in phrase:
		if c not in letters:
			d = d + c
		else:
			d = d + letters[ (letters.find(c) - key) % 26 ]
	return d	

def vigenere(message, key, decrypt=True):
	letters = string.ascii_lowercase
	keynum = [letters.find(c) for c in key]
	keylen = len(key)
	retval = ''
	for i in range( len(message) ):
		if not decrypt:
			retval = retval + letters[ ( letters.find(message[i]) + keynum[i%keylen] ) % 26 ]
		else:
			retval = retval + letters[ ( letters.find(message[i]) - keynum[i%keylen] ) % 26 ]
	return retval

def cv_encode(s):
	output = ''
	vowels = {"a","e","i","o","u","y"}
	for c in s:
		if c == " ":
			continue
		if c in vowels:
			output = output + '1'
		else:
			output = output + '0'
	return output

pbsq = [
['f','g','h','i','j','k'],
['e','x','y','z','0','l'],
['d','w','7','8','1','m'],
['c','v','6','9','2','n'],
['b','u','5','4','3','o'],
['a','t','s','r','q','p'],
]



news = "thewholegraingoodnessofbluechipdividendstockshasitslimitsutilitystocksconsumerstaplespipelinestelecomsandrealestateinvestmenttrustshavealllostgroundoverthepastmonthevenwhilethebroadermarkethasbeenflatwiththebondmarketsignallinganexpectationofrisinginterestratesthefiveyearrallyforsteadybluechipdividendpayershasstalledshouldyoubescaredifyouownalotofthesestockseitherdirectlyorthroughmutualfundsorexchangetradedfundsdavidbaskinpresidentofbaskinfinancialserviceshasatwoprongedanswerkeepyourtopqualitydividendstocksbutbepreparedtofollowhisfirmsexampleintrimmingholdingsinstockssuchastranscanadacorpkeyeracorpandpembinapipelinecorp"

codenum = [22,33,20,21,2,33,32,1,0,22,20,0,30,22,11,33,3,32,0,30,3,2,20,1,33,23,23,12,3,20,13,13,22,1,11,3,20,22,22,22,20,33,22,13,23,13,33,20,32,33,1,22,21,12,10,11,2,30,23,13,20,0,2,12,31,0,33,22,31,3,10,1,11,33,30,23,0,1,2,30,12,12,32,1,12,23,31,12,0,2,32,23,31,12,3,3,1,0,33,0,23,21,32,10,3,10,20,2,3,13,31,2,12,11,21,3,23,0,22,13,0,30,32,31,23,33,22,0,10,33,32,2,32,10,32,13,3,1,3,3,23,20,0,32,22,3,20,23,30,23,0,0,31,22,23,13,32,0]
binarycodenum = ["1010","1111","1000","1001","0010","1111","1110","0001","0000","1010","1000","0000","1100","1010","0101","1111","0011","1110","0000","1100","0011","0010","1000","0001","1111","1011","1011","0110","0011","1000","0111","0111","1010","0001","0101","0011","1000","1010","1010","1010","1000","1111","1010","0111","1011","0111","1111","1000","1110","1111","0001","1010","1001","0110","0100","0101","0010","1100","1011","0111","1000","0000","0010","0110","1101","0000","1111","1010","1101","0011","0100","0001","0101","1111","1100","1011","0000","0001","0010","1100","0110","0110","1110","0001","0110","1011","1101","0110","0000","0010","1110","1011","1101","0110","0011","0011","0001","0000","1111","0000","1011","1001","1110","0100","0011","0100","1000","0010","0011","0111","1101","0010","0110","0101","1001","0011","1011","0000","1010","0111","0000","1100","1110","1101","1011","1111","1010","0000","0100","1111","1110","0010","1110","0100","1110","0111","0011","0001","0011","0011","1011","1000","0000","1110","1010","0011","1000","1011","1100","1011","0000","0000","1101","1010","1011","0111","1110","0000"]

def compassToBinary(data):
	output = []
	for d in data:
		output.append(bin(str(d[0])) + bin(str(d[1])))
	return output

def codetobytes(arr):
	output = []
	for i in range(0,len(arr)-1,2):
		output.append(arr[i] + arr[i+1])
	return output

def pbfind(c):
	pbsq = [['f','g','h','i','j','k'],['e','x','y','z','0','l'],['d','w','7','8','1','m'],['c','v','6','9','2','n'],['b','u','5','4','3','o'],['a','t','s','r','q','p']]
	for i in range(len(pbsq)): 
		if c in pbsq[i]: return (i, pbsq[i].index(c))
	return None

def binpb(tup):
	return "{:03b}{:03b}".format(tup[0],tup[1])

def pbstr(s):
	output = []
	for c in s:
		output.append(binpb(pbfind(c)))
	return output

def xore(s1,s2):
	return "{:06b}".format( int(s1, 2) ^ int(s2, 2) )

def newsencode(input_array,enc_string):
	output = []
	binary_enc_string = cv_encode(enc_string)
	encode_len = len(binary_enc_string)
	input_len = len(input_array)
	while encode_len < input_len:
		binary_enc_string = binary_enc_string + binary_enc_string

	for i in range(input_len):
		output.append(xore(input_array[i], binary_enc_string[i*8:(i*8)+8]))
	return output

#encoded = newsencode(codetobytes(binarycodenum), news)


def binaryToPB(e):
	output = []
	for s in encoded:
		output.append( [int(s[0] + s[1],2), int(s[2] + s[3],2)] )
		output.append( [int(s[4] + s[5],2), int(s[6] + s[7],2)] )
	return output


# for pair in binaryToPB(encoded):
# 	print(pbsq[pair[0]][pair[1]], end='')

def encode_string(input_string, secret):
	secret_binary = cv_encode(secret) 
	input_binary = pbstr(input_string)
	while len(secret_binary) < len(input_binary):
		secret_binary = secret_binary + secret_binary
	output = []
	for i in range(len(input_binary)):
		t = len(input_binary[i])
		output.append(xore(input_binary[i], secret_binary[i*t:(i*t)+t]))
	return "".join(output)


def polybus_lookup(message,polybus):
	output = []
	for c in message.lower():	
		for i in range(len(polybus)): 
			if c in polybus[i]: output.append( ( i, polybus[i].index(c) ) )
	return output

def convertCoordinatesAndCombine(coordinates):
	output = ""
	for xy in coordinates:
		output = output + "{:03b}{:03b}".format(xy[0],xy[1])
	return output

def xorBinaryPad(binary_message, binary_pad):
	while len(binary_message) % 3:
		binary_message = binary_message + '0'
	while len(binary_pad) < len(binary_message):
		binary_pad = binary_pad + binary_pad
	binary_pad = binary_pad[:len(binary_message)]
	format_string = "{:0" + str(len(binary_message)) + "b}"
	return format_string.format( int(binary_message, 2) ^ int(binary_pad, 2) )

def compassRoseEncrypt(binary_input):
	output = []
	compass_rose_map = [["N","E","S","W"],["NW","SW","SE","NE"]]
	for i in range(0,len(binary_input),4):
		try:
			main_idx = binary_input[i] + binary_input[i+1]
			next_idx = binary_input[i+2] + binary_input[i+3]
			output.append((int(main_idx,2),int(next_idx,2)))
		except:
			pass
	return output
	
def compassRoseDecrypt(list_of_tuples):
	output = ""
	for t in list_of_tuples:
		format_string = "{:02b}{:02b}".format(t[0],t[1])

		output = output + format_string
	return output

def divide3bitPairs(binary_input):
	import sys
	output = []
	for i in range(0,len(binary_input),6):
		try:
			main_idx = "{:03b}".format(int(binary_input[i:i+3],2))
			next_idx = "{:03b}".format(int(binary_input[i+3:i+6],2))
			output.append((int(main_idx,2),int(next_idx,2)))
		except Exception as e:
			print(e)
			pass
	return output

def polybus_coordinate_lookup(list_of_coordinates, polybus):
	output = ""
	for xy in list_of_coordinates:
		try:
			output = output + polybus[xy[0]][xy[1]]
		except Exception as e:
			print(e)
	return output

def compassToNumbers(code,codekey):
	output = []
	for c in code:
		xy = codekey[c]
		output.append((int(xy[0]),int(xy[1])))
	return output


def encrypt(message, pad, polybus, debug=False):
	# 1. Find the coordinates of each letter in the polybus square (spiral). Ex: 'y' -> (1,2)
	# 2. Convert each digit to three-bit binary and combine. Ex: (1,2), (3,5) -> ('001', '010'), ('011', '101') -> '001010011101'
	# 3. Convert the pad to binary using the consonant/vowel method. Ex: "cat in the hat" -> '01010001010'
	# 4. Run xor on the message binary and the pad binary (repeat pad as needed). Ex: 0b001010011101 ^ 0b01010001010 = '011110001001'
	# 5. Convert 2-bits pairs to a compass rose: N=0,E=1,S=2,W=3 | SE=0,SW=1,NW=2,NE=3 
	# 		Ex: '011110001001' -> 01 11 10 00 10 01 -> (1,2), (2,0), (2,1) -> ENW SSE SSW
	coordinates = polybus_lookup(message, polybus)
	binary_message = convertCoordinatesAndCombine(coordinates)
	binary_pad = cv_encode(pad)
	xor_message = xorBinaryPad(binary_message, binary_pad)
	compass_rose = compassRoseEncrypt(xor_message)
	return compass_rose

def decrypt(list_of_tuples, pad, polybus, debug=False):
	# 1. Convert each compass rose digit to 2-bit binary and combine
	# 2. Convert the pad to binary using the consonant/vowel method. Ex: "cat in the hat" -> '01010001010'
	# 3. Run xor on the message binary and the pad binary (repeat pad as needed)
	# 4. Divide into 3-bit pairs(011,101)
	# 5. Find letters in polybus using the given coordinates.
	binary_compass = compassRoseDecrypt(list_of_tuples)
	binary_pad = cv_encode(pad)
	xor_message = xorBinaryPad(binary_compass, binary_pad)
	coordinates = divide3bitPairs(xor_message)
	message = polybus_coordinate_lookup( coordinates, polybus )
	return message

polybus = [['f','g','h','i','j','k'],['e','x','y','z','0','l'],['d','w','7','8','1','m'],['c','v','6','9','2','n'],['b','u','5','4','3','o'],['a','t','s','r','q','p']]
compass_rose = ["ddr","lur","dul","ddl","udr","lur","ldr","udl","uul","ddr","dul","uul","lul","ddr","rdl","lur","uur","ldr","uul","lul","uur","udr","dul","udl","lur","dur","dur","rdr","uur","dul","rur","rur","ddr","udl","rdl","uur","dul","ddr","ddr","ddr","dul","lur","ddr","rur","dur","rur","lur","dul","ldr","lur","udl","ddr","ddl","rdr","rul","rdl","udr","lul","dur","rur","dul","uul","udr","rdr","ldl","uul","lur","ddr","ldl","uur","rul","udl","rdl","lur","lul","dur","uul","udl","udr","lul","rdr","rdr","ldr","udl","rdr","dur","ldl","rdr","uul","udr","ldr","dur","ldl","rdr","uur","uur","udl","uul","lur","uul","dur","ddl","ldr","rul","uur","rul","dul","udr","uur","rur","ldl","udr","rdr","rdl","ddl","uur","dur","uul","ddr","rur","uul","lul","ldr","ldl","dur","lur","ddr","uul","rul","lur","ldr","udr","ldr","rul","ldr","rur","uur","udl","uur","uur","dur","dul","uul","ldr","ddr","uur","dul","dur","lul","dur","uul","uul","ldl","ddr","dur","rur","ldr","uul"]
codekey = {'rul' : "12", 'uul' : "02", 'uur' : "03", 'udr' : "00", 'ddl' : "21", 'ddr' : "20", 'rdl' : "11", 'rdr' : "10", 'lul' : "32", 'ldr' : "30", 'udl' : "01", 'rur' : "13", 'dul' : "22", 'dur' : "23", 'lur' : "33", 'ldl' : "31"}

code3 = compassToNumbers(compass_rose,codekey)

#code1 = encrypt("start", news, polybus, debug=True)

print(
	decrypt(code3, news, polybus)
	
)
