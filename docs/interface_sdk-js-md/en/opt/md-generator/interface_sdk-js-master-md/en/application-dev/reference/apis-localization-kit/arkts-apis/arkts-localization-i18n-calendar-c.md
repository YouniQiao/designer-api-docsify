# Calendar

Provides calendar management capabilities, such as calendar name retrieval and date calculation.

**Since:** 7

<!--Device-i18n-export class Calendar--><!--Device-i18n-export class Calendar-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## add

```TypeScript
add(field: string, amount: number): void
```

Performs addition or subtraction on the calendar attributes of this **Calendar** object.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-add(field: string, amount: int): void--><!--Device-Calendar-add(field: string, amount: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| amount | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [890001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-localization-kit/errorcode-i18n.md#890001-parameter-error) |

## Examples

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

```TypeScript
compareDays(date: Date): number
```

Compares the current date of this **Calendar** object with the specified date for the difference in the number of days.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-compareDays(date: Date): int--><!--Device-Calendar-compareDays(date: Date): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| date | Date | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

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

```TypeScript
get(field: string): number
```

Obtains the values of the calendar attributes in this **Calendar** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-get(field: string): int--><!--Device-Calendar-get(field: string): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

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

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-getDisplayName(locale: string): string--><!--Device-Calendar-getDisplayName(locale: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locale | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('en-US', 'buddhist');
let calendarName: string = calendar.getDisplayName('zh'); // calendarName = 'Buddhist'
```

## getFirstDayOfWeek

```TypeScript
getFirstDayOfWeek(): number
```

Obtains the first day of a week for this **Calendar** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-getFirstDayOfWeek(): int--><!--Device-Calendar-getFirstDayOfWeek(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('en-US', 'gregory');
let firstDayOfWeek: number = calendar.getFirstDayOfWeek(); // firstDayOfWeek = 1
```

## getMinimalDaysInFirstWeek

```TypeScript
getMinimalDaysInFirstWeek(): number
```

Obtains the minimum number of days in the first week for this **Calendar** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-getMinimalDaysInFirstWeek(): int--><!--Device-Calendar-getMinimalDaysInFirstWeek(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
let minimalDaysInFirstWeek: number = calendar.getMinimalDaysInFirstWeek(); // minimalDaysInFirstWeek = 1
```

## getTimeInMillis

```TypeScript
getTimeInMillis(): number
```

Obtains the timestamp of this **Calendar** object.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-getTimeInMillis(): long--><!--Device-Calendar-getTimeInMillis(): long-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

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

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-getTimeZone(): string--><!--Device-Calendar-getTimeZone(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

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

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-isWeekend(date?: Date): boolean--><!--Device-Calendar-isWeekend(date?: Date): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| date | Date | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.set(2021, 11, 11, 8, 0, 0); // Set the time to 2021.12.11 08:00:00.
let isWeekend: boolean = calendar.isWeekend(); // isWeekend = true
let date: Date = new Date(2011, 11, 6, 9, 0, 0); // The date and time is 2011-12-06 09:00:00.
isWeekend = calendar.isWeekend(date); // isWeekend = false
```

## set

```TypeScript
set(year: number, month: number, date:number, hour?: number, minute?: number, second?: number): void
```

Sets the year, month, day, hour, minute, and second for this **Calendar** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-set(year: int, month: int, date:int, hour?: int, minute?: int, second?: int): void--><!--Device-Calendar-set(year: int, month: int, date:int, hour?: int, minute?: int, second?: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| year | number | Yes |
| month | number | Yes |
| date | number | Yes |
| hour | number | No |
| minute | number | No |
| second | number | No |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.set(2021, 10, 1, 8, 0, 0); // Set the date and time to 2021.11.1 08:00:00.
```

## setFirstDayOfWeek

```TypeScript
setFirstDayOfWeek(value: number): void
```

Sets the first day of a week for this **Calendar** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-setFirstDayOfWeek(value: int): void--><!--Device-Calendar-setFirstDayOfWeek(value: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setFirstDayOfWeek(3);
let firstDayOfWeek: number = calendar.getFirstDayOfWeek(); // firstDayOfWeek = 3
```

## setMinimalDaysInFirstWeek

```TypeScript
setMinimalDaysInFirstWeek(value: number): void
```

Sets the minimum number of days in the first week for this **Calendar** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-setMinimalDaysInFirstWeek(value: int): void--><!--Device-Calendar-setMinimalDaysInFirstWeek(value: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## Examples

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

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-setTime(date: Date): void--><!--Device-Calendar-setTime(date: Date): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| date | Date | Yes |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('en-US', 'gregory');
let date: Date = new Date(2021, 10, 7, 8, 0, 0); // The date and time is 2021.11.07 08:00:00.
calendar.setTime(date);
```

## setTime

```TypeScript
setTime(time: number): void
```

Sets the date and time for a **Calendar** object based on the input timestamp.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-setTime(time: double): void--><!--Device-Calendar-setTime(time: double): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| time | number | Yes |

## Examples

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

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Calendar-setTimeZone(timezone: string): void--><!--Device-Calendar-setTimeZone(timezone: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timezone | string | Yes |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setTimeZone('Asia/Shanghai');
```
