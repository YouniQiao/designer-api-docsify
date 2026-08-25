# Date

与JS Date API兼容的类。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor()
```

默认构造函数，使用当前时间初始化Date实例。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(value: long | string | Date)
```

`Date`构造函数。注意：`1921-01-01T00:00:00 GMT`之前的日期 转换为UTC毫秒的方式可能与TS不同。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | long \| string \| Date | 是 |

## constructor

```TypeScript
constructor(year: int, monthIndex: int, day?: int, hours?: int, minutes?: int, seconds?: int, ms?: int)
```

`Date`构造函数。注意：`1921-01-01T00:00:00 GMT`之前的日期 转换为UTC毫秒的方式可能与TS不同。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| year | int | 是 |
| monthIndex | int | 是 |
| day | int | 否 |
| hours | int | 否 |
| minutes | int | 否 |
| seconds | int | 否 |
| ms | int | 否 |

## getDate

```TypeScript
public getDate(): int
```

`getDate()`方法按本地时间返回指定日期中月份的第几天。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## getDay

```TypeScript
public getDay(): int
```

按本地时间返回指定日期是星期几， 其中0表示周日。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## getFullYear

```TypeScript
public getFullYear(): int
```

按本地时间返回指定日期的年份。 对于1000年到9999年之间的日期，`getFullYear()`返回四位数， 例如1995。使用该方法可确保年份与2000年之后的年份保持一致。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## getHours

```TypeScript
public getHours(): int
```

按本地时间返回指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## getLocalTimezoneOffset

```TypeScript
public static getLocalTimezoneOffset(ms: long): long
```

获取本地时间偏移量。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ms | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## getMilliseconds

```TypeScript
public getMilliseconds(): int
```

按本地时间返回指定日期的毫秒数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## getMinutes

```TypeScript
public getMinutes(): int
```

按本地时间返回指定日期的分钟数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## getMonth

```TypeScript
public getMonth(): int
```

按本地时间返回指定日期的月份， 月份从0开始计数（0表示一年中的第一个月）。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## getSeconds

```TypeScript
public getSeconds(): int
```

按本地时间返回指定日期的秒数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## getTime

```TypeScript
public getTime(): long
```

返回自纪元起经过的毫秒数， 纪元定义为UTC时间1970年1月1日零点。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| long |

## getTimezoneName

```TypeScript
public static getTimezoneName(ms: long): string
```

获取时区名称。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ms | long | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## getTimezoneOffset

```TypeScript
public getTimezoneOffset(): long
```

返回同一日期分别在UTC时区与本地时区下 在UTC时区与本地时区下求值所得的差值，单位为分钟。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| long |

## getUTCDate

```TypeScript
public getUTCDate(): int
```

按世界时返回指定日期中月份的第几天（1到31）。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## getUTCDay

```TypeScript
public getUTCDay(): int
```

按世界时返回指定日期是星期几，其中0表示周日。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## getUTCFullYear

```TypeScript
public getUTCFullYear(): int
```

按世界时返回指定日期的年份。 对于1000年到9999年之间的日期，`getUTCFullYear()`返回四位数， 例如1995。使用该方法可确保年份与2000年之后的年份保持一致。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## getUTCHours

```TypeScript
public getUTCHours(): int
```

按世界时返回指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## getUTCMilliseconds

```TypeScript
public getUTCMilliseconds(): int
```

按世界时返回时间对象值中的毫秒部分。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## getUTCMinutes

```TypeScript
public getUTCMinutes(): int
```

按世界时返回指定日期的分钟数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## getUTCMonth

```TypeScript
public getUTCMonth(): int
```

按世界时返回指定日期的月份。 月份从0开始计数（0表示一年中的第一个月）。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## getUTCSeconds

```TypeScript
public getUTCSeconds(): int
```

按世界时返回指定日期的秒数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## getYear

```TypeScript
public getYear(): int
```

按本地时间返回指定日期的年份。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## isDateValid

```TypeScript
public isDateValid(): boolean
```

检查所构造的日期是否合法。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## now

```TypeScript
static now(): long
```

