# Calendar

提供历法相关的能力，包括历法名称获取和日期计算等。

**起始版本：** 7

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## add

```TypeScript
add(field: string, amount: number): void
```

对日历对象中的表示时间日期的日历属性值进行加减操作。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| amount | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

## compareDays

```TypeScript
compareDays(date: Date): number
```

比较日历对象当前日期和指定日期相差的天数。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| date | Date | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## get

```TypeScript
get(field: string): number
```

获取日历对象中日历属性的值。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getDisplayName

```TypeScript
getDisplayName(locale: string): string
```

获取日历对象名称在指定语言下的翻译。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locale | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## getFirstDayOfWeek

```TypeScript
getFirstDayOfWeek(): number
```

获取日历对象的周起始日。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| number |

## getMinimalDaysInFirstWeek

```TypeScript
getMinimalDaysInFirstWeek(): number
```

获取日历对象一年中第一周的最小天数。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| number |

## getTimeInMillis

```TypeScript
getTimeInMillis(): number
```

获取当前日历对象的时间戳。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| number |

## getTimeZone

```TypeScript
getTimeZone(): string
```

获取日历对象的时区ID。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| string |

## isWeekend

```TypeScript
isWeekend(date?: Date): boolean
```

判断指定的日期在日历对象中是否为周末。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| date | Date | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

## set

```TypeScript
set(year: number, month: number, date:number, hour?: number, minute?: number, second?: number): void
```

设置日历对象的年、月、日、时、分、秒。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| year | number | 是 |
| month | number | 是 |
| date | number | 是 |
| hour | number | 否 |
| minute | number | 否 |
| second | number | 否 |

## setFirstDayOfWeek

```TypeScript
setFirstDayOfWeek(value: number): void
```

设置日历对象的周起始日。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## setMinimalDaysInFirstWeek

```TypeScript
setMinimalDaysInFirstWeek(value: number): void
```

设置日历对象一年中第一周的最小天数。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## setTime

```TypeScript
setTime(date: Date): void
```

基于传入的Date对象，设置日历对象内部的时间日期。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| date | Date | 是 |

## setTime

```TypeScript
setTime(time: number): void
```

基于传入的时间戳，设置日历对象内部的时间日期。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| time | number | 是 |

## setTimeZone

```TypeScript
setTimeZone(timezone: string): void
```

设置日历对象的时区。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timezone | string | 是 |
