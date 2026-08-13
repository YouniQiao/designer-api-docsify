# AVRecorder

AVRecorder is a class for audio and video recording management. It provides APIs to record media assets. Before calling any API in AVRecorder, you must use [createAVRecorder()](arkts-media-media-createavrecorder-f.md#createAVRecorder) to create an AVRecorder instance. For details about the audio and video recording demo, see [Audio Recording](../../../media/media/using-avrecorder-for-recording.md) and [Video Recording](../../../media/media/video-recording.md). > **NOTE：**> > > To use the camera to record videos, the camera module is required. For details about how to use the APIs > provided by the camera module, see [Camera Management](../../apis-camera-kit/arkts-apis/arkts-multimedia-camera.md#@ohos.multimedia.camera).

**Since:** 23

**Deprecated since:** -1

<!--Device-media-interface AVRecorder--><!--Device-media-interface AVRecorder-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## getInputMetaSurface

```TypeScript
getInputMetaSurface(type: MetaSourceType): Promise<string>
```

Get input meta surface for specified meta source type. it must be called between prepare completed and start.

**Since:** 12

**Deprecated since:** -1

<!--Device-AVRecorder-getInputMetaSurface(type: MetaSourceType): Promise<string>--><!--Device-AVRecorder-getInputMetaSurface(type: MetaSourceType): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [MetaSourceType](arkts-media-media-metasourcetype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getInputMetaSurface

```TypeScript
getInputMetaSurface(type: MetaSourceType): Promise<string | undefined>
```

Get input meta surface for specified meta source type. it must be called between prepare completed and start.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-getInputMetaSurface(type: MetaSourceType): Promise<string | undefined>--><!--Device-AVRecorder-getInputMetaSurface(type: MetaSourceType): Promise<string | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [MetaSourceType](arkts-media-media-metasourcetype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string \ | undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## isWatermarkSupported

```TypeScript
isWatermarkSupported(): Promise<boolean>
```

Checks whether the device supports the hardware digital watermark. This API uses a promise to return the result. This API can be called after the prepare(), start(), or paused() event is triggered.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-isWatermarkSupported(): Promise<boolean>--><!--Device-AVRecorder-isWatermarkSupported(): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.isWatermarkSupported().then((isWatermarkSupported: boolean) => {
  console.info(`Succeeded in get, isWatermarkSupported: ${isWatermarkSupported}`);
}).catch((error: BusinessError) => {
  console.error(`Failed to get and catch error is ${error.message}`);
});
```

## setMetadata

```TypeScript
setMetadata(metadata: Record<string, string>): void
```

Set metadata (key-value pairs) for the recording file of the recorder. This metadata overwrites the value in config.metadata.customInfo (see {prepare()} and {AVRecorderConfig}) if they have same key. This API can be called only after the prepare() event is successfully triggered and before the stop() API is called.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-setMetadata(metadata: Record<string, string>): void--><!--Device-AVRecorder-setMetadata(metadata: Record<string, string>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| metadata | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400108](../errorcode-media.md#5400108-parameter-value-out-of-range) |

## setWatermark

```TypeScript
setWatermark(watermark: image.PixelMap, config: WatermarkConfig): Promise<void>
```

Sets a watermark for the AVRecorder. This API uses a promise to return the result. This API can be called only after the prepare() event is triggered and before the start() event is triggered.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-setWatermark(watermark: image.PixelMap, config: WatermarkConfig): Promise<void>--><!--Device-AVRecorder-setWatermark(watermark: image.PixelMap, config: WatermarkConfig): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| watermark | image.PixelMap | Yes |
| config | [WatermarkConfig](arkts-media-media-watermarkconfig-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

let watermark: image.PixelMap|undefined = undefined; // need data.
let watermarkConfig: media.WatermarkConfig = { top: 100, left: 100 }

avRecorder.setWatermark(watermark, watermarkConfig).then(() => {
  console.info('Succeeded in setWatermark');
}).catch((error: BusinessError) => {
  console.error(`Failed to setWatermark and catch error is ${error.message}`);
});
```
