# BigInt

与JS BigInt API兼容的类。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class BigInt--><!--Device-unnamed-export class BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(value: BigInt): BigInt
```

根据现有的BigInt数值创建新的BigInt实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-static $_invoke(value: BigInt): BigInt--><!--Device-BigInt-static $_invoke(value: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BigInt](arkts-arkts-bigint-c.md) | 是 | BigInt值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 根据现有的BigInt数值创建的新BigInt实例。 |

## $_invoke

```TypeScript
static $_invoke(value: long): BigInt
```

根据现有的Long数值创建新的BigInt实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-static $_invoke(value: long): BigInt--><!--Device-BigInt-static $_invoke(value: long): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | BigInt值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 根据现有的Long数值创建的新BigInt实例。 |

## $_invoke

```TypeScript
static $_invoke(value: double): BigInt
```

根据number实例创建新的BigInt实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-static $_invoke(value: double): BigInt--><!--Device-BigInt-static $_invoke(value: double): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | number值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 根据number实例创建的新BigInt实例。 |

## $_invoke

```TypeScript
static $_invoke(value: string): BigInt
```

根据字符串创建新的BigInt实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-static $_invoke(value: string): BigInt--><!--Device-BigInt-static $_invoke(value: string): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 字符串值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 根据字符串创建的新BigInt实例。 |

## $_invoke

```TypeScript
static $_invoke(value: boolean): BigInt
```

根据boolean值创建新的BigInt实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-static $_invoke(value: boolean): BigInt--><!--Device-BigInt-static $_invoke(value: boolean): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | boolean值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 根据boolean值创建的新BigInt实例。 |

## $_invoke

```TypeScript
static $_invoke(value: bigint | double | string | boolean): BigInt
```

根据bigint/double/string/boolean联合类型创建新的BigInt实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-static $_invoke(value: bigint | double | string | boolean): BigInt--><!--Device-BigInt-static $_invoke(value: bigint | double | string | boolean): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | bigint \| double \| string \| boolean | 是 | 源值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 根据bigint/double/string/boolean联合类型创建的新BigInt实例。 |

## asIntN

```TypeScript
public static asIntN(bits: long, num: BigInt): BigInt
```

将BigInt按指定位数截断为有符号整数。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public static asIntN(bits: long, num: BigInt): BigInt--><!--Device-BigInt-public static asIntN(bits: long, num: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bits | long | 是 | 有符号整数表示所使用的位数。 |
| num | [BigInt](arkts-arkts-bigint-c.md) | 是 | 待截断的BigInt值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 按指定位数截断为有符号整数后的BigInt值。 |

## asUintN

```TypeScript
public static asUintN(bits: long, num: BigInt): BigInt
```

将BigInt按指定位数截断为无符号整数。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public static asUintN(bits: long, num: BigInt): BigInt--><!--Device-BigInt-public static asUintN(bits: long, num: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bits | long | 是 | 无符号整数表示所使用的位数。 |
| num | [BigInt](arkts-arkts-bigint-c.md) | 是 | 待截断的BigInt值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 按指定位数截断为无符号整数后的BigInt值。 |

## constructor

```TypeScript
constructor()
```

创建值为0的新`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor()--><!--Device-BigInt-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(d: byte)
```

根据byte值创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(d: byte)--><!--Device-BigInt-constructor(d: byte)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | byte | 是 | 待转换的byte值。 |

## constructor

```TypeScript
constructor(d: short)
```

根据short值创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(d: short)--><!--Device-BigInt-constructor(d: short)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | short | 是 | 待转换的short值。 |

## constructor

```TypeScript
constructor(d: int)
```

根据int值创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(d: int)--><!--Device-BigInt-constructor(d: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | int | 是 | 待转换的int值。 <br>取值约束：应为整数。 |

## constructor

```TypeScript
constructor(d: long)
```

根据long值创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(d: long)--><!--Device-BigInt-constructor(d: long)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | long | 是 | 待转换的long值。 |

## constructor

```TypeScript
constructor(d: double)
```

根据double值创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(d: double)--><!--Device-BigInt-constructor(d: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 是 | 待转换为BigInt的double值，必须为整数。 |

## constructor

```TypeScript
constructor(d: string)
```

根据字符串值创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(d: string)--><!--Device-BigInt-constructor(d: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | string | 是 | 待转换为BigInt的字符串值。 |

## constructor

```TypeScript
constructor(d: boolean)
```

根据boolean值创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(d: boolean)--><!--Device-BigInt-constructor(d: boolean)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | boolean | 是 | boolean值，true对应1，false对应0。 |

## constructor

```TypeScript
constructor(d: BigInt)
```

通过复制另一个BigInt创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(d: BigInt)--><!--Device-BigInt-constructor(d: BigInt)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | [BigInt](arkts-arkts-bigint-c.md) | 是 | 待复制的BigInt对象。 |

## constructor

```TypeScript
constructor(v: FixedArray<int>, sign: int)
```

根据内部组成部分创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-constructor(v: FixedArray<int>, sign: int)--><!--Device-BigInt-constructor(v: FixedArray<int>, sign: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | FixedArray&lt;int&gt; | 是 | 数字位数组。 |
| sign | int | 是 | 数值的符号。 <br>取值约束：应为整数。 |

## doubleValue

```TypeScript
public doubleValue(): double
```

以double形式返回该对象的值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public doubleValue(): double--><!--Device-BigInt-public doubleValue(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | double值。 |

## equals

```TypeScript
public equals(to: BigInt): boolean
```

判断当前BigInt是否与另一个BigInt相等。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public equals(to: BigInt): boolean--><!--Device-BigInt-public equals(to: BigInt): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| to | [BigInt](arkts-arkts-bigint-c.md) | 是 | 用于比较的BigInt。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果相等则返回true，否则返回false。 |

## equals

```TypeScript
equals(other: Any): boolean
```

判断当前BigInt是否与另一个值相等。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-equals(other: Any): boolean--><!--Device-BigInt-equals(other: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Any | 是 | 用于比较的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该值是BigInt且与当前BigInt相等则返回true，否则返回false。 |

## fromULong

```TypeScript
public static fromULong(val: long): BigInt
```

根据无符号的long值创建BigInt。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public static fromULong(val: long): BigInt--><!--Device-BigInt-public static fromULong(val: long): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | long | 是 | 无符号的long值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 新的BigInt实例。 |

## getLong

```TypeScript
public getLong(): long
```

以long形式返回该对象的值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public getLong(): long--><!--Device-BigInt-public getLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | long值。 |

## getULong

```TypeScript
public getULong(): long
```

返回截断为无符号long后的当前值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public getULong(): long--><!--Device-BigInt-public getULong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 无符号的long值。 |

## negate

```TypeScript
public negate(): BigInt
```

返回该BigInt取负后的值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public negate(): BigInt--><!--Device-BigInt-public negate(): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 取负后的值。 |

## negative

```TypeScript
public negative(): boolean
```

返回该BigInt是否为负数。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public negative(): boolean--><!--Device-BigInt-public negative(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果为负数则返回true，否则返回false。 |

## operatorAdd

```TypeScript
public operatorAdd(other: BigInt): BigInt
```

将另一个BigInt与当前BigInt相加。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorAdd(other: BigInt): BigInt--><!--Device-BigInt-public operatorAdd(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | 相加的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 加法运算的结果。 |

## operatorBitwiseAnd

```TypeScript
public operatorBitwiseAnd(other: BigInt): BigInt
```

与另一个BigInt执行按位与运算。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorBitwiseAnd(other: BigInt): BigInt--><!--Device-BigInt-public operatorBitwiseAnd(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | 另一个BigInt。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 按位与运算的结果。 |

## operatorBitwiseNot

```TypeScript
public operatorBitwiseNot(): BigInt
```

对该BigInt执行按位取反运算。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorBitwiseNot(): BigInt--><!--Device-BigInt-public operatorBitwiseNot(): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 按位取反运算的结果。 |

## operatorBitwiseOr

```TypeScript
public operatorBitwiseOr(other: BigInt): BigInt
```

与另一个BigInt执行按位或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorBitwiseOr(other: BigInt): BigInt--><!--Device-BigInt-public operatorBitwiseOr(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | 另一个BigInt。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 按位或运算的结果。 |

## operatorBitwiseXor

```TypeScript
public operatorBitwiseXor(other: BigInt): BigInt
```

与另一个BigInt执行按位异或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorBitwiseXor(other: BigInt): BigInt--><!--Device-BigInt-public operatorBitwiseXor(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | 另一个BigInt。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 按位异或运算的结果。 |

## operatorDecrement

```TypeScript
public operatorDecrement(): BigInt
```

将该BigInt的值减1。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorDecrement(): BigInt--><!--Device-BigInt-public operatorDecrement(): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 自减后的值。 |

## operatorDivide

```TypeScript
public operatorDivide(other: BigInt): BigInt
```

将当前BigInt除以另一个BigInt。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorDivide(other: BigInt): BigInt--><!--Device-BigInt-public operatorDivide(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | 除数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 除法运算的商。 |

## operatorGreaterThan

```TypeScript
public operatorGreaterThan(other: BigInt): boolean
```

判断当前BigInt是否大于另一个BigInt。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorGreaterThan(other: BigInt): boolean--><!--Device-BigInt-public operatorGreaterThan(other: BigInt): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | 用于比较的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值大于传入值则返回true，否则返回false。 |

## operatorGreaterThanEqual

```TypeScript
public operatorGreaterThanEqual(other: BigInt): boolean
```

判断当前BigInt是否大于或等于另一个BigInt。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorGreaterThanEqual(other: BigInt): boolean--><!--Device-BigInt-public operatorGreaterThanEqual(other: BigInt): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | 用于比较的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值大于或等于传入值则返回true，否则返回false。 |

## operatorIncrement

```TypeScript
public operatorIncrement(): BigInt
```

将该BigInt的值加1。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorIncrement(): BigInt--><!--Device-BigInt-public operatorIncrement(): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 自增后的值。 |

## operatorLeftShift

```TypeScript
public operatorLeftShift(other: BigInt): BigInt
```

将该BigInt左移指定的位数。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorLeftShift(other: BigInt): BigInt--><!--Device-BigInt-public operatorLeftShift(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | 移位的位数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 移位后的BigInt。 |

## operatorLessThan

```TypeScript
public operatorLessThan(other: BigInt): boolean
```

判断当前BigInt是否小于另一个BigInt。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorLessThan(other: BigInt): boolean--><!--Device-BigInt-public operatorLessThan(other: BigInt): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | 用于比较的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值小于传入值则返回true，否则返回false。 |

## operatorLessThanEqual

```TypeScript
public operatorLessThanEqual(other: BigInt): boolean
```

判断当前BigInt是否小于或等于另一个BigInt。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorLessThanEqual(other: BigInt): boolean--><!--Device-BigInt-public operatorLessThanEqual(other: BigInt): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | 用于比较的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前值小于或等于传入值则返回true，否则返回false。 |

## operatorModule

```TypeScript
public operatorModule(other: BigInt): BigInt
```

计算当前BigInt除以另一个BigInt的余数。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorModule(other: BigInt): BigInt--><!--Device-BigInt-public operatorModule(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | 除数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 余数。 |

## operatorMultiply

```TypeScript
public operatorMultiply(other: BigInt): BigInt
```

将当前BigInt与另一个BigInt相乘。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorMultiply(other: BigInt): BigInt--><!--Device-BigInt-public operatorMultiply(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | 乘数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 乘法运算的结果。 |

## operatorRightShift

```TypeScript
public operatorRightShift(other: BigInt): BigInt
```

将该BigInt右移指定的位数。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorRightShift(other: BigInt): BigInt--><!--Device-BigInt-public operatorRightShift(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | 移位的位数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 移位后的BigInt。 |

## operatorSubtract

```TypeScript
public operatorSubtract(other: BigInt): BigInt
```

从当前BigInt中减去另一个BigInt。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public operatorSubtract(other: BigInt): BigInt--><!--Device-BigInt-public operatorSubtract(other: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 | 相减的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | 减法运算的结果。 |

## positive

```TypeScript
public positive(): boolean
```

返回该BigInt是否为正数。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public positive(): boolean--><!--Device-BigInt-public positive(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果为正数（含0）则返回true，否则返回false。 |

## pow

```TypeScript
public pow(exponent: BigInt): BigInt
```

返回base的exponent次幂。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public pow(exponent: BigInt): BigInt--><!--Device-BigInt-public pow(exponent: BigInt): BigInt-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exponent | [BigInt](arkts-arkts-bigint-c.md) | 是 | 指数值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BigInt](arkts-arkts-bigint-c.md) | base的exponent次幂的结果。 |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string
```

使用当前或指定的区域设置将number值转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string--><!--Device-BigInt-public toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | 否 | 包含BCP 47语言标签的字符串，或由此类 字符串组成的数组。 |
| options | [BigIntToLocaleStringOptions](arkts-arkts-bigint-biginttolocalestringoptions-i.md) | 否 | 包含Intl.NumberFormat选项的部分或 全部属性的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 按区域设置和选项格式化后表示该BigInt的字符串。 |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

返回表示数组元素的字符串。数组元素通过各自的toLocaleString 方法转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-BigInt-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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

## toString

```TypeScript
public toString(): string
```

以10为基数将BigInt转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public toString(): string--><!--Device-BigInt-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 以10为基数的BigInt字符串表示。 |

## toString

```TypeScript
public toString(radix: int): string
```

返回该BigInt对象的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BigInt-public toString(radix: int): string--><!--Device-BigInt-public toString(radix: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radix | int | 是 | 用于表示数值的基数，取值为2到36之间的 整数。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 表示指定BigInt对象的字符串。 |

