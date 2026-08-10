# Char

Represents boxed char value and related operations

**继承/实现关系：** Char extends [Object](arkts-arkts-object-c.md) implements [Comparable<Char>](Comparable<Char>)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-class Char extends Object implements Comparable<Char>--><!--Device-unnamed-class Char extends Object implements Comparable<Char>-End-->

**系统能力：** SystemCapability.Utils.Lang

## charsToCodePoint

```TypeScript
public static charsToCodePoint(highValue: char, lowValue: char): int
```

charsToCodePoint(char, char) combines two chars to code point.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static charsToCodePoint(highValue: char, lowValue: char): int--><!--Device-Char-public static charsToCodePoint(highValue: char, lowValue: char): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| highValue | char | 是 | the high surrogate value. |
| lowValue | char | 是 | the low surrogate value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the combined UTF-16 code point. |

## codeUnitsToEncode

```TypeScript
public static codeUnitsToEncode(value: int): int
```

codeUnitsToEncode(int) counts a number of code units to encode the UTF-16 code point. See UTF-16 for more details.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static codeUnitsToEncode(value: int): int--><!--Device-Char-public static codeUnitsToEncode(value: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | UTF-16 code point to be examined.. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the number of UTF-16 code units required to encode the code point. |

## compare

```TypeScript
public compare(lhs: Char, rhs: Char): boolean
```

compare(Char, Char) compares two Chars by their underlying chars.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public compare(lhs: Char, rhs: Char): boolean--><!--Device-Char-public compare(lhs: Char, rhs: Char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lhs | [Char](arkts-arkts-char-c.md) | 是 | the first Char to compare. |
| rhs | [Char](arkts-arkts-char-c.md) | 是 | the second Char to compare. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the two Chars are equal, false otherwise. |

## compareTo

```TypeScript
public compareTo(other: Char): int
```

Compares this instance to other Char object. The result is less than 0 if this instance lesser than provided object, 0 if they are equal, and greater than 0 otherwise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public compareTo(other: Char): int--><!--Device-Char-public compareTo(other: Char): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Char](arkts-arkts-char-c.md) | 是 | Char object to compare with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | a negative number if this instance is less than other, zero if equal, positive if greater. |

## constructor

```TypeScript
public constructor()
```

constructor() creates a default Char object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public constructor()--><!--Device-Char-public constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(value: char)
```

constructor(char) creates a Char object from a specified primitive char.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public constructor(value: char)--><!--Device-Char-public constructor(value: char)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | a primitive char to create Char from. |

## equals

```TypeScript
public equals(other: Any): boolean
```

equals(Object) compares two Chars by their underlying primitive chars.Returns false if the argument is not an instance of Char.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public equals(other: Any): boolean--><!--Device-Char-public equals(other: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Any | 是 | a reference to object to be compared with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the two Chars are equal, false otherwise. |

## getHighSurrogate

```TypeScript
public static getHighSurrogate(value: int): char
```

getHighSurrogate(int) splits code point as a two code units and returns the first one. The result can be malformed and thus has to be checked.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static getHighSurrogate(value: int): char--><!--Device-Char-public static getHighSurrogate(value: int): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | an encoded code point. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | the high surrogate code unit. |

## getLowSurrogate

```TypeScript
public static getLowSurrogate(value: int): char
```

getLowSurrogate(int) splits code point as a two code units and returns the second one. The result can be malformed and thus has to be checked.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static getLowSurrogate(value: int): char--><!--Device-Char-public static getLowSurrogate(value: int): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | an encoded code point. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | the low surrogate code unit. |

## isBinDigit

```TypeScript
public static isBinDigit(value: char): boolean
```

isBinDigit(char) checks whether the char represents a binary digit.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isBinDigit(value: char): boolean--><!--Device-Char-public static isBinDigit(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | a char to check. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the char is a binary digit, false otherwise. |

## isBinDigit

```TypeScript
public isBinDigit(): boolean
```

isBinDigit() checks whether the underlying char represents a binary digit.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public isBinDigit(): boolean--><!--Device-Char-public isBinDigit(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying char is a binary digit, false otherwise. |

## isDecDigit

```TypeScript
static isDecDigit(value: char): boolean
```

isDecDigit() checks whether the char represents a decimal digit.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-static isDecDigit(value: char): boolean--><!--Device-Char-static isDecDigit(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | a char to check. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the char is a decimal digit, false otherwise. |

## isDecDigit

```TypeScript
isDecDigit(): boolean
```

isDecDigit() checks whether the underlying char represents a decimal digit.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-isDecDigit(): boolean--><!--Device-Char-isDecDigit(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying char is a decimal digit, false otherwise. |

## isHexDigit

```TypeScript
public static isHexDigit(value: char): boolean
```

isHexDigit(char) checks whether the char represents a hexadecimal digit.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isHexDigit(value: char): boolean--><!--Device-Char-public static isHexDigit(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | a char to check. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the char is a hexadecimal digit, false otherwise. |

## isHexDigit

```TypeScript
public isHexDigit(): boolean
```

isHexDigit() checks whether the underlying char represents a hexadecimal digit.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public isHexDigit(): boolean--><!--Device-Char-public isHexDigit(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying char is a hexadecimal digit, false otherwise. |

## isHighSurrogate

```TypeScript
public static isHighSurrogate(value: char): boolean
```

isHighSurrogate(char) checks if the char is a high surrogate.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isHighSurrogate(value: char): boolean--><!--Device-Char-public static isHighSurrogate(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | the char to be checked. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the char is a high surrogate, false otherwise. |

## isInBasicMultilingualPlane

```TypeScript
public static isInBasicMultilingualPlane(value: char): boolean
```

isInBasicMultilingualPlane(char) checks if the char is in Basic Multilingual Plane. See UTF-16 for more details.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isInBasicMultilingualPlane(value: char): boolean--><!--Device-Char-public static isInBasicMultilingualPlane(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | the char to be checked. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the char is in Basic Multilingual Plane, false otherwise. |

## isInBasicMultilingualPlane

```TypeScript
public static isInBasicMultilingualPlane(value: int): boolean
```

isInBasicMultilingualPlane(int) checks if the code point is in Basic Multilingual Plane. See UTF-16 for more details.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isInBasicMultilingualPlane(value: int): boolean--><!--Device-Char-public static isInBasicMultilingualPlane(value: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | the code point to be checked. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the code point is in Basic Multilingual Plane, false otherwise. |

## isInBasicMultilingualPlane

```TypeScript
public isInBasicMultilingualPlane(): boolean
```

isInBasicMultilingualPlane() checks if the underlying char is in Basic Multilingual Plane. See UTF-16 for more details.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public isInBasicMultilingualPlane(): boolean--><!--Device-Char-public isInBasicMultilingualPlane(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying char is in Basic Multilingual Plane, false otherwise. |

## isLetter

```TypeScript
public static isLetter(value: char): boolean
```

isLetter(char) checks whether the char is a letter.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isLetter(value: char): boolean--><!--Device-Char-public static isLetter(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | a char to be tested. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the char is a letter, false otherwise. |

## isLetter

```TypeScript
public isLetter(): boolean
```

isLetter() checks whether the underlying char is a letter.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public isLetter(): boolean--><!--Device-Char-public isLetter(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying char is a letter, false otherwise. |

## isLowSurrogate

```TypeScript
public static isLowSurrogate(value: char): boolean
```

isLowSurrogate(char) checks if the char is a low surrogate.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isLowSurrogate(value: char): boolean--><!--Device-Char-public static isLowSurrogate(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | the char to be checked. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the char is a low surrogate, false otherwise. |

## isLowerCase

```TypeScript
public static isLowerCase(value: char): boolean
```

isLowerCase(char) checks whether the char is a lower case letter.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isLowerCase(value: char): boolean--><!--Device-Char-public static isLowerCase(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | a char to be tested. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the char is a lower case letter, false otherwise. |

## isLowerCase

```TypeScript
public isLowerCase(): boolean
```

isLowerCase() checks whether the underlying char is a lower case letter.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public isLowerCase(): boolean--><!--Device-Char-public isLowerCase(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying char is a lower case letter, false otherwise. |

## isPartOfSurrogatePair

```TypeScript
public static isPartOfSurrogatePair(value: char): boolean
```

isPartOfSurrogatePair(char) checks whether the char is low or high surrogate.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isPartOfSurrogatePair(value: char): boolean--><!--Device-Char-public static isPartOfSurrogatePair(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | the char to be tested. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the char is part of a surrogate pair, false otherwise. |

## isPartOfSurrogatePair

```TypeScript
public isPartOfSurrogatePair(): boolean
```

isPartOfSurrogatePair() checks whether the underlying char is low or high surrogate.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public isPartOfSurrogatePair(): boolean--><!--Device-Char-public isPartOfSurrogatePair(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying char is part of a surrogate pair, false otherwise. |

## isUpperCase

```TypeScript
public static isUpperCase(value: char): boolean
```

isUpperCase(char) checks whether the char is an upper case letter.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isUpperCase(value: char): boolean--><!--Device-Char-public static isUpperCase(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | a char to be tested. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the char is an upper case letter, false otherwise. |

## isUpperCase

```TypeScript
public isUpperCase(): boolean
```

isUpperCase() checks whether the underlying char is an upper case letter.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public isUpperCase(): boolean--><!--Device-Char-public isUpperCase(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying char is an upper case letter, false otherwise. |

## isValidCodePoint

```TypeScript
public static isValidCodePoint(codePoint: int): boolean
```

isValidCodePoint() checks if the code point is correctly encoded.See UTF-16 for more details.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isValidCodePoint(codePoint: int): boolean--><!--Device-Char-public static isValidCodePoint(codePoint: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| codePoint | int | 是 | the code point to be checked. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the code point is correctly encoded, false otherwise. |

## isWhiteSpace

```TypeScript
static isWhiteSpace(value: char): boolean
```

isWhiteSpace(char) checks whether the char is a whitespace char.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-static isWhiteSpace(value: char): boolean--><!--Device-Char-static isWhiteSpace(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | a char to be tested. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the char is a whitespace, false otherwise. |

## isWhiteSpace

```TypeScript
isWhiteSpace(): boolean
```

isWhiteSpace() checks whether the underlying char is a whitespace char.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-isWhiteSpace(): boolean--><!--Device-Char-isWhiteSpace(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the underlying char is a whitespace, false otherwise. |

## toByte

```TypeScript
public toByte(): byte
```

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toByte(): byte--><!--Device-Char-public toByte(): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | the byte value of this Char instance. |

## toByte

```TypeScript
public static toByte(value: char): byte
```

Returns the primitive as byte value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toByte(value: char): byte--><!--Device-Char-public static toByte(value: char): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | the byte value of the char. |

## toChar

```TypeScript
public toChar(): char
```

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toChar(): char--><!--Device-Char-public toChar(): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | the char value of this Char instance. |

## toChar

```TypeScript
public static toChar(value: char): char
```

Returns the primitive as char value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toChar(value: char): char--><!--Device-Char-public static toChar(value: char): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | the char value. |

## toDouble

```TypeScript
public toDouble(): double
```

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toDouble(): double--><!--Device-Char-public toDouble(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the double value of this Char instance. |

## toDouble

```TypeScript
public static toDouble(value: char): double
```

Returns the primitive as double value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toDouble(value: char): double--><!--Device-Char-public static toDouble(value: char): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the double value of the char. |

## toFloat

```TypeScript
public toFloat(): float
```

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toFloat(): float--><!--Device-Char-public toFloat(): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | the float value of this Char instance. |

## toFloat

```TypeScript
public static toFloat(value: char): float
```

Returns the primitive as float value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toFloat(value: char): float--><!--Device-Char-public static toFloat(value: char): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | the float value of the char. |

## toInt

```TypeScript
public toInt(): int
```

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toInt(): int--><!--Device-Char-public toInt(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the int value of this Char instance. |

## toInt

```TypeScript
public static toInt(value: char): int
```

Returns the primitive as int value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toInt(value: char): int--><!--Device-Char-public static toInt(value: char): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the int value of the char. |

## toLong

```TypeScript
public toLong(): long
```

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toLong(): long--><!--Device-Char-public toLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | the long value of this Char instance. |

## toLong

```TypeScript
public static toLong(value: char): long
```

Returns the primitive as long value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toLong(value: char): long--><!--Device-Char-public static toLong(value: char): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | the long value of the char. |

## toLowerCase

```TypeScript
public static toLowerCase(value: char): char
```

toLowerCase(char) converts the char to lower case if it is in upper case,otherwise the char is returned unchanged.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toLowerCase(value: char): char--><!--Device-Char-public static toLowerCase(value: char): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | a char to transform to lower case. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | the lower case char converted from the input char. |

## toLowerCase

```TypeScript
public toLowerCase(): Char
```

toLowerCase() converts the underlying char to lower case if it is in upper case, otherwise the char is returned unchanged.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toLowerCase(): Char--><!--Device-Char-public toLowerCase(): Char-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Char](arkts-arkts-char-c.md) | the lower case char converted from the underlying char. |

## toShort

```TypeScript
public toShort(): short
```

Returns value of this instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toShort(): short--><!--Device-Char-public toShort(): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | the short value of this Char instance. |

## toShort

```TypeScript
public static toShort(value: char): short
```

Returns the primitive as short value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toShort(value: char): short--><!--Device-Char-public static toShort(value: char): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | value to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | the short value of the char. |

## toString

```TypeScript
toString(): string
```

toString() converts Char to String object that contains a single element with the underlying char.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-toString(): string--><!--Device-Char-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the string representation of the Char. |

## toString

```TypeScript
static toString(value: char): string
```

Returns the primitive as string value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-static toString(value: char): string--><!--Device-Char-static toString(value: char): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | value to cast |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the string representation of the char value. |

## toString

```TypeScript
public toString(radix: int): string
```

Converts this object to a string with specified radix.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toString(radix: int): string--><!--Device-Char-public toString(radix: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | int | 是 | the radix of conversion. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | result of the conversion. |

## toUpperCase

```TypeScript
public static toUpperCase(value: char): char
```

toUpperCase(char) converts the char to upper case if it is in lower case,otherwise the char is returned unchanged.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toUpperCase(value: char): char--><!--Device-Char-public static toUpperCase(value: char): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | a char to transform to upper case. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | the upper case char converted from the input char. |

## toUpperCase

```TypeScript
public toUpperCase(): Char
```

toUpperCase() converts the underlying char to upper case if it is in lower case, otherwise the char is returned unchanged.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toUpperCase(): Char--><!--Device-Char-public toUpperCase(): Char-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Char](arkts-arkts-char-c.md) | the upper case char converted from the underlying char. |

## '\u0000'

```TypeScript
'\u0000'
```

**ArkTS模式：** 仅支持ArkTS-Sta

<!--Device-Char-'\u0000'--><!--Device-Char-'\u0000'-End-->

## '\uD800'

```TypeScript
'\uD800'
```

**ArkTS模式：** 仅支持ArkTS-Sta

<!--Device-Char-'\uD800'--><!--Device-Char-'\uD800'-End-->

## '\uDBFF'

```TypeScript
'\uDBFF'
```

**ArkTS模式：** 仅支持ArkTS-Sta

<!--Device-Char-'\uDBFF'--><!--Device-Char-'\uDBFF'-End-->

## '\uDC00'

```TypeScript
'\uDC00'
```

**ArkTS模式：** 仅支持ArkTS-Sta

<!--Device-Char-'\uDC00'--><!--Device-Char-'\uDC00'-End-->

## '\uDFFF'

```TypeScript
'\uDFFF'
```

**ArkTS模式：** 仅支持ArkTS-Sta

<!--Device-Char-'\uDFFF'--><!--Device-Char-'\uDFFF'-End-->

## '\uFFFF'

```TypeScript
'\uFFFF'
```

**ArkTS模式：** 仅支持ArkTS-Sta

<!--Device-Char-'\uFFFF'--><!--Device-Char-'\uFFFF'-End-->

## CHAR_BIT_SIZE

```TypeScript
public readonly CHAR_BIT_SIZE: int = 16
```

Size of the char type in bits.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public readonly CHAR_BIT_SIZE: int = 16--><!--Device-Char-public readonly CHAR_BIT_SIZE: int = 16-End-->

**系统能力：** SystemCapability.Utils.Lang

## HIGH_SURROGATE_MAX

```TypeScript
public static readonly HIGH_SURROGATE_MAX: char = c
```

Maximal high surrogate value.

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static readonly HIGH_SURROGATE_MAX: char = c--><!--Device-Char-public static readonly HIGH_SURROGATE_MAX: char = c-End-->

**系统能力：** SystemCapability.Utils.Lang

## HIGH_SURROGATE_MIN

```TypeScript
public static readonly HIGH_SURROGATE_MIN: char = c
```

Minimal high surrogate value.

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static readonly HIGH_SURROGATE_MIN: char = c--><!--Device-Char-public static readonly HIGH_SURROGATE_MIN: char = c-End-->

**系统能力：** SystemCapability.Utils.Lang

## LOW_SURROGATE_MAX

```TypeScript
public static readonly LOW_SURROGATE_MAX: char = c
```

Maximal low surrogate value.

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static readonly LOW_SURROGATE_MAX: char = c--><!--Device-Char-public static readonly LOW_SURROGATE_MAX: char = c-End-->

**系统能力：** SystemCapability.Utils.Lang

## LOW_SURROGATE_MIN

```TypeScript
public static readonly LOW_SURROGATE_MIN: char = c
```

Minimal low surrogate value.

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static readonly LOW_SURROGATE_MIN: char = c--><!--Device-Char-public static readonly LOW_SURROGATE_MIN: char = c-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_CODE_POINT

```TypeScript
public readonly MAX_CODE_POINT: int = 0x10FFFF
```

Maximal code point value.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public readonly MAX_CODE_POINT: int = 0x10FFFF--><!--Device-Char-public readonly MAX_CODE_POINT: int = 0x10FFFF-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static readonly MAX_VALUE: char = c
```

MAX_VALUE is a largest value of type char.

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static readonly MAX_VALUE: char = c--><!--Device-Char-public static readonly MAX_VALUE: char = c-End-->

**系统能力：** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static readonly MIN_VALUE: char = c
```

MIN_VALUE is a smallest value of type char.

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static readonly MIN_VALUE: char = c--><!--Device-Char-public static readonly MIN_VALUE: char = c-End-->

**系统能力：** SystemCapability.Utils.Lang

