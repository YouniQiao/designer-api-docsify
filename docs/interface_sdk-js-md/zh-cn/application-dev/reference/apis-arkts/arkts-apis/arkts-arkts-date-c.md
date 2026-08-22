# Date

与JS Date API兼容的类。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

<!--Device-unnamed-export class Date--><!--Device-unnamed-export class Date-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## UTC

```TypeScript
public static UTC(d: Date): long
```

返回自纪元起经过的毫秒数， 纪元定义为UTC时间1970年1月1日零点。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public static UTC(d: Date): long--><!--Device-Date-public static UTC(d: Date): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | Date | 是 | 待转换为毫秒的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## UTC

```TypeScript
public static UTC(year: int): long
```

返回自纪元起经过的毫秒数， 纪元定义为UTC时间1970年1月1日零点。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public static UTC(year: int): long--><!--Device-Date-public static UTC(year: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| year | int | 是 | 待转换为毫秒的值。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## UTC

```TypeScript
public static UTC(year: int, month: int, day?: int, hours?: int, minutes?: int, seconds?: int, ms?: int): long
```

返回自纪元起经过的毫秒数， 纪元定义为UTC时间1970年1月1日零点。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public static UTC(year: int, month: int, day?: int, hours?: int, minutes?: int, seconds?: int, ms?: int): long--><!--Device-Date-public static UTC(year: int, month: int, day?: int, hours?: int, minutes?: int, seconds?: int, ms?: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| year | int | 是 | 待转换为毫秒的值。 <br>取值约束：可以为任意整数。 |
| month | int | 是 | 待转换为毫秒的值。 <br>取值约束：可以为任意整数。 |
| day | int | 否 | 待转换为毫秒的值。 <br>取值约束：可以为任意整数。 |
| hours | int | 否 | 待转换为毫秒的值。 <br>取值约束：可以为任意整数。 |
| minutes | int | 否 | 待转换为毫秒的值。 <br>取值约束：可以为任意整数。 |
| seconds | int | 否 | 待转换为毫秒的值。 <br>取值约束：可以为任意整数。 |
| ms | int | 否 | 待转换为毫秒的值。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## constructor

```TypeScript
constructor()
```

默认构造函数，使用当前时间初始化Date实例。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-constructor()--><!--Device-Date-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(value: long | string | Date)
```

`Date`构造函数。注意：`1921-01-01T00:00:00 GMT`之前的日期 转换为UTC毫秒的方式可能与TS不同。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-constructor(value: long | string | Date)--><!--Device-Date-constructor(value: long | string | Date)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long \| string \| Date | 是 | 表示日期的值，可以是毫秒时间戳（long）、 日期字符串（string），或已有的Date对象（Date）。 |

## constructor

```TypeScript
constructor(year: int, monthIndex: int, day?: int, hours?: int, minutes?: int, seconds?: int, ms?: int)
```

`Date`构造函数。注意：`1921-01-01T00:00:00 GMT`之前的日期 转换为UTC毫秒的方式可能与TS不同。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-constructor(year: int, monthIndex: int, day?: int, hours?: int, minutes?: int, seconds?: int, ms?: int)--><!--Device-Date-constructor(year: int, monthIndex: int, day?: int, hours?: int, minutes?: int, seconds?: int, ms?: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| year | int | 是 | 年。 <br>取值约束：可以为任意整数。 |
| monthIndex | int | 是 | 月。 <br>取值约束：可以为任意整数。 |
| day | int | 否 | 日。 <br>取值约束：可以为任意整数。 |
| hours | int | 否 | 小时。 <br>取值约束：可以为任意整数。 |
| minutes | int | 否 | 分钟。 <br>取值约束：可以为任意整数。 |
| seconds | int | 否 | 秒。 <br>取值约束：可以为任意整数。 |
| ms | int | 否 | 毫秒。 <br>取值约束：可以为任意整数。 |

## getDate

```TypeScript
public getDate(): int
```

`getDate()`方法按本地时间返回指定日期中月份的第几天。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getDate(): int--><!--Device-Date-public getDate(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 按本地时间计算的月份中的第几天（1到31）。 |

## getDay

```TypeScript
public getDay(): int
```

按本地时间返回指定日期是星期几， 其中0表示周日。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getDay(): int--><!--Device-Date-public getDay(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 星期几（0表示周日，1表示周一，……，6表示周六）。 |

## getFullYear

```TypeScript
public getFullYear(): int
```

按本地时间返回指定日期的年份。 对于1000年到9999年之间的日期，`getFullYear()`返回四位数， 例如1995。使用该方法可确保年份与2000年之后的年份保持一致。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getFullYear(): int--><!--Device-Date-public getFullYear(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 完整年份。 |

## getHours

```TypeScript
public getHours(): int
```

按本地时间返回指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getHours(): int--><!--Device-Date-public getHours(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 按本地时间计算的指定日期的小时数（0到23）。 |

## getLocalTimezoneOffset

```TypeScript
public static getLocalTimezoneOffset(ms: long): long
```

获取本地时间偏移量。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public static getLocalTimezoneOffset(ms: long): long--><!--Device-Date-public static getLocalTimezoneOffset(ms: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ms | long | 是 | 以毫秒表示的时间。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 本地时间偏移量。 |

## getMilliseconds

```TypeScript
public getMilliseconds(): int
```

按本地时间返回指定日期的毫秒数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getMilliseconds(): int--><!--Device-Date-public getMilliseconds(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 按本地时间计算的指定日期的毫秒数（0到999）。 |

## getMinutes

```TypeScript
public getMinutes(): int
```

按本地时间返回指定日期的分钟数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getMinutes(): int--><!--Device-Date-public getMinutes(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 0到59之间的整数。 表示按本地时间计算的给定日期的分钟数。 |

## getMonth

```TypeScript
public getMonth(): int
```

按本地时间返回指定日期的月份， 月份从0开始计数（0表示一年中的第一个月）。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getMonth(): int--><!--Device-Date-public getMonth(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 月份（0到11），其中0表示一月，11表示十二月。 |

## getSeconds

```TypeScript
public getSeconds(): int
```

按本地时间返回指定日期的秒数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getSeconds(): int--><!--Device-Date-public getSeconds(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 0到59之间的整数。 表示按本地时间计算的给定日期的秒数。 |

## getTime

```TypeScript
public getTime(): long
```

返回自纪元起经过的毫秒数， 纪元定义为UTC时间1970年1月1日零点。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getTime(): long--><!--Device-Date-public getTime(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## getTimezoneName

```TypeScript
public static getTimezoneName(ms: long): string
```

获取时区名称。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public static getTimezoneName(ms: long): string--><!--Device-Date-public static getTimezoneName(ms: long): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ms | long | 是 | 以毫秒表示的时间。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 时区名称。 |

## getTimezoneOffset

```TypeScript
public getTimezoneOffset(): long
```

返回同一日期分别在UTC时区与本地时区下 在UTC时区与本地时区下求值所得的差值，单位为分钟。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getTimezoneOffset(): long--><!--Device-Date-public getTimezoneOffset(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 以分钟表示的时区偏移量（早于UTC的时区为负值）。 |

## getUTCDate

```TypeScript
public getUTCDate(): int
```

按世界时返回指定日期中月份的第几天（1到31）。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getUTCDate(): int--><!--Device-Date-public getUTCDate(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 按世界时计算的月份中的第几天（1到31）。 |

## getUTCDay

```TypeScript
public getUTCDay(): int
```

按世界时返回指定日期是星期几，其中0表示周日。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getUTCDay(): int--><!--Device-Date-public getUTCDay(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 星期几（0表示周日，1表示周一，……，6表示周六）。 |

## getUTCFullYear

```TypeScript
public getUTCFullYear(): int
```

按世界时返回指定日期的年份。 对于1000年到9999年之间的日期，`getUTCFullYear()`返回四位数， 例如1995。使用该方法可确保年份与2000年之后的年份保持一致。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getUTCFullYear(): int--><!--Device-Date-public getUTCFullYear(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 按世界时计算的年份。 |

## getUTCHours

```TypeScript
public getUTCHours(): int
```

按世界时返回指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getUTCHours(): int--><!--Device-Date-public getUTCHours(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 按世界时计算的指定日期的小时数（0到23）。 |

## getUTCMilliseconds

```TypeScript
public getUTCMilliseconds(): int
```

按世界时返回时间对象值中的毫秒部分。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getUTCMilliseconds(): int--><!--Device-Date-public getUTCMilliseconds(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int |  |

## getUTCMinutes

```TypeScript
public getUTCMinutes(): int
```

按世界时返回指定日期的分钟数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getUTCMinutes(): int--><!--Device-Date-public getUTCMinutes(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 解析得到的日期值。 |

## getUTCMonth

```TypeScript
public getUTCMonth(): int
```

按世界时返回指定日期的月份。 月份从0开始计数（0表示一年中的第一个月）。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getUTCMonth(): int--><!--Device-Date-public getUTCMonth(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 解析得到的日期值。 |

## getUTCSeconds

```TypeScript
public getUTCSeconds(): int
```

按世界时返回指定日期的秒数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getUTCSeconds(): int--><!--Device-Date-public getUTCSeconds(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 按世界时计算的指定日期的秒数。 |

## getYear

```TypeScript
public getYear(): int
```

按本地时间返回指定日期的年份。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public getYear(): int--><!--Device-Date-public getYear(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 年份值。 |

## isDateValid

```TypeScript
public isDateValid(): boolean
```

检查所构造的日期是否合法。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public isDateValid(): boolean--><!--Device-Date-public isDateValid(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该日期合法则返回true，否则返回false。 |

## now

```TypeScript
static now(): long
```

静态方法`now()`返回自纪元起经过的毫秒数， 纪元定义为UTC时间1970年1月1日 零点。纪元定义为UTC时间1970年1月1日零点。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-static now(): long--><!--Device-Date-static now(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 以毫秒表示的当前时间。 |

## parse

```TypeScript
static parse(dateStr: string): long
```

解析日期的字符串表示， 返回自UTC时间1970年1月1日00:00:00起经过的毫秒数； 如果字符串无法识别，或在某些情况下包含非法的日期值 （例如2015-02-31），则抛出`RangeError`。

明确要求支持(YYYY-MM-DDTHH:mm:ss.sssZ)格式。 其他格式由实现决定，可能无法在所有浏览器（目标平台）上生效。 如果需要兼容多种格式，可借助相应的库。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-static parse(dateStr: string): long--><!--Device-Date-static parse(dateStr: string): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dateStr | string | 是 | 待解析的字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setDate

```TypeScript
public setDate(value: int): long
```

按本地时间修改给定Date实例中月份的第几天。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setDate(value: int): long--><!--Device-Date-public setDate(value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的日期（日）。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long |  |

## setFullYear

```TypeScript
public setFullYear(value: int): long
```

按本地时间设置指定日期的完整年份。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setFullYear(value: int): long--><!--Device-Date-public setFullYear(value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的年份。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setFullYear

```TypeScript
public setFullYear(value: int, month: int): long
```

按本地时间设置指定日期的完整年份。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setFullYear(value: int, month: int): long--><!--Device-Date-public setFullYear(value: int, month: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的年份。 <br>取值约束：可以为任意整数。 |
| month | int | 是 | 新的月份。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setFullYear

```TypeScript
public setFullYear(value: int, month: int, date: int): long
```

按本地时间设置指定日期的完整年份。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setFullYear(value: int, month: int, date: int): long--><!--Device-Date-public setFullYear(value: int, month: int, date: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的年份。 <br>取值约束：可以为任意整数。 |
| month | int | 是 | 新的月份。 <br>取值约束：可以为任意整数。 |
| date | int | 是 | 新的日期。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setHours

```TypeScript
public setHours(value: int): long
```

按本地时间设置指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setHours(value: int): long--><!--Device-Date-public setHours(value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的小时数。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setHours

```TypeScript
public setHours(value: int, min: int): long
```

按本地时间设置指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setHours(value: int, min: int): long--><!--Device-Date-public setHours(value: int, min: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的小时数。 <br>取值约束：可以为任意整数。 |
| min | int | 是 | 分钟。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setHours

```TypeScript
public setHours(value: int, min: int, sec: int): long
```

按本地时间设置指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setHours(value: int, min: int, sec: int): long--><!--Device-Date-public setHours(value: int, min: int, sec: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的小时数。 <br>取值约束：可以为任意整数。 |
| min | int | 是 | 分钟。 <br>取值约束：可以为任意整数。 |
| sec | int | 是 | 秒。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setHours

```TypeScript
public setHours(value: int, min: int, sec: int, ms: int): long
```

按本地时间设置指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setHours(value: int, min: int, sec: int, ms: int): long--><!--Device-Date-public setHours(value: int, min: int, sec: int, ms: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的小时数。 <br>取值约束：可以为任意整数。 |
| min | int | 是 | 分钟。 <br>取值约束：可以为任意整数。 |
| sec | int | 是 | 秒。 <br>取值约束：可以为任意整数。 |
| ms | int | 是 | 毫秒。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setMilliseconds

```TypeScript
public setMilliseconds(value: int): long
```

按本地时间设置指定日期的毫秒数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setMilliseconds(value: int): long--><!--Device-Date-public setMilliseconds(value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的毫秒数。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setMinutes

```TypeScript
public setMinutes(value: int): long
```

按本地时间设置指定日期的分钟数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setMinutes(value: int): long--><!--Device-Date-public setMinutes(value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的分钟数。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setMinutes

```TypeScript
public setMinutes(value: int, sec: int): long
```

按本地时间设置指定日期的分钟数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setMinutes(value: int, sec: int): long--><!--Device-Date-public setMinutes(value: int, sec: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的分钟数。 <br>取值约束：可以为任意整数。 |
| sec | int | 是 | 秒。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setMinutes

```TypeScript
public setMinutes(value: int, sec: int, ms: int): long
```

按本地时间设置指定日期的分钟数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setMinutes(value: int, sec: int, ms: int): long--><!--Device-Date-public setMinutes(value: int, sec: int, ms: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的分钟数。 <br>取值约束：可以为任意整数。 |
| sec | int | 是 | 秒。 <br>取值约束：可以为任意整数。 |
| ms | int | 是 | 毫秒。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setMonth

```TypeScript
public setMonth(month: int): long
```

按当前已设置的年份设置指定日期的月份。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setMonth(month: int): long--><!--Device-Date-public setMonth(month: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| month | int | 是 | 新的月份。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setMonth

```TypeScript
public setMonth(month: int, date: int): long
```

按当前已设置的年份设置指定日期的月份。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setMonth(month: int, date: int): long--><!--Device-Date-public setMonth(month: int, date: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| month | int | 是 | 新的月份。 <br>取值约束：可以为任意整数。 |
| date | int | 是 | 日期值。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setSeconds

```TypeScript
public setSeconds(value: int): long
```

按本地时间设置指定日期的秒数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setSeconds(value: int): long--><!--Device-Date-public setSeconds(value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的秒数。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setSeconds

```TypeScript
public setSeconds(value: int, ms: int): long
```

按本地时间设置指定日期的秒数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setSeconds(value: int, ms: int): long--><!--Device-Date-public setSeconds(value: int, ms: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的秒数。 <br>取值约束：可以为任意整数。 |
| ms | int | 是 | 毫秒。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setTime

```TypeScript
public setTime(value: long): long
```

设置自纪元起经过的毫秒数， 纪元定义为UTC时间1970年1月1日零点。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setTime(value: long): long--><!--Device-Date-public setTime(value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | 以毫秒表示的新时间。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 自纪元起经过的毫秒数。 |

## setTimezoneOffset

```TypeScript
public setTimezoneOffset(value: int): long
```

设置同一日期分别在UTC时区与本地时区下 在UTC时区与本地时区下求值所得的差值，单位为分钟。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setTimezoneOffset(value: int): long--><!--Device-Date-public setTimezoneOffset(value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 相对于UTC、以分钟表示的时区偏移量。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 以毫秒表示的新时间值。 |

## setUTCDate

```TypeScript
public setUTCDate(value: int): long
```

按UTC时间修改给定Date实例中月份的第几天。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCDate(value: int): long--><!--Device-Date-public setUTCDate(value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的日期（日）。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long |  |

## setUTCDay

```TypeScript
public setUTCDay(value: int): long
```

使用协调世界时（UTC）设置Date对象中月份的第几天。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCDay(value: int): long--><!--Device-Date-public setUTCDay(value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 按世界时计算的星期几。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 待设置的世界时日期（日）。 |

## setUTCFullYear

```TypeScript
public setUTCFullYear(value: int): long
```

按世界时设置指定日期的完整年份。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCFullYear(value: int): long--><!--Device-Date-public setUTCFullYear(value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的年份。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setUTCFullYear

```TypeScript
public setUTCFullYear(value: int, month: int): long
```

按世界时设置指定日期的完整年份。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCFullYear(value: int, month: int): long--><!--Device-Date-public setUTCFullYear(value: int, month: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的年份。 <br>取值约束：可以为任意整数。 |
| month | int | 是 | 新的月份。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setUTCFullYear

```TypeScript
public setUTCFullYear(value: int, month: int, date: int): long
```

按世界时设置指定日期的完整年份。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCFullYear(value: int, month: int, date: int): long--><!--Device-Date-public setUTCFullYear(value: int, month: int, date: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的年份。 <br>取值约束：可以为任意整数。 |
| month | int | 是 | 新的月份。 <br>取值约束：可以为任意整数。 |
| date | int | 是 | 新的日期。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setUTCHours

```TypeScript
public setUTCHours(value: int): long
```

按世界时设置指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCHours(value: int): long--><!--Device-Date-public setUTCHours(value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的小时数。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setUTCHours

```TypeScript
public setUTCHours(value: int, min: int): long
```

按世界时设置指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCHours(value: int, min: int): long--><!--Device-Date-public setUTCHours(value: int, min: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的小时数。 <br>取值约束：可以为任意整数。 |
| min | int | 是 | 分钟。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setUTCHours

```TypeScript
public setUTCHours(value: int, min: int, sec: int): long
```

按世界时设置指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCHours(value: int, min: int, sec: int): long--><!--Device-Date-public setUTCHours(value: int, min: int, sec: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的小时数。 <br>取值约束：可以为任意整数。 |
| min | int | 是 | 分钟。 <br>取值约束：可以为任意整数。 |
| sec | int | 是 | 秒。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setUTCHours

```TypeScript
public setUTCHours(value: int, min: int, sec: int, ms: int): long
```

按世界时设置指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCHours(value: int, min: int, sec: int, ms: int): long--><!--Device-Date-public setUTCHours(value: int, min: int, sec: int, ms: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的小时数。 <br>取值约束：可以为任意整数。 |
| min | int | 是 | 分钟。 <br>取值约束：可以为任意整数。 |
| sec | int | 是 | 秒。 <br>取值约束：可以为任意整数。 |
| ms | int | 是 | 毫秒。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setUTCMilliseconds

```TypeScript
public setUTCMilliseconds(value: int): long
```

按世界时设置指定日期的毫秒数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCMilliseconds(value: int): long--><!--Device-Date-public setUTCMilliseconds(value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的毫秒数。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setUTCMinutes

```TypeScript
public setUTCMinutes(value: int): long
```

按世界时设置指定日期的分钟数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCMinutes(value: int): long--><!--Device-Date-public setUTCMinutes(value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的分钟数。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setUTCMinutes

```TypeScript
public setUTCMinutes(value: int, sec: int): long
```

按世界时设置指定日期的分钟数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCMinutes(value: int, sec: int): long--><!--Device-Date-public setUTCMinutes(value: int, sec: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的分钟数。 <br>取值约束：可以为任意整数。 |
| sec | int | 是 | 秒。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setUTCMinutes

```TypeScript
public setUTCMinutes(value: int, sec: int, ms: int): long
```

按世界时设置指定日期的分钟数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCMinutes(value: int, sec: int, ms: int): long--><!--Device-Date-public setUTCMinutes(value: int, sec: int, ms: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的分钟数。 <br>取值约束：可以为任意整数。 |
| sec | int | 是 | 秒。 <br>取值约束：可以为任意整数。 |
| ms | int | 是 | 毫秒。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setUTCMonth

```TypeScript
public setUTCMonth(month: int): long
```

按世界时设置指定日期的月份。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCMonth(month: int): long--><!--Device-Date-public setUTCMonth(month: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| month | int | 是 | 新的月份。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setUTCMonth

```TypeScript
public setUTCMonth(month: int, date: int): long
```

按世界时设置指定日期的月份。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCMonth(month: int, date: int): long--><!--Device-Date-public setUTCMonth(month: int, date: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| month | int | 是 | 新的月份。 <br>取值约束：可以为任意整数。 |
| date | int | 是 | 日期值。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 解析得到的日期值。 |

## setUTCSeconds

```TypeScript
public setUTCSeconds(value: int): long
```

按世界时设置指定日期的秒数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCSeconds(value: int): long--><!--Device-Date-public setUTCSeconds(value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的秒数。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long |  |

## setUTCSeconds

```TypeScript
public setUTCSeconds(value: int, ms: int): long
```

按世界时设置指定日期的秒数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setUTCSeconds(value: int, ms: int): long--><!--Device-Date-public setUTCSeconds(value: int, ms: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的秒数。 <br>取值约束：可以为任意整数。 |
| ms | int | 是 | 毫秒。 <br>取值约束：可以为任意整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long |  |

## setYear

```TypeScript
public setYear(value: int): void
```

按本地时间设置指定日期的完整年份。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public setYear(value: int): void--><!--Device-Date-public setYear(value: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 新的年份。 <br>取值约束：可以为任意整数。 |

## toDateString

```TypeScript
public toDateString(): string
```

以英文返回日期中的日期部分。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public toDateString(): string--><!--Device-Date-public toDateString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 日期字符串。 |

## toISOString

```TypeScript
public toISOString(): string
```

按世界时返回符合ISO 8601格式的字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public toISOString(): string--><!--Device-Date-public toISOString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 符合ISO 8601格式的字符串。 |

## toJSON

```TypeScript
public toJSON(): string | null
```

返回该日期的JSON表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public toJSON(): string | null--><!--Device-Date-public toJSON(): string | null-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string \| null | 对应的JSON字符串；如果日期非法，则返回null。 |

## toLocaleDateString

```TypeScript
public toLocaleDateString(locales?: Intl.LocalesArgument,
        options?: Intl.DateTimeFormatOptions): string
```

获取日期部分的本地化表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public toLocaleDateString(locales?: Intl.LocalesArgument,        options?: Intl.DateTimeFormatOptions): string--><!--Device-Date-public toLocaleDateString(locales?: Intl.LocalesArgument,        options?: Intl.DateTimeFormatOptions): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | 否 | 区域设置。 |
| options | Intl.DateTimeFormatOptions | 否 | 格式化选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 本地化的日期字符串。 |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

返回表示数组元素的字符串。数组元素通过各自的toLocaleString 方法转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Date-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

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

## toLocaleTimeString

```TypeScript
public toLocaleTimeString(): string
```

获取日期中时间部分的本地化表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public toLocaleTimeString(): string--><!--Device-Date-public toLocaleTimeString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 本地化的时间字符串。 |

## toLocaleTimeString

```TypeScript
public toLocaleTimeString(locales?: Intl.LocalesArgument,
        options?: Intl.DateTimeFormatOptions): string
```

获取日期中时间部分的本地化表示。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public toLocaleTimeString(locales?: Intl.LocalesArgument,        options?: Intl.DateTimeFormatOptions): string--><!--Device-Date-public toLocaleTimeString(locales?: Intl.LocalesArgument,        options?: Intl.DateTimeFormatOptions): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | 否 | 区域设置。 |
| options | Intl.DateTimeFormatOptions | 否 | 格式化选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 本地化的时间字符串。 |

## toString

```TypeScript
public toString(): string
```

返回表示该Date对象的字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public toString(): string--><!--Device-Date-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 字符串表示。 |

## toTimeString

```TypeScript
public toTimeString(): string
```

以英文返回日期中的时间部分。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public toTimeString(): string--><!--Device-Date-public toTimeString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 时间字符串。 |

## toUTCString

```TypeScript
public toUTCString(): string
```

返回以世界时表示该Date对象的字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public toUTCString(): string--><!--Device-Date-public toUTCString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 世界时的字符串表示。 |

## valueOf

```TypeScript
public valueOf(): long
```

`valueOf()`方法返回`Date`对象的原始值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Date-public valueOf(): long--><!--Device-Date-public valueOf(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | `Date`对象的原始值。 |

