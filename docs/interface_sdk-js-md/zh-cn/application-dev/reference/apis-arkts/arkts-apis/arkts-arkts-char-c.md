# Char

表示装箱后的char值及其相关操作。

**继承/实现关系：** Char extends [Object](arkts-arkts-object-c.md) implements Comparable<Char>

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

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

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| highValue | char | 是 |
| lowValue | char | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## codeUnitsToEncode

```TypeScript
public static codeUnitsToEncode(value: int): int
```

codeUnitsToEncode(int)统计编码该UTF-16码点所需 码元的数量。详见UTF-16相关说明。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## compare

```TypeScript
public compare(lhs: Char, rhs: Char): boolean
```

compare(Char, Char)按底层的char值比较两个Char。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| lhs | Char | 是 |
| rhs | Char | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## compareTo

```TypeScript
public compareTo(other: Char): int
```

将当前实例与另一个Char对象进行比较。当前实例小于 当前实例小于传入对象时结果小于0，相等时为0， 否则大于0。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | Char | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## constructor

```TypeScript
public constructor()
```

constructor()创建默认的Char对象。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(value: char)
```

constructor(char)根据指定的基本类型char值创建Char对象。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

## equals

```TypeScript
public equals(other: Any): boolean
```

equals(Object)按底层的基本类型char值比较两个Char。 如果参数不是Char的实例，则返回false。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | Any | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## getHighSurrogate

```TypeScript
public static getHighSurrogate(value: int): char
```

getHighSurrogate(int)将码点拆分为两个码元，并返回其中的 第一个。返回结果可能不合法，因此需要进行校验。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| char |

## getLowSurrogate

```TypeScript
public static getLowSurrogate(value: int): char
```

getLowSurrogate(int)将码点拆分为两个码元，并返回其中的 第二个。返回结果可能不合法，因此需要进行校验。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| char |

## isBinDigit

```TypeScript
public static isBinDigit(value: char): boolean
```

isBinDigit(char)检查该char值是否表示二进制数字。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isBinDigit

```TypeScript
public isBinDigit(): boolean
```

isBinDigit()检查底层的char值是否表示二进制数字。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isDecDigit

```TypeScript
static isDecDigit(value: char): boolean
```

isDecDigit()检查该char值是否表示十进制数字。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isDecDigit

```TypeScript
isDecDigit(): boolean
```

isDecDigit()检查底层的char值是否表示十进制数字。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isHexDigit

```TypeScript
public static isHexDigit(value: char): boolean
```

isHexDigit(char)检查该char值是否表示十六进制数字。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isHexDigit

```TypeScript
public isHexDigit(): boolean
```

isHexDigit()检查底层的char值是否表示十六进制数字。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isHighSurrogate

```TypeScript
public static isHighSurrogate(value: char): boolean
```

isHighSurrogate(char)检查该char值是否为高位代理项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isInBasicMultilingualPlane

```TypeScript
public static isInBasicMultilingualPlane(value: char): boolean
```

isInBasicMultilingualPlane(char)检查该char值是否位于基本多文种 平面。详见UTF-16相关说明。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isInBasicMultilingualPlane

```TypeScript
public static isInBasicMultilingualPlane(value: int): boolean
```

isInBasicMultilingualPlane(int)检查该码点是否位于 基本多文种平面。详见UTF-16相关说明。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isInBasicMultilingualPlane

```TypeScript
public isInBasicMultilingualPlane(): boolean
```

isInBasicMultilingualPlane()检查底层的char值是否位于基本 多文种平面。详见UTF-16相关说明。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isLetter

```TypeScript
public static isLetter(value: char): boolean
```

isLetter(char)检查该char值是否为字母。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isLetter

```TypeScript
public isLetter(): boolean
```

isLetter()检查底层的char值是否为字母。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isLowerCase

```TypeScript
public static isLowerCase(value: char): boolean
```

isLowerCase(char)检查该char值是否为小写字母。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isLowerCase

```TypeScript
public isLowerCase(): boolean
```

isLowerCase()检查底层的char值是否为小写字母。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isLowSurrogate

```TypeScript
public static isLowSurrogate(value: char): boolean
```

isLowSurrogate(char)检查该char值是否为低位代理项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isPartOfSurrogatePair

```TypeScript
public static isPartOfSurrogatePair(value: char): boolean
```

isPartOfSurrogatePair(char)检查该char值是低位还是高位代理项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isPartOfSurrogatePair

```TypeScript
public isPartOfSurrogatePair(): boolean
```

isPartOfSurrogatePair()检查底层的char值是低位还是高位代理项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isUpperCase

```TypeScript
public static isUpperCase(value: char): boolean
```

isUpperCase(char)检查该char值是否为大写字母。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isUpperCase

```TypeScript
public isUpperCase(): boolean
```

isUpperCase()检查底层的char值是否为大写字母。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isValidCodePoint

```TypeScript
public static isValidCodePoint(codePoint: int): boolean
```

isValidCodePoint()检查该码点的编码是否正确。 详见UTF-16相关说明。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| codePoint | int | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isWhiteSpace

```TypeScript
static isWhiteSpace(value: char): boolean
```

isWhiteSpace(char)检查该char值是否为空白字符。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isWhiteSpace

```TypeScript
isWhiteSpace(): boolean
```

isWhiteSpace()检查底层的char值是否为空白字符。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## toByte

```TypeScript
public toByte(): byte
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| byte |

