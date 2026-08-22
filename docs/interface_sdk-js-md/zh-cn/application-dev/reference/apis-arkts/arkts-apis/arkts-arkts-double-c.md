# Double

表示装箱后的double值及其相关操作。

**继承/实现关系：** Double extends [Floating](arkts-arkts-numeric-floating-c.md) implements Comparable<Double>

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

<!--Device-unnamed-export class Double--><!--Device-unnamed-export class Double-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(): Double
```

创建新的Double实例。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static $_invoke(): Double--><!--Device-Double-static $_invoke(): Double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Double](arkts-arkts-double-c.md) | 新的Double实例。 |

## $_invoke

```TypeScript
static $_invoke(value: string | Double | BigInt | undefined | null): Double
```

创建新的Double实例。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static $_invoke(value: string | Double | BigInt | undefined | null): Double--><!--Device-Double-static $_invoke(value: string | Double | BigInt | undefined | null): Double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string \| [Double](arkts-arkts-double-c.md) \| [BigInt](arkts-arkts-bigint-c.md) \| undefined \| null | 是 | 待转换为number的值。 可以是string、number或BigInt（可选）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Double](arkts-arkts-double-c.md) | 新的Double实例。 |

## add

```TypeScript
public add(other: Double): Double
```

将当前实例与传入实例做浮点加法运算，并以新实例返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public add(other: Double): Double--><!--Device-Double-public add(other: Double): Double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | 加法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Double](arkts-arkts-double-c.md) | 加法运算的结果。 |

## bitCastFromLong

```TypeScript
public static bitCastFromLong(bits: long): double
```

将位表示转换为对应的IEEE-754浮点表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static bitCastFromLong(bits: long): double--><!--Device-Double-public static bitCastFromLong(bits: long): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bits | long | 是 | 待转换的位表示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 转换后的值。 |

## bitCastToLong

```TypeScript
public static bitCastToLong(val: double): long
```

将IEEE-754浮点表示转换为对应的位表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static bitCastToLong(val: double): long--><!--Device-Double-public static bitCastToLong(val: double): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | double | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 位表示。 |

## compare

```TypeScript
public static compare(lhs: double, rhs: double): boolean
```

compare(double, double)检查两个double值的差异是否不超过Double.DELTA。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static compare(lhs: double, rhs: double): boolean--><!--Device-Double-public static compare(lhs: double, rhs: double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lhs | double | 是 | 参与比较的左侧double值。 |
| rhs | double | 是 | 参与比较的右侧double值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果lhs与rhs在Double.DELTA精度范围内相等则返回true，否则返回false。 |

## compareTo

```TypeScript
public compareTo(other: Double): int
```

将当前实例与另一个Double对象进行比较。 当前实例小于传入对象时结果小于0， 相等时为0， 否则大于0。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public compareTo(other: Double): int--><!--Device-Double-public compareTo(other: Double): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | 用于比较的Double对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 当前值大于传入值时返回0，否则返回-1。 |

## constructor

```TypeScript
constructor()
```

构造初始值为0的新Double实例。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-constructor()--><!--Device-Double-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(value: double)
```

使用指定的初始值构造新的Double实例。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-constructor(value: double)--><!--Device-Double-constructor(value: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 初始值。 |

## constructor

```TypeScript
constructor(value: BigInt)
```

根据BigInt构造新的Double实例。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-constructor(value: BigInt)--><!--Device-Double-constructor(value: BigInt)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BigInt](arkts-arkts-bigint-c.md) | 是 |  |

## constructor

```TypeScript
constructor(value: string)
```

根据字符串构造新的Double实例。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-constructor(value: string)--><!--Device-Double-constructor(value: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 可能包含number值的字符串。 |

## div

```TypeScript
public div(other: Double): Double
```

将当前实例与传入实例做浮点除法运算，并以新实例返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public div(other: Double): Double--><!--Device-Double-public div(other: Double): Double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | 除法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Double](arkts-arkts-double-c.md) | 除法运算的结果。 |

## equals

```TypeScript
equals(other: Any): boolean
```

