# create

## Modules to Import

```TypeScript
import { videoProcessingEngine } from 'videoProcessingEngine';
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

| Type | Description |
| --- | --- |
| [ImageProcessor](arkts-image-videoprocessingengine-imageprocessor-i.md) | Returns the ImageProcessor instance if <br>the operation is successful; returns null otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Function create can not work correctly due to limited <br>device capabilities. |
| [29200007](../errorcode-videoprocessingengine.md#29200007-insufficient-memory) | Out of memory. |
| [29200003](../errorcode-videoprocessingengine.md#29200003-creation-failure) | Failed to create image processing instance. For example, <br>the number of instances exceeds the upper limit. |

**Examples**

```TypeScript
import { videoProcessingEngine } from '@kit.ImageKit';

async function create() {
  videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
}
```

