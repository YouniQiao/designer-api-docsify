# getController

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## getController

```TypeScript
function getController(): InputMethodController
```

Obtains an [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) instance.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

**Examples**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
```
