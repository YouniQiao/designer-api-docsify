# Byte

表示装箱后的byte值及其相关操作。

**继承/实现关系：** Byte extends [Integral](arkts-arkts-numeric-integral-c.md) implements Comparable<Byte>

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export class Byte--><!--Device-unnamed-export class Byte-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## add

```TypeScript
public add(other: Byte): Byte
```

将当前实例与传入实例做整型加法运算，并以新实例返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public add(other: Byte): Byte--><!--Device-Byte-public add(other: Byte): Byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | 加法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Byte](arkts-arkts-byte-c.md) | 加法运算的结果。 |

## compareTo

```TypeScript
public compareTo(other: Byte): int
```

将当前实例与另一个Byte对象进行比较。当前实例小于传入对象时结果小于0， 相等时为0，否则大于0。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public compareTo(other: Byte): int--><!--Device-Byte-public compareTo(other: Byte): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | 用于比较的Byte对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 比较结果。 |

## constructor

```TypeScript
public constructor()
```

构造初始值为0的新Byte实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public constructor()--><!--Device-Byte-public constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(value: byte)
```

使用指定的初始值构造新的Byte实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public constructor(value: byte)--><!--Device-Byte-public constructor(value: byte)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | 初始值。 |

## div

```TypeScript
public div(other: Byte): Byte
```

将当前实例与传入实例做整型除法运算，并以新实例返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public div(other: Byte): Byte--><!--Device-Byte-public div(other: Byte): Byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | 除法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Byte](arkts-arkts-byte-c.md) | 除法运算的结果。 |

## equals

```TypeScript
public equals(other: Any): boolean
```

判断当前实例与按Byte处理的传入对象是否相等。如果传入对象的类型 与当前类型不一致，则返回false。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public equals(other: Any): boolean--><!--Device-Byte-public equals(other: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Any | 是 | 待比较的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果相等则返回true，否则返回false。 |

## isGreaterEqualThan

```TypeScript
public isGreaterEqualThan(other: Byte): boolean
```

判断当前实例的值是否大于或等于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public isGreaterEqualThan(other: Byte): boolean--><!--Device-Byte-public isGreaterEqualThan(other: Byte): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前实例大于或等于传入实例则返回true，否则返回false。 |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Byte): boolean
```

判断当前实例的值是否大于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public isGreaterThan(other: Byte): boolean--><!--Device-Byte-public isGreaterThan(other: Byte): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前实例大于传入实例则返回true，否则返回false。 |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Byte): boolean
```

判断当前实例的值是否小于或等于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public isLessEqualThan(other: Byte): boolean--><!--Device-Byte-public isLessEqualThan(other: Byte): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前实例小于或等于传入实例则返回true，否则返回false。 |

## isLessThan

```TypeScript
public isLessThan(other: Byte): boolean
```

判断当前实例的值是否小于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public isLessThan(other: Byte): boolean--><!--Device-Byte-public isLessThan(other: Byte): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前实例小于传入实例则返回true，否则返回false。 |

## mul

```TypeScript
public mul(other: Byte): Byte
```

将当前实例与传入实例做整型乘法运算，并以新实例返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public mul(other: Byte): Byte--><!--Device-Byte-public mul(other: Byte): Byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | 乘法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Byte](arkts-arkts-byte-c.md) | 乘法运算的结果。 |

## parseInt

```TypeScript
public static parseInt(s: string, r: int): byte
```

将字符串解析为byte值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static parseInt(s: string, r: int): byte--><!--Device-Byte-public static parseInt(s: string, r: int): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | 待解析的字符串。 |
| r | int | 是 | 字符串使用的基数。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | 解析得到的byte值。 |

## sub

```TypeScript
public sub(other: Byte): Byte
```

将当前实例与传入实例做整型减法运算，并以新实例返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public sub(other: Byte): Byte--><!--Device-Byte-public sub(other: Byte): Byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Byte](arkts-arkts-byte-c.md) | 是 | 减法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Byte](arkts-arkts-byte-c.md) | 减法运算的结果。 |

## toByte

```TypeScript
public toByte(): byte
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toByte(): byte--><!--Device-Byte-public toByte(): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | byte值。 |

## toByte

```TypeScript
public static toByte(value: byte): byte
```

以byte值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static toByte(value: byte): byte--><!--Device-Byte-public static toByte(value: byte): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | byte值。 |

