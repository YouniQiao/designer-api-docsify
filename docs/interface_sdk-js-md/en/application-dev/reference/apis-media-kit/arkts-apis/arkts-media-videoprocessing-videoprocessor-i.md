# VideoProcessor

Provides the VideoProcessor type, including AIHDR related functions.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-videoProcessing-interface VideoProcessor--><!--Device-videoProcessing-interface VideoProcessor-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

## Modules to Import

```TypeScript
import { videoProcessing } from 'kits/@kit.MediaKit';
```

## getStatus

```TypeScript
getStatus(): Promise<VideoProcessorStatus | undefined>
```

Gets the current status of video processor features.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoProcessor-getStatus(): Promise<VideoProcessorStatus | undefined>--><!--Device-VideoProcessor-getStatus(): Promise<VideoProcessorStatus | undefined>-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;VideoProcessorStatus \| undefined&gt; | Promise used to return VideoProcessorStatus or undefined. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |

## offStatusChange

```TypeScript
offStatusChange(callback?: VideoProcessorStatusCallback): void
```

Unregisters a listener for video processor status changes.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoProcessor-offStatusChange(callback?: VideoProcessorStatusCallback): void--><!--Device-VideoProcessor-offStatusChange(callback?: VideoProcessorStatusCallback): void-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VideoProcessorStatusCallback](arkts-media-videoprocessing-videoprocessorstatuscallback-t.md) | No | The callback function to remove. If not provided, all callbacks for this event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [29200009](../../apis-image-kit/errorcode-videoprocessingengine.md#29200009-invalid-value) | Input value is invalid. |
| [29200006](../../apis-image-kit/errorcode-videoprocessingengine.md#29200006-operation-not-allowed) | The operation is not permitted. This may be caused by incorrect status. |

## onStatusChange

```TypeScript
onStatusChange(callback: VideoProcessorStatusCallback): void
```

Registers a listener for video processor status changes.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoProcessor-onStatusChange(callback: VideoProcessorStatusCallback): void--><!--Device-VideoProcessor-onStatusChange(callback: VideoProcessorStatusCallback): void-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VideoProcessorStatusCallback](arkts-media-videoprocessing-videoprocessorstatuscallback-t.md) | Yes | The callback function to invoke when status changes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [29200009](../../apis-image-kit/errorcode-videoprocessingengine.md#29200009-invalid-value) | Input value is invalid. |
| [29200007](../../apis-image-kit/errorcode-videoprocessingengine.md#29200007-insufficient-memory) | Out of memory. |

