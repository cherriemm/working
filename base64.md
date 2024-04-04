**Base64 is a binary to a text encoding scheme that represents binary data in an ASCII string format and then carries that data across channels .**



## Data Format

BLOB

BLOB stands for binary large object file. Whenever we transfer image, audio or video data over the network, that data is classified as BLOB data .

CLOB, which stands for character large object file, includes any kind of text XML or character data transfered over the network. 



## theory

http://www.sunshine2k.de/articles/coding/base64/understanding_base64.html



Base64 is an algorithm to convert a stream of bytes into a stream of printable characters (and back). The origin of such binary-to-text encoding scheme like Base64 is the requirement to send a stream of bytes over a communication channel which does not allow binary data but only text-based data. E.g. the ASCII standard is based on seven-bit values, thus uses a range of 0-127. Still an ASCII value is normally stored in a byte which has eight bits (0-255). The usage of the most significant bit of an ascii value is not completely defined (could be used as a parity bit for example). So if a stream which is expected to contain only ASCII values actually also contain non-ASCII values, this could potentially lead to problems. However, it is not convenient that a programm shall know whether the data bytes to process are 'text' or 'binary' - and often binary data shall be processed / transmitted via a text-based protocol / algorithm. This is where Base64 encoding & decoding could come into play.

So how to represent a data byte which can hold 256 different values by a set of only 64 characters? Well, of course this is not possible by a 1:1 mapping, so the Base64 encoded data stream needs more characters than the original byte-based. In fact three data byte values are encoded to four Base64 values: 



Base64 encoding contains 64 characters to encode any string  :

![image-20240404191549213](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240404191549213.png)





### BASE64 ENCODING 

```
Example encoding for the input string "Sun":

Input character bytes: S          u           n
ASCII Hex value:       0x53       0x75        0x6E
Binary                 01010011   01110101    01101110
6bit parts:            010100 110111 010101 101110
Decimal (index)values: 20     55     21     46
Base64 characters:     U      3      V      u

So the string "Sun" has encoded in Base64 the value "U3Vu".
```









**WHAT IF OUR INPUT STRING ISN’T A MULTIPLE OF 3?**

In this case, the input buffer is filled up with zeros until it is divisable by three. Then each 6bit part which was filled up with zero is encoded with the special padding character '='.



**three cases to distinct:**

1. There is only one input character byte left in the last triple:
   The most significant 6 bits are normally encoded, the other 2 bits are expanded with zeros and also encoded. To fill up the based64 encoded quadruple, two padding '=' characters are appended.

   ```
   Example encoding with two padding characters: Encoding of "S"
   
   Input character bytes: S
   Hex value:             0x53
   Binary                 01010011
   6bit parts:            010100 110000 xxxxxx xxxxxx
   Decimal (index)values: 20     48     N/A    N/A
   Base64 characters:     U      w      =      =
   
   After encoding the first 6 bits (010100) of 'S', the lower two bits (11) are expanded with zeros. Two padding characters are inserted. So the string "S" has base64-encoded the value "Uw=="
   ```

   

2. There are two input character bytes left in the last triple:
   From those 16 bits, the most significant 2 x 6 bits are encoded to two base64 output characters. The remaining 4 bits are expanded with zeros and also encoded. Then a single padding character is appended to fill up the base64 quadruple.

   ```
   Input character bytes: S         u
   Hex value:             0x53      0x75
   Binary                 01010011  01110101
   6bit parts:            010100 110111 010100 xxxxxx
   Decimal (index)values: 20     55     20      x
   Base64 characters:     U      3      U      =
   
   The four remaining bits (0101) uf 'u' are expanded with two zeros. So 010100 are normally encoded and one padding character is inserted. So the string "Su" has base64-encoded the value "U3U="
   ```

   

3. The number of input character bytes is divisable by three:
   No padding, thus no special handling necessary.





### BASE64 DECODING


Due to the padding during encoding, the number of characters of a Base64 string is always divisable by four. Thus we can process four characters of the string in one step to retrieve three decoded bytes. 

This means: Extract the next four characters, get the index value from the lookup table (reverse lookup), merge the four 6bit values to three 8bit values 



```
Example decoding for the Base64 string "U3Vu":

Base64 characters      : U          3          V          u
Decimal (index) values : 20         55         21         46
6bit parts:              010100     110111     010101     101110
Binary                   01010011   01110101   01101110
Hex value:               0x53       0x75       0x6E
Character bytes        : S          u          n

So the Base64-encoded string "U3Vu" has decoded the value "Sun"
```

Only special care has to taken for the last quadruple if it contains padding characters.

 three cases to distinct:

1. The third and fourth byte of the quadruple equal the padding byte '='. (Two padding characters)

   ```
   Example decoding with two padding characters: Decoding of "Uw==":
   
   Base64 characters      : U          w          =          =
   Decimal (index) values : 20         55         N/A        N/A
   6bit parts:              010100     110111     N/A        N/A
   Binary                   01010011   0111xxxx
   Hex value:               0x53       N/A        N/A
   Character bytes        : S
   
   So the Base64-encoded string "Uw==" has decoded the value "S".
   ```

   

2. The fourth byte of the quadruple is the padding byte '=', but not the third byte. (One padding character)

   ```
   Example decoding with one padding character: Decoding of "U3U=":
   
   Base64 characters      : U          3          U          =
   Decimal (index) values : 20         55         21         N/A
   6bit parts:              010100     110111     010100     N/A
   Binary                   01010011   01110101   00xxxx
   Hex value:               0x53       0x75       N/A
   Character bytes:         S          u
   
   So the Base64-encoded string "U3U" has decoded the value "Su"
   ```

   

