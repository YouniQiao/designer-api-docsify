# is24HourClock

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## is24HourClock

```TypeScript
export function is24HourClock(): boolean
```

Checks whether the 24-hour clock is used.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** [is24HourClock](arkts-localization-i18n-system-c.md#is24hourclock)

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let is24HourClock: boolean = i18n.System.is24HourClock(); // If the 24-hour clock is used, then is24HourClock is true.
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let is24HourClock: boolean = i18n.is24HourClock();
```
