# Long

表示装箱后的long值及其相关操作。

**继承/实现关系：** Long extends [Integral](arkts-arkts-numeric-integral-c.md) implements Comparable<Long>

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class Long--><!--Device-unnamed-export class Long-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## add

```TypeScript
public add(other: Long): Long
```

将当前实例与传入实例做整型加法运算，并以新实例返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public add(other: Long): Long--><!--Device-Long-public add(other: Long): Long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | 加法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Long](arkts-arkts-long-c.md) | 加法运算的结果。 |

## compareTo

```TypeScript
public compareTo(other: Long): int
```

将当前实例与另一个Long对象进行比较。当前实例小于传入对象时 结果小于0，相等时为0，否则大于0。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public compareTo(other: Long): int--><!--Device-Long-public compareTo(other: Long): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | 用于比较的Long对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 比较结果：当前实例小于传入对象时为-1， 相等时为0，大于时为1。 |

## constructor

```TypeScript
constructor()
```

构造初始值为0的新Long实例。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-constructor()--><!--Device-Long-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(value: long)
```

使用指定的初始值构造新的Long实例。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-constructor(value: long)--><!--Device-Long-constructor(value: long)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | 初始值。 |

## div

```TypeScript
public div(other: Long): Long
```

将当前实例与传入实例做整型除法运算，并以新实例返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public div(other: Long): Long--><!--Device-Long-public div(other: Long): Long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | 除法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Long](arkts-arkts-long-c.md) | 除法运算的结果。 |

## equals

```TypeScript
public equals(other: Any): boolean
```

判断当前实例与按Long处理的传入对象是否相等。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public equals(other: Any): boolean--><!--Device-Long-public equals(other: Any): boolean-End-->

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
public isGreaterEqualThan(other: Long): boolean
```

判断当前实例的值是否大于或等于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public isGreaterEqualThan(other: Long): boolean--><!--Device-Long-public isGreaterEqualThan(other: Long): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值大于或等于传入值则返回true，否则返回false。 |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Long): boolean
```

判断当前实例的值是否大于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public isGreaterThan(other: Long): boolean--><!--Device-Long-public isGreaterThan(other: Long): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值大于传入值则返回true，否则返回false。 |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Long): boolean
```

判断当前实例的值是否小于或等于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public isLessEqualThan(other: Long): boolean--><!--Device-Long-public isLessEqualThan(other: Long): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值小于或等于传入值则返回true，否则返回false。 |

## isLessThan

```TypeScript
public isLessThan(other: Long): boolean
```

判断当前实例的值是否小于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public isLessThan(other: Long): boolean--><!--Device-Long-public isLessThan(other: Long): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值小于传入值则返回true，否则返回false。 |

## mul

```TypeScript
public mul(other: Long): Long
```

将当前实例与传入实例做整型乘法运算，并以新实例返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public mul(other: Long): Long--><!--Device-Long-public mul(other: Long): Long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | 乘法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Long](arkts-arkts-long-c.md) | 乘法运算的结果。 |

## parseInt

```TypeScript
public static parseInt(s: string, r: int): long
```

按指定基数从字符串解析出整数。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static parseInt(s: string, r: int): long--><!--Device-Long-public static parseInt(s: string, r: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | 待转换的字符串。 |
| r | int | 是 | 转换使用的基数，取值范围为[2, 36]，传入0时按10处理。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析结果。 |

## sub

```TypeScript
public sub(other: Long): Long
```

将当前实例与传入实例做整型减法运算，并以新实例返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public sub(other: Long): Long--><!--Device-Long-public sub(other: Long): Long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Long](arkts-arkts-long-c.md) | 是 | 减法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Long](arkts-arkts-long-c.md) | 减法运算的结果。 |

## toByte

```TypeScript
public toByte(): byte
```

以byte形式返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toByte(): byte--><!--Device-Long-public toByte(): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | byte类型的值。 |

## toByte

```TypeScript
public static toByte(value: long): byte
```

以byte值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static toByte(value: long): byte--><!--Device-Long-public static toByte(value: long): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | 待转换的值。 |

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

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toChar(): char--><!--Device-Long-public toChar(): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | char类型的值。 |

## toChar

```TypeScript
public static toChar(value: long): char
```

以char值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static toChar(value: long): char--><!--Device-Long-public static toChar(value: long): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | 待转换的值。 |

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

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toDouble(): double--><!--Device-Long-public toDouble(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | double类型的值。 |

## toDouble

```TypeScript
public static toDouble(value: long): double
```

以double值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static toDouble(value: long): double--><!--Device-Long-public static toDouble(value: long): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | 待转换的值。 |

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

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toFloat(): float--><!--Device-Long-public toFloat(): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | float类型的值。 |

## toFloat

```TypeScript
public static toFloat(value: long): float
```

以float值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static toFloat(value: long): float--><!--Device-Long-public static toFloat(value: long): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | 待转换的值。 |

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

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toInt(): int--><!--Device-Long-public toInt(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | int类型的值。 |

## toInt

```TypeScript
public static toInt(value: long): int
```

以int值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static toInt(value: long): int--><!--Device-Long-public static toInt(value: long): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | 待转换的值。 |

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

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string--><!--Device-Long-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string-End-->

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

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Long-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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
toLong(): long
```

返回当前实例的值。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-toLong(): long--><!--Device-Long-toLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | long类型的值。 |

## toLong

```TypeScript
static toLong(value: long): long
```

以long值的形式返回该基本类型值。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-static toLong(value: long): long--><!--Device-Long-static toLong(value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | 待转换的值。 |

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

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toShort(): short--><!--Device-Long-public toShort(): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | short类型的值。 |

## toShort

```TypeScript
public static toShort(value: long): short
```

以short值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static toShort(value: long): short--><!--Device-Long-public static toShort(value: long): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | 转换后的值。 |

## toString

```TypeScript
static toString(v: long): string
```

将基本类型值转换为字符串。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-static toString(v: long): string--><!--Device-Long-static toString(v: long): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | long | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toString

```TypeScript
toString(): string
```

将当前对象转换为字符串。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-toString(): string--><!--Device-Long-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) | 输入参数错误。 |

## toString

```TypeScript
public toString(radix: int): string
```

使用指定基数将当前对象转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toString(radix: int): string--><!--Device-Long-public toString(radix: int): string-End-->

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

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public toString(radix: double): string--><!--Device-Long-public toString(radix: double): string-End-->

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
public static BIT_SIZE: byte = 64
```

该类型占用的位数。

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static BIT_SIZE: byte = 64--><!--Device-Long-public static BIT_SIZE: byte = 64-End-->

**系统能力：** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static BYTE_SIZE: byte = 8
```

该类型占用的字节数。

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static BYTE_SIZE: byte = 8--><!--Device-Long-public static BYTE_SIZE: byte = 8-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static MAX_VALUE: long = 9223372036854775807
```

该类型作为long时可表示的最大值。

**类型：** long

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static MAX_VALUE: long = 9223372036854775807--><!--Device-Long-public static MAX_VALUE: long = 9223372036854775807-End-->

**系统能力：** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static MIN_VALUE: long = -9223372036854775808
```

该类型作为long时可表示的最小值。

**类型：** long

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Long-public static MIN_VALUE: long = -9223372036854775808--><!--Device-Long-public static MIN_VALUE: long = -9223372036854775808-End-->

**系统能力：** SystemCapability.Utils.Lang

