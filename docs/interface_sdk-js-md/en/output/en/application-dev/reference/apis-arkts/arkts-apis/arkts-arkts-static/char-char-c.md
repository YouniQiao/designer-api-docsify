# Char

Represents boxed char value and related operations

**Inheritance/Implementation:** Char extends [Object](../../../apis-na/arkts-apis/arkts-na-dynamic/lib-es5-object-i.md) and implements [Comparable<Char>](Comparable<Char>)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-class Char extends Object implements Comparable<Char>--><!--Device-unnamed-class Char extends Object implements Comparable<Char>-End-->

**System capability:** SystemCapability.Utils.Lang

## charsToCodePoint

```TypeScript
public static charsToCodePoint(highValue: char, lowValue: char): int
```

charsToCodePoint(char, char) combines two chars to code point.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static charsToCodePoint(highValue: char, lowValue: char): int--><!--Device-Char-public static charsToCodePoint(highValue: char, lowValue: char): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| highValue | char | Yes | the high surrogate value. |
| lowValue | char | Yes | the low surrogate value. |

**Return value:**

| Type | Description |
| --- | --- |
| int | the combined UTF-16 code point. |

## codeUnitsToEncode

```TypeScript
public static codeUnitsToEncode(value: int): int
```

codeUnitsToEncode(int) counts a number of code units to encode the UTF-16 code point. See UTF-16 for more details.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static codeUnitsToEncode(value: int): int--><!--Device-Char-public static codeUnitsToEncode(value: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | UTF-16 code point to be examined..\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | the number of UTF-16 code units required to encode the code point. |

## compare

```TypeScript
public compare(lhs: Char, rhs: Char): boolean
```

compare(Char, Char) compares two Chars by their underlying chars.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public compare(lhs: Char, rhs: Char): boolean--><!--Device-Char-public compare(lhs: Char, rhs: Char): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lhs | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the first Char to compare. |
| rhs | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the second Char to compare. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the two Chars are equal, false otherwise. |

## compareTo

```TypeScript
public compareTo(other: Char): int
```

Compares this instance to other Char object. The result is less than 0 if this instance lesser than provided object, 0 if they are equal, and greater than 0 otherwise.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public compareTo(other: Char): int--><!--Device-Char-public compareTo(other: Char): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Char object to compare with. |

**Return value:**

| Type | Description |
| --- | --- |
| int | a negative number if this instance is less than other, zero if equal, positive if greater. |

## constructor

```TypeScript
public constructor()
```

constructor() creates a default Char object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public constructor()--><!--Device-Char-public constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(value: char)
```

constructor(char) creates a Char object from a specified primitive char.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public constructor(value: char)--><!--Device-Char-public constructor(value: char)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | a primitive char to create Char from. |

## equals

```TypeScript
public equals(other: Any): boolean
```

equals(Object) compares two Chars by their underlying primitive chars. Returns false if the argument is not an instance of Char.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public equals(other: Any): boolean--><!--Device-Char-public equals(other: Any): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Any | Yes | a reference to object to be compared with. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the two Chars are equal, false otherwise. |

## getHighSurrogate

```TypeScript
public static getHighSurrogate(value: int): char
```

getHighSurrogate(int) splits code point as a two code units and returns the first one. The result can be malformed and thus has to be checked.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static getHighSurrogate(value: int): char--><!--Device-Char-public static getHighSurrogate(value: int): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | an encoded code point.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| char | the high surrogate code unit. |

## getLowSurrogate

```TypeScript
public static getLowSurrogate(value: int): char
```

getLowSurrogate(int) splits code point as a two code units and returns the second one. The result can be malformed and thus has to be checked.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static getLowSurrogate(value: int): char--><!--Device-Char-public static getLowSurrogate(value: int): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | an encoded code point.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| char | the low surrogate code unit. |

## isBinDigit

```TypeScript
public static isBinDigit(value: char): boolean
```

isBinDigit(char) checks whether the char represents a binary digit.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static isBinDigit(value: char): boolean--><!--Device-Char-public static isBinDigit(value: char): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | a char to check. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the char is a binary digit, false otherwise. |

## isBinDigit

```TypeScript
public isBinDigit(): boolean
```

isBinDigit() checks whether the underlying char represents a binary digit.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public isBinDigit(): boolean--><!--Device-Char-public isBinDigit(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying char is a binary digit, false otherwise. |

## isDecDigit

```TypeScript
static isDecDigit(value: char): boolean
```

isDecDigit() checks whether the char represents a decimal digit.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-static isDecDigit(value: char): boolean--><!--Device-Char-static isDecDigit(value: char): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | a char to check. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the char is a decimal digit, false otherwise. |

## isDecDigit

```TypeScript
isDecDigit(): boolean
```

isDecDigit() checks whether the underlying char represents a decimal digit.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-isDecDigit(): boolean--><!--Device-Char-isDecDigit(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying char is a decimal digit, false otherwise. |

## isHexDigit

```TypeScript
public static isHexDigit(value: char): boolean
```

isHexDigit(char) checks whether the char represents a hexadecimal digit.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static isHexDigit(value: char): boolean--><!--Device-Char-public static isHexDigit(value: char): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | a char to check. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the char is a hexadecimal digit, false otherwise. |

## isHexDigit

```TypeScript
public isHexDigit(): boolean
```

isHexDigit() checks whether the underlying char represents a hexadecimal digit.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public isHexDigit(): boolean--><!--Device-Char-public isHexDigit(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying char is a hexadecimal digit, false otherwise. |

## isHighSurrogate

```TypeScript
public static isHighSurrogate(value: char): boolean
```

isHighSurrogate(char) checks if the char is a high surrogate.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static isHighSurrogate(value: char): boolean--><!--Device-Char-public static isHighSurrogate(value: char): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | the char to be checked. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the char is a high surrogate, false otherwise. |

## isInBasicMultilingualPlane

```TypeScript
public static isInBasicMultilingualPlane(value: char): boolean
```

isInBasicMultilingualPlane(char) checks if the char is in Basic Multilingual Plane. See UTF-16 for more details.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static isInBasicMultilingualPlane(value: char): boolean--><!--Device-Char-public static isInBasicMultilingualPlane(value: char): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | the char to be checked. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the char is in Basic Multilingual Plane, false otherwise. |

## isInBasicMultilingualPlane

```TypeScript
public static isInBasicMultilingualPlane(value: int): boolean
```

isInBasicMultilingualPlane(int) checks if the code point is in Basic Multilingual Plane. See UTF-16 for more details.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static isInBasicMultilingualPlane(value: int): boolean--><!--Device-Char-public static isInBasicMultilingualPlane(value: int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | the code point to be checked.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the code point is in Basic Multilingual Plane, false otherwise. |

## isInBasicMultilingualPlane

```TypeScript
public isInBasicMultilingualPlane(): boolean
```

isInBasicMultilingualPlane() checks if the underlying char is in Basic Multilingual Plane. See UTF-16 for more details.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public isInBasicMultilingualPlane(): boolean--><!--Device-Char-public isInBasicMultilingualPlane(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying char is in Basic Multilingual Plane, false otherwise. |

## isLetter

```TypeScript
public static isLetter(value: char): boolean
```

isLetter(char) checks whether the char is a letter.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static isLetter(value: char): boolean--><!--Device-Char-public static isLetter(value: char): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | a char to be tested. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the char is a letter, false otherwise. |

## isLetter

```TypeScript
public isLetter(): boolean
```

isLetter() checks whether the underlying char is a letter.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public isLetter(): boolean--><!--Device-Char-public isLetter(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying char is a letter, false otherwise. |

## isLowSurrogate

```TypeScript
public static isLowSurrogate(value: char): boolean
```

isLowSurrogate(char) checks if the char is a low surrogate.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static isLowSurrogate(value: char): boolean--><!--Device-Char-public static isLowSurrogate(value: char): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | the char to be checked. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the char is a low surrogate, false otherwise. |

## isLowerCase

```TypeScript
public static isLowerCase(value: char): boolean
```

isLowerCase(char) checks whether the char is a lower case letter.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static isLowerCase(value: char): boolean--><!--Device-Char-public static isLowerCase(value: char): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | a char to be tested. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the char is a lower case letter, false otherwise. |

## isLowerCase

```TypeScript
public isLowerCase(): boolean
```

isLowerCase() checks whether the underlying char is a lower case letter.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public isLowerCase(): boolean--><!--Device-Char-public isLowerCase(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying char is a lower case letter, false otherwise. |

## isPartOfSurrogatePair

```TypeScript
public static isPartOfSurrogatePair(value: char): boolean
```

isPartOfSurrogatePair(char) checks whether the char is low or high surrogate.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static isPartOfSurrogatePair(value: char): boolean--><!--Device-Char-public static isPartOfSurrogatePair(value: char): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | the char to be tested. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the char is part of a surrogate pair, false otherwise. |

## isPartOfSurrogatePair

```TypeScript
public isPartOfSurrogatePair(): boolean
```

isPartOfSurrogatePair() checks whether the underlying char is low or high surrogate.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public isPartOfSurrogatePair(): boolean--><!--Device-Char-public isPartOfSurrogatePair(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying char is part of a surrogate pair, false otherwise. |

## isUpperCase

```TypeScript
public static isUpperCase(value: char): boolean
```

isUpperCase(char) checks whether the char is an upper case letter.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static isUpperCase(value: char): boolean--><!--Device-Char-public static isUpperCase(value: char): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | a char to be tested. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the char is an upper case letter, false otherwise. |

## isUpperCase

```TypeScript
public isUpperCase(): boolean
```

isUpperCase() checks whether the underlying char is an upper case letter.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public isUpperCase(): boolean--><!--Device-Char-public isUpperCase(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying char is an upper case letter, false otherwise. |

## isValidCodePoint

```TypeScript
public static isValidCodePoint(codePoint: int): boolean
```

isValidCodePoint() checks if the code point is correctly encoded. See UTF-16 for more details.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static isValidCodePoint(codePoint: int): boolean--><!--Device-Char-public static isValidCodePoint(codePoint: int): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| codePoint | int | Yes | the code point to be checked.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the code point is correctly encoded, false otherwise. |

## isWhiteSpace

```TypeScript
static isWhiteSpace(value: char): boolean
```

isWhiteSpace(char) checks whether the char is a whitespace char.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-static isWhiteSpace(value: char): boolean--><!--Device-Char-static isWhiteSpace(value: char): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | a char to be tested. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the char is a whitespace, false otherwise. |

## isWhiteSpace

```TypeScript
isWhiteSpace(): boolean
```

isWhiteSpace() checks whether the underlying char is a whitespace char.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-isWhiteSpace(): boolean--><!--Device-Char-isWhiteSpace(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the underlying char is a whitespace, false otherwise. |

## toByte

```TypeScript
public toByte(): byte
```

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public toByte(): byte--><!--Device-Char-public toByte(): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| byte | the byte value of this Char instance. |

## toByte

```TypeScript
public static toByte(value: char): byte
```

Returns the primitive as byte value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static toByte(value: char): byte--><!--Device-Char-public static toByte(value: char): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| byte | the byte value of the char. |

## toChar

```TypeScript
public toChar(): char
```

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public toChar(): char--><!--Device-Char-public toChar(): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| char | the char value of this Char instance. |

## toChar

```TypeScript
public static toChar(value: char): char
```

Returns the primitive as char value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static toChar(value: char): char--><!--Device-Char-public static toChar(value: char): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| char | the char value. |

## toDouble

```TypeScript
public toDouble(): double
```

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public toDouble(): double--><!--Device-Char-public toDouble(): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| double | the double value of this Char instance. |

## toDouble

```TypeScript
public static toDouble(value: char): double
```

Returns the primitive as double value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static toDouble(value: char): double--><!--Device-Char-public static toDouble(value: char): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| double | the double value of the char. |

## toFloat

```TypeScript
public toFloat(): float
```

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public toFloat(): float--><!--Device-Char-public toFloat(): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| float | the float value of this Char instance. |

## toFloat

```TypeScript
public static toFloat(value: char): float
```

Returns the primitive as float value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static toFloat(value: char): float--><!--Device-Char-public static toFloat(value: char): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| float | the float value of the char. |

## toInt

```TypeScript
public toInt(): int
```

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public toInt(): int--><!--Device-Char-public toInt(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | the int value of this Char instance. |

## toInt

```TypeScript
public static toInt(value: char): int
```

Returns the primitive as int value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static toInt(value: char): int--><!--Device-Char-public static toInt(value: char): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| int | the int value of the char. |

## toLong

```TypeScript
public toLong(): long
```

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public toLong(): long--><!--Device-Char-public toLong(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | the long value of this Char instance. |

## toLong

```TypeScript
public static toLong(value: char): long
```

Returns the primitive as long value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static toLong(value: char): long--><!--Device-Char-public static toLong(value: char): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| long | the long value of the char. |

## toLowerCase

```TypeScript
public static toLowerCase(value: char): char
```

toLowerCase(char) converts the char to lower case if it is in upper case, otherwise the char is returned unchanged.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static toLowerCase(value: char): char--><!--Device-Char-public static toLowerCase(value: char): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | a char to transform to lower case. |

**Return value:**

| Type | Description |
| --- | --- |
| char | the lower case char converted from the input char. |

## toLowerCase

```TypeScript
public toLowerCase(): Char
```

toLowerCase() converts the underlying char to lower case if it is in upper case, otherwise the char is returned unchanged.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public toLowerCase(): Char--><!--Device-Char-public toLowerCase(): Char-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the lower case char converted from the underlying char. |

## toShort

```TypeScript
public toShort(): short
```

Returns value of this instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public toShort(): short--><!--Device-Char-public toShort(): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| short | the short value of this Char instance. |

## toShort

```TypeScript
public static toShort(value: char): short
```

Returns the primitive as short value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static toShort(value: char): short--><!--Device-Char-public static toShort(value: char): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | value to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| short | the short value of the char. |

## toString

```TypeScript
toString(): string
```

toString() converts Char to String object that contains a single element with the underlying char.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-toString(): string--><!--Device-Char-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the string representation of the Char. |

## toString

```TypeScript
static toString(value: char): string
```

Returns the primitive as string value

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-static toString(value: char): string--><!--Device-Char-static toString(value: char): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | value to cast |

**Return value:**

| Type | Description |
| --- | --- |
| string | the string representation of the char value. |

## toString

```TypeScript
public toString(radix: int): string
```

Converts this object to a string with specified radix.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public toString(radix: int): string--><!--Device-Char-public toString(radix: int): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radix | int | Yes | the radix of conversion.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| string | result of the conversion. |

## toUpperCase

```TypeScript
public static toUpperCase(value: char): char
```

toUpperCase(char) converts the char to upper case if it is in lower case, otherwise the char is returned unchanged.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static toUpperCase(value: char): char--><!--Device-Char-public static toUpperCase(value: char): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | a char to transform to upper case. |

**Return value:**

| Type | Description |
| --- | --- |
| char | the upper case char converted from the input char. |

## toUpperCase

```TypeScript
public toUpperCase(): Char
```

toUpperCase() converts the underlying char to upper case if it is in lower case, otherwise the char is returned unchanged.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public toUpperCase(): Char--><!--Device-Char-public toUpperCase(): Char-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the upper case char converted from the underlying char. |

## '\u0000'

```TypeScript
'\u0000'
```

**ArkTS mode:** ArkTS-Sta only

<!--Device-Char-'\u0000'--><!--Device-Char-'\u0000'-End-->

## '\uD800'

```TypeScript
'\uD800'
```

**ArkTS mode:** ArkTS-Sta only

<!--Device-Char-'\uD800'--><!--Device-Char-'\uD800'-End-->

## '\uDBFF'

```TypeScript
'\uDBFF'
```

**ArkTS mode:** ArkTS-Sta only

<!--Device-Char-'\uDBFF'--><!--Device-Char-'\uDBFF'-End-->

## '\uDC00'

```TypeScript
'\uDC00'
```

**ArkTS mode:** ArkTS-Sta only

<!--Device-Char-'\uDC00'--><!--Device-Char-'\uDC00'-End-->

## '\uDFFF'

```TypeScript
'\uDFFF'
```

**ArkTS mode:** ArkTS-Sta only

<!--Device-Char-'\uDFFF'--><!--Device-Char-'\uDFFF'-End-->

## '\uFFFF'

```TypeScript
'\uFFFF'
```

**ArkTS mode:** ArkTS-Sta only

<!--Device-Char-'\uFFFF'--><!--Device-Char-'\uFFFF'-End-->

## CHAR_BIT_SIZE

```TypeScript
public readonly CHAR_BIT_SIZE: int = 16
```

Size of the char type in bits.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public readonly CHAR_BIT_SIZE: int = 16--><!--Device-Char-public readonly CHAR_BIT_SIZE: int = 16-End-->

**System capability:** SystemCapability.Utils.Lang

## HIGH_SURROGATE_MAX

```TypeScript
public static readonly HIGH_SURROGATE_MAX: char = c
```

Maximal high surrogate value.

**Type:** char

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static readonly HIGH_SURROGATE_MAX: char = c--><!--Device-Char-public static readonly HIGH_SURROGATE_MAX: char = c-End-->

**System capability:** SystemCapability.Utils.Lang

## HIGH_SURROGATE_MIN

```TypeScript
public static readonly HIGH_SURROGATE_MIN: char = c
```

Minimal high surrogate value.

**Type:** char

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static readonly HIGH_SURROGATE_MIN: char = c--><!--Device-Char-public static readonly HIGH_SURROGATE_MIN: char = c-End-->

**System capability:** SystemCapability.Utils.Lang

## LOW_SURROGATE_MAX

```TypeScript
public static readonly LOW_SURROGATE_MAX: char = c
```

Maximal low surrogate value.

**Type:** char

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static readonly LOW_SURROGATE_MAX: char = c--><!--Device-Char-public static readonly LOW_SURROGATE_MAX: char = c-End-->

**System capability:** SystemCapability.Utils.Lang

## LOW_SURROGATE_MIN

```TypeScript
public static readonly LOW_SURROGATE_MIN: char = c
```

Minimal low surrogate value.

**Type:** char

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static readonly LOW_SURROGATE_MIN: char = c--><!--Device-Char-public static readonly LOW_SURROGATE_MIN: char = c-End-->

**System capability:** SystemCapability.Utils.Lang

## MAX_CODE_POINT

```TypeScript
public readonly MAX_CODE_POINT: int = 0x10FFFF
```

Maximal code point value.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public readonly MAX_CODE_POINT: int = 0x10FFFF--><!--Device-Char-public readonly MAX_CODE_POINT: int = 0x10FFFF-End-->

**System capability:** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static readonly MAX_VALUE: char = c
```

MAX\_VALUE is a largest value of type char.

**Type:** char

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static readonly MAX_VALUE: char = c--><!--Device-Char-public static readonly MAX_VALUE: char = c-End-->

**System capability:** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static readonly MIN_VALUE: char = c
```

MIN\_VALUE is a smallest value of type char.

**Type:** char

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Char-public static readonly MIN_VALUE: char = c--><!--Device-Char-public static readonly MIN_VALUE: char = c-End-->

**System capability:** SystemCapability.Utils.Lang

