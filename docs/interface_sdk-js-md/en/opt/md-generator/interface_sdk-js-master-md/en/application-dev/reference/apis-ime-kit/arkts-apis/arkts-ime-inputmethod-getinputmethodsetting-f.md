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

**Substitutes:** [getSetting](arkts-ime-inputmethod-getsetting-f.md#getSetting)

<!--Device-inputMethod-function getInputMethodSetting(): InputMethodSetting--><!--Device-inputMethod-function getInputMethodSetting(): InputMethodSetting-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) |

## Examples

```TypeScript
let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getInputMethodSetting();
```
