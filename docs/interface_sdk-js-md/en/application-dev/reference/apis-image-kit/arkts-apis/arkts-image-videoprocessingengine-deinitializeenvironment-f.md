# deinitializeEnvironment

## Modules to Import

```TypeScript
import { videoProcessingEngine } from 'videoProcessingEngine';
```

## deinitializeEnvironment

```TypeScript
function deinitializeEnvironment(): Promise<void>
```

Deinitialize global environment for image processing.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-videoProcessingEngine-function deinitializeEnvironment(): Promise<void>--><!--Device-videoProcessingEngine-function deinitializeEnvironment(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise instance used to return the operation result. If the operation fails, an error message is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [29200006](../errorcode-videoprocessingengine.md#29200006-operation-not-allowed) | The operation is not permitted. This may be caused by incorrect status. |

## Examples

```TypeScript
import { videoProcessingEngine } from '@kit.ImageKit';

async function deinitializeEnvironment() {
  videoProcessingEngine.initializeEnvironment();
  videoProcessingEngine.deinitializeEnvironment();
}
```

