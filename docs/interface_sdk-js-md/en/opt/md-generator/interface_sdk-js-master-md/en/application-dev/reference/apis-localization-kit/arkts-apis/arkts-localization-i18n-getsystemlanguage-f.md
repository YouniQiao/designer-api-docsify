# getSystemLanguage

## Modules to Import

```TypeScript
```

## getSystemLanguage

```TypeScript
export function getSystemLanguage(): string
```

Obtains the system language.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getSystemLanguage](arkts-localization-i18n-system-c.md#getsystemlanguage)

<!--Device-i18n-export function getSystemLanguage(): string--><!--Device-i18n-export function getSystemLanguage(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let systemLanguage: string = i18n.getSystemLanguage();
```
