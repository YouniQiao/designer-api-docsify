# getInputMethodController

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## getInputMethodController

```TypeScript
function getInputMethodController(): InputMethodController
```

Input method controller

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [inputMethod#getController](arkts-ime-inputmethod-getcontroller-f.md#getcontroller)

<!--Device-inputMethod-function getInputMethodController(): InputMethodController--><!--Device-inputMethod-function getInputMethodController(): InputMethodController-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) | the object of InputMethodController. |

## Examples

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getInputMethodController();
```

