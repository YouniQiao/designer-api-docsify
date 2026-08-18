# getSystemLocale

## Modules to Import

```TypeScript
```

## getSystemLocale

```TypeScript
export function getSystemLocale(): string
```

Obtains the system locale.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getSystemLocale](arkts-localization-i18n-system-c.md#getsystemlocale)

<!--Device-i18n-export function getSystemLocale(): string--><!--Device-i18n-export function getSystemLocale(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let locale: string = i18n.getSystemLocale();
```
