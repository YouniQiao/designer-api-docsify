# getController

## getController

```TypeScript
function getController(): InputMethodController
```

Input method controller

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-inputMethod-function getController(): InputMethodController--><!--Device-inputMethod-function getController(): InputMethodController-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the object of InputMethodController. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) | input method controller error. Possible cause: create InputMethodController object failed. |

**Example**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
```

