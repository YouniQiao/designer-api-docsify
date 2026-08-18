# initializeEnvironment

## Modules to Import

```TypeScript
```

## initializeEnvironment

```TypeScript
function initializeEnvironment(): Promise<void>
```

Initialize global environment for image processing.

**Since:** 23

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-videoProcessingEngine-function initializeEnvironment(): Promise<void>--><!--Device-videoProcessingEngine-function initializeEnvironment(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-insufficient-memory) |
| [29200006](../errorcode-videoprocessingengine.md#29200006-operation-not-allowed) |
| [29200002](../errorcode-videoprocessingengine.md#29200002-initialization-failure) |

**Examples**

```TypeScript
import { videoProcessingEngine } from '@kit.ImageKit';

async function initializeEnvironment() {
  videoProcessingEngine.initializeEnvironment();
}
```
