# VideoProcessor

Provides the VideoProcessor type, including AIHDR related functions.

**Since:** 26.0.0

<!--Device-videoProcessing-interface VideoProcessor--><!--Device-videoProcessing-interface VideoProcessor-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

## Modules to Import

```TypeScript
import { videoProcessing } from '@kit.MediaKit';
```

## getStatus

```TypeScript
getStatus(): Promise<VideoProcessorStatus | undefined>
```

Gets the current status of video processor features.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoProcessor-getStatus(): Promise<VideoProcessorStatus | undefined>--><!--Device-VideoProcessor-getStatus(): Promise<VideoProcessorStatus | undefined>-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[VideoProcessorStatus](arkts-media-videoprocessing-videoprocessorstatus-i.md) \| undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

## offStatusChange

```TypeScript
offStatusChange(callback?: VideoProcessorStatusCallback): void
```

Unregisters a listener for video processor status changes.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoProcessor-offStatusChange(callback?: VideoProcessorStatusCallback): void--><!--Device-VideoProcessor-offStatusChange(callback?: VideoProcessorStatusCallback): void-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [VideoProcessorStatusCallback](arkts-media-videoprocessing-videoprocessorstatuscallback-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [29200009](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-image-kit/errorcode-videoprocessingengine.md#29200009-invalid-value) |
| [29200006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-image-kit/errorcode-videoprocessingengine.md#29200006-operation-not-allowed) |

## onStatusChange

```TypeScript
onStatusChange(callback: VideoProcessorStatusCallback): void
```

Registers a listener for video processor status changes.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoProcessor-onStatusChange(callback: VideoProcessorStatusCallback): void--><!--Device-VideoProcessor-onStatusChange(callback: VideoProcessorStatusCallback): void-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [VideoProcessorStatusCallback](arkts-media-videoprocessing-videoprocessorstatuscallback-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [29200009](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-image-kit/errorcode-videoprocessingengine.md#29200009-invalid-value) |
| [29200007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-image-kit/errorcode-videoprocessingengine.md#29200007-insufficient-memory) |
