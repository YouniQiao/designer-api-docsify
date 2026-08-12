# getController

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## getController

```TypeScript
function getController(): InputMethodController
```

Input method controller

**Since:** 9

<!--Device-inputMethod-function getController(): InputMethodController--><!--Device-inputMethod-function getController(): InputMethodController-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [12800006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## Examples

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
```