## toChar

```TypeScript
public toChar(): char
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toChar(): char--><!--Device-Byte-public toChar(): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | char值。 |

## toChar

```TypeScript
public static toChar(value: byte): char
```

以char值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static toChar(value: byte): char--><!--Device-Byte-public static toChar(value: byte): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | 待转换的值。 |

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

<!--Device-Byte-public toDouble(): double--><!--Device-Byte-public toDouble(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | double值。 |

## toDouble

```TypeScript
public static toDouble(value: byte): double
```

以double值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static toDouble(value: byte): double--><!--Device-Byte-public static toDouble(value: byte): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | double值。 |

## toFloat

```TypeScript
public toFloat(): float
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toFloat(): float--><!--Device-Byte-public toFloat(): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | float值。 |

## toFloat

```TypeScript
public static toFloat(value: byte): float
```

以float值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static toFloat(value: byte): float--><!--Device-Byte-public static toFloat(value: byte): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | float值。 |

## toInt

```TypeScript
public toInt(): int
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toInt(): int--><!--Device-Byte-public toInt(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | int值。 |

## toInt

```TypeScript
public static toInt(value: byte): int
```

以int值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static toInt(value: byte): int--><!--Device-Byte-public static toInt(value: byte): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | int值。 |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string
```

返回表示数组元素的字符串。数组元素通过各自的toLocaleString 方法转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string--><!--Device-Byte-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | 否 | 包含BCP 47语言标签的字符串，或由此类 字符串组成的数组。 |
| options | Intl.NumberFormatOptions | 否 | 包含Intl.NumberFormat选项的部分或 全部属性的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 表示数组元素的字符串。 |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

返回表示数组元素的字符串。数组元素通过各自的toLocaleString 方法转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Byte-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | 否 | 包含BCP 47语言标签的字符串，或由此类 字符串组成的数组。 |
| options | object | 否 | 包含配置属性的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 表示数组元素的字符串。 |

## toLong

```TypeScript
public toLong(): long
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toLong(): long--><!--Device-Byte-public toLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | long值。 |

## toLong

```TypeScript
public static toLong(value: byte): long
```

以long值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static toLong(value: byte): long--><!--Device-Byte-public static toLong(value: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | long值。 |

## toShort

```TypeScript
public toShort(): short
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toShort(): short--><!--Device-Byte-public toShort(): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | short值。 |

## toShort

```TypeScript
public static toShort(value: byte): short
```

以short值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static toShort(value: byte): short--><!--Device-Byte-public static toShort(value: byte): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | short值。 |

## toString

```TypeScript
public toString(): string
```

将当前对象转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toString(): string--><!--Device-Byte-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 字符串表示。 |

## toString

```TypeScript
public static toString(v: byte): string
```

将基本类型值转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static toString(v: byte): string--><!--Device-Byte-public static toString(v: byte): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | byte | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 字符串表示。 |

## toString

```TypeScript
public toString(radix: int): string
```

将当前对象转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toString(radix: int): string--><!--Device-Byte-public toString(radix: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | int | 是 | 转换使用的基数。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 字符串表示。 |

## toString

```TypeScript
public toString(radix: double): string
```

将当前对象转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public toString(radix: double): string--><!--Device-Byte-public toString(radix: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | double | 是 | 转换使用的基数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 字符串表示。 |

## BIT_SIZE

```TypeScript
public static BIT_SIZE: byte = 8
```

该类型占用的位数。

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static BIT_SIZE: byte = 8--><!--Device-Byte-public static BIT_SIZE: byte = 8-End-->

**系统能力：** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static BYTE_SIZE: byte = 1
```

该类型占用的字节数。

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static BYTE_SIZE: byte = 1--><!--Device-Byte-public static BYTE_SIZE: byte = 1-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static MAX_VALUE: byte = 127
```

该类型作为整型时可表示的最大值。

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static MAX_VALUE: byte = 127--><!--Device-Byte-public static MAX_VALUE: byte = 127-End-->

**系统能力：** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static MIN_VALUE: byte = -128
```

该类型作为整型时可表示的最小值。

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Byte-public static MIN_VALUE: byte = -128--><!--Device-Byte-public static MIN_VALUE: byte = -128-End-->

**系统能力：** SystemCapability.Utils.Lang

