# create

## Modules to Import

```TypeScript
```

## create

```TypeScript
function create(): ImageProcessor
```

Create an image processing instance.

**Since:** 23

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-videoProcessingEngine-function create(): ImageProcessor--><!--Device-videoProcessingEngine-function create(): ImageProcessor-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageProcessor](arkts-image-videoprocessingengine-imageprocessor-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-insufficient-memory) |
| [29200003](../errorcode-videoprocessingengine.md#29200003-creation-failure) |

**Examples**

```TypeScript
import { videoProcessingEngine } from '@kit.ImageKit';

async function create() {
  videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
}
```
