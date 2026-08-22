# Int

表示装箱后的int值及其相关操作。

**继承/实现关系：** Int extends [Integral](arkts-arkts-numeric-integral-c.md) implements Comparable<Int>

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

<!--Device-unnamed-export class Int--><!--Device-unnamed-export class Int-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## add

```TypeScript
public add(other: Int): Int
```

与传入实例做整型加法运算。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public add(other: Int): Int--><!--Device-Int-public add(other: Int): Int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | 加法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Int](arkts-arkts-int-c.md) | 加法运算的结果。 |

## compareTo

```TypeScript
public compareTo(other: Int): int
```

将当前实例与另一个Int对象进行比较。当前实例小于 传入对象时结果小于0，相等时为0，否则 大于0。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public compareTo(other: Int): int--><!--Device-Int-public compareTo(other: Int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | 用于比较的Int对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 比较结果，取值为-1、0或1。 |

## constructor

```TypeScript
constructor()
```

构造初始值为0的新Int实例。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-constructor()--><!--Device-Int-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(value: int)
```

使用指定的初始值构造新的Int实例。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-constructor(value: int)--><!--Device-Int-constructor(value: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 初始值。 <br>取值约束：应为整数。 |

## div

```TypeScript
public div(other: Int): Int
```

与传入实例做整型除法运算。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public div(other: Int): Int--><!--Device-Int-public div(other: Int): Int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | 除法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Int](arkts-arkts-int-c.md) | 除法运算的结果。 |

## equals

```TypeScript
equals(other: Any): boolean
```

将当前对象与指定对象进行相等性比较。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-equals(other: Any): boolean--><!--Device-Int-equals(other: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Any | 是 | 用于比较的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果指定对象与当前对象相等则返回true，否则返回false。 |

## isGreaterEqualThan

```TypeScript
public isGreaterEqualThan(other: Int): boolean
```

判断当前实例的值是否大于或等于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public isGreaterEqualThan(other: Int): boolean--><!--Device-Int-public isGreaterEqualThan(other: Int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值大于或等于传入值则返回true，否则返回false。 |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Int): boolean
```

判断当前实例的值是否大于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public isGreaterThan(other: Int): boolean--><!--Device-Int-public isGreaterThan(other: Int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值大于传入值则返回true，否则返回false。 |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Int): boolean
```

判断当前实例的值是否小于或等于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public isLessEqualThan(other: Int): boolean--><!--Device-Int-public isLessEqualThan(other: Int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值小于或等于传入值则返回true，否则返回false。 |

## isLessThan

```TypeScript
public isLessThan(other: Int): boolean
```

判断当前实例的值是否小于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public isLessThan(other: Int): boolean--><!--Device-Int-public isLessThan(other: Int): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值小于传入值则返回true，否则返回false。 |

## mul

```TypeScript
public mul(other: Int): Int
```

与传入实例做整型乘法运算。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public mul(other: Int): Int--><!--Device-Int-public mul(other: Int): Int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | 乘法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Int](arkts-arkts-int-c.md) | 乘法运算的结果。 |

## parseInt

```TypeScript
public static parseInt(s: string, r: int): int
```

按指定基数从字符串解析出整数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static parseInt(s: string, r: int): int--><!--Device-Int-public static parseInt(s: string, r: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | 待转换的字符串。 |
| r | int | 是 | 转换使用的基数，取值范围为2~36。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 解析结果。 |

## sub

```TypeScript
public sub(other: Int): Int
```

与传入实例做整型减法运算。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public sub(other: Int): Int--><!--Device-Int-public sub(other: Int): Int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Int](arkts-arkts-int-c.md) | 是 | 减法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Int](arkts-arkts-int-c.md) | 减法运算的结果。 |

## toByte

```TypeScript
public toByte(): byte
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toByte(): byte--><!--Device-Int-public toByte(): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | byte类型的值。 |

## toByte

```TypeScript
public static toByte(value: int): byte
```

以byte值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static toByte(value: int): byte--><!--Device-Int-public static toByte(value: int): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 待转换的值。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | 转换后的值。 |

## toChar

```TypeScript
public toChar(): char
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toChar(): char--><!--Device-Int-public toChar(): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | char类型的值。 |

## toChar

```TypeScript
public static toChar(value: int): char
```

以char值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static toChar(value: int): char--><!--Device-Int-public static toChar(value: int): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 待转换的值。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | 转换后的值。 |

## toDouble

```TypeScript
public toDouble(): double
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toDouble(): double--><!--Device-Int-public toDouble(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | double类型的值。 |

## toDouble

```TypeScript
public static toDouble(value: int): double
```

以double值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static toDouble(value: int): double--><!--Device-Int-public static toDouble(value: int): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 待转换的值。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 转换后的值。 |

## toFloat

```TypeScript
public toFloat(): float
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toFloat(): float--><!--Device-Int-public toFloat(): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | float类型的值。 |

## toFloat

```TypeScript
public static toFloat(value: int): float
```

以float值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static toFloat(value: int): float--><!--Device-Int-public static toFloat(value: int): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 待转换的值。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | 转换后的值。 |

## toInt

```TypeScript
toInt(): int
```

将当前实例的值转换为int。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-toInt(): int--><!--Device-Int-toInt(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 该实例表示的int值。 |

## toInt

```TypeScript
static toInt(value: int): int
```

直接返回基本类型的int值。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-static toInt(value: int): int--><!--Device-Int-static toInt(value: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 待返回的int值。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 与传入值相同的int值。 |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string
```

将当前对象转换为符合区域设置的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string--><!--Device-Int-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | 否 | 包含BCP 47语言标签的字符串，或由此类 字符串组成的数组。 |
| options | Intl.NumberFormatOptions | 否 | 包含Intl.NumberFormat选项的部分或 全部属性的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 按区域设置转换后的结果。 |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

将当前对象转换为符合区域设置的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Int-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | 否 | 包含BCP 47语言标签的字符串，或由此类 字符串组成的数组。 |
| options | object | 否 | 包含Intl.NumberFormat选项的部分或 全部属性的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 按区域设置转换后的结果。 |

## toLong

```TypeScript
public toLong(): long
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toLong(): long--><!--Device-Int-public toLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | long类型的值。 |

## toLong

```TypeScript
public static toLong(value: int): long
```

以long值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static toLong(value: int): long--><!--Device-Int-public static toLong(value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 待转换的值。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 转换后的值。 |

## toShort

```TypeScript
public toShort(): short
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toShort(): short--><!--Device-Int-public toShort(): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | short类型的值。 |

## toShort

```TypeScript
public static toShort(value: int): short
```

以short值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static toShort(value: int): short--><!--Device-Int-public static toShort(value: int): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 待转换的值。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | 转换后的值。 |

## toString

```TypeScript
static toString(v: int): string
```

将指定的int值转换为字符串表示。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-static toString(v: int): string--><!--Device-Int-static toString(v: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | int | 是 | 待转换的int值。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该int值的字符串表示。 |

## toString

```TypeScript
toString(): string
```

将当前Int对象的值转换为字符串表示。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-toString(): string--><!--Device-Int-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该Int对象值的字符串表示。 |

## toString

```TypeScript
public toString(radix: int): string
```

使用指定基数将当前对象转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toString(radix: int): string--><!--Device-Int-public toString(radix: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | int | 是 | 使用的基数。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toString

```TypeScript
public toString(radix: double): string
```

使用指定基数将当前对象转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public toString(radix: double): string--><!--Device-Int-public toString(radix: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | double | 是 | 使用的基数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## BIT_SIZE

```TypeScript
public static readonly BIT_SIZE: byte = 32
```

该类型占用的位数。

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static readonly BIT_SIZE: byte = 32--><!--Device-Int-public static readonly BIT_SIZE: byte = 32-End-->

**系统能力：** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static readonly BYTE_SIZE: byte = 4
```

该类型占用的字节数。

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static readonly BYTE_SIZE: byte = 4--><!--Device-Int-public static readonly BYTE_SIZE: byte = 4-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static readonly MAX_VALUE: int = 2147483647
```

该类型作为整型时可表示的最大值。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static readonly MAX_VALUE: int = 2147483647--><!--Device-Int-public static readonly MAX_VALUE: int = 2147483647-End-->

**系统能力：** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static readonly MIN_VALUE: int = -2147483648
```

该类型作为整型时可表示的最小值。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Int-public static readonly MIN_VALUE: int = -2147483648--><!--Device-Int-public static readonly MIN_VALUE: int = -2147483648-End-->

**系统能力：** SystemCapability.Utils.Lang

