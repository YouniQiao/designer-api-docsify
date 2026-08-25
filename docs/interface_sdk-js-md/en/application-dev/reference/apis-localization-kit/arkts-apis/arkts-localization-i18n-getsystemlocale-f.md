# getSystemLocale

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## getSystemLocale

```TypeScript
export function getSystemLocale(): string
```

Obtains the system locale.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** [getSystemLocale](arkts-localization-i18n-system-c.md#getsystemlocale)

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let systemLocale: string = i18n.System.getSystemLocale(); // If the system language is simplified Chinese and the system region is China, then systemLocale is zh-Hans-CN.
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let locale: string = i18n.getSystemLocale();
```
