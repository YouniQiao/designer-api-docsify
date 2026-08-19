# getSimpleDateTimeFormatByPattern

## Modules to Import

```TypeScript
```

## getSimpleDateTimeFormatByPattern

```TypeScript
export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat
```

Obtains a SimpleDateTimeFormat object based on the specified pattern string. For details about the display differences between the objects obtained by this API and getSimpleDateTimeFormatBySkeleton, see SimpleDateTimeFormat.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-i18n-export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat--><!--Device-i18n-export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pattern | string | Yes | Valid pattern. For details about the supported characters and their meanings, see [Date Field Symbol Table](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table). This parameter also supports custom text enclosed in single quotation marks (''). |
| locale | Intl.Locale | No | Locale object. The default value is the current system locale. |

**Return value:**

| Type | Description |
| --- | --- |
| [SimpleDateTimeFormat](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-simpledatetimeformat-c.md) | SimpleDateTimeFormat object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8900001](../../apis-localization-kit/errorcode-i18n.md#8900001-parameter-verification-error) | Invalid parameter. Possible causes: Parameter verification failed. |

