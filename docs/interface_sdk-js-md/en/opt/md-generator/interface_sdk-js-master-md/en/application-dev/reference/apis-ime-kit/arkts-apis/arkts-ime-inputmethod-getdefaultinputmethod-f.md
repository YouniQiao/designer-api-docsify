# getDefaultInputMethod

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## getDefaultInputMethod

```TypeScript
function getDefaultInputMethod(): InputMethodProperty
```

Get default input method

**Since:** 23

**Deprecated since:** -1

<!--Device-inputMethod-function getDefaultInputMethod(): InputMethodProperty--><!--Device-inputMethod-function getDefaultInputMethod(): InputMethodProperty-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## Examples

```TypeScript
let defaultIme: inputMethod.InputMethodProperty = inputMethod.getDefaultInputMethod();
```
