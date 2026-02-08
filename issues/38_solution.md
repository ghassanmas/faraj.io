# 38 Solution 

This intended to answer the vaggy defined questoins in issues/38.md, it migth change the structure of it, 
as long as it try to asnwer a simple question that is:

> How secure is OpenPGP?


## Stauts

 > Still work in progress.

issues/38 assumed the use a stream cipher _only_, while the recent openpgp uses either pucket id 18 or 20. Which rely
on authricated encryption (by default), which uses block cipher and steam cipher but as input to the for the state of the
hash function. and then the result of hash functoin used as padding for block cipher (assuming it's on CCM mode). 

The below is revision of OpenPGP packet syntax, along with suggested next steps, in order complete main goal of 
issues/38, that is how secure is OpenPGP as a fuction of (message_length, public algrothim, symetric algothim).

- The public algorthim depends on recipent public key, and might not be in hand with sender
- message length and symetric algorthim are in hand of the sender

## Some playing around to refresh

```bash

gpg --output 13_20_GM_UN_COM_ML.gpg --compress-algo none  --encrypt --recipient XXXXXXXXXXXXXXXXXXXX long.txt

                                                                                                           01 legacy type syntax
                                                                                                              001: 1 > Type 1 one packet
                                                                                                                 00: next ocet is length
BEGIN PACKET: Public Key Encrypted Session Key*  PKESK   TYPE ID: 1
Header of PKESK
00000000  84 5e (first ocet packet header 84 1010100 and length 0x 5e or 94 oct)  length of packet start with body, exculing header which is 2 octet 84 5e for this packet.
Body of PKESK
00000002  03 First oct is version thus we have dealing with PKESK V3 as described in  5.1.1 @ RFC9580 
00000003  id id id id id  id id id  8 Oct the id of recipent 
0000000b  12  The algorthim of the public key, e.g. RSA or Eliptic curve.  0x 12 is 18: ECDH Alrgorthim in 9.1 @ RFC9580
0000000c  01 07 40 11  |.^..;);).;)...@.|  Body of PKESK
00000010  a9 d9 a3 83 79 77 51 0c  e9 56 12 ab b9 06 b8 0e  |.....q..P...6.f.|
00000020  d0 88 90 d0 39 de de 72  bc 92 61 94 7e de 1f 30  |..a...9D`......0| The body of PKESK packet: start with [03 id id id id id  id $
00000030  e4 6b e4 43 29 7b 97 95  ed 6c 63 d7 03 23 db c5  |.C...9K......P.y|  03 id id id id id  id id id]
00000040  0f 76 d8 73 04 e6 ee 67  21 36 60 97 9f 21 ca 8b  |.v.s...g!6`..!..|
00000050  5a da 
            d2 92 e5 f6 46 8b  ec 6c af d0 8f 07 88 22  |Z.....F..l....."|  22 is last oct the packet



BEGIN PACKET: Symetric Encryption and Integrity Protected SEIPD* Type 20*

00000060  d4  
00000061   e9 01: e9 is 233 > 192 thus it's two octet length = (233-192) 41 * 16 + 192 + 01 
                                                                    (29      +     C1)**  = 
                            841
                09 02 10 a7 b4  18 14 75 fd b9 75 ee c7  |..........u..u..|

We are sure it's container of symetric encrypted packet, since PKESK always
followed by encryption container, note it could have yet another PKESK or/and
SKESK, but note the next e9, which 

** Summing according to  RTF9580 of two scaler, that is the first is times * 8 
and the second as it's thus 29 is 41 *   + 193 

 0x c5 197 - 192 = 0x 05 - 192

FB + 192 = 443 = 0x 1BB  + 0x 5 (only the first one)  6BB = 1723 (same as example p25) 

0x e9 - 192  = 41 = 0x 29 (first octet)
0x 01 + 192  =  193 = 0x C1 (second octet). 
29 + C1 = 29 C1

e9: 1110 1001 
1f: 0001 1111
&:  0000 1001

29: 0010 1001
C1:            1100 0001
      10 1001  1100 0001   

L: 0011  0101 0001

844 841 
00000070  bc a0 96 46 ce e3 fa 0f  14 6b 8f 1d d5 8a 6f 39  |...F.....k....o9| 
00000080  80 f7 2a 91 97 aa 90 f5  1c d3 11 09 a4 f3 fd bc  |..*.............|
00000090  8e 8c 21 56 f1 63 be 69  dc f2 9b 32 e6 05 e3 d5  |..!V.c.i...2....|
000000a0  81 7e cb 0f f2 2d 72 8e  99 35 d1 14 84 72 ee 45  |.~...-r..5...r.E|
000000b0  4f 1b d0 28 94 38 f4 ac  5d 01 7c d8 6e 4d f9 17  |O..(.8..].|.nM..|
000000c0  bd 30 7c fa 16 48 b1 fc  97 03 13 4c 52 a4 32 f3  |.0|..H.....LR.2.|
000000d0  e1 fc 98 e8 88 7b 48 c8  de 69 78 94 a6 39 cc 6b  |.....{H..ix..9.k|
000000e0  31 45 0b b4 70 5a 2f 29  92 23 b3 d2 8d ad 9d a9  |1E..pZ/).#......|
000000f0  ea 17 72 1f 8a c2 e0 58  18 ae f7 97 95 0d 9c 06  |..r....X........|
00000100  e2 79 7a 32 54 74 5e b1  50 2f de cf 51 d0 15 66  |.yz2Tt^.P/..Q..f|
00000110  88 3d f5 f4 c3 f7 12 1d  b4 85 6c 84 20 ed c8 84  |.=........l. ...|
00000120  4a db 5c 29 66 ee ce 61  b5 6f 4b 52 89 da a8 bf  |J.\)f..a.oKR....|
00000130  32 45 bf 88 20 38 2d 90  78 86 e7 1d 05 41 85 99  |2E.. 8-.x....A..|
00000140  e0 56 ed 9c 08 5c fa 34  ca ed 1b 33 36 ef ea c7  |.V...\.4...36...|
00000150  f7 6e 27 bd 4a ab 9b 58  2b c6 21 0b 51 03 f6 a6  |.n'.J..X+.!.Q...|
00000160  ba 72 f2 6d 24 c2 9b 38  0c 63 a9 1d 67 04 9c 4b  |.r.m$..8.c..g..K|
00000170  f8 80 55 12 dc 6a 61 84  30 db 1b b3 1a 6f 05 c9  |..U..ja.0....o..|
00000180  4c 9b 62 84 c1 a0 1e 3b  e5 ac 0e 3c 1c f2 f0 d5  |L.b....;...<....|
00000190  75 29 f2 5a fb 8d b9 ae  55 7d 65 14 da 65 4c b1  |u).Z....U}e..eL.|
000001a0  49 a2 68 af 7f 7e 80 90  41 dd 2b 2b 17 c0 18 9d  |I.h..~..A.++....|
000001b0  01 a8 21 86 4d b1 be f9  b9 70 cb 62 09 61 3c 04  |..!.M....p.b.a<.|
000001c0  7f d7 4f e4 3a e4 3d 23  9a cd 50 02 a7 82 f1 ab  |..O.:.=#..P.....|
000001d0  2b c8 5d 15 81 54 4a dd  f1 83 c1 91 3f c6 81 28  |+.]..TJ.....?..(|
000001e0  3c 1c 8a 0c a6 ec eb 26  9e 3c bd 7b b8 bb 4c 2a  |<......&.<.{..L*|
000001f0  6b 36 d6 1e f8 38 fd 56  0b b8 86 d5 ec dd 9f b6  |k6...8.V........|
00000200  08 a5 d6 b1 6a 5e 62 c2  92 1e 6d 08 c8 85 83 49  |....j^b...m....I|
00000210  8d 13 66 6c 06 f7 c1 ab  98 f8 0c fa df 3a a0 f7  |..fl.........:..|
00000220  9b 06 69 ec 08 04 26 0a  fc 75 a3 91 f1 47 fb 16  |..i...&..u...G..|
00000230  3c 38 18 7d 7d ff 54 9a  0e 4a 33 3c 79 0d 17 de  |<8.}}.T..J3<y...|
00000240  23 e5 ce ad b3 8e 6b ec  e7 80 8a 6b 28 12 1d 05  |#.....k....k(...|
00000250  b9 e3 a6 31 d5 50 84 ec  80 d0 d9 27 78 77 2b c8  |...1.P.....'xw+.|
00000260  04 6d (END of Partial packet)
00000262  c0 87 (Start of secon portion) 
          c0: = 192 thus either 4.2.1.1 or 4.2.1.2 applies hence first oct - 192
          = 0. Thus total length is 192 + 0x 87 = 192 + 135 = 327 which is 0x 147
          
             
00000264              3c bc 3d b9  f6 00 15 84 bc 67 ef 2e  |.m..<.=......g..|
00000270  3b 0d 0a ac 3e 17 3b 6a  18 ca 50 db 3d 1c 61 31  |;...>.;j..P.=.a1|
00000280  62 aa fa 36 70 e5 fc d1  bb df ae 9a ed 30 08 28  |b..6p........0.(|
00000290  15 5b db a8 15 1f 57 0f  b5 21 0b 5e 98 02 55 f6  |.[....W..!.^..U.|
000002a0  35 24 59 e9 ae 08 f0 ba  83 a3 62 6f da 8a 6c 24  |5$Y.......bo..l$|
000002b0  8d 02 cb 3d 4a 1e 14 1e  57 ee 9a 7b bd 3f 49 15  |...=J...W..{.?I.|
000002c0  f8 7b df 6a 71 d8 3e 5b  06 be c1 a5 44 21 af 92  |.{.jq.>[....D!..|
000002d0  05 6d f1 c8 72 41 6d 10  55 31 ab e0 6d e9 6b 3a  |.m..rAm.U1..m.k:|
000002e0  70 2c 22 af 68 85 0a 97  12 8b 22 8e e4 05 b6 35  |p,".h....."....5|
000002f0  b7 7a 3c ce bb 44 e6 da  7a 4f d7 2e 5b 96 6c 33  |.z<..D..zO..[.l3|
00000300  7a 97 c7 a4 c3 11 10 20  d9 81 fe 10 be a8 85 61  |z...... .......a|
00000310  c3 9a 74 16 52 1d c9 ce  d9 ee fd a6 da 97 87 db  |..t.R...........|
00000323  1e c6 c1 b5 d2 a6 5a bd  f8 40 41 36 af ac 33 01  |......Z..@A6..3.|
00000330  0b 06 f8 2c cd 50 47 ca  53 34 7e 5e b8 84 36 75  |...,.PG.S4~^..6u|
00000340  dd d7 22 34 9e fc df 55  b5 aa 55 4b 23 cd 93 00  |.."4...U..UK#...|
00000350  24 3b 98 a6 70 d2 16 d9  36 df 1f ed 7b 6e f2 c2  |$;..p...6...{n..|
00000360  bd 3f 10 ec 46 1e db f1  b6 63 d8 cd a4 99 67 9f  |.?..F....c....g.|
00000370  50 f5 c3 ab 4e 93 d4 55  b8 37 38 52 f9 c7 42 a6  |P...N..U.78R..B.|
00000380  17 99 4e fa e4 49 be 2b  df c7 13 48 2c 95 f9 91  |..N..I.+...H,...|
00000390  e4 d8 b3 06 64 6e 5c 25  a8 4b d9 94 e0 59 1d 92  |....dn\%.K...Y..|
000003a0  c8 37 ec 13 d0 3a 71 1c  fd d5 f8                 |.7...:q....|             

To confirm We reached the end the last oct location is 0x 3ab - ox 147 =  265
FINALLY IT MAKE SENSE




* The second *key* in the packet refers to the symetric key, while former is public
 public key used to encrypt the message and in this case it happen
 that the content of the message is the symetric key for the following
 packet.
```


```bash
hexdump -C 13_20_RD_UN_COM_OL.gpg
Header of packet
00000000 85: 1000 0101 meaning legacy header format, packet type is 1, length is 2 oct
00000001 01 0c: length of packet body is meaning lengh is 0x 10C 268 

body of packet
00000003  03: is the version of packet
00000004  id id id id id id id id  of recipent
0000000c  01 Algorthim of public key  RSA as per 9.1
BEGIN encrypted session key
0000000d  08 00 c7  |;) ;) ;) ;) ;) |
00000010  1d 31 83 bc 34 98 d1 c6  f8 8e a6 b8 06 3d af 18  |.1..4........=..|
00000020  cc ee 63 2b f2 2f 6c 93  9c 1a 18 f7 a5 1f dc 93  |..c+./l.........|
00000030  67 e7 8a 73 d4 3a bc 30  ff f7 63 a0 59 49 7d 99  |g..s.:.0..c.YI}.|
00000040  a2 da bc 2f b8 8d ec aa  1e 9e 7a cd fa 66 fe 19  |.../......z..f..|
00000050  19 d0 ab 38 f3 ad dc f7  d5 99 f9 a1 b0 08 84 71  |...8...........q|
00000060  f1 50 e1 3a 6c 24 c7 ba  94 48 af 69 fe 6e 54 a3  |.P.:l$...H.i.nT.|
00000070  07 73 fb 1f 18 5d f0 77  4e 6c 26 39 cb ca 8c b6  |.s...].wNl&9....|
00000080  aa 22 79 ad 9c 48 bf 81  de e3 76 8c 47 57 68 2b  |."y..H....v.GWh+|
00000090  e3 34 07 c2 33 b7 a9 29  8d 5b cb b3 7f a4 74 27  |.4..3..).[....t'|
000000a0  23 84 19 ee 0f f2 19 13  a3 a0 0b 54 fb 0d c7 2d  |#..........T...-|
000000b0  f6 1e fb 9e 93 65 28 8f  04 c4 d3 6c 2d 6e eb 64  |.....e(....l-n.d|
000000c0  a4 5d 44 50 af 6e ff 1d  a6 c4 fb 7a 33 07 dd 63  |.]DP.n.....z3..c|
000000d0  12 8b 31 21 fe 69 18 31  19 11 a2 30 ce 80 fe 95  |..1!.i.1...0....|
000000e0  5c c7 ca 17 62 95 1e 2e  76 b4 30 62 3e 4b 02 c0  |\...b...v.0b>K..|
000000f0  7f 11 0a b0 99 e3 7d 83  cf 44 15 cb b7 a6 aa 29  |......}..D.....)|
00000100  49 4d b9 c3 56 df da 33  78 00 23 2f 5a 0f 1a.
End Encrypted session key

~~0000010d  0f 1a Check SUM  of session key = 3866 = sum of octex % 65536 per 5.1.3~~
The check sum is contacted priror to encryption not decryption



END OF PSKET packet.

Start of Header
0000010f  d2:  is 1101 0010 header is recent format as 6th bit is 1. Packet type is 18   |IM..V..3x.#/Z...| 
00000110  a8: is 168 < 192 thus length is 1 oct
Start of Body of packet
00000111: 01 is the version 
5a 71 f0 38 87 83  3c c8 37 9c 0c 0d 10 27  |..Zq.8..<.7....'|
00000120  cb 21 42 41 f8 67 53 9e  95 ed 7c 76 bc 30 17 b4  |.!BA.gS...|v.0..|
00000130  dc b1 92 10 90 a4 b1 df  3a c5 97 cc a9 31 5f dc  |........:....1_.|
00000140  48 b2 be a9 8f 34 b6 d5  18 bc 97 30 55 c7 b1 59  |H....4.....0U..Y|
00000150  38 25 c2 bd c7 d0 ca fb  e4 7a 88 70 09 48 da b9  |8%.......z.p.H..|
00000160  d3 79 5b 81 87 a2 c5 a9  69 13 58 52 82 73 2c 0a  |.y[.....i.XR.s,.|
00000170  e8 20 62 f0 c8 14 3a 56  29 03 b8 bb a0 9b 59 c6  |. b...:V).....Y.|
00000180  54 99 9a c2 d4 4f d5 19  c2 5d 96 eb ef 6b e0 e4  |T....O...]...k..|
00000190  f5 c6 b6 63 6a 74 c4 23  65 36 d8 84 84 6b b9 07  |...cjt.#e6...k..|
000001a0  77 c1 06 2a 60 fd 17 c1  5e 7b 44 db e4 d8 16 e2  |w..*`...^{D.....|
000001b0  f2 63 bb e6 55 12 a7 f6  c6                       |.c..U....|
000001b9
```



## Apendix

Python function that calcualte check sum per oct given hex input:

```python
# This still not working right, it expect each element of array to be
# length 2. 
# This can be used after decrypting the public packet, so to confirm
# it's the correct key, we sum all oct but the fist and last two e.g. 


def sum_hex_pairs(data) -> int:
    if isinstance(data, str):
        # Remove spaces if string
        data = data.replace(" ", "")
        if len(data) % 2 != 0:
            raise ValueError("Hex string length must be even (pairs of 2).")
        items = [data[i:i+2] for i in range(0, len(data), 2)]
    elif isinstance(data, (list, tuple)):
        items = [x.strip() for x in data if x.strip()]  # clean up spaces
    else:
        raise TypeError("Input must be a string or list/tuple of strings.")
    return sum(int(x.strip().replace(" ",""), 16) for x in items) # problamtic line expect "xx"


check_sum = sum_hex_pairs(k[1:-2]) = sum_hex_pairs[:-2]

#LLM: https://chatgpt.com/share/68e39ffc-b81c-8004-9c28-ba13093d4c46

```

## Conculsion so far and Next Steps:

1. Understanding of AEAD is required as its the default symetric encryption for latest OpenGP or gpg.
2. Given 1, a recap on block ciphering and hasing algorthim is needed
3. To ensure understanding of how an openpgp message is created a manual decryption of message is needed see Next Steps below

point 1,2 and 3 can be done in parrallel, 1,2 requires course/book while 3 require development RFC9580. At one point 

## Next Step 1 and 2 

 Preceed with the book(s) and course.  Check probabilty book if needed. 

1. Check resources, course, books to ensure how the inner working of those algorthim. 
2. Get knowledge of vunablriity of the algrothim used
3. Write notes on study_notes/*.txt|md

## Next Step 3

 It just require creating openpgp key pairs and message, in different cirumistances. decrypting the message manually
 hence we know the private part of the asymetirc key(s).

 Then to manually decrypt the syemtric part, note we cannot do this step before previous, unless gpg implmentatoin of 
 OpenPG is tweaked to echo symetric key (which supposely chosen at random).


### Prepare samples message

1. Create key pair of RSA and eliptic curve
2. Look at the metadata of each key, what does an openpgp key metadata included (hence it would be used for next step 4)
3. Prepare messages, one small and other multi lines  (ensure the latter length > k length of of previous step)
4. For each of them or both, create message that is encrypted with different syemtric key algorthims
5. For each of them or both, create message that is not compressed, and other is compressed

### Public key pucket RSA and EC

 1. Create a pair of RSA key pairs
 2. Go over RFC 9580 Step by step for when ecrypting a message for one recipient
 3. Decrypt the key session message _PSKET packet_ not through `gpg` but through low level manual function
    1. We suppose to have as input private key from
    2. Other metadata passed through the packet.
    3. AS RFC 9580 refers RFC to 8017 mainly section 7.2.1 and 7.2.2 for ecryption, decryption respectively.
      That Assuming public key algorthim (second bit of PASKET body when its v3) is 01 RSA RFC9580 @ 5.1.3
  4. Simliar to RSA, repeat the above but for eliptic curve.

### Syemtric key packet

 Now that we have got the secret key manually in previous step, try to manually
 decrypt the syemtric key part given key, and cipher of the message. 

  1. Try with compressed and uncompressed message 


## Outcomes: 
  
  1. Ensure correct understanding of under working of openpgp
  2. How does compression affect message
    1. Can Adv knows by looking at hexdump of pgp message if it's compressed or not.
  3. How does Authticated encryption works
    1. And it's relation to the hashiing function. 
  4. What is the relation of message length to public key length
  5. Can adv knows by looking at 
  
For 2, we know that the message is the syemtric key, and thus according
RFC8017 message length (syemtric key in our case), cannot be to long.

Nonetheless, the real message can be long. Thus depending on the algorthim 
used for syemtric encryption. We cannot assume key length for symetric key
is as long as the message. Because it need to respect the length of the public
key. 

## Next next steps

 1. Try to crack the code as suggested in issues/38.md
 2. IF not, what kind of resources in theory is required, 
   1. Also how does that affect condition defined in previous steps 
      (e.g. message length, public/symetric algorhtim)
