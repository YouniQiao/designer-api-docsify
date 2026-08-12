# getCalendar

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## getCalendar

```TypeScript
export function getCalendar(locale: string, type?: string): Calendar
```

Obtains the **Calendar** object for the specified locale and calendar type.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-i18n-export function getCalendar(locale: string, type?: string): Calendar--><!--Device-i18n-export function getCalendar(locale: string, type?: string): Calendar-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locale | string | Yes |
| type | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Calendar](arkts-localization-i18n-calendar-c.md) |
