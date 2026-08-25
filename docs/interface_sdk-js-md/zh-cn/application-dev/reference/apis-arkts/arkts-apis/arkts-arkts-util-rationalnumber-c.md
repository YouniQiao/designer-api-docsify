# RationalNumber

提供比较有理数、获取分子和分母的 API。例如，可以使用 **toString()** API 将有理数转换为字符串。

**起始版本：** 8

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## compare

```TypeScript
compare(another: RationalNumber): number
```

将当前的 RationalNumber 对象与给定对象进行比较。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| another | [RationalNumber](arkts-arkts-util-rationalnumber-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## compareTo

```TypeScript
compareTo(another: RationalNumber): number
```

将当前的 RationalNumber 对象与给定对象进行比较。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** compare

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| another | [RationalNumber](arkts-arkts-util-rationalnumber-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## constructor

```TypeScript
constructor(numerator: number, denominator: number)
```

用于创建 **RationalNumber** 对象的构造函数。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [parseRationalNumber](#parserationalnumber)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| numerator | number | 是 |
| denominator | number | 是 |

## constructor

```TypeScript
constructor()
```

用于创建 **RationalNumber** 对象的构造函数。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## createRationalFromString

```TypeScript
static createRationalFromString(rationalString: string): RationalNumber
```

根据给定的字符串创建一个 **RationalNumber** 对象。

> **NOTE：**&gt;
> **rationalString** 参数必须为字符串。如果传入小数字符串，该函数不会被拦截，但会显示错误信息
> "createRationalFromString: The type of Parameter must be integer string"。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rationalString | string | 是 |

**返回值：**

| 类型 |
| --- |
| [RationalNumber](arkts-arkts-util-rationalnumber-c.md) |

## equals

```TypeScript
equals(obj: Object): boolean
```

判断此 **RationalNumber** 对象与给定对象是否相等。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## getCommonDivisor

```TypeScript
static getCommonDivisor(number1: number, number2: number): number
```

获取两个指定整数的最大公约数。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getCommonFactor](#getcommonfactor)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| number1 | number | 是 |
| number2 | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getCommonFactor

```TypeScript
static getCommonFactor(number1: number, number2: number): number
```

获取两个指定整数的最大公约数。

> **NOTE：**&gt;
> **number1** 和 **number2** 参数必须为整数。如果传入小数，该函数不会被拦截，但会显示错误信息
> "getCommonFactor: The type of Parameter must be integer"。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| number1 | number | 是 |
| number2 | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getDenominator

```TypeScript
getDenominator(): number
```

获取此 **RationalNumber** 对象的分母。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

## getNumerator

```TypeScript
getNumerator(): number
```

获取此 **RationalNumber** 对象的分子。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

## isFinite

```TypeScript
isFinite(): boolean
```

判断此 **RationalNumber** 对象表示的是否为有限值。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isNaN

```TypeScript
isNaN(): boolean
```

判断此 **RationalNumber** 对象是否为非数字（NaN）。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isZero

```TypeScript
isZero(): boolean
```

判断此 **RationalNumber** 对象的值是否为 **0**。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## parseRationalNumber

```TypeScript
static parseRationalNumber(numerator: number, denominator: number): RationalNumber
```

根据给定的分子和分母创建一个 **RationalNumber** 实例。

> **NOTE：**&gt;
> **numerator** 和 **denominator** 参数必须为整数。如果传入小数，该函数不会被拦截，但会显示错误信息
> "parseRationalNumber: The type of Parameter must be integer"。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| numerator | number | 是 |
| denominator | number | 是 |

**返回值：**

| 类型 |
| --- |
| [RationalNumber](arkts-arkts-util-rationalnumber-c.md) |

## toString

```TypeScript
toString(): string
```

获取此 **RationalNumber** 对象的字符串表示形式。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## valueOf

```TypeScript
valueOf(): number
```

获取此 **RationalNumber** 对象的整数或浮点数值。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |
