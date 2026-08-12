# createKeyboardController

## Modules to Import

```TypeScript
import { inputEventClient } from '@kit.InputKit';
```

## createKeyboardController

```TypeScript
function createKeyboardController(): Promise<KeyboardController>
```

Creates a keyboard controller for simulating key operations. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [3800001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-input-kit/errorcode-infraredemitter.md#3800001-multimodal-input-service-internal-error) | Input service exception. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |

