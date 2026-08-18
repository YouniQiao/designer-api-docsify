# getSystemRegion

## Modules to Import

```TypeScript
```

## getSystemRegion

```TypeScript
export function getSystemRegion(): string
```

Obtains the system region.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getSystemRegion](arkts-localization-i18n-system-c.md#getsystemregion)

<!--Device-i18n-export function getSystemRegion(): string--><!--Device-i18n-export function getSystemRegion(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let region: string = i18n.getSystemRegion();
```
