# getInputMethodSetting

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## getInputMethodSetting

```TypeScript
function getInputMethodSetting(): InputMethodSetting
```

Input method setting

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getSetting](arkts-ime-getsetting-f.md#getsetting-1)

<!--Device-inputMethod-function getInputMethodSetting(): InputMethodSetting--><!--Device-inputMethod-function getInputMethodSetting(): InputMethodSetting-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodSetting](arkts-ime-inputmethodsetting-i.md) | the object of InputMethodSetting |

**Example**

```TypeScript
let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getInputMethodSetting();

```

