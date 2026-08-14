# getSystemInputMethodConfigAbility

## Modules to Import

```TypeScript
import { inputMethod } from 'inputMethod';
```

## getSystemInputMethodConfigAbility

```TypeScript
function getSystemInputMethodConfigAbility(): ElementName
```

Get system input method config ability

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-inputMethod-function getSystemInputMethodConfigAbility(): ElementName--><!--Device-inputMethod-function getSystemInputMethodConfigAbility(): ElementName-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | the information of system input method config ability. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';

let inputMethodConfig: bundleManager.ElementName = inputMethod.getSystemInputMethodConfigAbility();
```

