# getSimpleDateTimeFormatBySkeleton

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## getSimpleDateTimeFormatBySkeleton

```TypeScript
export function getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: Intl.Locale): SimpleDateTimeFormat
```

Obtains a **SimpleDateTimeFormat** object based on the specified skeleton. For details about the difference between the objects obtained by this API and  
[getSimpleDateTimeFormatByPattern](arkts-localization-i18n-getsimpledatetimeformatbypattern-f.md#getSimpleDateTimeFormatByPattern), see the examples in [SimpleDateTimeFormat.format](arkts-localization-i18n-simpledatetimeformat-c.md#format).

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-i18n-export function getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: Intl.Locale): SimpleDateTimeFormat--><!--Device-i18n-export function getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: Intl.Locale): SimpleDateTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| skeleton | string | Yes |
| locale | Intl.Locale | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SimpleDateTimeFormat](arkts-localization-i18n-simpledatetimeformat-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [8900001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-localization-kit/errorcode-i18n.md#8900001-parameter-verification-error) |


## getSimpleDateTimeFormatBySkeleton

```TypeScript
export function getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleDateTimeFormat
```

Obtains a **SimpleDateTimeFormat** object based on the specified skeleton. For details about the difference between the objects obtained by this API and  
[getSimpleDateTimeFormatByPattern](arkts-localization-i18n-getsimpledatetimeformatbypattern-f.md#getSimpleDateTimeFormatByPattern-1), see the examples in [SimpleDateTimeFormat.format](arkts-localization-i18n-simpledatetimeformat-c.md#format).

**Since:** 18

**Deprecated since:** 20

**Substitutes:** [getSimpleDateTimeFormatBySkeleton](i18n.getSimpleDateTimeFormatBySkeleton(skeleton:)

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-i18n-export function getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleDateTimeFormat--><!--Device-i18n-export function getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleDateTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| skeleton | string | Yes |
| locale | intl.Locale | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SimpleDateTimeFormat](arkts-localization-i18n-simpledatetimeformat-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [890001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-localization-kit/errorcode-i18n.md#890001-parameter-error) |
