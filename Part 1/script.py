import freqAnalysis, detectEnglish, itertools

MAX_KEY_LENGTH = 12
cipher1 = "zg bbr wh zh sstt? k dsbb, ewqb ou haqu, ccpy tb kk! o xcktf sijzm wp woohtaa! jmohamvzq fahbkfbt wg bjv tpff wh gwmzl! xupqicewizqbz pitwoss bv vys gcku qw oejxzvzgjbz! uker bzmmtzbh qamozqbzl qp kvf thzo ft gchl! diojbpiuywou lmozbbfl qp kvf thzo ft nswqc! tcohkwncse wlwnrhfr ucdszfg bv vys gcku qw gpqbin esukhzmj. ffoe? gql kbbm bq komy tjqlh ssttkkm? xs aixvb'u zbdgu wo oggvywou kmofhfzr knfgf hh qv jwoqx bjv hvfg wh kvf qxvvlfz! kx bwibfr bb qwt, uchs qlh uvx jckhffbmu, jbbqdmf fb b pto qw uncl, ejzzf kx bqjgfr mpg isnbtvvj wohh bjv swsk mzgoorbvi uindlbgi cg ham jlabb vwpuwuwhv. yv zjjx qp sfbbwmf ycvgxa, vioesfitbse pr kqidpftbkfbt, pnqnk co pbxqcos bnudvft, xnurzbh ii ipu rpkg wp uwhwmin uwtdeiaj, vzdgwvznjbz cu zbuc mpg swhuxav jzvaumt dooybvf yot somt jsfb. rww'u vbjx bq uwh dkmvkm esxx, mzrec, umhfff mhc erb gwgl cemuvbvi isbz. pm nzjf wg i mzbhrhu qw pvzeajzh, uvtb gmso mhc jrjf zbdgu wo thz hrf uch tqeu. tc wwp'k hfze ug rppim vqk pfwgo tvom: w'f vq cstg kmcc hiog bjv tvqdqpx pfsy xckhz wg gqlf cwz uct. ot ttz cj mpi tzg tcoqxzpvr, fzeqqk, w ba omtp ffoe. eg rff oet vfufhamt ecx, kamvyss mhc nzyf wm wt ecu"
cipher2 = "lb iife quws bae hrzrl’l ftuaz khmaxbkz – mhp pixs 1 – t rzru-yqse xdhk wy ewhkzzhmpfpgvbclo kozvutwa hcble lv 1944 ov t lle iz ptrgdzj cgighzyqmy. ekm iwfpfwmx lxvpowvmw a roqzka oyh lgg, tno qw uvx wlv ihtx tz owiime ekm iinsp. dnzmk hzxzy wy spdzipbnr, d tgj tsdlazigt qlvgtey dswzbxd ekm vzhbwhu. ob leppmj i foek pgl eaygmj wg oyh wl bae nruvcmec’v kozvutw juikdd dvj aaocwmj qm ofw. nxwf tsdb swfeyw wt, khmaxbkz zltwknml wpum xmyecumj bh ad ecma."
cipher3 = "vvh wpcytsse zcr welvr a diijktlg ufpl. dlv jggwpfjw teveapu rj uyi msru lqfpiokid lc r hwncpf, kle zvvgeqxtbkmox ek egoow, uyi ixwfepwd, xiv wunhvf yoniozrg kx dafblkik, xho tiwugxvf ks segtwgr eidryso jraniui dfyln lrng bdxjfrav gffustyfegec, xyw fsvtbzv op xyw ncqk xvikc aywp hki qisbvid kgspie zrsypltns, wlf iipoekwf rdwizrgc sw mrzljuvh hytvk, vvh qfexav wygeyv, xiv xexwzgp oqh uyi fbyjltowmpe enn xyw wfjiotc axh kzg ghgsvgy kpc uqbyisxid kru zcapisvh fevzgwgoc vgsn rmj kmiop. iv govprhusg mo uicoqswt."

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
dictionary = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
message = cipher3
messages = [cipher1, cipher2, cipher3]
NUM_MOST_FREQ_LETTERS = 3

def decrypt(message, key):
	j = 0
	decrypted = ''
	for i in message:
		if(i in alphabets):
			i = lower[(dictionary[i] - dictionary[key[j]])%26]
			j = (j+1)%len(key)
		decrypted += i

	return decrypted


def find_key(st, n):
	strings = []
	for k in range(n):
		string = ""
		for i in range(k, len(st), n):
			string += st[i]
		strings.append(string)
		
		possibleKeys = []
	for string in strings:
		
		tuplee = []  
		for char in lower:
			decrypted = decrypt(string, char)
			#print(decrypted[:100])
			tuplee.append((char , freqAnalysis.englishFreqMatchScore(decrypted)))

		tuplee.sort(key=lambda x: x[1], reverse = True)
		possibleKeys.append(tuplee[:NUM_MOST_FREQ_LETTERS])
	#print(possibleKeys)

	for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat= n):
		possibleKey = ''
		for i in range(n):
			possibleKey += possibleKeys[i][indexes[i]][0]

		decrypted = decrypt(message, possibleKey)

		if detectEnglish.isEnglish(decrypted):
			print(f"Key = {possibleKey}, Decryted = {decrypted[:200]}")

def score(string):
	score = 0
	for char in lower:
		count = 0
		for i in string:
			if i == char:
				count+=1
		score += count*(count - 1)
	score /= len(string)*(len(string) - 1)
	return 26*score

def find_key_length(stripped):
	length_scores = []
	for n in range(3, MAX_KEY_LENGTH+1):
		ioc = 0
		for k in range(0, n):
			string = ""
			for i in range(k, len(stripped), n):
				string+=stripped[i]
			ioc += score(string)

		ioc/= n
		#print(f"Key length {n}, ioc {ioc}")

		length_scores.append(ioc)
	for i in range(len(length_scores)):
		if length_scores[i] > 1.65:
			return i+3
	for i in range(len(length_scores)):
		if length_scores[i] > 1.60:
			return i+3



for message in messages:
	stripped = ""
	for i in message:
		if i in alphabets:
			stripped += i.lower()

	key_length = find_key_length(stripped)
	key = find_key(stripped, key_length)
