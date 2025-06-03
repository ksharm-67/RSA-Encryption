# RSA-Encryption-Program

DESCRIPTION:

Using existing libraries to perform the extended Euclidean algorithm, and encrypt a plaintext using RSA. To generate the key, we will implement the Extended Euclidean Algorithm, where we will first generate the private key. Then we will use the formula ciphertext = plaintext ^ key % N to encrypt and plaintext = ciphertext ^ key % N.

===================================================================

REQUIREMENTS:

Python 3.6 or higher

===================================================================

INSTALLATION:

Install Python 3 if it is not already installed. You can download it from Python.org.

===================================================================

USAGE:

Run the program from the command line, providing the necessary arguments.

Command Line Arguments

--p_e : pe in base 10 (power to raise 2)

--p_c : pc in base 10 (constant to subtract from 2^p_e)

--q_e : qe in base 10 (power to raise 2)

--q_c : qc in base 10 (constant to subtract from 2^q_e)

--e_e : ee in base 10 (power to raise 2)

--e_c : ec in base 10 (constant to subtract from 2^e_e)

--ciphertext : The ciphertext to be decrypted.

--plaintext : The plaintext string to be encrypted.

===================================================================

Example Usage

To run the program, use the following command:

python3 rsa.py \
--p_e 252 \
--p_c 3551320294972622704085158542068617432155596220113794691428435278300674188689 \
--q_e 261 \
--q_c 1194103838696593800434465377182188669000022374589724805392034067440035954998819 \
--e_e 26 \
--e_c 12320055 \
--ciphertext 2109636589475319481690033161025118722547237230723991210476034408842255762453948587714804726263356891979001833011601694803200495628743260668599194164851838 \
--plaintext 6024799506

===================================================================

Expected Output

The program prints the decrypted plaintext and the encrypted text in decimal format, separated by a comma.

Example output:

6024799506,2109636589475319481690033161025118722547237230723991210476034408842255762453948587714804726263356891979001833011601694803200495628743260668599194164851838

===================================================================

Troubleshooting

If decryption or encryption fails, check that all the arguments are correctly provided and formatted.
