# getCurrentInputMethod

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## getCurrentInputMethod

```TypeScript
function getCurrentInputMethod(): InputMethodProperty
```

Get current input method

**Since:** 23

**Deprecated since:** -1

<!--Device-inputMethod-function getCurrentInputMethod(): InputMethodProperty--><!--Device-inputMethod-function getCurrentInputMethod(): InputMethodProperty-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) |

## Examples

```TypeScript
let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
```
