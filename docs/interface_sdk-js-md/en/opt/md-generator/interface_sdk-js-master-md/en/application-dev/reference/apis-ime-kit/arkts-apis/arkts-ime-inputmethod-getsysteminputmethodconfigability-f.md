# getSystemInputMethodConfigAbility

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## getSystemInputMethodConfigAbility

```TypeScript
function getSystemInputMethodConfigAbility(): ElementName
```

Get system input method config ability

**Since:** 11

<!--Device-inputMethod-function getSystemInputMethodConfigAbility(): ElementName--><!--Device-inputMethod-function getSystemInputMethodConfigAbility(): ElementName-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';

let inputMethodConfig: bundleManager.ElementName = inputMethod.getSystemInputMethodConfigAbility();
```
