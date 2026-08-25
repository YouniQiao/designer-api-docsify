# BigInt

与JS BigInt API兼容的类。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

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

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## $_invoke

```TypeScript
static $_invoke(value: long): BigInt
```

根据现有的Long数值创建新的BigInt实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## $_invoke

```TypeScript
static $_invoke(value: double): BigInt
```

根据number实例创建新的BigInt实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## $_invoke

```TypeScript
static $_invoke(value: string): BigInt
```

根据字符串创建新的BigInt实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## $_invoke

```TypeScript
static $_invoke(value: boolean): BigInt
```

根据boolean值创建新的BigInt实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## $_invoke

```TypeScript
static $_invoke(value: bigint | double | string | boolean): BigInt
```

根据bigint/double/string/boolean联合类型创建新的BigInt实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | bigint \| double \| string \| boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## asIntN

```TypeScript
public static asIntN(bits: long, num: BigInt): BigInt
```

将BigInt按指定位数截断为有符号整数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [bits](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-zlib-deflatependingoutputinfo-i.md) | long | 是 |
| num | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## asUintN

```TypeScript
public static asUintN(bits: long, num: BigInt): BigInt
```

将BigInt按指定位数截断为无符号整数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [bits](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-zlib-deflatependingoutputinfo-i.md) | long | 是 |
| num | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## constructor

```TypeScript
constructor()
```

创建值为0的新`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(d: byte)
```

根据byte值创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | byte | 是 |

## constructor

```TypeScript
constructor(d: short)
```

根据short值创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | short | 是 |

## constructor

```TypeScript
constructor(d: int)
```

根据int值创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | int | 是 |

## constructor

```TypeScript
constructor(d: long)
```

根据long值创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | long | 是 |

## constructor

```TypeScript
constructor(d: double)
```

根据double值创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | double | 是 |

## constructor

```TypeScript
constructor(d: string)
```

根据字符串值创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | string | 是 |

## constructor

```TypeScript
constructor(d: boolean)
```

根据boolean值创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | boolean | 是 |

## constructor

```TypeScript
constructor(d: BigInt)
```

通过复制另一个BigInt创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | [BigInt](arkts-arkts-bigint-c.md) | 是 |

## constructor

```TypeScript
constructor(v: FixedArray<int>, sign: int)
```

根据内部组成部分创建新的`BigInt`实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| v | FixedArray & lt;int & gt; | 是 |
| sign | int | 是 |

## doubleValue

```TypeScript
public doubleValue(): double
```

以double形式返回该对象的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| double |

## equals

```TypeScript
public equals(to: BigInt): boolean
```

判断当前BigInt是否与另一个BigInt相等。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| to | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## equals

```TypeScript
equals(other: Any): boolean
```

判断当前BigInt是否与另一个值相等。

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

## fromULong

```TypeScript
public static fromULong(val: long): BigInt
```

根据无符号的long值创建BigInt。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| val | long | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## getLong

```TypeScript
public getLong(): long
```

以long形式返回该对象的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| long |

## getULong

```TypeScript
public getULong(): long
```

返回截断为无符号long后的当前值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| long |

## negate

```TypeScript
public negate(): BigInt
```

返回该BigInt取负后的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## negative

```TypeScript
public negative(): boolean
```

返回该BigInt是否为负数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## operatorAdd

```TypeScript
public operatorAdd(other: BigInt): BigInt
```

将另一个BigInt与当前BigInt相加。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## operatorBitwiseAnd

```TypeScript
public operatorBitwiseAnd(other: BigInt): BigInt
```

与另一个BigInt执行按位与运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## operatorBitwiseNot

```TypeScript
public operatorBitwiseNot(): BigInt
```

对该BigInt执行按位取反运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## operatorBitwiseOr

```TypeScript
public operatorBitwiseOr(other: BigInt): BigInt
```

与另一个BigInt执行按位或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## operatorBitwiseXor

```TypeScript
public operatorBitwiseXor(other: BigInt): BigInt
```

与另一个BigInt执行按位异或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## operatorDecrement

```TypeScript
public operatorDecrement(): BigInt
```

将该BigInt的值减1。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## operatorDivide

```TypeScript
public operatorDivide(other: BigInt): BigInt
```

将当前BigInt除以另一个BigInt。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## operatorGreaterThan

```TypeScript
public operatorGreaterThan(other: BigInt): boolean
```

判断当前BigInt是否大于另一个BigInt。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## operatorGreaterThanEqual

```TypeScript
public operatorGreaterThanEqual(other: BigInt): boolean
```

判断当前BigInt是否大于或等于另一个BigInt。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## operatorIncrement

```TypeScript
public operatorIncrement(): BigInt
```

将该BigInt的值加1。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## operatorLeftShift

```TypeScript
public operatorLeftShift(other: BigInt): BigInt
```

将该BigInt左移指定的位数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## operatorLessThan

```TypeScript
public operatorLessThan(other: BigInt): boolean
```

判断当前BigInt是否小于另一个BigInt。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## operatorLessThanEqual

```TypeScript
public operatorLessThanEqual(other: BigInt): boolean
```

判断当前BigInt是否小于或等于另一个BigInt。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## operatorModule

```TypeScript
public operatorModule(other: BigInt): BigInt
```

计算当前BigInt除以另一个BigInt的余数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## operatorMultiply

```TypeScript
public operatorMultiply(other: BigInt): BigInt
```

将当前BigInt与另一个BigInt相乘。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## operatorRightShift

```TypeScript
public operatorRightShift(other: BigInt): BigInt
```

将该BigInt右移指定的位数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## operatorSubtract

```TypeScript
public operatorSubtract(other: BigInt): BigInt
```

从当前BigInt中减去另一个BigInt。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## positive

```TypeScript
public positive(): boolean
```

返回该BigInt是否为正数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## pow

```TypeScript
public pow(exponent: BigInt): BigInt
```

返回base的exponent次幂。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| exponent | [BigInt](arkts-arkts-bigint-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BigInt](arkts-arkts-bigint-c.md) |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: BigIntToLocaleStringOptions): string
```

使用当前或指定的区域设置将number值转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | Intl.LocalesArgument | 否 |
| options | [BigIntToLocaleStringOptions](arkts-arkts-bigint-biginttolocalestringoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

返回表示数组元素的字符串。数组元素通过各自的toLocaleString 方法转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | Intl.LocalesArgument | 否 |
| options | object | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## toString

```TypeScript
public toString(): string
```

以10为基数将BigInt转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## toString

```TypeScript
public toString(radix: int): string
```

返回该BigInt对象的字符串表示。

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