静态方法`now()`返回自纪元起经过的毫秒数， 纪元定义为UTC时间1970年1月1日 零点。纪元定义为UTC时间1970年1月1日零点。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| long |

## parse

```TypeScript
static parse(dateStr: string): long
```

解析日期的字符串表示， 返回自UTC时间1970年1月1日00:00:00起经过的毫秒数； 如果字符串无法识别，或在某些情况下包含非法的日期值 （例如2015-02-31），则抛出`RangeError`。明确要求支持(YYYY-MM-DDTHH:mm:ss.sssZ)格式。 其他格式由实现决定，可能无法在所有浏览器（目标平台）上生效。 如果需要兼容多种格式，可借助相应的库。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dateStr | string | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setDate

```TypeScript
public setDate(value: int): long
```

按本地时间修改给定Date实例中月份的第几天。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setFullYear

```TypeScript
public setFullYear(value: int): long
```

按本地时间设置指定日期的完整年份。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setFullYear

```TypeScript
public setFullYear(value: int, month: int): long
```

按本地时间设置指定日期的完整年份。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |
| month | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setFullYear

```TypeScript
public setFullYear(value: int, month: int, date: int): long
```

按本地时间设置指定日期的完整年份。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |
| month | int | 是 |
| date | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setHours

```TypeScript
public setHours(value: int): long
```

按本地时间设置指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setHours

```TypeScript
public setHours(value: int, min: int): long
```

按本地时间设置指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |
| min | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setHours

```TypeScript
public setHours(value: int, min: int, sec: int): long
```

按本地时间设置指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |
| min | int | 是 |
| sec | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setHours

```TypeScript
public setHours(value: int, min: int, sec: int, ms: int): long
```

按本地时间设置指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |
| min | int | 是 |
| sec | int | 是 |
| ms | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setMilliseconds

```TypeScript
public setMilliseconds(value: int): long
```

按本地时间设置指定日期的毫秒数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setMinutes

```TypeScript
public setMinutes(value: int): long
```

按本地时间设置指定日期的分钟数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setMinutes

```TypeScript
public setMinutes(value: int, sec: int): long
```

按本地时间设置指定日期的分钟数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |
| sec | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setMinutes

```TypeScript
public setMinutes(value: int, sec: int, ms: int): long
```

按本地时间设置指定日期的分钟数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |
| sec | int | 是 |
| ms | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setMonth

```TypeScript
public setMonth(month: int): long
```

按当前已设置的年份设置指定日期的月份。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| month | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setMonth

```TypeScript
public setMonth(month: int, date: int): long
```

按当前已设置的年份设置指定日期的月份。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| month | int | 是 |
| date | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setSeconds

```TypeScript
public setSeconds(value: int): long
```

按本地时间设置指定日期的秒数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setSeconds

```TypeScript
public setSeconds(value: int, ms: int): long
```

按本地时间设置指定日期的秒数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |
| ms | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setTime

```TypeScript
public setTime(value: long): long
```

设置自纪元起经过的毫秒数， 纪元定义为UTC时间1970年1月1日零点。

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
| long |

## setTimezoneOffset

```TypeScript
public setTimezoneOffset(value: int): long
```

设置同一日期分别在UTC时区与本地时区下 在UTC时区与本地时区下求值所得的差值，单位为分钟。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCDate

```TypeScript
public setUTCDate(value: int): long
```

按UTC时间修改给定Date实例中月份的第几天。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCDay

```TypeScript
public setUTCDay(value: int): long
```

使用协调世界时（UTC）设置Date对象中月份的第几天。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCFullYear

```TypeScript
public setUTCFullYear(value: int): long
```

按世界时设置指定日期的完整年份。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCFullYear

```TypeScript
public setUTCFullYear(value: int, month: int): long
```

按世界时设置指定日期的完整年份。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |
| month | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCFullYear

```TypeScript
public setUTCFullYear(value: int, month: int, date: int): long
```

按世界时设置指定日期的完整年份。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |
| month | int | 是 |
| date | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCHours

```TypeScript
public setUTCHours(value: int): long
```

