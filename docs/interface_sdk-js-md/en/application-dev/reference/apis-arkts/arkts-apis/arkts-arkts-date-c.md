# Date

Date JS API-compatible class

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

<!--Device-unnamed-export class Date--><!--Device-unnamed-export class Date-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Default constructor.Initializes Date instance with current time.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-constructor()--><!--Device-Date-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(value: long | string | Date)
```

`Date` constructor. NOTE: Dates before `1921-01-01T00:00:00 GMT` can be represented as UTC milliseconds in different ways then TS do.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-constructor(value: long | string | Date)--><!--Device-Date-constructor(value: long | string | Date)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | long \| string \| Date | Yes | A value representing a date. Can be a timestamp in milliseconds (long), a date string (string), or an existing Date object (Date). |

## constructor

```TypeScript
constructor(year: int, monthIndex: int, day?: int, hours?: int, minutes?: int, seconds?: int, ms?: int)
```

`Date` constructor. NOTE: Dates before `1921-01-01T00:00:00 GMT` can be represented as UTC milliseconds in different ways then TS do.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-constructor(year: int, monthIndex: int, day?: int, hours?: int, minutes?: int, seconds?: int, ms?: int)--><!--Device-Date-constructor(year: int, monthIndex: int, day?: int, hours?: int, minutes?: int, seconds?: int, ms?: int)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| year | int | Yes | Year <br>The value range is all integers. |
| monthIndex | int | Yes | Month <br>The value range is all integers. |
| day | int | No | day <br>The value range is all integers. |
| hours | int | No | hours <br>The value range is all integers. |
| minutes | int | No | minutes <br>The value range is all integers. |
| seconds | int | No | seconds <br>The value range is all integers. |
| ms | int | No | ms <br>The value range is all integers. |

## getDate

```TypeScript
public getDate(): int
```

The `getDate()` method returns the day of the month for the specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getDate(): int--><!--Device-Date-public getDate(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | The day of the month (1 to 31) using local time. |

## getDay

```TypeScript
public getDay(): int
```

Returns the day of the week for the specified date according to local time, where 0 represents Sunday.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getDay(): int--><!--Device-Date-public getDay(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | The day of the week (0 for Sunday, 1 for Monday, ..., 6 for Saturday). |

## getFullYear

```TypeScript
public getFullYear(): int
```

Returns the year of the specified date according to local time. For dates between the years 1000 and 9999, `getFullYear()` returns a four-digit number, for example, 1995. Use this function to make sure a year is compliant with years after 2000.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getFullYear(): int--><!--Device-Date-public getFullYear(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | get fullyear |

## getHours

```TypeScript
public getHours(): int
```

Returns the hour for the specified date, according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getHours(): int--><!--Device-Date-public getHours(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | The hour (0 to 23) for the specified date according to local time. |

## getLocalTimezoneOffset

```TypeScript
public static getLocalTimezoneOffset(ms: long): long
```

Gets local time offset.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public static getLocalTimezoneOffset(ms: long): long--><!--Device-Date-public static getLocalTimezoneOffset(ms: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ms | long | Yes | the time in milliseconds. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The local time offset. |

## getMilliseconds

```TypeScript
public getMilliseconds(): int
```

Returns the milliseconds in the specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getMilliseconds(): int--><!--Device-Date-public getMilliseconds(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | The milliseconds (0 to 999) for the specified date according to local time. |

## getMinutes

```TypeScript
public getMinutes(): int
```

Returns the minutes in the specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getMinutes(): int--><!--Device-Date-public getMinutes(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | An integer number, between 0 and 59 representing the minutes in the given date according to local time. |

## getMonth

```TypeScript
public getMonth(): int
```

Returns the month in the specified date according to local time, as a zero-based value (where zero indicates the first month of the year).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getMonth(): int--><!--Device-Date-public getMonth(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | The month (0 to 11), where 0 represents January and 11 represents December. |

## getSeconds

```TypeScript
public getSeconds(): int
```

Returns the seconds in the specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getSeconds(): int--><!--Device-Date-public getSeconds(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | An integer number, between 0 and 59 representing the seconds in the given date according to local time. |

## getTime

```TypeScript
public getTime(): long
```

Returns the number of milliseconds since the epoch, which is defined as the midnight at the beginning of January 1, 1970, UTC.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getTime(): long--><!--Device-Date-public getTime(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## getTimezoneName

```TypeScript
public static getTimezoneName(ms: long): string
```

Gets time zone name.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public static getTimezoneName(ms: long): string--><!--Device-Date-public static getTimezoneName(ms: long): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ms | long | Yes | the time in milliseconds. |

**Return value:**

| Type | Description |
| --- | --- |
| string | The time zone name. |

## getTimezoneOffset

```TypeScript
public getTimezoneOffset(): long
```

Returns the difference, in minutes, between a date as evaluated in the UTC time zone, and the same date as evaluated in the local time zone.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getTimezoneOffset(): long--><!--Device-Date-public getTimezoneOffset(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | The timezone offset in minutes (negative for time zones ahead of UTC). |

## getUTCDate

```TypeScript
public getUTCDate(): int
```

Returns the day of the month (from 1 to 31) in the specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getUTCDate(): int--><!--Device-Date-public getUTCDate(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | The day of the month (1 to 31) using universal time. |

## getUTCDay

```TypeScript
public getUTCDay(): int
```

Returns the day of the week in the specified date according to universal time, where 0 represents Sunday.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getUTCDay(): int--><!--Device-Date-public getUTCDay(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | The day of the week (0 for Sunday, 1 for Monday, ..., 6 for Saturday) |

## getUTCFullYear

```TypeScript
public getUTCFullYear(): int
```

Returns the year of the specified date according to universal time. For dates between the years 1000 and 9999, `getUTCFullYear()` returns a four-digit number, for example, 1995. Use this function to make sure a year is compliant with years after 2000.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getUTCFullYear(): int--><!--Device-Date-public getUTCFullYear(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | get the UTCYear |

## getUTCHours

```TypeScript
public getUTCHours(): int
```

Returns the hours in the specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getUTCHours(): int--><!--Device-Date-public getUTCHours(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | The hour (0 to 23) for the specified date according to universal time. |

## getUTCMilliseconds

```TypeScript
public getUTCMilliseconds(): int
```

Returns the milliseconds portion of the time object's value according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getUTCMilliseconds(): int--><!--Device-Date-public getUTCMilliseconds(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int |  |

## getUTCMinutes

```TypeScript
public getUTCMinutes(): int
```

Returns the minutes in the specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getUTCMinutes(): int--><!--Device-Date-public getUTCMinutes(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | get new date value |

## getUTCMonth

```TypeScript
public getUTCMonth(): int
```

Returns the month of the specified date according to universal time as a zero-based value (where zero indicates the first month of the year).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getUTCMonth(): int--><!--Device-Date-public getUTCMonth(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | get new date value |

## getUTCSeconds

```TypeScript
public getUTCSeconds(): int
```

Returns the seconds in the specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getUTCSeconds(): int--><!--Device-Date-public getUTCSeconds(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | the seconds in the specified date according to universal time. |

## getYear

```TypeScript
public getYear(): int
```

Returns the year of the specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public getYear(): int--><!--Device-Date-public getYear(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | The year value. |

## isDateValid

```TypeScript
public isDateValid(): boolean
```

Checks if the constructed date is valid.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public isDateValid(): boolean--><!--Device-Date-public isDateValid(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the date is valid. |

## now

```TypeScript
static now(): long
```

The `now()` static method returns the number of milliseconds elapsed since the epoch, which is defined as the midnight at the beginning of January 1, 1970, UTC. which is defined as the midnight at the beginning of January 1, 1970, UTC.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-static now(): long--><!--Device-Date-static now(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | Returns the current time in milliseconds. |

## parse

```TypeScript
static parse(dateStr: string): long
```

Parses a string representation of a date, and returns the number of milliseconds since January 1, 1970, 00:00:00 UTC or throws `RangeError` if the string is unrecognized or, in some cases, contains illegal date values (e.g. 2015-02-31).

(YYYY-MM-DDTHH:mm:ss.sssZ) is explicitly specified to be supported. Other formats are implementation-defined and may not work across all browsers (targets). A library can help if many different formats are to be accommodated.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-static parse(dateStr: string): long--><!--Device-Date-static parse(dateStr: string): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dateStr | string | Yes | to be parsed |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setDate

```TypeScript
public setDate(value: int): long
```

Changes the day of the month of a given Date instance, based on local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setDate(value: int): long--><!--Device-Date-public setDate(value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new day <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long |  |

## setFullYear

```TypeScript
public setFullYear(value: int): long
```

Sets the full year for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setFullYear(value: int): long--><!--Device-Date-public setFullYear(value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new year <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setFullYear

```TypeScript
public setFullYear(value: int, month: int): long
```

Sets the full year for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setFullYear(value: int, month: int): long--><!--Device-Date-public setFullYear(value: int, month: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new year <br>The value range is all integers. |
| month | int | Yes | new month <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setFullYear

```TypeScript
public setFullYear(value: int, month: int, date: int): long
```

Sets the full year for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setFullYear(value: int, month: int, date: int): long--><!--Device-Date-public setFullYear(value: int, month: int, date: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new year <br>The value range is all integers. |
| month | int | Yes | new month <br>The value range is all integers. |
| date | int | Yes | new date <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setHours

```TypeScript
public setHours(value: int): long
```

Sets the hours for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setHours(value: int): long--><!--Device-Date-public setHours(value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new hours <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setHours

```TypeScript
public setHours(value: int, min: int): long
```

Sets the hours for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setHours(value: int, min: int): long--><!--Device-Date-public setHours(value: int, min: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new hours <br>The value range is all integers. |
| min | int | Yes | minutes <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setHours

```TypeScript
public setHours(value: int, min: int, sec: int): long
```

Sets the hours for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setHours(value: int, min: int, sec: int): long--><!--Device-Date-public setHours(value: int, min: int, sec: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new hours <br>The value range is all integers. |
| min | int | Yes | minutes <br>The value range is all integers. |
| sec | int | Yes | seconds <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setHours

```TypeScript
public setHours(value: int, min: int, sec: int, ms: int): long
```

Sets the hours for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setHours(value: int, min: int, sec: int, ms: int): long--><!--Device-Date-public setHours(value: int, min: int, sec: int, ms: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new hours <br>The value range is all integers. |
| min | int | Yes | minutes <br>The value range is all integers. |
| sec | int | Yes | seconds <br>The value range is all integers. |
| ms | int | Yes | millisecond <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setMilliseconds

```TypeScript
public setMilliseconds(value: int): long
```

Sets the milliseconds for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setMilliseconds(value: int): long--><!--Device-Date-public setMilliseconds(value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new ms <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setMinutes

```TypeScript
public setMinutes(value: int): long
```

Sets the minutes for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setMinutes(value: int): long--><!--Device-Date-public setMinutes(value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new minutes <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setMinutes

```TypeScript
public setMinutes(value: int, sec: int): long
```

Sets the minutes for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setMinutes(value: int, sec: int): long--><!--Device-Date-public setMinutes(value: int, sec: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new minutes <br>The value range is all integers. |
| sec | int | Yes | seconds <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setMinutes

```TypeScript
public setMinutes(value: int, sec: int, ms: int): long
```

Sets the minutes for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setMinutes(value: int, sec: int, ms: int): long--><!--Device-Date-public setMinutes(value: int, sec: int, ms: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new minutes <br>The value range is all integers. |
| sec | int | Yes | seconds <br>The value range is all integers. |
| ms | int | Yes | milliseconds <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setMonth

```TypeScript
public setMonth(month: int): long
```

Sets the month for a specified date according to the currently set year.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setMonth(month: int): long--><!--Device-Date-public setMonth(month: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| month | int | Yes | new month <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setMonth

```TypeScript
public setMonth(month: int, date: int): long
```

Sets the month for a specified date according to the currently set year.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setMonth(month: int, date: int): long--><!--Device-Date-public setMonth(month: int, date: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| month | int | Yes | new month <br>The value range is all integers. |
| date | int | Yes | Dated <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setSeconds

```TypeScript
public setSeconds(value: int): long
```

Sets the seconds for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setSeconds(value: int): long--><!--Device-Date-public setSeconds(value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new seconds <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setSeconds

```TypeScript
public setSeconds(value: int, ms: int): long
```

Sets the seconds for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setSeconds(value: int, ms: int): long--><!--Device-Date-public setSeconds(value: int, ms: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new seconds <br>The value range is all integers. |
| ms | int | Yes | milliseconds <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setTime

```TypeScript
public setTime(value: long): long
```

Sets the number of milliseconds since the epoch, which is defined as the midnight at the beginning of January 1, 1970, UTC.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setTime(value: long): long--><!--Device-Date-public setTime(value: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | long | Yes | new time in milliseconds. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The number of milliseconds since the epoch. |

## setTimezoneOffset

```TypeScript
public setTimezoneOffset(value: int): long
```

Sets the difference, in minutes, between a date as evaluated in the UTC time zone, and the same date as evaluated in the local time zone.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setTimezoneOffset(value: int): long--><!--Device-Date-public setTimezoneOffset(value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | The timezone offset in minutes from UTC. <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The new time value in milliseconds. |

## setUTCDate

```TypeScript
public setUTCDate(value: int): long
```

Changes the day of the month of a given Date instance, based on UTC time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCDate(value: int): long--><!--Device-Date-public setUTCDate(value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new day <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long |  |

## setUTCDay

```TypeScript
public setUTCDay(value: int): long
```

Sets the numeric day of the month in the Date object using Universal Coordinated Time (UTC).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCDay(value: int): long--><!--Device-Date-public setUTCDay(value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | The day of the week using universal time. <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | set UTCDay |

## setUTCFullYear

```TypeScript
public setUTCFullYear(value: int): long
```

Sets the full year for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCFullYear(value: int): long--><!--Device-Date-public setUTCFullYear(value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new year <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setUTCFullYear

```TypeScript
public setUTCFullYear(value: int, month: int): long
```

Sets the full year for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCFullYear(value: int, month: int): long--><!--Device-Date-public setUTCFullYear(value: int, month: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new year <br>The value range is all integers. |
| month | int | Yes | new month <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setUTCFullYear

```TypeScript
public setUTCFullYear(value: int, month: int, date: int): long
```

Sets the full year for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCFullYear(value: int, month: int, date: int): long--><!--Device-Date-public setUTCFullYear(value: int, month: int, date: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new year <br>The value range is all integers. |
| month | int | Yes | new month <br>The value range is all integers. |
| date | int | Yes | new date <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setUTCHours

```TypeScript
public setUTCHours(value: int): long
```

Sets the hour for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCHours(value: int): long--><!--Device-Date-public setUTCHours(value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new hours <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setUTCHours

```TypeScript
public setUTCHours(value: int, min: int): long
```

Sets the hour for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCHours(value: int, min: int): long--><!--Device-Date-public setUTCHours(value: int, min: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new hours <br>The value range is all integers. |
| min | int | Yes | minutes <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setUTCHours

```TypeScript
public setUTCHours(value: int, min: int, sec: int): long
```

Sets the hour for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCHours(value: int, min: int, sec: int): long--><!--Device-Date-public setUTCHours(value: int, min: int, sec: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new hours <br>The value range is all integers. |
| min | int | Yes | minutes <br>The value range is all integers. |
| sec | int | Yes | seconds <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setUTCHours

```TypeScript
public setUTCHours(value: int, min: int, sec: int, ms: int): long
```

Sets the hour for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCHours(value: int, min: int, sec: int, ms: int): long--><!--Device-Date-public setUTCHours(value: int, min: int, sec: int, ms: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new hours <br>The value range is all integers. |
| min | int | Yes | minutes <br>The value range is all integers. |
| sec | int | Yes | seconds <br>The value range is all integers. |
| ms | int | Yes | millisecond <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setUTCMilliseconds

```TypeScript
public setUTCMilliseconds(value: int): long
```

Sets the milliseconds for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCMilliseconds(value: int): long--><!--Device-Date-public setUTCMilliseconds(value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new ms <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setUTCMinutes

```TypeScript
public setUTCMinutes(value: int): long
```

Sets the minutes for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCMinutes(value: int): long--><!--Device-Date-public setUTCMinutes(value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new minutes <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setUTCMinutes

```TypeScript
public setUTCMinutes(value: int, sec: int): long
```

Sets the minutes for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCMinutes(value: int, sec: int): long--><!--Device-Date-public setUTCMinutes(value: int, sec: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new minutes <br>The value range is all integers. |
| sec | int | Yes | seconds <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setUTCMinutes

```TypeScript
public setUTCMinutes(value: int, sec: int, ms: int): long
```

Sets the minutes for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCMinutes(value: int, sec: int, ms: int): long--><!--Device-Date-public setUTCMinutes(value: int, sec: int, ms: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new minutes <br>The value range is all integers. |
| sec | int | Yes | seconds <br>The value range is all integers. |
| ms | int | Yes | milliseconds <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setUTCMonth

```TypeScript
public setUTCMonth(month: int): long
```

Sets the month for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCMonth(month: int): long--><!--Device-Date-public setUTCMonth(month: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| month | int | Yes | new month <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setUTCMonth

```TypeScript
public setUTCMonth(month: int, date: int): long
```

Sets the month for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCMonth(month: int, date: int): long--><!--Device-Date-public setUTCMonth(month: int, date: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| month | int | Yes | new month <br>The value range is all integers. |
| date | int | Yes | Dated <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## setUTCSeconds

```TypeScript
public setUTCSeconds(value: int): long
```

Sets the seconds for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCSeconds(value: int): long--><!--Device-Date-public setUTCSeconds(value: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new seconds <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long |  |

## setUTCSeconds

```TypeScript
public setUTCSeconds(value: int, ms: int): long
```

Sets the seconds for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setUTCSeconds(value: int, ms: int): long--><!--Device-Date-public setUTCSeconds(value: int, ms: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new seconds <br>The value range is all integers. |
| ms | int | Yes | milliseconds <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long |  |

## setYear

```TypeScript
public setYear(value: int): void
```

Sets the full year for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public setYear(value: int): void--><!--Device-Date-public setYear(value: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | new year <br>The value range is all integers. |

## toDateString

```TypeScript
public toDateString(): string
```

Returns the date portion of the date in English.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public toDateString(): string--><!--Device-Date-public toDateString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | The date string. |

## toISOString

```TypeScript
public toISOString(): string
```

Returns a string in ISO 8601 format according to universal time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public toISOString(): string--><!--Device-Date-public toISOString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | The ISO 8601 formatted string. |

## toJSON

```TypeScript
public toJSON(): string | null
```

Returns a JSON representation of the date.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public toJSON(): string | null--><!--Device-Date-public toJSON(): string | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string \| null | The JSON string or null if invalid. |

## toLocaleDateString

```TypeScript
public toLocaleDateString(locales?: Intl.LocalesArgument,
        options?: Intl.DateTimeFormatOptions): string
