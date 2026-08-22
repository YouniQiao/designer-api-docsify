# Float

表示装箱后的float值及其相关操作。

**继承/实现关系：** Float extends [Floating](arkts-arkts-numeric-floating-c.md) implements Comparable<Float>

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export class Float--><!--Device-unnamed-export class Float-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## add

```TypeScript
public add(other: Float): Float
```

与传入实例做浮点加法运算。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public add(other: Float): Float--><!--Device-Float-public add(other: Float): Float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | 加法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Float](arkts-arkts-float-c.md) | 加法运算的结果。 |

## bitCastFromInt

```TypeScript
public static bitCastFromInt(bits: int): float
```

将位表示转换为对应的IEEE-754浮点表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static bitCastFromInt(bits: int): float--><!--Device-Float-public static bitCastFromInt(bits: int): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bits | int | 是 | 待转换的位表示。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | 转换后的值。 |

## bitCastToInt

```TypeScript
public static bitCastToInt(val: float): int
```

将IEEE-754浮点表示转换为对应的位表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static bitCastToInt(val: float): int--><!--Device-Float-public static bitCastToInt(val: float): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | float | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 位表示。 |

## compare

```TypeScript
public static compare(lhs: float, rhs: float): boolean
```

比较两个float值的差异是否不超过DELTA。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static compare(lhs: float, rhs: float): boolean--><!--Device-Float-public static compare(lhs: float, rhs: float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lhs | float | 是 | 参与比较的左侧float值。 |
| rhs | float | 是 | 参与比较的右侧float值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果在DELTA精度范围内相等则返回true，否则返回false。 |

## compareTo

```TypeScript
public compareTo(other: Float): int
```

将当前实例与另一个Float对象进行比较。当前实例小于 当前实例小于传入对象时结果小于0，相等时为0， 否则大于0。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public compareTo(other: Float): int--><!--Device-Float-public compareTo(other: Float): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | 用于比较的Float对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 比较结果，取值为-1、0或1。 |

## constructor

```TypeScript
public constructor()
```

构造初始值为0的新Float实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public constructor()--><!--Device-Float-public constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(value: float)
```

使用指定的初始值构造新的Float实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public constructor(value: float)--><!--Device-Float-public constructor(value: float)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | float | 是 | 初始值。 |

## constructor

```TypeScript
public constructor(value: double)
```

使用指定的初始值（double类型字面量）构造新的Float实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public constructor(value: double)--><!--Device-Float-public constructor(value: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 初始值。 |

## div

```TypeScript
public div(other: Float): Float
```

与传入实例做浮点除法运算。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public div(other: Float): Float--><!--Device-Float-public div(other: Float): Float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | 除法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Float](arkts-arkts-float-c.md) | 除法运算的结果。 |

## equals

```TypeScript
public equals(other: Any): boolean
```

判断当前实例与传入对象是否相等。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public equals(other: Any): boolean--><!--Device-Float-public equals(other: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Any | 是 | 待比较的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果相等则返回true，否则返回false。 |

## isFinite

```TypeScript
public static isFinite(v: float): boolean
```

检查float值是否为有限浮点数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static isFinite(v: float): boolean--><!--Device-Float-public static isFinite(v: float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | float | 是 | 待检测的float值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果参数为有限值则返回true，否则返回false。 |

## isFinite

```TypeScript
public isFinite(): boolean
```

检查底层的float值是否为有限浮点数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public isFinite(): boolean--><!--Device-Float-public isFinite(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的float值为有限值则返回true，否则返回false。 |

## isGreaterEqualThan

```TypeScript
public isGreaterEqualThan(other: Float): boolean
```

判断当前实例的值是否大于或等于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public isGreaterEqualThan(other: Float): boolean--><!--Device-Float-public isGreaterEqualThan(other: Float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值大于或等于传入值则返回true，否则返回false。 |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Float): boolean
```

判断当前实例的值是否大于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public isGreaterThan(other: Float): boolean--><!--Device-Float-public isGreaterThan(other: Float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值大于传入值则返回true，否则返回false。 |

## isInteger

```TypeScript
public static isInteger(v: float): boolean
```

检查float值是否接近整数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static isInteger(v: float): boolean--><!--Device-Float-public static isInteger(v: float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | float | 是 | 待检测的float值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果参数接近整数则返回true，否则返回false。 |

## isInteger

```TypeScript
public isInteger(): boolean
```

检查底层的float值是否接近整数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public isInteger(): boolean--><!--Device-Float-public isInteger(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的float值接近整数则返回true，否则返回false。 |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Float): boolean
```

判断当前实例的值是否小于或等于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public isLessEqualThan(other: Float): boolean--><!--Device-Float-public isLessEqualThan(other: Float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值小于或等于传入值则返回true，否则返回false。 |

## isLessThan

```TypeScript
public isLessThan(other: Float): boolean
```

判断当前实例的值是否小于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public isLessThan(other: Float): boolean--><!--Device-Float-public isLessThan(other: Float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值小于传入值则返回true，否则返回false。 |

## isNaN

```TypeScript
public static isNaN(v: float): boolean
```

检查float值是否为NaN。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static isNaN(v: float): boolean--><!--Device-Float-public static isNaN(v: float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | float | 是 | 待检测的float值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果参数为NaN则返回true，否则返回false。 |

## isNaN

```TypeScript
public isNaN(): boolean
```

检查底层的float值是否为NaN。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public isNaN(): boolean--><!--Device-Float-public isNaN(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的float值为NaN则返回true，否则返回false。 |

## isSafeInteger

```TypeScript
public static isSafeInteger(v: float): boolean
```

检查float值是否为安全整数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static isSafeInteger(v: float): boolean--><!--Device-Float-public static isSafeInteger(v: float): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | float | 是 | 待检测的float值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果参数为安全整数则返回true，否则返回false。 |

## isSafeInteger

```TypeScript
public isSafeInteger(): boolean
```

检查底层的float值是否为安全整数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public isSafeInteger(): boolean--><!--Device-Float-public isSafeInteger(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的float值为安全整数则返回true，否则返回false。 |

## mul

```TypeScript
public mul(other: Float): Float
```

与传入实例做浮点乘法运算。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public mul(other: Float): Float--><!--Device-Float-public mul(other: Float): Float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | 乘法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Float](arkts-arkts-float-c.md) | 乘法运算的结果。 |

## sub

```TypeScript
public sub(other: Float): Float
```

与传入实例做浮点减法运算。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public sub(other: Float): Float--><!--Device-Float-public sub(other: Float): Float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Float](arkts-arkts-float-c.md) | 是 | 减法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Float](arkts-arkts-float-c.md) | 减法运算的结果。 |

## toByte

```TypeScript
public toByte(): byte
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public toByte(): byte--><!--Device-Float-public toByte(): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | byte类型的值。 |

## toByte

```TypeScript
public static toByte(value: float): byte
```

以byte值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static toByte(value: float): byte--><!--Device-Float-public static toByte(value: float): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | float | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | 转换后的值。 |

## toDouble

```TypeScript
public toDouble(): double
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public toDouble(): double--><!--Device-Float-public toDouble(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | double类型的值。 |

## toDouble

```TypeScript
public static toDouble(value: float): double
```

以double值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static toDouble(value: float): double--><!--Device-Float-public static toDouble(value: float): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | float | 是 | 待转换的值。 |

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

<!--Device-Float-public toFloat(): float--><!--Device-Float-public toFloat(): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | float类型的值。 |

## toFloat

```TypeScript
public static toFloat(value: float): float
```

以float值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static toFloat(value: float): float--><!--Device-Float-public static toFloat(value: float): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | float | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | 转换后的值。 |

## toInt

```TypeScript
public toInt(): int
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public toInt(): int--><!--Device-Float-public toInt(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | int类型的值。 |

## toInt

```TypeScript
public static toInt(value: float): int
```

以int值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static toInt(value: float): int--><!--Device-Float-public static toInt(value: float): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | float | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 转换后的值。 |

## toLocaleString

```TypeScript
public toLocaleString(): string
```

将当前对象转换为符合区域设置的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public toLocaleString(): string--><!--Device-Float-public toLocaleString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

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

<!--Device-Float-public toLong(): long--><!--Device-Float-public toLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | long类型的值。 |

## toLong

```TypeScript
public static toLong(value: float): long
```

以long值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static toLong(value: float): long--><!--Device-Float-public static toLong(value: float): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | float | 是 | 待转换的值。 |

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

<!--Device-Float-public toShort(): short--><!--Device-Float-public toShort(): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | short类型的值。 |

## toShort

```TypeScript
public static toShort(value: float): short
```

以short值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static toShort(value: float): short--><!--Device-Float-public static toShort(value: float): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | float | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | 转换后的值。 |

## toString

```TypeScript
public static toString(f: float, r: int): string
```

按基数r返回float值的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static toString(f: float, r: int): string--><!--Device-Float-public static toString(f: float, r: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| f | float | 是 | float值。 |
| r | int | 是 | 使用的基数。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 字符串表示。 |

## toString

```TypeScript
public static toString(f: float): string
```

以10为基数返回float值的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static toString(f: float): string--><!--Device-Float-public static toString(f: float): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| f | float | 是 | float值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 字符串表示。 |

## toString

```TypeScript
public toString(r: int): string
```

使用指定基数将当前对象转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public toString(r: int): string--><!--Device-Float-public toString(r: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| r | int | 是 | 使用的基数。 <br>取值约束：应为整数。 |

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

<!--Device-Float-public toString(): string--><!--Device-Float-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## BIT_SIZE

```TypeScript
public static BIT_SIZE: byte = 32
```

该类型占用的位数。

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static BIT_SIZE: byte = 32--><!--Device-Float-public static BIT_SIZE: byte = 32-End-->

**系统能力：** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static BYTE_SIZE: byte = 4
```

该类型占用的字节数。

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static BYTE_SIZE: byte = 4--><!--Device-Float-public static BYTE_SIZE: byte = 4-End-->

**系统能力：** SystemCapability.Utils.Lang

## DELTA

```TypeScript
public static DELTA: float = Float.bitCastFromInt(0x34000000)
```

两个float值之间可能的最小差值。

**类型：** float

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static DELTA: float = Float.bitCastFromInt(0x34000000)--><!--Device-Float-public static DELTA: float = Float.bitCastFromInt(0x34000000)-End-->

**系统能力：** SystemCapability.Utils.Lang

## EPSILON

```TypeScript
public static EPSILON: float = Float.DELTA
```

两个float值之间可能的最小差值。

**类型：** float

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static EPSILON: float = Float.DELTA--><!--Device-Float-public static EPSILON: float = Float.DELTA-End-->

**系统能力：** SystemCapability.Utils.Lang

## f

```TypeScript
f
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-Float-f--><!--Device-Float-f-End-->

## MAX_SAFE_INTEGER

```TypeScript
public static MAX_SAFE_INTEGER: float = 16777215
```

可用float精确表示而不丢失精度的最大整数值。

**类型：** float

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static MAX_SAFE_INTEGER: float = 16777215--><!--Device-Float-public static MAX_SAFE_INTEGER: float = 16777215-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static MAX_VALUE: float = 3.40282346638528860e+38
```

该类型作为float时可表示的最大值。

**类型：** float

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static MAX_VALUE: float = 3.40282346638528860e+38--><!--Device-Float-public static MAX_VALUE: float = 3.40282346638528860e+38-End-->

**系统能力：** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static MIN_VALUE: float = 1.4e-45
```

该类型作为float时可表示的最小值。

**类型：** float

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static MIN_VALUE: float = 1.4e-45--><!--Device-Float-public static MIN_VALUE: float = 1.4e-45-End-->

**系统能力：** SystemCapability.Utils.Lang

## NaN

```TypeScript
public static NaN: float = Double.toFloat(0.0 / 0.0)
```

表示IEEE-754规范中的NaN值。

**类型：** float

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static NaN: float = Double.toFloat(0.0 / 0.0)--><!--Device-Float-public static NaN: float = Double.toFloat(0.0 / 0.0)-End-->

**系统能力：** SystemCapability.Utils.Lang

## NEGATIVE_INFINITY

```TypeScript
public static NEGATIVE_INFINITY: float = Double.toFloat(-1.0 / 0.0)
```

表示IEEE-754规范中的-Infinity值。

**类型：** float

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static NEGATIVE_INFINITY: float = Double.toFloat(-1.0 / 0.0)--><!--Device-Float-public static NEGATIVE_INFINITY: float = Double.toFloat(-1.0 / 0.0)-End-->

**系统能力：** SystemCapability.Utils.Lang

## POSITIVE_INFINITY

```TypeScript
public static POSITIVE_INFINITY: float = Double.toFloat(1.0 / 0.0)
```

表示IEEE-754规范中的+Infinity值。

**类型：** float

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static POSITIVE_INFINITY: float = Double.toFloat(1.0 / 0.0)--><!--Device-Float-public static POSITIVE_INFINITY: float = Double.toFloat(1.0 / 0.0)-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRECISION

```TypeScript
public static PRECISION: byte = 24
```

该浮点类型中有效精度位的数量。

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Float-public static PRECISION: byte = 24--><!--Device-Float-public static PRECISION: byte = 24-End-->

**系统能力：** SystemCapability.Utils.Lang

