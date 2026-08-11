# getDefaultInputMethod

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## getDefaultInputMethod

```TypeScript
function getDefaultInputMethod(): InputMethodProperty
```

Get default input method

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-inputMethod-function getDefaultInputMethod(): InputMethodProperty--><!--Device-inputMethod-function getDefaultInputMethod(): InputMethodProperty-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | property of the default input method. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
let defaultIme: inputMethod.InputMethodProperty = inputMethod.getDefaultInputMethod();
```

