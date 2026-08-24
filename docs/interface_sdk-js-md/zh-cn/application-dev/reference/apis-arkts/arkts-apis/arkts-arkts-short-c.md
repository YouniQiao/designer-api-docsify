# Short

表示装箱后的short值及其相关操作。

**继承/实现关系：** Short extends [Integral](arkts-arkts-numeric-integral-c.md) implements Comparable<Short>

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export class Short--><!--Device-unnamed-export class Short-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## add

```TypeScript
public add(other: Short): Short
```

将当前实例与传入实例做整型加法运算，并以新实例返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public add(other: Short): Short--><!--Device-Short-public add(other: Short): Short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Short | 是 | 加法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Short | 加法运算的结果。 |

## compareTo

```TypeScript
public compareTo(other: Short): int
```

将当前实例与另一个Short对象进行比较。当前实例小于传入对象时 结果小于0，相等时为0，否则大于0。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public compareTo(other: Short): int--><!--Device-Short-public compareTo(other: Short): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Short | 是 | 用于比较的Short对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 比较结果：当前实例小于传入对象时为-1，相等时为0， 大于时为1。 |

## constructor

```TypeScript
public constructor()
```

构造初始值为0的新Short实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public constructor()--><!--Device-Short-public constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(value: short)
```

使用指定的初始值构造新的Short实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public constructor(value: short)--><!--Device-Short-public constructor(value: short)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | 初始值。 |

## div

```TypeScript
public div(other: Short): Short
```

将当前实例与传入实例做整型除法运算，并以新实例返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public div(other: Short): Short--><!--Device-Short-public div(other: Short): Short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Short | 是 | 除法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Short | 除法运算的结果。 |

## equals

```TypeScript
public equals(other: Any): boolean
```

判断当前实例与按Short处理的传入对象是否相等。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public equals(other: Any): boolean--><!--Device-Short-public equals(other: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Any | 是 | 待比较的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果传入对象与当前实例的值相同则返回true，否则返回false。 |

## isGreaterEqualThan

```TypeScript
public isGreaterEqualThan(other: Short): boolean
```

判断当前实例的值是否大于或等于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public isGreaterEqualThan(other: Short): boolean--><!--Device-Short-public isGreaterEqualThan(other: Short): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Short | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值大于或等于传入值则返回true，否则返回false。 |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Short): boolean
```

判断当前实例的值是否大于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public isGreaterThan(other: Short): boolean--><!--Device-Short-public isGreaterThan(other: Short): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Short | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值大于传入值则返回true，否则返回false。 |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Short): boolean
```

判断当前实例的值是否小于或等于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public isLessEqualThan(other: Short): boolean--><!--Device-Short-public isLessEqualThan(other: Short): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Short | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值小于或等于传入值则返回true，否则返回false。 |

## isLessThan

```TypeScript
public isLessThan(other: Short): boolean
```

判断当前实例的值是否小于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public isLessThan(other: Short): boolean--><!--Device-Short-public isLessThan(other: Short): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Short | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值小于传入值则返回true，否则返回false。 |

## mul

```TypeScript
public mul(other: Short): Short
```

将当前实例与传入实例做整型乘法运算，并以新实例返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public mul(other: Short): Short--><!--Device-Short-public mul(other: Short): Short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Short | 是 | 乘法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Short | 乘法运算的结果。 |

## parseInt

```TypeScript
public static parseInt(s: string, r: int): short
```

按指定基数从字符串解析出整数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static parseInt(s: string, r: int): short--><!--Device-Short-public static parseInt(s: string, r: int): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | 待转换的字符串。 |
| r | int | 是 | 转换使用的基数，取值范围为[2, 36]，传入0时按10处理。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | 解析结果。 |

## sub

```TypeScript
public sub(other: Short): Short
```

将当前实例与传入实例做整型减法运算，并以新实例返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public sub(other: Short): Short--><!--Device-Short-public sub(other: Short): Short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Short | 是 | 减法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Short | 减法运算的结果。 |

## toByte

```TypeScript
public toByte(): byte
```

以byte形式返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public toByte(): byte--><!--Device-Short-public toByte(): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | byte类型的值。 |

## toByte

```TypeScript
public static toByte(value: short): byte
```

以byte值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static toByte(value: short): byte--><!--Device-Short-public static toByte(value: short): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | 转换后的值。 |

## toChar

```TypeScript
public toChar(): char
```

以char形式返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public toChar(): char--><!--Device-Short-public toChar(): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | char类型的值。 |

## toChar

```TypeScript
public static toChar(value: short): char
```

以char值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static toChar(value: short): char--><!--Device-Short-public static toChar(value: short): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | 转换后的值。 |

## toDouble

```TypeScript
public toDouble(): double
```

以double形式返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public toDouble(): double--><!--Device-Short-public toDouble(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | double类型的值。 |

## toDouble

```TypeScript
public static toDouble(value: short): double
```

以double值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static toDouble(value: short): double--><!--Device-Short-public static toDouble(value: short): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 转换后的值。 |

## toFloat

```TypeScript
public toFloat(): float
```

以float形式返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public toFloat(): float--><!--Device-Short-public toFloat(): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | float类型的值。 |

## toFloat

```TypeScript
public static toFloat(value: short): float
```

以float值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static toFloat(value: short): float--><!--Device-Short-public static toFloat(value: short): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | 转换后的值。 |

## toInt

```TypeScript
public toInt(): int
```

以int形式返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public toInt(): int--><!--Device-Short-public toInt(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | int类型的值。 |

## toInt

```TypeScript
public static toInt(value: short): int
```

以int值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static toInt(value: short): int--><!--Device-Short-public static toInt(value: short): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 转换后的值。 |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string
```

