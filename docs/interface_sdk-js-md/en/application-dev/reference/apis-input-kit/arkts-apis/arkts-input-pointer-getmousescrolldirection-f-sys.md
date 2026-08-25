# getMouseScrollDirection (System API)

## Modules to Import

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## getMouseScrollDirection

```TypeScript
function getMouseScrollDirection(): Promise<boolean>
```

Obtains the scroll direction of the mouse wheel. This API uses a promise to return the result asynchronously.

**Since:** 24

**Required permissions:** ohos.permission.INPUT_DEVICE_CONTROLLER

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3800001](../errorcode-infraredemitter.md#3800001-multimodal-input-service-internal-error) |
