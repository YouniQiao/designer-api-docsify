# getSimpleDateTimeFormatByPattern

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## getSimpleDateTimeFormatByPattern

```TypeScript
export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat
```

Obtains a **SimpleDateTimeFormat** object based on the specified pattern string. For details about the difference between the objects obtained by this API and  
[getSimpleDateTimeFormatBySkeleton](arkts-localization-i18n-getsimpledatetimeformatbyskeleton-f.md#getsimpledatetimeformatbyskeleton), see the examples in [SimpleDateTimeFormat.format](arkts-localization-i18n-simpledatetimeformat-c.md#format).

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-i18n-export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat--><!--Device-i18n-export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pattern | string | Yes |
| locale | Intl.Locale | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SimpleDateTimeFormat](arkts-localization-i18n-simpledatetimeformat-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [8900001](../errorcode-i18n.md#8900001-parameter-verification-error) |


## getSimpleDateTimeFormatByPattern

```TypeScript
export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale): SimpleDateTimeFormat
```

Obtains a **SimpleDateTimeFormat** object based on the specified pattern string. For details about the difference between the objects obtained by this API and  
[getSimpleDateTimeFormatBySkeleton](arkts-localization-i18n-getsimpledatetimeformatbyskeleton-f.md#getsimpledatetimeformatbyskeleton), see the examples in [SimpleDateTimeFormat.format](arkts-localization-i18n-simpledatetimeformat-c.md#format).

**Since:** 18

**Deprecated since:** 20

**Substitutes:** [i18n.getSimpleDateTimeFormatByPattern](arkts-localization-i18n-getsimpledatetimeformatbypattern-f.md#getsimpledatetimeformatbypattern)(pattern:

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-i18n-export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale): SimpleDateTimeFormat--><!--Device-i18n-export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale): SimpleDateTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pattern | string | Yes |
| locale | intl.Locale | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SimpleDateTimeFormat](arkts-localization-i18n-simpledatetimeformat-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [890001](../errorcode-i18n.md#890001-parameter-error) |
