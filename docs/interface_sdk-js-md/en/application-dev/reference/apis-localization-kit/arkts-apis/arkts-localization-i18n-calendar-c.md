# Calendar

提供历法相关的能力，包括历法名称获取和日期计算等。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export class Calendar--><!--Device-i18n-export class Calendar-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## add

```TypeScript
add(field: string, amount: int): void
```

对日历对象中的表示时间日期的日历属性值进行加减操作。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-add(field: string, amount: int): void--><!--Device-Calendar-add(field: string, amount: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 指定的日历属性，目前支持的属性值有 year, month, week_of_year, week_of_month, date, day_of_year,  day_of_week, day_of_week_in_month, hour, hour_of_day, minute, second, millisecond。 &lt;br&gt;各取值代表的含义请参考[get](arkts-localization-i18n-calendar-c.md#get)。 |
| amount | int | Yes | 进行加减操作的具体数值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

## compareDays

```TypeScript
compareDays(date: Date): int
```

比较日历对象当前日期和指定日期相差的天数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-compareDays(date: Date): int--><!--Device-Calendar-compareDays(date: Date): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | Yes | 时间日期。 &lt;br&gt;**说明：** &lt;br&gt;月份从0开始计数，0表示一月。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 相差的天数，正数表示日历时间更早，负数表示指定时间更早。 &lt;br&gt;按毫秒级的精度，不足一天按一天计。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

## get

```TypeScript
get(field: string): int
```

获取日历对象中日历属性的值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-get(field: string): int--><!--Device-Calendar-get(field: string): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 指定的日历属性，取值包括： &lt;br&gt;"era"：纪元，例如公历中的公元前或者公元后。 &lt;br&gt;"year"：年。 &lt;br&gt;"month"：月，从0开始计数，0表示一月。 &lt;br&gt;"date"：日。 &lt;br&gt;"hour"：挂钟小时数。 &lt;br&gt;"hour_of_day"：一天中的第几小时。 &lt;br&gt;"minute"：分。 &lt;br&gt;"second"：秒。 &lt;br&gt;"millisecond"：毫秒。 &lt;br&gt;"week_of_year"：一年中的第几周，按照星期计算周，第一周的归属各地有区别。 &lt;br&gt;"year_woy"：一年中的第几周，按照数值计算周，例如一年中前1~7日属于第一周。 &lt;br&gt;"week_of_month"：一个月中的第几周，按照星期计算周。 &lt;br&gt;"day_of_week_in_month"：一月中的第几周，按照数值计算周，例如1-7日属于第一周。 &lt;br&gt;"day_of_year"：一年中的第几天。 &lt;br&gt;"day_of_week"：一周中的第几天(星期)。 &lt;br&gt;"milliseconds_in_day"：一天中的第几毫秒。 &lt;br&gt;"zone_offset"：以毫秒计时的时区固定偏移量（不含夏令时）。 &lt;br&gt;"dst_offset"：以毫秒计时的夏令时偏移量。 &lt;br&gt;"dow_local"：本地星期。 &lt;br&gt;"extended_year"：扩展的年份数值，支持负数。 &lt;br&gt;"julian_day"：儒略日，与当前时区相关。 &lt;br&gt;"is_leap_month"：返回1表示是闰月，返回0表示不是闰月。 &lt;br&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| int | 日历属性的值，如当前Calendar对象的内部日期的年份为1990，get('year')返回1990。 |

## getDisplayName

```TypeScript
getDisplayName(locale: string): string
```

获取日历对象名称在指定语言下的翻译。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-getDisplayName(locale: string): string--><!--Device-Calendar-getDisplayName(locale: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | [表示区域ID的字符串](../../../internationalization/i18n-locale-culture.md#实现原理)，由语言、脚本、国家地区组 成。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 日历对象名称在指定语言下的翻译。如buddhist在en-US上显示的名称为“Buddhist Calendar”。 |

## getFirstDayOfWeek

```TypeScript
getFirstDayOfWeek(): int
```

获取日历对象的周起始日。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-getFirstDayOfWeek(): int--><!--Device-Calendar-getFirstDayOfWeek(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| int | 周起始日，1代表周日，7代表周六。 |

## getMinimalDaysInFirstWeek

```TypeScript
getMinimalDaysInFirstWeek(): int
```

获取日历对象一年中第一周的最小天数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-getMinimalDaysInFirstWeek(): int--><!--Device-Calendar-getMinimalDaysInFirstWeek(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| int | 一年中第一周的最小天数。 |

## getTimeInMillis

```TypeScript
getTimeInMillis(): long
```

获取当前日历对象的时间戳。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-getTimeInMillis(): long--><!--Device-Calendar-getTimeInMillis(): long-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| long | Unix时间戳，表示从1970.1.1 00:00:00 GMT逝去的毫秒数。 |

## getTimeZone

```TypeScript
getTimeZone(): string
```

获取日历对象的时区ID。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-getTimeZone(): string--><!--Device-Calendar-getTimeZone(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | 表示时区ID的字符串。 |

## isWeekend

```TypeScript
isWeekend(date?: Date): boolean
```

判断指定的日期在日历对象中是否为周末。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-isWeekend(date?: Date): boolean--><!--Device-Calendar-isWeekend(date?: Date): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | No | 时间日期。 &lt;br&gt;**说明：** &lt;br&gt;月份从0开始计数，0表示一月。 &lt;br&gt;默认值：日历对象的当前日期。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true表示指定的日期是周末，false表示指定的日期不是周末。 |

## set

```TypeScript
set(year: int, month: int, date:int, hour?: int, minute?: int, second?: int): void
```

设置日历对象的年、月、日、时、分、秒。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-set(year: int, month: int, date:int, hour?: int, minute?: int, second?: int): void--><!--Device-Calendar-set(year: int, month: int, date:int, hour?: int, minute?: int, second?: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| year | int | Yes | 设置的年。 |
| month | int | Yes | 设置的月。 &lt;br&gt;**说明：** &lt;br&gt;月份从0开始计数，0表示一月。 |
| date | int | Yes | 设置的日。 |
| hour | int | No | 设置的小时。默认值：系统时间。 |
| minute | int | No | 设置的分钟。默认值：系统时间。 |
| second | int | No | 设置的秒。默认值：系统时间。 |

## setFirstDayOfWeek

```TypeScript
setFirstDayOfWeek(value: int): void
```

设置日历对象的周起始日。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-setFirstDayOfWeek(value: int): void--><!--Device-Calendar-setFirstDayOfWeek(value: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | 一周的起始日，1代表周日，7代表周六。 |

## setMinimalDaysInFirstWeek

```TypeScript
setMinimalDaysInFirstWeek(value: int): void
```

设置日历对象一年中第一周的最小天数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-setMinimalDaysInFirstWeek(value: int): void--><!--Device-Calendar-setMinimalDaysInFirstWeek(value: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | 一年中第一周的最小天数。 |

## setTime

```TypeScript
setTime(date: Date): void
```

基于传入的Date对象，设置日历对象内部的时间日期。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-setTime(date: Date): void--><!--Device-Calendar-setTime(date: Date): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | Yes | 时间日期。 &lt;br&gt;**说明：** &lt;br&gt;月份从0开始计数，0表示一月。 |

## setTime

```TypeScript
setTime(time: double): void
```

基于传入的时间戳，设置日历对象内部的时间日期。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-setTime(time: double): void--><!--Device-Calendar-setTime(time: double): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| time | double | Yes | Unix时间戳，表示从1970.1.1 00:00:00 GMT逝去的毫秒数。 |

## setTimeZone

```TypeScript
setTimeZone(timezone: string): void
```

设置日历对象的时区。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-setTimeZone(timezone: string): void--><!--Device-Calendar-setTimeZone(timezone: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timezone | string | Yes | 合法的时区ID，如“Asia/Shanghai”。 |

