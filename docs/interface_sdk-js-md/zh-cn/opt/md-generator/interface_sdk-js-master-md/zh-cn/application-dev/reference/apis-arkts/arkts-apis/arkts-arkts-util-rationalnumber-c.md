# RationalNumber

提供比较有理数、获取分子和分母的 API。例如，可以使用 **toString()** API 将有理数转换为字符串。

**起始版本：** 8

**废弃版本：** -1

<!--Device-util-class RationalNumber--><!--Device-util-class RationalNumber-End-->

**系统能力：** SystemCapability.Utils.Lang

## compare

```TypeScript
compare(another: RationalNumber): number
```

将当前的 RationalNumber 对象与给定对象进行比较。

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RationalNumber-compare(another: RationalNumber): number--><!--Device-RationalNumber-compare(another: RationalNumber): number-End-->

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

<!--Device-RationalNumber-compareTo(another: RationalNumber): number--><!--Device-RationalNumber-compareTo(another: RationalNumber): number-End-->

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

**替代接口：** [parseRationalNumber](#parseRationalNumber)

<!--Device-RationalNumber-constructor(numerator: number, denominator: number)--><!--Device-RationalNumber-constructor(numerator: number, denominator: number)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| numerator | number | 是 |
| denominator | number | 是 |

## 示例

```TypeScript
let rationalNumber = new util.RationalNumber(1,2);
```

## constructor

```TypeScript
constructor()
```

用于创建 **RationalNumber** 对象的构造函数。

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RationalNumber-constructor()--><!--Device-RationalNumber-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## 示例

```TypeScript
let rationalNumber = new util.RationalNumber();
```

## createRationalFromString

```TypeScript
static createRationalFromString(rationalString: string): RationalNumber
```

根据给定的字符串创建一个 **RationalNumber** 对象。 > **NOTE：**> > **rationalString** 参数必须为字符串。如果传入小数字符串，该函数不会被拦截，但会显示错误信息 > "createRationalFromString: The type of Parameter must be integer string"。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RationalNumber-static createRationalFromString(rationalString: string): RationalNumber--><!--Device-RationalNumber-static createRationalFromString(rationalString: string): RationalNumber-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rationalString | string | 是 |

**返回值：**

| 类型 |
| --- |
| [RationalNumber](arkts-arkts-util-rationalnumber-c.md) |

## 示例

```TypeScript
let rational = util.RationalNumber.createRationalFromString("3/4");
```

## equals

```TypeScript
equals(obj: Object): boolean
```

判断此 **RationalNumber** 对象与给定对象是否相等。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RationalNumber-equals(obj: Object): boolean--><!--Device-RationalNumber-equals(obj: Object): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
let rationalNumber = new util.RationalNumber(1,2);
let rational = util.RationalNumber.createRationalFromString("3/4");
let result = rationalNumber.equals(rational);
console.info("result = " + result);
// 输出结果：result = false
```

API 9及以上建议使用以下写法：

```TypeScript
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let rational = util.RationalNumber.createRationalFromString("3/4");
let result = rationalNumber.equals(rational);
console.info("result = " + result);
// 输出结果：result = false
```

## getCommonDivisor

```TypeScript
static getCommonDivisor(number1: number, number2: number): number
```

获取两个指定整数的最大公约数。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getCommonFactor](#getCommonFactor)

<!--Device-RationalNumber-static getCommonDivisor(number1: number, number2: number): number--><!--Device-RationalNumber-static getCommonDivisor(number1: number, number2: number): number-End-->

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

获取两个指定整数的最大公约数。 > **NOTE：**> > **number1** 和 **number2** 参数必须为整数。如果传入小数，该函数不会被拦截，但会显示错误信息 > "getCommonFactor: The type of Parameter must be integer"。

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RationalNumber-static getCommonFactor(number1: number, number2: number): number--><!--Device-RationalNumber-static getCommonFactor(number1: number, number2: number): number-End-->

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

## 示例

```TypeScript
let result = util.RationalNumber.getCommonFactor(4,6);
console.info("result = " + result);
// 输出结果：result = 2
```

## getDenominator

```TypeScript
getDenominator(): number
```

获取此 **RationalNumber** 对象的分母。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RationalNumber-getDenominator(): number--><!--Device-RationalNumber-getDenominator(): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.getDenominator();
console.info("result = " + result);
// 输出结果：result = 2
```

API 9及以上建议使用以下写法：

```TypeScript
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2)
let result = rationalNumber.getDenominator();
console.info("result = " + result);
// 输出结果：result = 2
```

## getNumerator

```TypeScript
getNumerator(): number
```

获取此 **RationalNumber** 对象的分子。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RationalNumber-getNumerator(): number--><!--Device-RationalNumber-getNumerator(): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.getNumerator();
console.info("result = " + result);
// 输出结果：result = 1
```

API 9及以上建议使用以下写法：

```TypeScript
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.getNumerator();
console.info("result = " + result);
// 输出结果：result = 1
```

## isFinite

```TypeScript
isFinite(): boolean
```

判断此 **RationalNumber** 对象表示的是否为有限值。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RationalNumber-isFinite(): boolean--><!--Device-RationalNumber-isFinite(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.isFinite();
console.info("result = " + result);
// 输出结果：result = true
```

API 9及以上建议使用以下写法：

```TypeScript
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.isFinite();
console.info("result = " + result);
// 输出结果：result = true
```

## isNaN

```TypeScript
isNaN(): boolean
```

判断此 **RationalNumber** 对象是否为非数字（NaN）。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RationalNumber-isNaN(): boolean--><!--Device-RationalNumber-isNaN(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.isNaN();
console.info("result = " + result);
// 输出结果：result = false
```

API 9及以上建议使用以下写法：

```TypeScript
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.isNaN();
console.info("result = " + result);
// 输出结果：result = false
```

## isZero

```TypeScript
isZero(): boolean
```

判断此 **RationalNumber** 对象的值是否为 **0**。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RationalNumber-isZero(): boolean--><!--Device-RationalNumber-isZero(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.isZero();
console.info("result = " + result);
// 输出结果：result = false
```

API 9及以上建议使用以下写法：

```TypeScript
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.isZero();
console.info("result = " + result);
// 输出结果：result = false
```

## parseRationalNumber

```TypeScript
static parseRationalNumber(numerator: number, denominator: number): RationalNumber
```

根据给定的分子和分母创建一个 **RationalNumber** 实例。 > **NOTE：**> > **numerator** 和 **denominator** 参数必须为整数。如果传入小数，该函数不会被拦截，但会显示错误信息 > "parseRationalNumber: The type of Parameter must be integer"。

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RationalNumber-static parseRationalNumber(numerator: number, denominator: number): RationalNumber--><!--Device-RationalNumber-static parseRationalNumber(numerator: number, denominator: number): RationalNumber-End-->

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

## 示例

```TypeScript
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
```

## toString

```TypeScript
toString(): string
```

获取此 **RationalNumber** 对象的字符串表示形式。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RationalNumber-toString(): string--><!--Device-RationalNumber-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## 示例

```TypeScript
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.toString();
console.info("result = " + result);
// 输出结果：result = 1/2
```

API 9及以上建议使用以下写法：

```TypeScript
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.toString();
console.info("result = " + result);
// 输出结果：result = 1/2
```

## valueOf

```TypeScript
valueOf(): number
```

获取此 **RationalNumber** 对象的整数或浮点数值。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RationalNumber-valueOf(): number--><!--Device-RationalNumber-valueOf(): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.valueOf();
console.info("result = " + result);
// 输出结果：result = 0.5
```

API 9及以上建议使用以下写法：

```TypeScript
let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.valueOf();
console.info("result = " + result);
// 输出结果：result = 0.5
```