按世界时设置指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCHours

```TypeScript
public setUTCHours(value: int, min: int): long
```

按世界时设置指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |
| min | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCHours

```TypeScript
public setUTCHours(value: int, min: int, sec: int): long
```

按世界时设置指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |
| min | int | 是 |
| sec | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCHours

```TypeScript
public setUTCHours(value: int, min: int, sec: int, ms: int): long
```

按世界时设置指定日期的小时数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |
| min | int | 是 |
| sec | int | 是 |
| ms | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCMilliseconds

```TypeScript
public setUTCMilliseconds(value: int): long
```

按世界时设置指定日期的毫秒数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCMinutes

```TypeScript
public setUTCMinutes(value: int): long
```

按世界时设置指定日期的分钟数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCMinutes

```TypeScript
public setUTCMinutes(value: int, sec: int): long
```

按世界时设置指定日期的分钟数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |
| sec | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCMinutes

```TypeScript
public setUTCMinutes(value: int, sec: int, ms: int): long
```

按世界时设置指定日期的分钟数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |
| sec | int | 是 |
| ms | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCMonth

```TypeScript
public setUTCMonth(month: int): long
```

按世界时设置指定日期的月份。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| month | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCMonth

```TypeScript
public setUTCMonth(month: int, date: int): long
```

按世界时设置指定日期的月份。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| month | int | 是 |
| date | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCSeconds

```TypeScript
public setUTCSeconds(value: int): long
```

按世界时设置指定日期的秒数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setUTCSeconds

```TypeScript
public setUTCSeconds(value: int, ms: int): long
```

按世界时设置指定日期的秒数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |
| ms | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## setYear

```TypeScript
public setYear(value: int): void
```

按本地时间设置指定日期的完整年份。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

## toDateString

```TypeScript
public toDateString(): string
```

以英文返回日期中的日期部分。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## toISOString

```TypeScript
public toISOString(): string
```

按世界时返回符合ISO 8601格式的字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## toJSON

```TypeScript
public toJSON(): string | null
```

返回该日期的JSON表示。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string \| null |

## toLocaleDateString

```TypeScript
public toLocaleDateString(locales?: Intl.LocalesArgument,
        options?: Intl.DateTimeFormatOptions): string
```

获取日期部分的本地化表示。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | Intl.LocalesArgument | 否 |
| options | Intl.DateTimeFormatOptions | 否 |

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

## toLocaleTimeString

```TypeScript
public toLocaleTimeString(): string
```

获取日期中时间部分的本地化表示。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## toLocaleTimeString

```TypeScript
public toLocaleTimeString(locales?: Intl.LocalesArgument,
        options?: Intl.DateTimeFormatOptions): string
```

获取日期中时间部分的本地化表示。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | Intl.LocalesArgument | 否 |
| options | Intl.DateTimeFormatOptions | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## toString

```TypeScript
public toString(): string
```

返回表示该Date对象的字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## toTimeString

```TypeScript
public toTimeString(): string
```

以英文返回日期中的时间部分。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## toUTCString

```TypeScript
public toUTCString(): string
```

返回以世界时表示该Date对象的字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## UTC

```TypeScript
public static UTC(d: Date): long
```

返回自纪元起经过的毫秒数， 纪元定义为UTC时间1970年1月1日零点。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | Date | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## UTC

```TypeScript
public static UTC(year: int): long
```

返回自纪元起经过的毫秒数， 纪元定义为UTC时间1970年1月1日零点。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| year | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## UTC

```TypeScript
public static UTC(year: int, month: int, day?: int, hours?: int, minutes?: int, seconds?: int, ms?: int): long
```

返回自纪元起经过的毫秒数， 纪元定义为UTC时间1970年1月1日零点。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| year | int | 是 |
| month | int | 是 |
| day | int | 否 |
| hours | int | 否 |
| minutes | int | 否 |
| seconds | int | 否 |
| ms | int | 否 |

**返回值：**

| 类型 |
| --- |
| long |

## valueOf

```TypeScript
public valueOf(): long
```

`valueOf()`方法返回`Date`对象的原始值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| long |
