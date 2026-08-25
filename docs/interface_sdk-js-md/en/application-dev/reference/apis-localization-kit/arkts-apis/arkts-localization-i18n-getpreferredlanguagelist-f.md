# getPreferredLanguageList

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## getPreferredLanguageList

```TypeScript
export function getPreferredLanguageList(): Array<string>
```

Obtains the list of preferred languages.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Deprecated since:** 9

**Substitutes:** [getPreferredLanguageList](arkts-localization-i18n-system-c.md#getpreferredlanguagelist)

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let preferredLanguageList: Array<string> = i18n.System.getPreferredLanguageList();
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let preferredLanguageList: Array<string> = i18n.getPreferredLanguageList();
```