将当前对象转换为符合区域设置的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string--><!--Device-Short-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string-End-->

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

<!--Device-Short-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Short-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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

以long形式返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public toLong(): long--><!--Device-Short-public toLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | long类型的值。 |

## toLong

```TypeScript
public static toLong(value: short): long
```

以long值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static toLong(value: short): long--><!--Device-Short-public static toLong(value: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 转换后的值。 |

## toShort

```TypeScript
public toShort(): short
```

以short形式返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public toShort(): short--><!--Device-Short-public toShort(): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | short类型的值。 |

## toShort

```TypeScript
public static toShort(value: short): short
```

以short值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static toShort(value: short): short--><!--Device-Short-public static toShort(value: short): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | 转换后的值。 |

## toString

```TypeScript
public static toString(v: short): string
```

将基本类型值转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static toString(v: short): string--><!--Device-Short-public static toString(v: short): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | short | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toString

```TypeScript
public toString(): string
```

将当前对象转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public toString(): string--><!--Device-Short-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toString

```TypeScript
public toString(radix: int): string
```

使用指定基数将当前对象转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public toString(radix: int): string--><!--Device-Short-public toString(radix: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | int | 是 | 转换使用的基数。 <br>取值约束：应为整数。 |

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

<!--Device-Short-public toString(radix: double): string--><!--Device-Short-public toString(radix: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | double | 是 | 转换使用的基数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## BIT_SIZE

```TypeScript
public static BIT_SIZE: byte = 16
```

该类型占用的位数。

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static BIT_SIZE: byte = 16--><!--Device-Short-public static BIT_SIZE: byte = 16-End-->

**系统能力：** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static BYTE_SIZE: byte = 2
```

该类型占用的字节数。

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static BYTE_SIZE: byte = 2--><!--Device-Short-public static BYTE_SIZE: byte = 2-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static MAX_VALUE: short = 32767
```

该类型作为short时可表示的最大值。

**类型：** short

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static MAX_VALUE: short = 32767--><!--Device-Short-public static MAX_VALUE: short = 32767-End-->

**系统能力：** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static MIN_VALUE: short = -32768
```

该类型作为short时可表示的最小值。

**类型：** short

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Short-public static MIN_VALUE: short = -32768--><!--Device-Short-public static MIN_VALUE: short = -32768-End-->

**系统能力：** SystemCapability.Utils.Lang