3. The third and fourth byte of the quadruple do not equal the padding byte '='. This is the standard case from above.





### Length Calculation

The number of required Base64 characters (y) from an input stream with x bytes is calculated as:

y = floor((x + 2) / 3) * 4 (for x >= 1)





x = ((y / 4) * 3)) (for y >= 4 and y is divisable by 4).

This second formula correctly results the maximum value out of the three possible lengths (e.g. a 12 character long Base64-encoded string could be made of a 7, 8 or 9 byte stream, so the formula returns 9.).





## Implementation



### Encoding thoughts

The actual conversion from an input byte to an output character is above listed as a mapping table, so the most obvious way is an lookup table for this conversion. So let's define a 1:1 mapping, where the index into this string matches exactly the Base64 character (e.g. index 1 = 'B'):

```
private static string encLookupTable = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
```



Another point is the extraction of the index values. Remember that three 8bit characters result in four 6bit Base64 characters, so we need a way to extract those 4 values from three consecutive bytes. 

This is easily achieved with some bit operations. Assume *inputBytes* is a 3-element array of bytes, so to extract the four index values idx1 to idx4 following code can be used:

```
// take the six most significant bits of first byte
byte idx1 = inputBytes[0] >> 2;

// take the lower two bits of first byte and place them to the most significant bit location , take the four most significant bits of second byte and place them to the four lowest bit locaitons
byte idx2 = ((inputBytes[0] & 0x03) << 4) | ((inputBytes[1] & 0xF0) >> 4);

byte idx3 = ((inputBytes[1] & 0x0F) << 4) |((inputBytes[2]) & 0xC0 >> 6);

byte idx4 = inputBytes[2] & 0x3F;
```

The index value is used to access the lookup table to retrieve the actual Base64 character, e.g. char c1 = encLookupTable[idx1];



- The input data is declared as *byte[] toEncodeAsBytes*.
- A Stringbuilder called *sb* is used to store the encoded Base64 characters. The initialization is left out.



#### version 1

The first idea is to convert first all complete input bytes triples to four output characters. Afterwards, the special cases must be handled: Either no, one or two bytes are left and must be encoded and finally filled up with the padding characters.
Using this approach and above mentioned notes, a possible implementation looks like this:

```
int i = 0;
int indexOfLastCompleteTriple = (int)(toEncodeAsBytes.Length / 3) * 3;
/* handle triples of input characters per loop */
for (i = 0; i < indexOfLastCompleteTriple; i += 3)
{
    sb.Append(encLookupTable[toEncodeAsBytes[i] >> 2]);
    sb.Append(encLookupTable[((toEncodeAsBytes[i] & 0x03) << 4) | ((toEncodeAsBytes[i + 1] & 0xF0) >> 4)]);
    sb.Append(encLookupTable[((toEncodeAsBytes[i + 1] & 0x0F) << 2) | ((toEncodeAsBytes[i + 2] & 0xC0) >> 6)]);
    sb.Append(encLookupTable[toEncodeAsBytes[i + 2] & 0x3F]);
}

if (i < toEncodeAsBytes.Length)
{   /* last triple incomplete, either one or two input characters 'missing' */
    /* get first index value, always available */
    byte idx1 = toEncodeAsBytes[i];
    /* get second index value, if second input byte of last triple not available 'fill up with zeros' */
    byte idx2 = (i + 1 < toEncodeAsBytes.Length) ? toEncodeAsBytes[i + 1] : (byte)0;
    /* encode first byte of last incomplete triple */
    sb.Append(encLookupTable[idx1 >> 2]);
    sb.Append(encLookupTable[((idx1 & 0x03) << 4) | ((idx2 & 0xF0) >> 4)]);

    if (i + 1 < toEncodeAsBytes.Length)
    {   /* only one byte 'missing', encode last character = second byte in last triple */
        sb.Append(encLookupTable[((idx2 & 0x0F) << 2)]);
    }
    else
    {   /* two bytes 'missing', add one padding character */
        sb.Append('=');
    }
    sb.Append('=');
}
return sb.ToString()
```





#### version 2

Another approach is to always try to handle the next input triple, and in each iteration check if the triple is completer or if we are already at the last , possibly incomplete triple.

The advantage of this approach is a slightly shorter implementation, however the checks in each iteration makes it less performant.

```
for(int i = 0; i < toEncodeAsBytes.Length; i += 3)
{
	// First encoding byte is never '='
	sb.Append(encLookupTable[toEncodeAsBytes[i]>>2]);
	
	if(i < toEncodeAsBytes.Length - 1)
	{
		sb.Append(encLookupTable[((toEncodeAsBytes[i] & 0x03) << 4) | ((toEncodeAsBytes[i + 1] & 0xF0) >> 4)]);
		if(i < toEncodeAsBytes.Length - 2)
		{
			sb.Append(encLookupTable[((toEncodeAsBytes[i + 1] & 0x0F) << 2) | ((toEncodeAsBytes[i + 2] & 0xC0) >> 6)]);
			sb.Append(encLookupTable[toEncodeAsBytes[i + 2] & 0x3F]);
		}
	else
        {   /* last input byte missing, encode third output character with zeros expanded and add padding char */
            sb.Append(encLookupTable[((toEncodeAsBytes[i + 1] & 0x0F) << 2)]);
            sb.Append('=');
        }
    }
    else
    {   /* only one input byte available, encode second output character with zeros expanded and add two padding chars */
        sb.Append(encLookupTable[((toEncodeAsBytes[i] & 0x03) << 4) | 0]);
        sb.Append('=');
        sb.Append('=');
    }
	
}
```

