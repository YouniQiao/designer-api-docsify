# getCurrentInputMethod

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
import { inputMethodEngine } from '@kit.IMEKit';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKit';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';
import { InputMethodExtraConfig } from '@kit.IMEKit';
import { inputMethodSystemPanelManager } from '@kit.IMEKit';
```

## getCurrentInputMethod

```TypeScript
function getCurrentInputMethod(): InputMethodProperty
```

Get current input method

**Since:** 23

<!--Device-inputMethod-function getCurrentInputMethod(): InputMethodProperty--><!--Device-inputMethod-function getCurrentInputMethod(): InputMethodProperty-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | the property of current inputmethod. |

**Examples**

```TypeScript
let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
```

