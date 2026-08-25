# createVideoProcessor

## Modules to Import

```TypeScript
import { videoProcessing } from 'kits/@kit.MediaKit';
```

## createVideoProcessor

```TypeScript
function createVideoProcessor(): VideoProcessor
```

Create a video processing instance.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VideoProcessor](arkts-media-videoprocessing-videoprocessor-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29200003](../../apis-image-kit/errorcode-videoprocessingengine.md#29200003-creation-failure) |
| [29200007](../../apis-image-kit/errorcode-videoprocessingengine.md#29200007-insufficient-memory) |
