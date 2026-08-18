# getInputMethodController

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
import { inputMethodEngine } from '@kit.IMEKit';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKit';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';
import { InputMethodExtraConfig } from '@kit.IMEKit';
import { inputMethodSystemPanelManager } from '@kit.IMEKit';
```

## getInputMethodController

```TypeScript
function getInputMethodController(): InputMethodController
```

Input method controller

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getController](arkts-ime-inputmethod-getcontroller-f.md)

<!--Device-inputMethod-function getInputMethodController(): InputMethodController--><!--Device-inputMethod-function getInputMethodController(): InputMethodController-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) | the object of InputMethodController. |

**Examples**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getInputMethodController();
```

