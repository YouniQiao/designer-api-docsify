# createVideoProcessor

## createVideoProcessor

```TypeScript
function createVideoProcessor(): VideoProcessor
```

Create a video processing instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-videoProcessing-function createVideoProcessor(): VideoProcessor--><!--Device-videoProcessing-function createVideoProcessor(): VideoProcessor-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Returns the VideoProcessor instance if the operation is successful; returns null otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Function createVideoProcessor can not work correctly due to limited device capabilities. |
| [29200003](../../apis-image-kit/errorcode-videoprocessingengine.md#29200003-creation-failure) | Failed to create video processing instance. For example, the number of instances exceeds the upper limit. |
| [29200007](../../apis-image-kit/errorcode-videoprocessingengine.md#29200007-insufficient-memory) | Out of memory. |

