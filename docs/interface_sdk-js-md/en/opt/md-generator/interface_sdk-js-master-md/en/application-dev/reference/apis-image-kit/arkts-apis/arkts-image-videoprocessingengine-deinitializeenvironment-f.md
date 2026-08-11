# deinitializeEnvironment

## Modules to Import

```TypeScript
import { videoProcessingEngine } from 'kits/@kit.ImageKit';
```

## deinitializeEnvironment

```TypeScript
function deinitializeEnvironment(): Promise<void>
```

Deinitialize global environment for image processing.

**Since:** 18

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-videoProcessingEngine-function deinitializeEnvironment(): Promise<void>--><!--Device-videoProcessingEngine-function deinitializeEnvironment(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [29200006](../errorcode-videoprocessingengine.md#29200006-operation-not-allowed) |

## Examples

```TypeScript
import { videoProcessingEngine } from '@kit.ImageKit';

async function deinitializeEnvironment() {
  videoProcessingEngine.initializeEnvironment();
  videoProcessingEngine.deinitializeEnvironment();
}
```
