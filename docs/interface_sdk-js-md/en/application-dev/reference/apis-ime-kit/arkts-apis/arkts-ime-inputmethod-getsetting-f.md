# getSetting

## Modules to Import

```TypeScript
import { inputMethod } from 'inputMethod';
```

## getSetting

```TypeScript
function getSetting(): InputMethodSetting
```

Input method setting

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-inputMethod-function getSetting(): InputMethodSetting--><!--Device-inputMethod-function getSetting(): InputMethodSetting-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) | the object of InputMethodSetting. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800007](../errorcode-inputmethod-framework.md#12800007-input-method-setter-error) | input method setter error. Possible cause: create InputMethodSetting object failed. |

## Examples

```TypeScript
let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();
```

