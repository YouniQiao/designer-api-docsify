# getTimeZone

## Modules to Import

```TypeScript
```

## getTimeZone

```TypeScript
export function getTimeZone(zoneID?: string): TimeZone
```

Obtains the **TimeZone** object corresponding to the specified time zone ID.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-i18n-export function getTimeZone(zoneID?: string): TimeZone--><!--Device-i18n-export function getTimeZone(zoneID?: string): TimeZone-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| zoneID | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TimeZone](arkts-localization-i18n-timezone-c.md) |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.getTimeZone('Asia/Shanghai');
```
