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

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageProcessor](arkts-image-videoprocessingengine-imageprocessor-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29200003](../errorcode-videoprocessingengine.md#29200003-creation-failure) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-insufficient-memory) |
