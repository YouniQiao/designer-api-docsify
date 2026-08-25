# getSystemRegion

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## getSystemRegion

```TypeScript
export function getSystemRegion(): string
```

Obtains the system region.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** [getSystemRegion](arkts-localization-i18n-system-c.md#getsystemregion)

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let systemRegion: string = i18n.System.getSystemRegion(); // If the system region is China, then systemRegion is CN.
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let region: string = i18n.getSystemRegion();
```