```

Gets a language-sensitive representation of the date portion.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public toLocaleDateString(locales?: Intl.LocalesArgument,        options?: Intl.DateTimeFormatOptions): string--><!--Device-Date-public toLocaleDateString(locales?: Intl.LocalesArgument,        options?: Intl.DateTimeFormatOptions): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | No | the locale. |
| options | Intl.DateTimeFormatOptions | No | the format options. |

**Return value:**

| Type | Description |
| --- | --- |
| string | The localized date string. |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

Returns a string representing the elements of the array. The elements are converted to Strings using their toLocaleString methods.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string--><!--Device-Date-public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | No | A string with a BCP 47 language tag, or an array of such strings. |
| options | object | No | An object with configuration properties. |

**Return value:**

| Type | Description |
| --- | --- |
| string | A string representing the elements of the array. |

## toLocaleTimeString

```TypeScript
public toLocaleTimeString(): string
```

Gets a language-sensitive representation of the time portion of the date.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public toLocaleTimeString(): string--><!--Device-Date-public toLocaleTimeString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | The localized time string. |

## toLocaleTimeString

```TypeScript
public toLocaleTimeString(locales?: Intl.LocalesArgument,
        options?: Intl.DateTimeFormatOptions): string
```

Gets a language-sensitive representation of the time portion of the date.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public toLocaleTimeString(locales?: Intl.LocalesArgument,        options?: Intl.DateTimeFormatOptions): string--><!--Device-Date-public toLocaleTimeString(locales?: Intl.LocalesArgument,        options?: Intl.DateTimeFormatOptions): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | Intl.LocalesArgument | No | the locale. |
| options | Intl.DateTimeFormatOptions | No | the format options. |

**Return value:**

| Type | Description |
| --- | --- |
| string | The localized time string. |

## toString

```TypeScript
public toString(): string
```

Returns a string representing the Date object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public toString(): string--><!--Device-Date-public toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | The string representation. |

## toTimeString

```TypeScript
public toTimeString(): string
```

Returns the time portion of the date in English.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public toTimeString(): string--><!--Device-Date-public toTimeString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | The time string. |

## toUTCString

```TypeScript
public toUTCString(): string
```

Returns a string representing the Date object in UTC.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public toUTCString(): string--><!--Device-Date-public toUTCString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | The UTC string representation. |

## UTC

```TypeScript
public static UTC(d: Date): long
```

Returns the number of milliseconds elapsed since the epoch, which is defined as the midnight at the beginning of January 1, 1970, UTC.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public static UTC(d: Date): long--><!--Device-Date-public static UTC(d: Date): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | Date | Yes | to be converted to milliseconds. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## UTC

```TypeScript
public static UTC(year: int): long
```

Returns the number of milliseconds elapsed since the epoch, which is defined as the midnight at the beginning of January 1, 1970, UTC.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public static UTC(year: int): long--><!--Device-Date-public static UTC(year: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| year | int | Yes | to be converted to milliseconds <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## UTC

```TypeScript
public static UTC(year: int, month: int, day?: int, hours?: int, minutes?: int, seconds?: int, ms?: int): long
```

Returns the number of milliseconds elapsed since the epoch, which is defined as the midnight at the beginning of January 1, 1970, UTC.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public static UTC(year: int, month: int, day?: int, hours?: int, minutes?: int, seconds?: int, ms?: int): long--><!--Device-Date-public static UTC(year: int, month: int, day?: int, hours?: int, minutes?: int, seconds?: int, ms?: int): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| year | int | Yes | to be converted to milliseconds <br>The value range is all integers. |
| month | int | Yes | to be converted to milliseconds <br>The value range is all integers. |
| day | int | No | to be converted to milliseconds <br>The value range is all integers. |
| hours | int | No | to be converted to milliseconds <br>The value range is all integers. |
| minutes | int | No | to be converted to milliseconds <br>The value range is all integers. |
| seconds | int | No | to be converted to milliseconds <br>The value range is all integers. |
| ms | int | No | to be converted to milliseconds <br>The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| long | get new date value |

## valueOf

```TypeScript
public valueOf(): long
```

The `valueOf()` method returns the primitive value of a `Date` object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Date-public valueOf(): long--><!--Device-Date-public valueOf(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | return the primitive value of a `Date` object |

