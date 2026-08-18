# set24HourClock

## Modules to Import

```TypeScript
```

## set24HourClock

```TypeScript
export function set24HourClock(option: boolean): boolean
```

Sets the 24-hour clock.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-i18n-export function set24HourClock(option: boolean): boolean--><!--Device-i18n-export function set24HourClock(option: boolean): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| option | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

// Set the system time to the 24-hour clock.
let success: boolean = i18n.set24HourClock(true);
```
