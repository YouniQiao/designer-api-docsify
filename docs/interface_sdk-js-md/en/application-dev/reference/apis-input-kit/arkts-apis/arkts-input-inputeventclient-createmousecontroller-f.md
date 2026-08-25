# createMouseController

## Modules to Import

```TypeScript
import { inputEventClient } from 'kits/@kit.InputKit';
```

## createMouseController

```TypeScript
function createMouseController(): Promise<MouseController>
```

Creates a mouse controller for simulating mouse operations. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[MouseController](arkts-input-inputeventclient-mousecontroller-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3800001](../errorcode-infraredemitter.md#3800001-multimodal-input-service-internal-error) |
