# getFirstPreferredLanguage

## Modules to Import

```TypeScript
```

## getFirstPreferredLanguage

```TypeScript
export function getFirstPreferredLanguage(): string
```

Obtains the first language in the preferred language list.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getFirstPreferredLanguage](arkts-localization-i18n-system-c.md#getfirstpreferredlanguage)

<!--Device-i18n-export function getFirstPreferredLanguage(): string--><!--Device-i18n-export function getFirstPreferredLanguage(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let firstPreferredLanguage: string = i18n.getFirstPreferredLanguage();
```
