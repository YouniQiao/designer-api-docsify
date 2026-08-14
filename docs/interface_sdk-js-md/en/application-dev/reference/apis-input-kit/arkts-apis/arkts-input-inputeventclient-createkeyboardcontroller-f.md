# createKeyboardController

## Modules to Import

```TypeScript
import { inputEventClient } from 'inputEventClient';
```

## createKeyboardController

```TypeScript
function createKeyboardController(): Promise<KeyboardController>
```

Creates a keyboard controller for simulating key operations. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputEventClient-function createKeyboardController(): Promise<KeyboardController>--><!--Device-inputEventClient-function createKeyboardController(): Promise<KeyboardController>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;KeyboardController&gt; | Promise used to return the keyboard controller instance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3800001](../errorcode-infraredemitter.md#3800001-multimodal-input-service-internal-error) | Input service exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |

