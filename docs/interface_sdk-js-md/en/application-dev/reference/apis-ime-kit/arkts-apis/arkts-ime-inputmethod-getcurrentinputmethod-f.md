# getCurrentInputMethod

## Modules to Import

```TypeScript
import { inputMethod } from 'inputMethod';
```

## getCurrentInputMethod

```TypeScript
function getCurrentInputMethod(): InputMethodProperty
```

Get current input method

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-inputMethod-function getCurrentInputMethod(): InputMethodProperty--><!--Device-inputMethod-function getCurrentInputMethod(): InputMethodProperty-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | the property of current inputmethod. |

## Examples

```TypeScript
let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
```

