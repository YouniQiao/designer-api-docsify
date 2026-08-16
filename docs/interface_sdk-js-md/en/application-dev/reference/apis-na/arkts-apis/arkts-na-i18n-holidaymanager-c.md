# HolidayManager

Provide some functions to manage holidays in a country or region. Partly follows the RFC2445 standard.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-i18n-export class HolidayManager--><!--Device-i18n-export class HolidayManager-End-->

**System capability:** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor(icsPath: String)
```

Creates a HolidayManager object for parsing holiday data.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HolidayManager-constructor(icsPath: String)--><!--Device-HolidayManager-constructor(icsPath: String)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icsPath | String | Yes | Path of the .ics file with the read permission granted for applications. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## getHolidayInfoItemArray

```TypeScript
getHolidayInfoItemArray(year?: int): Array<HolidayInfoItem>
```

Obtains the holiday information list of the specified year.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HolidayManager-getHolidayInfoItemArray(year?: int): Array<HolidayInfoItem>--><!--Device-HolidayManager-getHolidayInfoItemArray(year?: int): Array<HolidayInfoItem>-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| year | int | No | <br>The value should be an integer. - Specified year, for example, 2023.<br>The default value is the current year. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[HolidayInfoItem](arkts-na-i18n-holidayinfoitem-i.md)&gt; | Holiday information list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## isHoliday

```TypeScript
isHoliday(date?: Date): boolean
```

Determines whether the specified date is a holiday.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HolidayManager-isHoliday(date?: Date): boolean--><!--Device-HolidayManager-isHoliday(date?: Date): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | No | Date and time. Note: The month starts from 0. For example, 0 indicates January. The default value is the current date. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the specified date is a holiday, and false otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

