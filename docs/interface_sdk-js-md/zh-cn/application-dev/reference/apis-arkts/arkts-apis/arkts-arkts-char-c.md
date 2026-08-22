# Char

表示装箱后的char值及其相关操作。

**继承/实现关系：** Char extends [Object](arkts-arkts-object-c.md) implements Comparable<Char>

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

<!--Device-unnamed-class Char--><!--Device-unnamed-class Char-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## charsToCodePoint

```TypeScript
public static charsToCodePoint(highValue: char, lowValue: char): int
```

charsToCodePoint(char, char)将两个char合并为一个码点。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static charsToCodePoint(highValue: char, lowValue: char): int--><!--Device-Char-public static charsToCodePoint(highValue: char, lowValue: char): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| highValue | char | 是 | 高位代理项的值。 |
| lowValue | char | 是 | 低位代理项的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 合并得到的UTF-16码点。 |

## codeUnitsToEncode

```TypeScript
public static codeUnitsToEncode(value: int): int
```

codeUnitsToEncode(int)统计编码该UTF-16码点所需 码元的数量。详见UTF-16相关说明。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static codeUnitsToEncode(value: int): int--><!--Device-Char-public static codeUnitsToEncode(value: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 待检查的UTF-16码点。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 编码该码点所需UTF-16码元的number。 |

## compare

```TypeScript
public compare(lhs: Char, rhs: Char): boolean
```

compare(Char, Char)按底层的char值比较两个Char。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public compare(lhs: Char, rhs: Char): boolean--><!--Device-Char-public compare(lhs: Char, rhs: Char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lhs | [Char](arkts-arkts-char-c.md) | 是 | 参与比较的第一个Char。 |
| rhs | [Char](arkts-arkts-char-c.md) | 是 | 参与比较的第二个Char。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果两个Char相等则返回true，否则返回false。 |

## compareTo

```TypeScript
public compareTo(other: Char): int
```

将当前实例与另一个Char对象进行比较。当前实例小于 当前实例小于传入对象时结果小于0，相等时为0， 否则大于0。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public compareTo(other: Char): int--><!--Device-Char-public compareTo(other: Char): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Char](arkts-arkts-char-c.md) | 是 | 用于比较的Char对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 当前实例小于传入实例时返回负number值，相等时返回0，大于时返回正值。 |

## constructor

```TypeScript
public constructor()
```

constructor()创建默认的Char对象。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public constructor()--><!--Device-Char-public constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(value: char)
```

constructor(char)根据指定的基本类型char值创建Char对象。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public constructor(value: char)--><!--Device-Char-public constructor(value: char)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 用于创建Char的基本类型char值。 |

## equals

```TypeScript
public equals(other: Any): boolean
```

equals(Object)按底层的基本类型char值比较两个Char。 如果参数不是Char的实例，则返回false。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public equals(other: Any): boolean--><!--Device-Char-public equals(other: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Any | 是 | 待比较对象的引用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果两个Char相等则返回true，否则返回false。 |

## getHighSurrogate

```TypeScript
public static getHighSurrogate(value: int): char
```

getHighSurrogate(int)将码点拆分为两个码元，并返回其中的 第一个。返回结果可能不合法，因此需要进行校验。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static getHighSurrogate(value: int): char--><!--Device-Char-public static getHighSurrogate(value: int): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 编码后的码点。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | 高位代理码元。 |

## getLowSurrogate

```TypeScript
public static getLowSurrogate(value: int): char
```

getLowSurrogate(int)将码点拆分为两个码元，并返回其中的 第二个。返回结果可能不合法，因此需要进行校验。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static getLowSurrogate(value: int): char--><!--Device-Char-public static getLowSurrogate(value: int): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 编码后的码点。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | 低位代理码元。 |

## isBinDigit

```TypeScript
public static isBinDigit(value: char): boolean
```

isBinDigit(char)检查该char值是否表示二进制数字。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isBinDigit(value: char): boolean--><!--Device-Char-public static isBinDigit(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待检查的char值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该char值是二进制数字则返回true，否则返回false。 |

## isBinDigit

```TypeScript
public isBinDigit(): boolean
```

isBinDigit()检查底层的char值是否表示二进制数字。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public isBinDigit(): boolean--><!--Device-Char-public isBinDigit(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的char值是二进制数字则返回true，否则返回false。 |

## isDecDigit

```TypeScript
static isDecDigit(value: char): boolean
```

isDecDigit()检查该char值是否表示十进制数字。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-static isDecDigit(value: char): boolean--><!--Device-Char-static isDecDigit(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待检查的char值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该char值是十进制数字则返回true，否则返回false。 |

## isDecDigit

```TypeScript
isDecDigit(): boolean
```

isDecDigit()检查底层的char值是否表示十进制数字。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-isDecDigit(): boolean--><!--Device-Char-isDecDigit(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的char值是十进制数字则返回true，否则返回false。 |

## isHexDigit

```TypeScript
public static isHexDigit(value: char): boolean
```

isHexDigit(char)检查该char值是否表示十六进制数字。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isHexDigit(value: char): boolean--><!--Device-Char-public static isHexDigit(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待检查的char值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该char值是十六进制数字则返回true，否则返回false。 |

## isHexDigit

```TypeScript
public isHexDigit(): boolean
```

isHexDigit()检查底层的char值是否表示十六进制数字。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public isHexDigit(): boolean--><!--Device-Char-public isHexDigit(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的char值是十六进制数字则返回true，否则返回false。 |

## isHighSurrogate

```TypeScript
public static isHighSurrogate(value: char): boolean
```

isHighSurrogate(char)检查该char值是否为高位代理项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isHighSurrogate(value: char): boolean--><!--Device-Char-public static isHighSurrogate(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待检查的char值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该char值是高位代理项则返回true，否则返回false。 |

## isInBasicMultilingualPlane

```TypeScript
public static isInBasicMultilingualPlane(value: char): boolean
```

isInBasicMultilingualPlane(char)检查该char值是否位于基本多文种 平面。详见UTF-16相关说明。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isInBasicMultilingualPlane(value: char): boolean--><!--Device-Char-public static isInBasicMultilingualPlane(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待检查的char值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该char值位于基本多文种平面则返回true，否则返回false。 |

## isInBasicMultilingualPlane

```TypeScript
public static isInBasicMultilingualPlane(value: int): boolean
```

isInBasicMultilingualPlane(int)检查该码点是否位于 基本多文种平面。详见UTF-16相关说明。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isInBasicMultilingualPlane(value: int): boolean--><!--Device-Char-public static isInBasicMultilingualPlane(value: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 待检查的码点。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该码点位于基本多文种平面则返回true，否则返回false。 |

## isInBasicMultilingualPlane

```TypeScript
public isInBasicMultilingualPlane(): boolean
```

isInBasicMultilingualPlane()检查底层的char值是否位于基本 多文种平面。详见UTF-16相关说明。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public isInBasicMultilingualPlane(): boolean--><!--Device-Char-public isInBasicMultilingualPlane(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的char值位于基本多文种平面则返回true，否则返回false。 |

## isLetter

```TypeScript
public static isLetter(value: char): boolean
```

isLetter(char)检查该char值是否为字母。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isLetter(value: char): boolean--><!--Device-Char-public static isLetter(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待检测的char值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该char值是字母则返回true，否则返回false。 |

## isLetter

```TypeScript
public isLetter(): boolean
```

isLetter()检查底层的char值是否为字母。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public isLetter(): boolean--><!--Device-Char-public isLetter(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的char值是字母则返回true，否则返回false。 |

## isLowerCase

```TypeScript
public static isLowerCase(value: char): boolean
```

isLowerCase(char)检查该char值是否为小写字母。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isLowerCase(value: char): boolean--><!--Device-Char-public static isLowerCase(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待检测的char值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该char值是小写字母则返回true，否则返回false。 |

## isLowerCase

```TypeScript
public isLowerCase(): boolean
```

isLowerCase()检查底层的char值是否为小写字母。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public isLowerCase(): boolean--><!--Device-Char-public isLowerCase(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的char值是小写字母则返回true，否则返回false。 |

## isLowSurrogate

```TypeScript
public static isLowSurrogate(value: char): boolean
```

isLowSurrogate(char)检查该char值是否为低位代理项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isLowSurrogate(value: char): boolean--><!--Device-Char-public static isLowSurrogate(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待检查的char值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该char值是低位代理项则返回true，否则返回false。 |

## isPartOfSurrogatePair

```TypeScript
public static isPartOfSurrogatePair(value: char): boolean
```

isPartOfSurrogatePair(char)检查该char值是低位还是高位代理项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isPartOfSurrogatePair(value: char): boolean--><!--Device-Char-public static isPartOfSurrogatePair(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待检测的char值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该char值是代理对的一部分则返回true，否则返回false。 |

## isPartOfSurrogatePair

```TypeScript
public isPartOfSurrogatePair(): boolean
```

isPartOfSurrogatePair()检查底层的char值是低位还是高位代理项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public isPartOfSurrogatePair(): boolean--><!--Device-Char-public isPartOfSurrogatePair(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的char值是代理对的一部分则返回true，否则返回false。 |

## isUpperCase

```TypeScript
public static isUpperCase(value: char): boolean
```

isUpperCase(char)检查该char值是否为大写字母。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isUpperCase(value: char): boolean--><!--Device-Char-public static isUpperCase(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待检测的char值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该char值是大写字母则返回true，否则返回false。 |

## isUpperCase

```TypeScript
public isUpperCase(): boolean
```

isUpperCase()检查底层的char值是否为大写字母。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public isUpperCase(): boolean--><!--Device-Char-public isUpperCase(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的char值是大写字母则返回true，否则返回false。 |

## isValidCodePoint

```TypeScript
public static isValidCodePoint(codePoint: int): boolean
```

isValidCodePoint()检查该码点的编码是否正确。 详见UTF-16相关说明。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static isValidCodePoint(codePoint: int): boolean--><!--Device-Char-public static isValidCodePoint(codePoint: int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| codePoint | int | 是 | 待检查的码点。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该码点编码正确则返回true，否则返回false。 |

## isWhiteSpace

```TypeScript
static isWhiteSpace(value: char): boolean
```

isWhiteSpace(char)检查该char值是否为空白字符。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-static isWhiteSpace(value: char): boolean--><!--Device-Char-static isWhiteSpace(value: char): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待检测的char值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该char值是空白字符则返回true，否则返回false。 |

## isWhiteSpace

```TypeScript
isWhiteSpace(): boolean
```

isWhiteSpace()检查底层的char值是否为空白字符。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-isWhiteSpace(): boolean--><!--Device-Char-isWhiteSpace(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的char值是空白字符则返回true，否则返回false。 |

## toByte

```TypeScript
public toByte(): byte
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toByte(): byte--><!--Device-Char-public toByte(): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | 该Char实例的byte值。 |

## toByte

```TypeScript
public static toByte(value: char): byte
```

以byte值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toByte(value: char): byte--><!--Device-Char-public static toByte(value: char): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | 该char的byte值。 |

## toChar

```TypeScript
public toChar(): char
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toChar(): char--><!--Device-Char-public toChar(): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | 该Char实例的char值。 |

## toChar

```TypeScript
public static toChar(value: char): char
```

以char值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toChar(value: char): char--><!--Device-Char-public static toChar(value: char): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | char值。 |

## toDouble

```TypeScript
public toDouble(): double
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toDouble(): double--><!--Device-Char-public toDouble(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 该Char实例的double值。 |

## toDouble

```TypeScript
public static toDouble(value: char): double
```

以double值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toDouble(value: char): double--><!--Device-Char-public static toDouble(value: char): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 该char的double值。 |

## toFloat

```TypeScript
public toFloat(): float
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toFloat(): float--><!--Device-Char-public toFloat(): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | 该Char实例的float值。 |

## toFloat

```TypeScript
public static toFloat(value: char): float
```

以float值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toFloat(value: char): float--><!--Device-Char-public static toFloat(value: char): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | 该char的float值。 |

## toInt

```TypeScript
public toInt(): int
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toInt(): int--><!--Device-Char-public toInt(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 该Char实例的int值。 |

## toInt

```TypeScript
public static toInt(value: char): int
```

以int值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toInt(value: char): int--><!--Device-Char-public static toInt(value: char): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 该char的int值。 |

## toLong

```TypeScript
public toLong(): long
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toLong(): long--><!--Device-Char-public toLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 该Char实例的long值。 |

## toLong

```TypeScript
public static toLong(value: char): long
```

以long值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toLong(value: char): long--><!--Device-Char-public static toLong(value: char): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 该char的long值。 |

## toLowerCase

```TypeScript
public static toLowerCase(value: char): char
```

toLowerCase(char)在该char值为大写时将其转换为小写， 否则原样返回该char值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toLowerCase(value: char): char--><!--Device-Char-public static toLowerCase(value: char): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待转换为小写的char值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | 由传入char值转换得到的小写char值。 |

## toLowerCase

```TypeScript
public toLowerCase(): Char
```

toLowerCase()在底层char值为大写时将其转换为小写， 否则原样返回该char值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toLowerCase(): Char--><!--Device-Char-public toLowerCase(): Char-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Char](arkts-arkts-char-c.md) | 由底层char值转换得到的小写char值。 |

## toShort

```TypeScript
public toShort(): short
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toShort(): short--><!--Device-Char-public toShort(): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | 该Char实例的short值。 |

## toShort

```TypeScript
public static toShort(value: char): short
```

以short值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toShort(value: char): short--><!--Device-Char-public static toShort(value: char): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | 该char的short值。 |

## toString

```TypeScript
toString(): string
```

toString()将Char转换为仅包含底层char值这一个元素的String对象。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-toString(): string--><!--Device-Char-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该Char的字符串表示。 |

## toString

```TypeScript
static toString(value: char): string
```

以字符串值的形式返回该基本类型值。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-static toString(value: char): string--><!--Device-Char-static toString(value: char): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该char值的字符串表示。 |

## toString

```TypeScript
public toString(radix: int): string
```

使用指定基数将当前对象转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toString(radix: int): string--><!--Device-Char-public toString(radix: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | int | 是 | 转换使用的基数。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toUpperCase

```TypeScript
public static toUpperCase(value: char): char
```

toUpperCase(char)在该char值为小写时将其转换为大写， 否则原样返回该char值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static toUpperCase(value: char): char--><!--Device-Char-public static toUpperCase(value: char): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 待转换为大写的char值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | 由传入char值转换得到的大写char值。 |

## toUpperCase

```TypeScript
public toUpperCase(): Char
```

toUpperCase()在底层char值为小写时将其转换为大写， 否则原样返回该char值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public toUpperCase(): Char--><!--Device-Char-public toUpperCase(): Char-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Char](arkts-arkts-char-c.md) | 由底层char值转换得到的大写char值。 |

## '\u0000'

```TypeScript
'\u0000'
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-Char-'\u0000'--><!--Device-Char-'\u0000'-End-->

## '\uD800'

```TypeScript
'\uD800'
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-Char-'\uD800'--><!--Device-Char-'\uD800'-End-->

## '\uDBFF'

```TypeScript
'\uDBFF'
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-Char-'\uDBFF'--><!--Device-Char-'\uDBFF'-End-->

## '\uDC00'

```TypeScript
'\uDC00'
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-Char-'\uDC00'--><!--Device-Char-'\uDC00'-End-->

## '\uDFFF'

```TypeScript
'\uDFFF'
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-Char-'\uDFFF'--><!--Device-Char-'\uDFFF'-End-->

## '\uFFFF'

```TypeScript
'\uFFFF'
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-Char-'\uFFFF'--><!--Device-Char-'\uFFFF'-End-->

## CHAR_BIT_SIZE

```TypeScript
public readonly CHAR_BIT_SIZE: int = 16
```

char类型占用的位数。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public readonly CHAR_BIT_SIZE: int = 16--><!--Device-Char-public readonly CHAR_BIT_SIZE: int = 16-End-->

**系统能力：** SystemCapability.Utils.Lang

## HIGH_SURROGATE_MAX

```TypeScript
public static readonly HIGH_SURROGATE_MAX: char = c
```

高位代理项的最大值。

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static readonly HIGH_SURROGATE_MAX: char = c--><!--Device-Char-public static readonly HIGH_SURROGATE_MAX: char = c-End-->

**系统能力：** SystemCapability.Utils.Lang

## HIGH_SURROGATE_MIN

```TypeScript
public static readonly HIGH_SURROGATE_MIN: char = c
```

高位代理项的最小值。

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static readonly HIGH_SURROGATE_MIN: char = c--><!--Device-Char-public static readonly HIGH_SURROGATE_MIN: char = c-End-->

**系统能力：** SystemCapability.Utils.Lang

## LOW_SURROGATE_MAX

```TypeScript
public static readonly LOW_SURROGATE_MAX: char = c
```

低位代理项的最大值。

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static readonly LOW_SURROGATE_MAX: char = c--><!--Device-Char-public static readonly LOW_SURROGATE_MAX: char = c-End-->

**系统能力：** SystemCapability.Utils.Lang

## LOW_SURROGATE_MIN

```TypeScript
public static readonly LOW_SURROGATE_MIN: char = c
```

低位代理项的最小值。

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static readonly LOW_SURROGATE_MIN: char = c--><!--Device-Char-public static readonly LOW_SURROGATE_MIN: char = c-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_CODE_POINT

```TypeScript
public readonly MAX_CODE_POINT: int = 0x10FFFF
```

码点的最大值。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public readonly MAX_CODE_POINT: int = 0x10FFFF--><!--Device-Char-public readonly MAX_CODE_POINT: int = 0x10FFFF-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static readonly MAX_VALUE: char = c
```

MAX_VALUE为char类型的最大值。

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static readonly MAX_VALUE: char = c--><!--Device-Char-public static readonly MAX_VALUE: char = c-End-->

**系统能力：** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static readonly MIN_VALUE: char = c
```

MIN_VALUE为char类型的最小值。

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Char-public static readonly MIN_VALUE: char = c--><!--Device-Char-public static readonly MIN_VALUE: char = c-End-->

**系统能力：** SystemCapability.Utils.Lang