判断当前实例与传入对象是否相等， 传入对象按Double处理。如果传入对象的类型与当前类型不一致，则返回false。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-equals(other: Any): boolean--><!--Device-Double-equals(other: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Any | 是 | 待比较的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果传入对象与当前实例的值相同则返回true，否则返回false。 如果传入对象的类型与当前类型不一致，则返回false。 |

## isFinite

```TypeScript
static isFinite(v: double): boolean
```

isFinite(double)检查double值是否为浮点数值（既非NaN也非无穷大）。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static isFinite(v: double): boolean--><!--Device-Double-static isFinite(v: double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | double | 是 | 待检测的double值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果参数为浮点数值则返回true，否则返回false。 |

## isFinite

```TypeScript
isFinite(): boolean
```

isFinite()检查底层的double值是否为浮点数值（既非NaN也非无穷大）。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-isFinite(): boolean--><!--Device-Double-isFinite(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的double值为浮点数值则返回true，否则返回false。 |

## isGreaterEqualThan

```TypeScript
public isGreaterEqualThan(other: Double): boolean
```

判断当前实例的值是否大于或等于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public isGreaterEqualThan(other: Double): boolean--><!--Device-Double-public isGreaterEqualThan(other: Double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值大于或等于传入值则返回true，否则返回false。 |

## isGreaterThan

```TypeScript
public isGreaterThan(other: Double): boolean
```

判断当前实例的值是否大于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public isGreaterThan(other: Double): boolean--><!--Device-Double-public isGreaterThan(other: Double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值大于传入值则返回true，否则返回false。 |

## isInteger

```TypeScript
public static isInteger(v: double): boolean
```

检查double值是否接近整数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static isInteger(v: double): boolean--><!--Device-Double-public static isInteger(v: double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | double | 是 | 待检测的double值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果参数接近整数则返回true，否则返回false。 |

## isInteger

```TypeScript
public isInteger(): boolean
```

检查底层的double值是否接近整数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public isInteger(): boolean--><!--Device-Double-public isInteger(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的double值接近整数则返回true，否则返回false。 |

## isLessEqualThan

```TypeScript
public isLessEqualThan(other: Double): boolean
```

判断当前实例的值是否小于或等于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public isLessEqualThan(other: Double): boolean--><!--Device-Double-public isLessEqualThan(other: Double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值小于或等于传入值则返回true，否则返回false。 |

## isLessThan

```TypeScript
public isLessThan(other: Double): boolean
```

判断当前实例的值是否小于传入实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public isLessThan(other: Double): boolean--><!--Device-Double-public isLessThan(other: Double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | 比较运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值小于传入值则返回true，否则返回false。 |

## isNaN

```TypeScript
static isNaN(v: double): boolean
```

isNaN(double)检查double值是否为NaN（非数字）。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static isNaN(v: double): boolean--><!--Device-Double-static isNaN(v: double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | double | 是 | 待检测的double值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果参数为NaN则返回true，否则返回false。 |

## isNaN

```TypeScript
isNaN(): boolean
```

isNaN()检查底层的double值是否为NaN（非数字）。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-isNaN(): boolean--><!--Device-Double-isNaN(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的double值为NaN则返回true，否则返回false。 |

## isSafeInteger

```TypeScript
public static isSafeInteger(v: double): boolean
```

检查double值是否为安全整数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static isSafeInteger(v: double): boolean--><!--Device-Double-public static isSafeInteger(v: double): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | double | 是 | 待检测的double值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果参数为整数且小于MAX_SAFE_INTEGER则返回true，否则返回false。 |

## isSafeInteger

```TypeScript
public isSafeInteger(): boolean
```

检查double值是否为安全整数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public isSafeInteger(): boolean--><!--Device-Double-public isSafeInteger(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果底层的double值为安全整数则返回true，否则返回false。 |

## mul

```TypeScript
public mul(other: Double): Double
```

将当前实例与传入实例做浮点乘法运算，并以新实例返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public mul(other: Double): Double--><!--Device-Double-public mul(other: Double): Double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | 乘法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Double](arkts-arkts-double-c.md) | 乘法运算的结果。 |

## parseFloat

```TypeScript
static parseFloat(s: string): double
```

parseFloat(String)将std.core.String转换为double值。 参数为'+Infinity'、'Infinity'或'-Infinity'时，分别返回`inf`或`-inf`。 参数为'+0'或'-0'时，分别返回0或-0。 参数带有前导零时会被忽略：'0001.5'返回1.5，'-0001.5'返回-1.5。 参数以'.'开头时，隐含前导零：'.5'返回0.5，'-.5'返回-0.5。 参数解析成功时，忽略末尾的非数字字符：'-.6ffg'返回-0.6。 如果参数无法解析为number值，则返回NaN。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static parseFloat(s: string): double--><!--Device-Double-static parseFloat(s: string): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | 待转换的字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 转换结果。 |

## parseInt

```TypeScript
static parseInt(s: string): double
```

parseInt(String)以10为基数从String中解析出整数。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static parseInt(s: string): double--><!--Device-Double-static parseInt(s: string): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | 待转换的字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 解析结果。 |

## parseInt

```TypeScript
static parseInt(s: string, r: int): double
```

parseInt(String, int)按指定基数从String中解析出整数。 参数为('10', 1)或('10', 37)时，抛出ArgumentOutOfRangeError。 参数为('10', 2)时，返回2。 参数为('10', 10)或('10', 0)时，返回10。 参数为('ff', 16)时，返回255。 以此类推。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static parseInt(s: string, r: int): double--><!--Device-Double-static parseInt(s: string, r: int): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | 待转换的字符串。 |
| r | int | 是 | 转换使用的基数，取值范围为[2, 36]，传入0时按10处理。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 解析结果。 |

## parseInt

```TypeScript
static parseInt(s: string, r: double): double
```

parseInt(String, double)按指定基数从String中解析出整数。 参数为('10', 1)或('10', 37)时，抛出ArgumentOutOfRangeError。 参数为('10', 2)时，返回2。 参数为('10', 10)或('10', 0)时，返回10。 参数为('ff', 16)时，返回255。 以此类推。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static parseInt(s: string, r: double): double--><!--Device-Double-static parseInt(s: string, r: double): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | 待转换的字符串。 |
| r | double | 是 | 转换使用的基数，取值范围为[2, 36]，传入0时按10处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 解析结果。 |

## sub

```TypeScript
public sub(other: Double): Double
```

将当前实例与传入实例做浮点减法运算，并以新实例返回结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public sub(other: Double): Double--><!--Device-Double-public sub(other: Double): Double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Double](arkts-arkts-double-c.md) | 是 | 减法运算的右操作数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Double](arkts-arkts-double-c.md) | 减法运算的结果。 |

## toByte

```TypeScript
public toByte(): byte
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toByte(): byte--><!--Device-Double-public toByte(): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | 当前值转换得到的byte值。 |

## toByte

```TypeScript
public static toByte(value: double): byte
```

以byte值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static toByte(value: double): byte--><!--Device-Double-public static toByte(value: double): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte |  |

## toDouble

```TypeScript
toDouble(): double
```

返回当前实例的值。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-toDouble(): double--><!--Device-Double-toDouble(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 当前值转换得到的double值。 |

## toDouble

```TypeScript
static toDouble(value: double): double
```

以double值的形式返回该基本类型值。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-static toDouble(value: double): double--><!--Device-Double-static toDouble(value: double): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double |  |

## toExponential

```TypeScript
public toExponential(): string
```

toExponential()以指数表示法返回底层double值对应的std.core.string。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toExponential(): string--><!--Device-Double-public toExponential(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toExponential

```TypeScript
public toExponential(d?: double): string
```

toExponential()以指数表示法返回底层double值对应的std.core.String。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toExponential(d?: double): string--><!--Device-Double-public toExponential(d?: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toExponentialWithNoDigit

```TypeScript
public toExponentialWithNoDigit(): string
```

toExponential(double)以指数表示法返回底层double值对应的std.core.string。 d = new Double(0.25)时，d.toExponential(2)返回'2.50e-1'。 d = new Double(0.25)时，d.toExponential(2.5)返回'2.50e-1'。 d = new Double(0.25)时，d.toExponential(1)返回'2.5e-1'。 d = new Double(12345.01)时，d.toExponential(10)返回'1.2345010000e+4'。 d = new Double(NaN)时，d.toExponential(10)返回'NaN'。 d = new Double(Double.POSITIVE_INFINITY)时，d.toExponential(10)返回'Infinity'， 负无穷时返回'-Infinity'。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toExponentialWithNoDigit(): string--><!--Device-Double-public toExponentialWithNoDigit(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toFixed

```TypeScript
public toFixed(): string
```

toFixed(double)以定点表示法返回底层double值对应的std.core.string。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toFixed(): string--><!--Device-Double-public toFixed(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## toFixed

```TypeScript
public toFixed(d?: double): string
```

toFixed(double)以定点表示法返回底层double值对应的std.core.string。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toFixed(d?: double): string--><!--Device-Double-public toFixed(d?: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## toFixedImpl

```TypeScript
public toFixedImpl(d: double): string
```

toFixed(double)以定点表示法返回底层double值对应的std.core.string。 d = new Double(0.1)时，d.toFixed(0)返回'0'。 d = new Double(0.7)时，d.toFixed(0)返回'1'。 d = new Double(0.12345)时，d.toFixed(1)返回'0.1'。 d = new Double(0.12345)时，d.toFixed(3)返回'0.123'。 d = new Double(Double.POSITIVE_INFINITY)时，d.toFixed(3)返回'Infinity'。 d = new Double(Double.NaN)时，d.toFixed(3)返回'NaN'。 d = new Double(0.25)时，d.toFixed(200)抛出ArgumentOutOfRangeError。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toFixedImpl(d: double): string--><!--Device-Double-public toFixedImpl(d: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 是 | 小数位数（取整数部分），取值范围必须为[0, 100]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toFloat

```TypeScript
public toFloat(): float
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toFloat(): float--><!--Device-Double-public toFloat(): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | 当前值转换得到的float值。 |

## toFloat

```TypeScript
public static toFloat(value: double): float
```

以float值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static toFloat(value: double): float--><!--Device-Double-public static toFloat(value: double): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float |  |

## toInt

```TypeScript
public toInt(): int
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toInt(): int--><!--Device-Double-public toInt(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 当前值转换得到的int值。 |

## toInt

```TypeScript
public static toInt(value: double): int
```

以int值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static toInt(value: double): int--><!--Device-Double-public static toInt(value: double): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int |  |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string
```

将当前对象转换为符合区域设置的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string--><!--Device-Double-public toLocaleString(locales?: Intl.LocalesArgument, options?: Intl.NumberFormatOptions): string-End-->

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

<!--Device-Double-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Double-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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

<!--Device-Double-public toLong(): long--><!--Device-Double-public toLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 当前值转换得到的long值。 |

## toLong

```TypeScript
public static toLong(value: double): long
```

以long值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static toLong(value: double): long--><!--Device-Double-public static toLong(value: double): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long |  |

## toPrecision

```TypeScript
public toPrecision(d: double): string
```

toPrecision(double)按指定精度返回底层double值对应的std.core.string。 d = new Double(0.25)时，d.toPrecision(4)返回'0.2500'。 d = new Double(1.01)时，d.toPrecision(4.7)返回'1.010'。 d = new Double(0.25)时，d.toPrecision(0)抛出ArgumentOutOfRangeError。 d = new Double(12345.123455)时，d.toPrecision(10)返回'12345.12346'。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toPrecision(d: double): string--><!--Device-Double-public toPrecision(d: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 是 | 精度（四舍五入取整），取值范围必须为[1, 100]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toPrecision

```TypeScript
public toPrecision(): string
```

toPrecision()以指数表示法返回底层double值对应的std.core.string。 按规范，不带参数调用toPrecision时其行为等同于toString。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toPrecision(): string--><!--Device-Double-public toPrecision(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toShort

```TypeScript
public toShort(): short
```

返回当前实例的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toShort(): short--><!--Device-Double-public toShort(): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | 当前值转换得到的short值。 |

## toShort

```TypeScript
public static toShort(value: double): short
```

以short值的形式返回该基本类型值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static toShort(value: double): short--><!--Device-Double-public static toShort(value: double): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short |  |

## toString

```TypeScript
public static toString(d: double, r: int): string
```

toString(d: double, r: int): string —— 按基数r返回d的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static toString(d: double, r: int): string--><!--Device-Double-public static toString(d: double, r: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 是 |  |
| r | int | 是 | <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 字符串形式的值。 |

## toString

```TypeScript
public static toString(d: double): string
```

将指定的double精度浮点值转换为字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static toString(d: double): string--><!--Device-Double-public static toString(d: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 是 | 字符串形式的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## toString

```TypeScript
public toString(r: int): string
```

将指定的double精度浮点值转换为字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toString(r: int): string--><!--Device-Double-public toString(r: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| r | int | 是 | <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 字符串形式的值。 |

## toString

```TypeScript
public toString(): string
```

将当前对象转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public toString(): string--><!--Device-Double-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 字符串形式的值。 |

## BIT_SIZE

```TypeScript
public static readonly BIT_SIZE: byte = 64
```

该类型占用的位数。

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly BIT_SIZE: byte = 64--><!--Device-Double-public static readonly BIT_SIZE: byte = 64-End-->

**系统能力：** SystemCapability.Utils.Lang

## BYTE_SIZE

```TypeScript
public static readonly BYTE_SIZE: byte = 8
```

该类型占用的字节数。

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly BYTE_SIZE: byte = 8--><!--Device-Double-public static readonly BYTE_SIZE: byte = 8-End-->

**系统能力：** SystemCapability.Utils.Lang

## DELTA

```TypeScript
public static readonly DELTA: double = Double.bitCastFromLong(0x3cb0000000000000)
```

两个double值之间可能的最小差值。 对于double（IEEE-754 binary64），其值为2^(-52)，位表示为0x3cb0000000000000。

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly DELTA: double = Double.bitCastFromLong(0x3cb0000000000000)--><!--Device-Double-public static readonly DELTA: double = Double.bitCastFromLong(0x3cb0000000000000)-End-->

**系统能力：** SystemCapability.Utils.Lang

## EPSILON

```TypeScript
public static readonly EPSILON: double = Double.DELTA
```

两个double值之间可能的最小差值。

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly EPSILON: double = Double.DELTA--><!--Device-Double-public static readonly EPSILON: double = Double.DELTA-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_SAFE_INTEGER

```TypeScript
public static readonly MAX_SAFE_INTEGER: double = 9007199254740991
```

可用double精确表示而不丢失精度的最大整数值。

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly MAX_SAFE_INTEGER: double = 9007199254740991--><!--Device-Double-public static readonly MAX_SAFE_INTEGER: double = 9007199254740991-End-->

**系统能力：** SystemCapability.Utils.Lang

## MAX_VALUE

```TypeScript
public static readonly MAX_VALUE: double = 1.7976931348623157e+308
```

该类型作为double时可表示的最大值。

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly MAX_VALUE: double = 1.7976931348623157e+308--><!--Device-Double-public static readonly MAX_VALUE: double = 1.7976931348623157e+308-End-->

**系统能力：** SystemCapability.Utils.Lang

## MIN_SAFE_INTEGER

```TypeScript
public static readonly MIN_SAFE_INTEGER: double = -9007199254740991
```

可用double精确表示而不丢失精度的最小整数值。

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly MIN_SAFE_INTEGER: double = -9007199254740991--><!--Device-Double-public static readonly MIN_SAFE_INTEGER: double = -9007199254740991-End-->

**系统能力：** SystemCapability.Utils.Lang

## MIN_VALUE

```TypeScript
public static readonly MIN_VALUE: double = 4.9e-300 / 1.e+24
```

该类型作为double时可表示的最小值。 用于规避libc解析double字面量缺陷的变通实现。

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly MIN_VALUE: double = 4.9e-300 / 1.e+24--><!--Device-Double-public static readonly MIN_VALUE: double = 4.9e-300 / 1.e+24-End-->

**系统能力：** SystemCapability.Utils.Lang

## NEGATIVE_INFINITY

```TypeScript
public static readonly NEGATIVE_INFINITY: double = -1.0 / 0.0
```

表示IEEE-754规范中的-Infinity值。

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly NEGATIVE_INFINITY: double = -1.0 / 0.0--><!--Device-Double-public static readonly NEGATIVE_INFINITY: double = -1.0 / 0.0-End-->

**系统能力：** SystemCapability.Utils.Lang

## NaN

```TypeScript
public static readonly NaN: double = 0.0 / 0.0
```

表示IEEE-754规范中的NaN值。

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly NaN: double = 0.0 / 0.0--><!--Device-Double-public static readonly NaN: double = 0.0 / 0.0-End-->

**系统能力：** SystemCapability.Utils.Lang

## POSITIVE_INFINITY

```TypeScript
public static readonly POSITIVE_INFINITY: double = 1.0 / 0.0
```

表示IEEE-754规范中的+Infinity值。

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly POSITIVE_INFINITY: double = 1.0 / 0.0--><!--Device-Double-public static readonly POSITIVE_INFINITY: double = 1.0 / 0.0-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRECISION

```TypeScript
public static readonly PRECISION: byte = 53
```

该浮点类型中有效精度位的数量。

**类型：** byte

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Double-public static readonly PRECISION: byte = 53--><!--Device-Double-public static readonly PRECISION: byte = 53-End-->

**系统能力：** SystemCapability.Utils.Lang

