# getSimpleDateTimeFormatByPattern

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## getSimpleDateTimeFormatByPattern

```TypeScript
export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat
```

Obtains a **SimpleDateTimeFormat** object based on the specified pattern string. For details about the difference between the objects obtained by this API and [getSimpleDateTimeFormatBySkeleton](../../apis-na/arkts-apis/arkts-na-i18n-getsimpledatetimeformatbyskeleton-f.md#getSimpleDateTimeFormatBySkeleton) , see the examples in [SimpleDateTimeFormat.format](../../apis-na/arkts-apis/arkts-na-i18n-simpledatetimeformat-c.md#format).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-i18n-export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat--><!--Device-i18n-export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pattern | string | Yes | Valid pattern, which supports free combinations of field patterns in [Date Field Symbol Table](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table). This parameter also supports custom text enclosed in single quotation marks (`''`). |
| locale | Intl.Locale | No | Locale** object. The default value is the current system locale. |

**Return value:**

| Type | Description |
| --- | --- |
| [SimpleDateTimeFormat](../../apis-na/arkts-apis/arkts-na-i18n-simpledatetimeformat-c.md) | SimpleDateTimeFormat** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8900001](../errorcode-i18n.md#8900001-parameter-verification-error) | Invalid parameter. Possible causes: Parameter verification failed. |


## getSimpleDateTimeFormatByPattern

```TypeScript
export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale): SimpleDateTimeFormat
```

Obtains a **SimpleDateTimeFormat** object based on the specified pattern string. For details about the difference between the objects obtained by this API and [getSimpleDateTimeFormatBySkeleton](../../apis-na/arkts-apis/arkts-na-i18n-getsimpledatetimeformatbyskeleton-f.md#getSimpleDateTimeFormatBySkeleton) , see the examples in [SimpleDateTimeFormat.format](../../apis-na/arkts-apis/arkts-na-i18n-simpledatetimeformat-c.md#format).

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** 20

**Substitutes:** [getSimpleDateTimeFormatByPattern](../../apis-na/arkts-apis/arkts-na-i18n-getsimpledatetimeformatbypattern-f.md#getSimpleDateTimeFormatByPattern)(pattern: string, locale?: Intl.Locale)

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-i18n-export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale): SimpleDateTimeFormat--><!--Device-i18n-export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale): SimpleDateTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pattern | string | Yes | Valid pattern, which supports free combinations of field patterns in [Date Field Symbol Table](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table). This parameter also supports custom text enclosed in single quotation marks (`''`). |
| locale | intl.Locale | No | Locale** object. The default value is the current system locale. |

**Return value:**

| Type | Description |
| --- | --- |
| [SimpleDateTimeFormat](../../apis-na/arkts-apis/arkts-na-i18n-simpledatetimeformat-c.md) | SimpleDateTimeFormat** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [890001](../errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