## toByte

```TypeScript
public static toByte(value: char): byte
```

以byte值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| byte |

## toChar

```TypeScript
public toChar(): char
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| char |

## toChar

```TypeScript
public static toChar(value: char): char
```

以char值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| char |

## toDouble

```TypeScript
public toDouble(): double
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| double |

## toDouble

```TypeScript
public static toDouble(value: char): double
```

以double值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| double |

## toFloat

```TypeScript
public toFloat(): float
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| float |

## toFloat

```TypeScript
public static toFloat(value: char): float
```

以float值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| float |

## toInt

```TypeScript
public toInt(): int
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## toInt

```TypeScript
public static toInt(value: char): int
```

以int值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## toLong

```TypeScript
public toLong(): long
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| long |

## toLong

```TypeScript
public static toLong(value: char): long
```

以long值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## toLowerCase

```TypeScript
public static toLowerCase(value: char): char
```

toLowerCase(char)在该char值为大写时将其转换为小写， 否则原样返回该char值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| char |

## toLowerCase

```TypeScript
public toLowerCase(): Char
```

toLowerCase()在底层char值为大写时将其转换为小写， 否则原样返回该char值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Char |

## toShort

```TypeScript
public toShort(): short
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| short |

## toShort

```TypeScript
public static toShort(value: char): short
```

以short值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| short |

## toString

```TypeScript
toString(): string
```

toString()将Char转换为仅包含底层char值这一个元素的String对象。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## toString

```TypeScript
static toString(value: char): string
```

以字符串值的形式返回该基本类型值。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## toString

```TypeScript
public toString(radix: int): string
```

使用指定基数将当前对象转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radix | int | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## toUpperCase

```TypeScript
public static toUpperCase(value: char): char
```

toUpperCase(char)在该char值为小写时将其转换为大写， 否则原样返回该char值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | char | 是 |

**返回值：**

| 类型 |
| --- |
| char |

## toUpperCase

```TypeScript
public toUpperCase(): Char
```

toUpperCase()在底层char值为小写时将其转换为大写， 否则原样返回该char值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Char |

## '\u0000'

```TypeScript
'\u0000'
```

**ArkTS模式：** 

## '\uD800'

```TypeScript
'\uD800'
```

**ArkTS模式：** 

## '\uDBFF'

```TypeScript
'\uDBFF'
```

**ArkTS模式：** 

## '\uDC00'

```TypeScript
'\uDC00'
```

**ArkTS模式：** 

## '\uDFFF'

```TypeScript
'\uDFFF'
```

**ArkTS模式：** 

## '\uFFFF'

```TypeScript
'\uFFFF'
```

**ArkTS模式：** 

## CHAR_BIT_SIZE

```TypeScript
public readonly CHAR_BIT_SIZE: int = 16
```

char类型占用的位数。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## HIGH_SURROGATE_MAX

```TypeScript
public static readonly HIGH_SURROGATE_MAX: char = c
```

高位代理项的最大值。

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## HIGH_SURROGATE_MIN

```TypeScript
public static readonly HIGH_SURROGATE_MIN: char = c
```

高位代理项的最小值。

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## LOW_SURROGATE_MAX

```TypeScript
public static readonly LOW_SURROGATE_MAX: char = c
```

低位代理项的最大值。

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## LOW_SURROGATE_MIN

```TypeScript
public static readonly LOW_SURROGATE_MIN: char = c
```

低位代理项的最小值。

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## MAX_CODE_POINT

```TypeScript
public readonly MAX_CODE_POINT: int = 0x10FFFF
```

码点的最大值。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static readonly MAX_VALUE: char = c
```

MAX_VALUE为char类型的最大值。

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static readonly MIN_VALUE: char = c
```

MIN_VALUE为char类型的最小值。

**类型：** char

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang
