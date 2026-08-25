# Date

Date JS API-compatible class

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

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

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(value: long | string | Date)
```

`Date` constructor. NOTE: Dates before `1921-01-01T00:00:00 GMT` can be represented as UTC milliseconds in different ways then TS do.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | long \| string \| Date | Yes |

## constructor

```TypeScript
constructor(year: int, monthIndex: int, day?: int, hours?: int, minutes?: int, seconds?: int, ms?: int)
```

`Date` constructor. NOTE: Dates before `1921-01-01T00:00:00 GMT` can be represented as UTC milliseconds in different ways then TS do.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| year | int | Yes |
| monthIndex | int | Yes |
| day | int | No |
| hours | int | No |
| minutes | int | No |
| seconds | int | No |
| ms | int | No |

## getDate

```TypeScript
public getDate(): int
```

The `getDate()` method returns the day of the month for the specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getDay

```TypeScript
public getDay(): int
```

Returns the day of the week for the specified date according to local time, where 0 represents Sunday.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getFullYear

```TypeScript
public getFullYear(): int
```

Returns the year of the specified date according to local time. For dates between the years 1000 and 9999, `getFullYear()` returns a four-digit number, for example, 1995. Use this function to make sure a year is compliant with years after 2000.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getHours

```TypeScript
public getHours(): int
```

Returns the hour for the specified date, according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getLocalTimezoneOffset

```TypeScript
public static getLocalTimezoneOffset(ms: long): long
```

Gets local time offset.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ms | long | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## getMilliseconds

```TypeScript
public getMilliseconds(): int
```

Returns the milliseconds in the specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getMinutes

```TypeScript
public getMinutes(): int
```

Returns the minutes in the specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getMonth

```TypeScript
public getMonth(): int
```

Returns the month in the specified date according to local time, as a zero-based value (where zero indicates the first month of the year).

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getSeconds

```TypeScript
public getSeconds(): int
```

Returns the seconds in the specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getTime

```TypeScript
public getTime(): long
```

Returns the number of milliseconds since the epoch, which is defined as the midnight at the beginning of January 1, 1970, UTC.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## getTimezoneName

```TypeScript
public static getTimezoneName(ms: long): string
```

Gets time zone name.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ms | long | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## getTimezoneOffset

```TypeScript
public getTimezoneOffset(): long
```

Returns the difference, in minutes, between a date as evaluated in the UTC time zone, and the same date as evaluated in the local time zone.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## getUTCDate

```TypeScript
public getUTCDate(): int
```

Returns the day of the month (from 1 to 31) in the specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getUTCDay

```TypeScript
public getUTCDay(): int
```

Returns the day of the week in the specified date according to universal time, where 0 represents Sunday.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getUTCFullYear

```TypeScript
public getUTCFullYear(): int
```

Returns the year of the specified date according to universal time. For dates between the years 1000 and 9999, `getUTCFullYear()` returns a four-digit number, for example, 1995. Use this function to make sure a year is compliant with years after 2000.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getUTCHours

```TypeScript
public getUTCHours(): int
```

Returns the hours in the specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getUTCMilliseconds

```TypeScript
public getUTCMilliseconds(): int
```

Returns the milliseconds portion of the time object's value according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getUTCMinutes

```TypeScript
public getUTCMinutes(): int
```

Returns the minutes in the specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getUTCMonth

```TypeScript
public getUTCMonth(): int
```

Returns the month of the specified date according to universal time as a zero-based value (where zero indicates the first month of the year).

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getUTCSeconds

```TypeScript
public getUTCSeconds(): int
```

Returns the seconds in the specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getYear

```TypeScript
public getYear(): int
```

Returns the year of the specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## isDateValid

```TypeScript
public isDateValid(): boolean
```

Checks if the constructed date is valid.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## now

```TypeScript
static now(): long
```

The `now()` static method returns the number of milliseconds elapsed since the epoch, which is defined as the midnight at the beginning of January 1, 1970, UTC. which is defined as the midnight at the beginning of January 1, 1970, UTC.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## parse

```TypeScript
static parse(dateStr: string): long
```

Parses a string representation of a date, and returns the number of milliseconds since January 1, 1970, 00:00:00 UTC or throws `RangeError` if the string is unrecognized or, in some cases, contains illegal date values (e.g. 2015-02-31).(YYYY-MM-DDTHH:mm:ss.sssZ) is explicitly specified to be supported. Other formats are implementation-defined and may not work across all browsers (targets). A library can help if many different formats are to be accommodated.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dateStr | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setDate

```TypeScript
public setDate(value: int): long
```

Changes the day of the month of a given Date instance, based on local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setFullYear

```TypeScript
public setFullYear(value: int): long
```

Sets the full year for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setFullYear

```TypeScript
public setFullYear(value: int, month: int): long
```

Sets the full year for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |
| month | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setFullYear

```TypeScript
public setFullYear(value: int, month: int, date: int): long
```

Sets the full year for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |
| month | int | Yes |
| date | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setHours

```TypeScript
public setHours(value: int): long
```

Sets the hours for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setHours

```TypeScript
public setHours(value: int, min: int): long
```

Sets the hours for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |
| min | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setHours

```TypeScript
public setHours(value: int, min: int, sec: int): long
```

Sets the hours for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |
| min | int | Yes |
| sec | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setHours

```TypeScript
public setHours(value: int, min: int, sec: int, ms: int): long
```

Sets the hours for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |
| min | int | Yes |
| sec | int | Yes |
| ms | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setMilliseconds

```TypeScript
public setMilliseconds(value: int): long
```

Sets the milliseconds for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setMinutes

```TypeScript
public setMinutes(value: int): long
```

Sets the minutes for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setMinutes

```TypeScript
public setMinutes(value: int, sec: int): long
```

Sets the minutes for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |
| sec | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setMinutes

```TypeScript
public setMinutes(value: int, sec: int, ms: int): long
```

Sets the minutes for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |
| sec | int | Yes |
| ms | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setMonth

```TypeScript
public setMonth(month: int): long
```

Sets the month for a specified date according to the currently set year.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| month | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setMonth

```TypeScript
public setMonth(month: int, date: int): long
```

Sets the month for a specified date according to the currently set year.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| month | int | Yes |
| date | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setSeconds

```TypeScript
public setSeconds(value: int): long
```

Sets the seconds for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setSeconds

```TypeScript
public setSeconds(value: int, ms: int): long
```

Sets the seconds for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |
| ms | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setTime

```TypeScript
public setTime(value: long): long
```

Sets the number of milliseconds since the epoch, which is defined as the midnight at the beginning of January 1, 1970, UTC.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | long | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setTimezoneOffset

```TypeScript
public setTimezoneOffset(value: int): long
```

Sets the difference, in minutes, between a date as evaluated in the UTC time zone, and the same date as evaluated in the local time zone.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCDate

```TypeScript
public setUTCDate(value: int): long
```

Changes the day of the month of a given Date instance, based on UTC time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCDay

```TypeScript
public setUTCDay(value: int): long
```

Sets the numeric day of the month in the Date object using Universal Coordinated Time (UTC).

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCFullYear

```TypeScript
public setUTCFullYear(value: int): long
```

Sets the full year for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCFullYear

```TypeScript
public setUTCFullYear(value: int, month: int): long
```

Sets the full year for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |
| month | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCFullYear

```TypeScript
public setUTCFullYear(value: int, month: int, date: int): long
```

Sets the full year for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |
| month | int | Yes |
| date | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCHours

```TypeScript
public setUTCHours(value: int): long
```

Sets the hour for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCHours

```TypeScript
public setUTCHours(value: int, min: int): long
```

Sets the hour for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |
| min | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCHours

```TypeScript
public setUTCHours(value: int, min: int, sec: int): long
```

Sets the hour for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |
| min | int | Yes |
| sec | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCHours

```TypeScript
public setUTCHours(value: int, min: int, sec: int, ms: int): long
```

Sets the hour for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |
| min | int | Yes |
| sec | int | Yes |
| ms | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCMilliseconds

```TypeScript
public setUTCMilliseconds(value: int): long
```

Sets the milliseconds for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCMinutes

```TypeScript
public setUTCMinutes(value: int): long
```

Sets the minutes for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCMinutes

```TypeScript
public setUTCMinutes(value: int, sec: int): long
```

Sets the minutes for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |
| sec | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCMinutes

```TypeScript
public setUTCMinutes(value: int, sec: int, ms: int): long
```

Sets the minutes for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |
| sec | int | Yes |
| ms | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCMonth

```TypeScript
public setUTCMonth(month: int): long
```

Sets the month for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| month | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCMonth

```TypeScript
public setUTCMonth(month: int, date: int): long
```

Sets the month for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| month | int | Yes |
| date | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCSeconds

```TypeScript
public setUTCSeconds(value: int): long
```

Sets the seconds for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setUTCSeconds

```TypeScript
public setUTCSeconds(value: int, ms: int): long
```

Sets the seconds for a specified date according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |
| ms | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## setYear

```TypeScript
public setYear(value: int): void
```

Sets the full year for a specified date according to local time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

## toDateString

```TypeScript
public toDateString(): string
```

Returns the date portion of the date in English.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toISOString

```TypeScript
public toISOString(): string
```

Returns a string in ISO 8601 format according to universal time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toJSON

```TypeScript
public toJSON(): string | null
```

Returns a JSON representation of the date.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string \| null |

## toLocaleDateString

```TypeScript
public toLocaleDateString(locales?: Intl.LocalesArgument,
        options?: Intl.DateTimeFormatOptions): string
```

Gets a language-sensitive representation of the date portion.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locales | Intl.LocalesArgument | No |
| options | Intl.DateTimeFormatOptions | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toLocaleString

```TypeScript
public toLocaleString(locales?: Intl.LocalesArgument, options?: object): string
```

Returns a string representing the elements of the array. The elements are converted to Strings using their toLocaleString methods.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locales | Intl.LocalesArgument | No |
| options | object | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toLocaleTimeString

```TypeScript
public toLocaleTimeString(): string
```

Gets a language-sensitive representation of the time portion of the date.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toLocaleTimeString

```TypeScript
public toLocaleTimeString(locales?: Intl.LocalesArgument,
        options?: Intl.DateTimeFormatOptions): string
```

Gets a language-sensitive representation of the time portion of the date.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locales | Intl.LocalesArgument | No |
| options | Intl.DateTimeFormatOptions | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toString

```TypeScript
public toString(): string
```

Returns a string representing the Date object.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toTimeString

```TypeScript
public toTimeString(): string
```

Returns the time portion of the date in English.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## toUTCString

```TypeScript
public toUTCString(): string
```

Returns a string representing the Date object in UTC.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## UTC

```TypeScript
public static UTC(d: Date): long
```

Returns the number of milliseconds elapsed since the epoch, which is defined as the midnight at the beginning of January 1, 1970, UTC.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | Date | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## UTC

```TypeScript
public static UTC(year: int): long
```

Returns the number of milliseconds elapsed since the epoch, which is defined as the midnight at the beginning of January 1, 1970, UTC.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| year | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## UTC

```TypeScript
public static UTC(year: int, month: int, day?: int, hours?: int, minutes?: int, seconds?: int, ms?: int): long
```

Returns the number of milliseconds elapsed since the epoch, which is defined as the midnight at the beginning of January 1, 1970, UTC.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| year | int | Yes |
| month | int | Yes |
| day | int | No |
| hours | int | No |
| minutes | int | No |
| seconds | int | No |
| ms | int | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## valueOf

```TypeScript
public valueOf(): long
```

The `valueOf()` method returns the primitive value of a `Date` object.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |
