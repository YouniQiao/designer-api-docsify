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

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-videoProcessingEngine-function create(): ImageProcessor--><!--Device-videoProcessingEngine-function create(): ImageProcessor-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageProcessor](arkts-image-videoprocessingengine-imageprocessor-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-insufficient-memory) |
| [29200003](../errorcode-videoprocessingengine.md#29200003-creation-failure) |

## Examples

```TypeScript
import { videoProcessingEngine } from '@kit.ImageKit';

async function create() {
  videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
}
```
