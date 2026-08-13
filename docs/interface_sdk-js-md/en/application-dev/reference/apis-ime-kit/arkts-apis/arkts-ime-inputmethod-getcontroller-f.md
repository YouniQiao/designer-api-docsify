# getController

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## getController

```TypeScript
function getController(): InputMethodController
```

Input method controller

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-inputMethod-function getController(): InputMethodController--><!--Device-inputMethod-function getController(): InputMethodController-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) | the object of InputMethodController. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) | input method controller error. Possible cause: create InputMethodController object failed. |

## Examples

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
```

