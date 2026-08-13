# getSetting

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## getSetting

```TypeScript
function getSetting(): InputMethodSetting
```

Input method setting

**Since:** 23

**Deprecated since:** -1

<!--Device-inputMethod-function getSetting(): InputMethodSetting--><!--Device-inputMethod-function getSetting(): InputMethodSetting-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [12800007](../errorcode-inputmethod-framework.md#12800007-input-method-setter-error) |

## Examples

```TypeScript
let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();
```
