# Calendar

Provides calendar management capabilities, such as calendar name retrieval and date calculation.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-i18n-export class Calendar--><!--Device-i18n-export class Calendar-End-->

**System capability:** SystemCapability.Global.I18n

## add

ArkTS-Dyn:
```TypeScript
add(field: string, amount: number): void
```

ArkTS-Sta:
```TypeScript
add(field: string, amount: int): void
```

Performs addition or subtraction on the calendar attributes of this **Calendar** object.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-add(field: string, amount: int): void--><!--Device-Calendar-add(field: string, amount: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Calendar attribute. The value can be any of the following: **year**, **month**,**week\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_year**, **week\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_month**, **date**, **day\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_year**, **day\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_week**, **day\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_week\_\_\_ESCAPED\_UNDERSCORE\_\_\_in\_\_\_ESCAPED\_UNDERSCORE\_\_\_month**,**hour**, **hour\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_day**, **minute**, **second**, **millisecond**.For details about the values, see [get]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| amount | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Addition or subtraction amount. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| [890001](../errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
  calendar.set(2021, 11, 11, 8, 0, 0); // Set the date and time to 2021.12.11 08:00:00.
  calendar.add('year', 8); // 2021 + 8
  let year: number = calendar.get('year'); // year = 2029
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call Calendar.add failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## compareDays

ArkTS-Dyn:
```TypeScript
compareDays(date: Date): number
```

ArkTS-Sta:
```TypeScript
compareDays(date: Date): int
```

Compares the current date of this **Calendar** object with the specified date for the difference in the number of days.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-compareDays(date: Date): int--><!--Device-Calendar-compareDays(date: Date): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Date and time. Note: The month starts from **0**. For example, **0** indicates January. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Difference in the number of days. A positive number indicates that the calendar date is earlier, |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
  calendar.setTime(5000);
  let date: Date = new Date(6000);
  let diff: number = calendar.compareDays(date); // diff = 1
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call Calendar.compareDays failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## get

ArkTS-Dyn:
```TypeScript
get(field: string): number
```

ArkTS-Sta:
```TypeScript
get(field: string): int
```

Obtains the values of the calendar attributes in this **Calendar** object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-get(field: string): int--><!--Device-Calendar-get(field: string): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Calendar attributes. The following table lists the supported attribute values.The value can be"era": Era, for example, AD or BC."year": Year."month": Month. Note: The month starts from **0**. For example, **0** indicates January."date": Date."hour": Wall-clock hour."hour\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_day": Hour of day."minute": Minute."second": Second."millisecond": Millisecond."week\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_year": Week of year. Note that the algorithm for calculating the first week of a year varies according to regions. For example, the first seven days in a year are the first week."year\_\_\_ESCAPED\_UNDERSCORE\_\_\_woy": Year used with the week of year field."week\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_month": Week of month."day\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_week\_\_\_ESCAPED\_UNDERSCORE\_\_\_in\_\_\_ESCAPED\_UNDERSCORE\_\_\_month": Day of week in month."day\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_year": Day of year."day\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_week": Day of week."milliseconds\_\_\_ESCAPED\_UNDERSCORE\_\_\_in\_\_\_ESCAPED\_UNDERSCORE\_\_\_day": Milliseconds in day."zone\_\_\_ESCAPED\_UNDERSCORE\_\_\_offset": Fixed time zone offset in milliseconds (excluding DST)."dst\_\_\_ESCAPED\_UNDERSCORE\_\_\_offset": DST offset in milliseconds."dow\_\_\_ESCAPED\_UNDERSCORE\_\_\_local": Localized day of week."extended\_\_\_ESCAPED\_UNDERSCORE\_\_\_year": Extended year, which can be a negative number."julian\_\_\_ESCAPED\_UNDERSCORE\_\_\_day": Julian day."is\_\_\_ESCAPED\_UNDERSCORE\_\_\_leap\_\_\_ESCAPED\_UNDERSCORE\_\_\_month": Whether a month is a leap month. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Value of the calendar attribute. For example, if the year of the internal date of the current |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.set(2021, 10, 1, 8, 0, 0); // Set the date and time to 2021.11.1 08:00:00.
let hourOfDay: number = calendar.get('hour_of_day'); // hourOfDay = 8
```

## getDisplayName

```TypeScript
getDisplayName(locale: string): string
```

Obtains calendar display name in the specified language.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-getDisplayName(locale: string): string--><!--Device-Calendar-getDisplayName(locale: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_,which consists of the language, script, and country/region. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Calendar display name in the specified language. For example, **buddhist** is displayed as |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('en-US', 'buddhist');
let calendarName: string = calendar.getDisplayName('zh'); // calendarName = 'Buddhist'
```

## getFirstDayOfWeek

ArkTS-Dyn:
```TypeScript
getFirstDayOfWeek(): number
```

ArkTS-Sta:
```TypeScript
getFirstDayOfWeek(): int
```

Obtains the first day of a week for this **Calendar** object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-getFirstDayOfWeek(): int--><!--Device-Calendar-getFirstDayOfWeek(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | First day of a week. The value **1** indicates Sunday, and the value **7** indicates Saturday. |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('en-US', 'gregory');
let firstDayOfWeek: number = calendar.getFirstDayOfWeek(); // firstDayOfWeek = 1
```

## getMinimalDaysInFirstWeek

ArkTS-Dyn:
```TypeScript
getMinimalDaysInFirstWeek(): number
```

ArkTS-Sta:
```TypeScript
getMinimalDaysInFirstWeek(): int
```

Obtains the minimum number of days in the first week for this **Calendar** object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-getMinimalDaysInFirstWeek(): int--><!--Device-Calendar-getMinimalDaysInFirstWeek(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Minimum number of days in the first week of a year. |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
let minimalDaysInFirstWeek: number = calendar.getMinimalDaysInFirstWeek(); // minimalDaysInFirstWeek = 1
```

## getTimeInMillis

ArkTS-Dyn:
```TypeScript
getTimeInMillis(): number
```

ArkTS-Sta:
```TypeScript
getTimeInMillis(): long
```

Obtains the timestamp of this **Calendar** object.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-getTimeInMillis(): long--><!--Device-Calendar-getTimeInMillis(): long-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Unix timestamp, which indicates the number of milliseconds that have elapsed since the Unix |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setTime(5000);
let millisecond: number = calendar.getTimeInMillis(); // millisecond = 5000
```

## getTimeZone

```TypeScript
getTimeZone(): string
```

Obtains the time zone ID of this **Calendar** object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-getTimeZone(): string--><!--Device-Calendar-getTimeZone(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | Time zone ID. |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setTimeZone('Asia/Shanghai');
let timezone: string = calendar.getTimeZone(); // timezone = 'Asia/Shanghai'
```

## isWeekend

```TypeScript
isWeekend(date?: Date): boolean
```

Checks whether a given date is a weekend in this **Calendar** object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-isWeekend(date?: Date): boolean--><!--Device-Calendar-isWeekend(date?: Date): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | No | Date and time. Note: The month starts from **0**. For example, **0** indicates January.The default value is current date of the **Calendar** object. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The value **true** indicates that the specified date is a weekend, and the value **false** |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.set(2021, 11, 11, 8, 0, 0); // Set the time to 2021.12.11 08:00:00.
let isWeekend: boolean = calendar.isWeekend(); // isWeekend = true
let date: Date = new Date(2011, 11, 6, 9, 0, 0); // The date and time is 2011-12-06 09:00:00.
isWeekend = calendar.isWeekend(date); // isWeekend = false
```

## set

ArkTS-Dyn:
```TypeScript
set(year: number, month: number, date:number, hour?: number, minute?: number, second?: number): void
```

ArkTS-Sta:
```TypeScript
set(year: int, month: int, date:int, hour?: int, minute?: int, second?: int): void
```

Sets the year, month, day, hour, minute, and second for this **Calendar** object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-set(year: int, month: int, date:int, hour?: int, minute?: int, second?: int): void--><!--Device-Calendar-set(year: int, month: int, date:int, hour?: int, minute?: int, second?: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| year | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Year to set. |
| month | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Month to set. Note: The month starts from **0**. For example, **0** indicates January. |
| date | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Day to set. |
| hour | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | No | Hour to set. The default value is the current system time. |
| minute | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | No | Minute to set. The default value is the current system time. |
| second | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | No | Second to set. The default value is the current system time. |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.set(2021, 10, 1, 8, 0, 0); // Set the date and time to 2021.11.1 08:00:00.
```

## setFirstDayOfWeek

ArkTS-Dyn:
```TypeScript
setFirstDayOfWeek(value: number): void
```

ArkTS-Sta:
```TypeScript
setFirstDayOfWeek(value: int): void
```

Sets the first day of a week for this **Calendar** object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-setFirstDayOfWeek(value: int): void--><!--Device-Calendar-setFirstDayOfWeek(value: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Start day of a week. The value **1** indicates Sunday, and the value **7** indicates Saturday. |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setFirstDayOfWeek(3);
let firstDayOfWeek: number = calendar.getFirstDayOfWeek(); // firstDayOfWeek = 3
```

## setMinimalDaysInFirstWeek

ArkTS-Dyn:
```TypeScript
setMinimalDaysInFirstWeek(value: number): void
```

ArkTS-Sta:
```TypeScript
setMinimalDaysInFirstWeek(value: int): void
```

Sets the minimum number of days in the first week for this **Calendar** object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-setMinimalDaysInFirstWeek(value: int): void--><!--Device-Calendar-setMinimalDaysInFirstWeek(value: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Minimum number of days in the first week of a year. |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setMinimalDaysInFirstWeek(3);
let minimalDaysInFirstWeek: number = calendar.getMinimalDaysInFirstWeek(); // minimalDaysInFirstWeek = 3
```

## setTime

```TypeScript
setTime(date: Date): void
```

Sets the date and time for a **Calendar** object based on the input **Date** object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-setTime(date: Date): void--><!--Device-Calendar-setTime(date: Date): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Date and time. Note: The month starts from **0**. For example, **0** indicates January. |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('en-US', 'gregory');
let date: Date = new Date(2021, 10, 7, 8, 0, 0); // The date and time is 2021.11.07 08:00:00.
calendar.setTime(date);
```

## setTime

ArkTS-Dyn:
```TypeScript
setTime(time: number): void
```

ArkTS-Sta:
```TypeScript
setTime(time: double): void
```

Sets the date and time for a **Calendar** object based on the input timestamp.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-setTime(time: double): void--><!--Device-Calendar-setTime(time: double): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| time | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Unix timestamp, which indicates the number of milliseconds that have elapsed since the Unix epoch. |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('en-US', 'gregory');
calendar.setTime(10540800000);
```

## setTimeZone

```TypeScript
setTimeZone(timezone: string): void
```

Sets the time zone of this **Calendar** object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-setTimeZone(timezone: string): void--><!--Device-Calendar-setTimeZone(timezone: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timezone | string | Yes | Valid time zone ID, for example, Asia/Shanghai. |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setTimeZone('Asia/Shanghai');
```

