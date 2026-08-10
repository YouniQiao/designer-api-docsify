# create

## Modules to Import

```TypeScript
import { videoProcessingEngine } from 'kits/@kit.ImageKit';
```

## create

```TypeScript
function create(): ImageProcessor
```

Create an image processing instance.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-videoProcessingEngine-function create(): ImageProcessor--><!--Device-videoProcessingEngine-function create(): ImageProcessor-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Return value:**

| Type | Description |
| --- | --- |
| [ImageProcessor](arkts-image-videoprocessingengine-imageprocessor-i.md) | Returns the ImageProcessor instance if &lt;br&gt;the operation is successful; returns null otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Function create can not work correctly due to limited &lt;br&gt;device capabilities. |
| 29200007 | Out of memory. |
| 29200003 | Failed to create image processing instance. For example, &lt;br&gt;the number of instances exceeds the upper limit. |

## Examples

```TypeScript
import { videoProcessingEngine } from '@kit.ImageKit';

async function create() {
  videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
}
```

