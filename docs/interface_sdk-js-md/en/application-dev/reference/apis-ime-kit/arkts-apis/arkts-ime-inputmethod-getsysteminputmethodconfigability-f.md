# getSystemInputMethodConfigAbility

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## getSystemInputMethodConfigAbility

```TypeScript
function getSystemInputMethodConfigAbility(): ElementName
```

Obtains the information about the input method configuration page ability.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

**Examples**

```TypeScript
import { bundleManager } from '@kit.AbilityKit';

let inputMethodConfig: bundleManager.ElementName = inputMethod.getSystemInputMethodConfigAbility();
```
