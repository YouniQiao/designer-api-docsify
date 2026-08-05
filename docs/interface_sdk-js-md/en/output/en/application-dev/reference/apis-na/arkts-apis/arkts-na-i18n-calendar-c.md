# Calendar

Provides the API for accessing Calendar name, time and date related information.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export class Calendar--><!--Device-i18n-export class Calendar-End-->

**System capability:** SystemCapability.Global.I18n

## add

```TypeScript
add(field: string, amount: int): void
```

Performs addition or subtraction on the calendar attributes of this Calendar object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-add(field: string, amount: int): void--><!--Device-Calendar-add(field: string, amount: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Calendar attribute. The value can be any of the following: year, month, week\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_year,week\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_month, date, day\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_year, day\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_week, day\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_week\_\_\_ESCAPED\_UNDERSCORE\_\_\_in\_\_\_ESCAPED\_UNDERSCORE\_\_\_month, hour,hour\_\_\_ESCAPED\_UNDERSCORE\_\_\_of\_\_\_ESCAPED\_UNDERSCORE\_\_\_day, minute, second, millisecond. For details about the values, see get. |
| amount | int | Yes | Addition or subtraction amount. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## compareDays

```TypeScript
compareDays(date: Date): int
```

Compares the current date of this Calendar object with the specified date for the difference in the number of days.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-compareDays(date: Date): int--><!--Device-Calendar-compareDays(date: Date): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Date and time. Note: The month starts from 0. For example, 0 indicates January. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Difference in the number of days. A positive number indicates that the calendar date is |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

## get

```TypeScript
get(field: string): int
```

Obtains the values of the calendar attributes in this Calendar object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-get(field: string): int--><!--Device-Calendar-get(field: string): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Calendar attributes. The following table lists the supported attribute values. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Value of the calendar attribute. For example, if the year of the internal date of the |

## getDisplayName

```TypeScript
getDisplayName(locale: string): string
```

Obtains calendar display name in the specified language.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-getDisplayName(locale: string): string--><!--Device-Calendar-getDisplayName(locale: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | System locale, which consists of the language, script, and country/region. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Calendar display name in the specified language. For example, buddhist is displayed as |

## getFirstDayOfWeek

```TypeScript
getFirstDayOfWeek(): int
```

Obtains the first day of a week for this Calendar object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-getFirstDayOfWeek(): int--><!--Device-Calendar-getFirstDayOfWeek(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| int | First day of a week. The value 1 indicates Sunday, and the value 7 indicates Saturday. |

## getMinimalDaysInFirstWeek

```TypeScript
getMinimalDaysInFirstWeek(): int
```

Obtains the minimum number of days in the first week for this Calendar object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-getMinimalDaysInFirstWeek(): int--><!--Device-Calendar-getMinimalDaysInFirstWeek(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| int | Minimum number of days in the first week of a year. |

## getTimeInMillis

```TypeScript
getTimeInMillis(): long
```

Obtains the timestamp of this Calendar object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-getTimeInMillis(): long--><!--Device-Calendar-getTimeInMillis(): long-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| long | Unix timestamp, which indicates the number of milliseconds that have elapsed since the |

## getTimeZone

```TypeScript
getTimeZone(): string
```

Obtains the time zone ID of this Calendar object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-getTimeZone(): string--><!--Device-Calendar-getTimeZone(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | Time zone ID. |

## isWeekend

```TypeScript
isWeekend(date?: Date): boolean
```

Checks whether a given date is a weekend in this Calendar object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-isWeekend(date?: Date): boolean--><!--Device-Calendar-isWeekend(date?: Date): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | No | Date and time. Note: The month starts from 0. For example, 0 indicates January.The default value is current date of the Calendar object. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The value "true" indicates that the specified date is a weekend, and the value "false" |

## set

```TypeScript
set(year: int, month: int, date:int, hour?: int, minute?: int, second?: int): void
```

Sets the year, month, day, hour, minute, and second for this Calendar object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-set(year: int, month: int, date:int, hour?: int, minute?: int, second?: int): void--><!--Device-Calendar-set(year: int, month: int, date:int, hour?: int, minute?: int, second?: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| year | int | Yes | Year to set. |
| month | int | Yes | Month to set. Note: The month starts from 0. For example, 0 indicates January. |
| date | int | Yes | Day to set. |
| hour | int | No | Hour to set. The default value is the current system time. |
| minute | int | No | Minute to set. The default value is the current system time. |
| second | int | No | Second to set. The default value is the current system time. |

## setFirstDayOfWeek

```TypeScript
setFirstDayOfWeek(value: int): void
```

Sets the first day of a week for this Calendar object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-setFirstDayOfWeek(value: int): void--><!--Device-Calendar-setFirstDayOfWeek(value: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | Start day of a week. The value 1 indicates Sunday, and the value 7 indicates Saturday. |

## setMinimalDaysInFirstWeek

```TypeScript
setMinimalDaysInFirstWeek(value: int): void
```

Sets the minimum number of days in the first week for this Calendar object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-setMinimalDaysInFirstWeek(value: int): void--><!--Device-Calendar-setMinimalDaysInFirstWeek(value: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | Minimum number of days in the first week of a year. |

## setTime

```TypeScript
setTime(date: Date): void
```

Sets the date and time for a Calendar object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-setTime(date: Date): void--><!--Device-Calendar-setTime(date: Date): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Date and time. Note: The month starts from 0. For example, 0 indicates January. |

## setTime

```TypeScript
setTime(time: double): void
```

Sets the date and time for a Calendar object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-setTime(time: double): void--><!--Device-Calendar-setTime(time: double): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| time | double | Yes | Unix timestamp, which indicates the number of milliseconds that have elapsed since the Unix epoch. |

## setTimeZone

```TypeScript
setTimeZone(timezone: string): void
```

Sets the time zone of this Calendar object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Calendar-setTimeZone(timezone: string): void--><!--Device-Calendar-setTimeZone(timezone: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timezone | string | Yes | Valid time zone ID, for example, Asia/Shanghai. |

