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

## addWatermark

```TypeScript
addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<number>
```

add a watermark for the AVRecorder. This API uses a promise to return the result. App can add up to 5 watermarks. This API can be called only before the prepared state.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVRecorder-addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<int>--><!--Device-AVRecorder-addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| watermark | image.PixelMap | Yes |
| config | [WatermarkConfiguration](arkts-media-media-watermarkconfiguration-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [5400108](../errorcode-media.md#5400108-parameter-value-out-of-range) |

## getAVRecorderConfig

```TypeScript
getAVRecorderConfig(callback: AsyncCallback<AVRecorderConfig>): void
```

Obtains the real-time configuration of this AVRecorder. This API uses an asynchronous callback to return the result. This API can be called only after [prepare()](#prepare) is called.

**Since:** 11

**Deprecated since:** -1

<!--Device-AVRecorder-getAVRecorderConfig(callback: AsyncCallback<AVRecorderConfig>): void--><!--Device-AVRecorder-getAVRecorderConfig(callback: AsyncCallback<AVRecorderConfig>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVRecorderConfig](arkts-media-media-avrecorderconfig-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getAVRecorderConfig

```TypeScript
getAVRecorderConfig(callback: AsyncCallback<AVRecorderConfig | undefined>): void
```

Obtains the real-time configuration of this AVRecorder. This API uses an asynchronous callback to return the result. This API can be called only after prepare() is called.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-getAVRecorderConfig(callback: AsyncCallback<AVRecorderConfig | undefined>): void--><!--Device-AVRecorder-getAVRecorderConfig(callback: AsyncCallback<AVRecorderConfig | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVRecorderConfig](arkts-media-media-avrecorderconfig-i.md) \| undefined & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getAVRecorderConfig

```TypeScript
getAVRecorderConfig(): Promise<AVRecorderConfig>
```

Obtains the real-time configuration of this AVRecorder. This API uses a promise to return the result. This API can be called only after [prepare()](#prepare) is called.

**Since:** 11

**Deprecated since:** -1

<!--Device-AVRecorder-getAVRecorderConfig(): Promise<AVRecorderConfig>--><!--Device-AVRecorder-getAVRecorderConfig(): Promise<AVRecorderConfig>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVRecorderConfig](arkts-media-media-avrecorderconfig-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getAVRecorderConfig

```TypeScript
getAVRecorderConfig(): Promise<AVRecorderConfig | undefined>
```

Obtains the real-time configuration of this AVRecorder. This API uses a promise to return the result. This API can be called only after prepare() is called.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-getAVRecorderConfig(): Promise<AVRecorderConfig | undefined>--><!--Device-AVRecorder-getAVRecorderConfig(): Promise<AVRecorderConfig | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVRecorderConfig](arkts-media-media-avrecorderconfig-i.md) \| undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getAudioCapturerMaxAmplitude

```TypeScript
getAudioCapturerMaxAmplitude(callback: AsyncCallback<number>): void
```

Obtains the maximum amplitude of the current audio capturer. This API uses an asynchronous callback to return the result. This API can be called only after the [prepare()](#prepare) API is called. If this API is called after [stop()](#stop) is successfully called, an error is reported. The return value is the maximum amplitude within the duration from the time the maximum amplitude is obtained last time to the current time. For example, if you have obtained the maximum amplitude at 1s and you call this API again at 2s, then the return value is the maximum amplitude within the duration from 1s to 2s.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-getAudioCapturerMaxAmplitude(callback: AsyncCallback<int>): void--><!--Device-AVRecorder-getAudioCapturerMaxAmplitude(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getAudioCapturerMaxAmplitude

```TypeScript
getAudioCapturerMaxAmplitude(): Promise<number>
```

Obtains the maximum amplitude of the current audio capturer. This API uses a promise to return the result. This API can be called only after the [prepare()](#prepare) API is called. If this API is called after [stop()](#stop) is successfully called, an error is reported. The return value is the maximum amplitude within the duration from the time the maximum amplitude is obtained last time to the current time. For example, if you have obtained the maximum amplitude at 1s and you call this API again at 2s, then the return value is the maximum amplitude within the duration from 1s to 2s.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-getAudioCapturerMaxAmplitude(): Promise<int>--><!--Device-AVRecorder-getAudioCapturerMaxAmplitude(): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getAvailableEncoder

```TypeScript
getAvailableEncoder(callback: AsyncCallback<Array<EncoderInfo>>): void
```

Obtains available encoders. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-getAvailableEncoder(callback: AsyncCallback<Array<EncoderInfo>>): void--><!--Device-AVRecorder-getAvailableEncoder(callback: AsyncCallback<Array<EncoderInfo>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[EncoderInfo](arkts-media-media-encoderinfo-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getAvailableEncoder

```TypeScript
getAvailableEncoder(): Promise<Array<EncoderInfo>>
```

Obtains available encoders. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-getAvailableEncoder(): Promise<Array<EncoderInfo>>--><!--Device-AVRecorder-getAvailableEncoder(): Promise<Array<EncoderInfo>>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[EncoderInfo](arkts-media-media-encoderinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getCurrentAudioCapturerInfo

```TypeScript
getCurrentAudioCapturerInfo(callback: AsyncCallback<audio.AudioCapturerChangeInfo>): void
```

Obtains the information about the current audio capturer. This API uses an asynchronous callback to return the result. This API can be called only after the [prepare()](#prepare) API is called. If this API is called after [stop()](#stop) is successfully called, an error is reported.

**Since:** 11

**Deprecated since:** -1

<!--Device-AVRecorder-getCurrentAudioCapturerInfo(callback: AsyncCallback<audio.AudioCapturerChangeInfo>): void--><!--Device-AVRecorder-getCurrentAudioCapturerInfo(callback: AsyncCallback<audio.AudioCapturerChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;audio.AudioCapturerChangeInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getCurrentAudioCapturerInfo

```TypeScript
getCurrentAudioCapturerInfo(callback: AsyncCallback<audio.AudioCapturerChangeInfo | undefined>): void
```

Obtains the information about the current audio capturer. This API uses an asynchronous callback to return the result. This API can be called only after the **prepare()** API is called. If this API is called after **stop()** is successfully called, an error is reported.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-getCurrentAudioCapturerInfo(callback: AsyncCallback<audio.AudioCapturerChangeInfo | undefined>): void--><!--Device-AVRecorder-getCurrentAudioCapturerInfo(callback: AsyncCallback<audio.AudioCapturerChangeInfo | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;audio.AudioCapturerChangeInfo \| undefined & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getCurrentAudioCapturerInfo

```TypeScript
getCurrentAudioCapturerInfo(): Promise<audio.AudioCapturerChangeInfo>
```

Obtains the information about the current audio capturer. This API uses a promise to return the result. This API can be called only after the [prepare()](#prepare) API is called. If this API is called after [stop()](#stop) is successfully called, an error is reported.

**Since:** 11

**Deprecated since:** -1

<!--Device-AVRecorder-getCurrentAudioCapturerInfo(): Promise<audio.AudioCapturerChangeInfo>--><!--Device-AVRecorder-getCurrentAudioCapturerInfo(): Promise<audio.AudioCapturerChangeInfo>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;audio.AudioCapturerChangeInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getCurrentAudioCapturerInfo

```TypeScript
getCurrentAudioCapturerInfo(): Promise<audio.AudioCapturerChangeInfo | undefined>
```

Obtains the information about the current audio capturer. This API uses a promise to return the result. This API can be called only after the **prepare()** API is called. If this API is called after **stop()** is successfully called, an error is reported.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-getCurrentAudioCapturerInfo(): Promise<audio.AudioCapturerChangeInfo | undefined>--><!--Device-AVRecorder-getCurrentAudioCapturerInfo(): Promise<audio.AudioCapturerChangeInfo | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;audio.AudioCapturerChangeInfo \ | undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getInputSurface

```TypeScript
getInputSurface(callback: AsyncCallback<string>): void
```

Obtains the surface required for recording. This API uses an asynchronous callback to return the result. The caller obtains the surface buffer from this surface and fills in the corresponding video data. Note that the video data must carry the timestamp (in ns) and buffer size, and the start time of the timestamp must be based on the system startup time. This API can be called only after the [prepare()](#prepare) API is called.

**Since:** 9

**Deprecated since:** -1

<!--Device-AVRecorder-getInputSurface(callback: AsyncCallback<string>): void--><!--Device-AVRecorder-getInputSurface(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getInputSurface

```TypeScript
getInputSurface(callback: AsyncCallback<string | undefined>): void
```

Obtains the surface required for recording. This API uses an asynchronous callback to return the result. The caller obtains the **surfaceBuffer** from this surface and fills in the corresponding video data. Note that the video data must carry the timestamp (in ns) and buffer size, and the start time of the timestamp must be based on the system startup time. This API can be called only after the prepare() API is called.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-getInputSurface(callback: AsyncCallback<string | undefined>): void--><!--Device-AVRecorder-getInputSurface(callback: AsyncCallback<string | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string \| undefined & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getInputSurface

```TypeScript
getInputSurface(): Promise<string>
```

Obtains the surface required for recording. This API uses a promise to return the result. The caller obtains the surface buffer from this surface and fills in the corresponding video data. Note that the video data must carry the timestamp (in ns) and buffer size, and the start time of the timestamp must be based on the system startup time. This API can be called only after the [prepare()](#prepare) API is called.

**Since:** 9

**Deprecated since:** -1

<!--Device-AVRecorder-getInputSurface(): Promise<string>--><!--Device-AVRecorder-getInputSurface(): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getInputSurface

```TypeScript
getInputSurface(): Promise<string | undefined>
```

Obtains the surface required for recording. This API uses a promise to return the result. The caller obtains the **surfaceBuffer** from this surface and fills in the corresponding video data. Note that the video data must carry the timestamp (in ns) and buffer size, and the start time of the timestamp must be based on the system startup time. This API can be called only after the prepare() API is called.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-getInputSurface(): Promise<string | undefined>--><!--Device-AVRecorder-getInputSurface(): Promise<string | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string \ | undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## offAudioCapturerChange

```TypeScript
offAudioCapturerChange(callback?: Callback<audio.AudioCapturerChangeInfo>): void
```

Subscribes to audio capturer configuration changes.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-offAudioCapturerChange(callback?: Callback<audio.AudioCapturerChangeInfo>): void--><!--Device-AVRecorder-offAudioCapturerChange(callback?: Callback<audio.AudioCapturerChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.AudioCapturerChangeInfo&gt; | No |

## offError

```TypeScript
offError(callback?: ErrorCallback): void
```

Unsubscribes from AVRecorder errors. After the unsubscription, your application can no longer receive AVRecorder errors.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-offError(callback?: ErrorCallback): void--><!--Device-AVRecorder-offError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## offPhotoAssetAvailable

```TypeScript
offPhotoAssetAvailable(callback?: Callback<photoAccessHelper.PhotoAsset>): void
```

Unsubscribes from media asset callback events.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-offPhotoAssetAvailable(callback?: Callback<photoAccessHelper.PhotoAsset>): void--><!--Device-AVRecorder-offPhotoAssetAvailable(callback?: Callback<photoAccessHelper.PhotoAsset>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | No |

## offStateChange

```TypeScript
offStateChange(callback?: OnAVRecorderStateChangeHandler): void
```

Unsubscribes from AVRecorder state changes. This event can be triggered by both user operations and the system.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-offStateChange(callback?: OnAVRecorderStateChangeHandler): void--><!--Device-AVRecorder-offStateChange(callback?: OnAVRecorderStateChangeHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnAVRecorderStateChangeHandler](arkts-media-media-onavrecorderstatechangehandler-t.md) | No |

## off_audioCapturerChange

```TypeScript
off(type: 'audioCapturerChange', callback?: Callback<audio.AudioCapturerChangeInfo>): void
```

Subscribes to audio capturer configuration changes. This API uses an asynchronous callback to return the result.

**Since:** 11

**Deprecated since:** -1

<!--Device-AVRecorder-off(type: 'audioCapturerChange', callback?: Callback<audio.AudioCapturerChangeInfo>): void--><!--Device-AVRecorder-off(type: 'audioCapturerChange', callback?: Callback<audio.AudioCapturerChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioCapturerChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.AudioCapturerChangeInfo&gt; | No |

## off_error

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from AVRecorder errors. After the unsubscription, your application can no longer receive AVRecorder errors. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorder-off(type: 'error', callback?: ErrorCallback): void--><!--Device-AVRecorder-off(type: 'error', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## off_photoAssetAvailable

```TypeScript
off(type: 'photoAssetAvailable', callback?: Callback<photoAccessHelper.PhotoAsset>): void
```

Unsubscribes from media asset callback events. This API uses an asynchronous callback to return the result.

**Since:** 12

**Deprecated since:** -1

<!--Device-AVRecorder-off(type: 'photoAssetAvailable', callback?: Callback<photoAccessHelper.PhotoAsset>): void--><!--Device-AVRecorder-off(type: 'photoAssetAvailable', callback?: Callback<photoAccessHelper.PhotoAsset>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'photoAssetAvailable' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | No |

## off_stateChange

```TypeScript
off(type: 'stateChange', callback?: OnAVRecorderStateChangeHandler): void
```

Unsubscribes from AVRecorder state changes. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorder-off(type: 'stateChange', callback?: OnAVRecorderStateChangeHandler): void--><!--Device-AVRecorder-off(type: 'stateChange', callback?: OnAVRecorderStateChangeHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'stateChange' | Yes |
| callback | [OnAVRecorderStateChangeHandler](arkts-media-media-onavrecorderstatechangehandler-t.md) | No |

## onAudioCapturerChange

```TypeScript
onAudioCapturerChange(callback: Callback<audio.AudioCapturerChangeInfo>): void
```

Subscribes to audio capturer configuration changes. Any configuration change triggers the callback that returns the entire configuration information. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-onAudioCapturerChange(callback: Callback<audio.AudioCapturerChangeInfo>): void--><!--Device-AVRecorder-onAudioCapturerChange(callback: Callback<audio.AudioCapturerChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.AudioCapturerChangeInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Subscribes to AVRecorder errors. This event is used only for error prompt and does not require the user to stop recording control. If the AVRecorderState is also switched to error, call reset() or release() to exit the recording. An application can subscribe to only one AVRecorder error event. When the application initiates multiple subscriptions to this event, the last subscription is applied. This event is triggered when an error occurs during recording.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-onError(callback: ErrorCallback): void--><!--Device-AVRecorder-onError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [5400107](../errorcode-media.md#5400107-audio-focus-conflict) |
| [5400104](../errorcode-media.md#5400104-operation-timeout) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## onPhotoAssetAvailable

```TypeScript
onPhotoAssetAvailable(callback: Callback<photoAccessHelper.PhotoAsset>): void
```

Subscribes to media asset callback events. When FileGenerationMode is used during media file creation, the PhotoAsset object is called back to the application after the stop operation is complete. When the application initiates multiple subscriptions to this event, the last subscription is applied. The event is triggered when a photo asset is available.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-onPhotoAssetAvailable(callback: Callback<photoAccessHelper.PhotoAsset>): void--><!--Device-AVRecorder-onPhotoAssetAvailable(callback: Callback<photoAccessHelper.PhotoAsset>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## onStateChange

```TypeScript
onStateChange(callback: OnAVRecorderStateChangeHandler): void
```

Subscribes to AVRecorder state changes. An application can subscribe to only one AVRecorder state change event. When the application initiates multiple subscriptions to this event, the last subscription is applied. This event can be triggered by both user operations and the system.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-onStateChange(callback: OnAVRecorderStateChangeHandler): void--><!--Device-AVRecorder-onStateChange(callback: OnAVRecorderStateChangeHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnAVRecorderStateChangeHandler](arkts-media-media-onavrecorderstatechangehandler-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## on_audioCapturerChange

```TypeScript
on(type: 'audioCapturerChange', callback: Callback<audio.AudioCapturerChangeInfo>): void
```

Subscribes to audio capturer configuration changes. Any configuration change triggers the callback that returns the entire configuration information. This API uses an asynchronous callback to return the result. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**Since:** 11

**Deprecated since:** -1

<!--Device-AVRecorder-on(type: 'audioCapturerChange', callback: Callback<audio.AudioCapturerChangeInfo>): void--><!--Device-AVRecorder-on(type: 'audioCapturerChange', callback: Callback<audio.AudioCapturerChangeInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioCapturerChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.AudioCapturerChangeInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on_error

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to AVRecorder errors. This event is used only for error prompt and does not require the user to stop recording control. If the [AVRecorderState](arkts-media-media-avrecorderstate-t.md#AVRecorderState) is also switched to error, call [reset()](#reset) or [release()] [release()](#release) to exit the recording. This API uses an asynchronous callback to return the result. An application can subscribe to only one AVRecorder error event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorder-on(type: 'error', callback: ErrorCallback): void--><!--Device-AVRecorder-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
| [5400106](../errorcode-media.md#5400106-format-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [5400107](../errorcode-media.md#5400107-audio-focus-conflict) |
| [5400104](../errorcode-media.md#5400104-operation-timeout) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## on_photoAssetAvailable

```TypeScript
on(type: 'photoAssetAvailable', callback: Callback<photoAccessHelper.PhotoAsset>): void
```

Subscribes to media asset callback events. When [FileGenerationMode](arkts-media-media-filegenerationmode-e.md#FileGenerationMode) is used during media file creation, the [PhotoAsset](../../apis-media-library-kit/arkts-apis/arkts-file-photoaccesshelper.md#@ohos.file.photoAccessHelper) object is called back to the application after the [stop](#stop) operation is complete. This API uses an asynchronous callback to return the result. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**Since:** 12

**Deprecated since:** -1

<!--Device-AVRecorder-on(type: 'photoAssetAvailable', callback: Callback<photoAccessHelper.PhotoAsset>): void--><!--Device-AVRecorder-on(type: 'photoAssetAvailable', callback: Callback<photoAccessHelper.PhotoAsset>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'photoAssetAvailable' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;photoAccessHelper.PhotoAsset&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## on_stateChange

```TypeScript
on(type: 'stateChange', callback: OnAVRecorderStateChangeHandler): void
```

Subscribes to AVRecorder state changes. An application can subscribe to only one AVRecorder state change event. When the application initiates multiple subscriptions to this event, the last subscription is applied. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorder-on(type: 'stateChange', callback: OnAVRecorderStateChangeHandler): void--><!--Device-AVRecorder-on(type: 'stateChange', callback: OnAVRecorderStateChangeHandler): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'stateChange' | Yes |
| callback | [OnAVRecorderStateChangeHandler](arkts-media-media-onavrecorderstatechangehandler-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

Pauses video recording. This API uses an asynchronous callback to return the result. This API can be called only after the [start()](#start) API is called. You can call [resume()](#resume) to resume recording.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-pause(callback: AsyncCallback<void>): void--><!--Device-AVRecorder-pause(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## pause

```TypeScript
pause(): Promise<void>
```

Pauses video recording. This API uses a promise to return the result. This API can be called only after the [start()](#start) API is called. You can call [resume()](#resume) to resume recording.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorder-pause(): Promise<void>--><!--Device-AVRecorder-pause(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## prepare

```TypeScript
prepare(config: AVRecorderConfig, callback: AsyncCallback<void>): void
```

Sets audio and video recording parameters. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MICROPHONE

<!--Device-AVRecorder-prepare(config: AVRecorderConfig, callback: AsyncCallback<void>): void--><!--Device-AVRecorder-prepare(config: AVRecorderConfig, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [AVRecorderConfig](arkts-media-media-avrecorderconfig-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## prepare

```TypeScript
prepare(config: AVRecorderConfig): Promise<void>
```

Sets audio and video recording parameters. This API uses a promise to return the result. The MICROPHONE permission is required only if audio recording is involved.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MICROPHONE

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorder-prepare(config: AVRecorderConfig): Promise<void>--><!--Device-AVRecorder-prepare(config: AVRecorderConfig): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [AVRecorderConfig](arkts-media-media-avrecorderconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases the audio and video recording resources. This API uses an asynchronous callback to return the result. After the resources are released, you can no longer perform any operation on the AVRecorder instance.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-release(callback: AsyncCallback<void>): void--><!--Device-AVRecorder-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## release

```TypeScript
release(): Promise<void>
```

Releases the audio and video recording resources. This API uses a promise to return the result. After the resources are released, you can no longer perform any operation on the AVRecorder instance.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorder-release(): Promise<void>--><!--Device-AVRecorder-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## reset

```TypeScript
reset(callback: AsyncCallback<void>): void
```

Resets audio and video recording. This API uses an asynchronous callback to return the result. For audio-only recording, you can call [prepare()](#prepare) again for re -recording. For video-only recording or audio and video recording, you can call [prepare()](#prepare) and [getInputSurface()](#getInputSurface) again for re- recording.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-reset(callback: AsyncCallback<void>): void--><!--Device-AVRecorder-reset(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## reset

```TypeScript
reset(): Promise<void>
```

Resets audio and video recording. This API uses a promise to return the result. For audio-only recording, you can call [prepare()](#prepare) again for re-recording. For video-only recording or audio and video recording, you can call [prepare()](#prepare) and [getInputSurface()](#getInputSurface) again for re-recording.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-reset(): Promise<void>--><!--Device-AVRecorder-reset(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## resume

```TypeScript
resume(callback: AsyncCallback<void>): void
```

Resumes video recording. This API uses an asynchronous callback to return the result. This API can be called only after the [pause()](#pause) API is called.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-resume(callback: AsyncCallback<void>): void--><!--Device-AVRecorder-resume(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## resume

```TypeScript
resume(): Promise<void>
```

Resumes video recording. This API uses a promise to return the result. This API can be called only after the [pause()](#pause) API is called.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorder-resume(): Promise<void>--><!--Device-AVRecorder-resume(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## setWillMuteWhenInterrupted

```TypeScript
setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>
```

Sets whether to mute the current audio recording stream when an audio interruption occurs. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>--><!--Device-AVRecorder-setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| muteWhenInterrupted | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts video recording. This API uses an asynchronous callback to return the result. For audio-only recording, this API can be called only after the [prepare()](#prepare) API is called. For video-only recording, this API can be called only after the [getInputSurface()](#getInputSurface) API is called.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-start(callback: AsyncCallback<void>): void--><!--Device-AVRecorder-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## start

```TypeScript
start(): Promise<void>
```

Starts video recording. This API uses a promise to return the result. For audio-only recording, this API can be called only after the [prepare()](#prepare) API is called. For video-only recording, this API can be called only after the [getInputSurface()](#getInputSurface) API is called.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorder-start(): Promise<void>--><!--Device-AVRecorder-start(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops video recording. This API uses an asynchronous callback to return the result. This API can be called only after the [start()](#start) or [pause()](#pause) API is called. For audio-only recording, you can call [prepare()](#prepare) again for re -recording. For video-only recording or audio and video recording, you can call [prepare()](#prepare) and [getInputSurface()](#getInputSurface) again for re- recording.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-stop(callback: AsyncCallback<void>): void--><!--Device-AVRecorder-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## stop

```TypeScript
stop(): Promise<void>
```

Stops video recording. This API uses a promise to return the result. This API can be called only after the [start()](#start) or [pause()](#pause) API is called. For audio-only recording, you can call [prepare()](#prepare) again for re-recording. For video-only recording or audio and video recording, you can call [prepare()](#prepare) and [getInputSurface()](#getInputSurface) again for re-recording.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorder-stop(): Promise<void>--><!--Device-AVRecorder-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## updateRotation

```TypeScript
updateRotation(rotation: number): Promise<void>
```

Updates the video rotation angle, in degrees. This API uses a promise to return the result. This API can be called only after the [prepare()](#prepare) event is triggered and before the [start()](#start) API is called.

**Since:** 23

**Deprecated since:** -1

<!--Device-AVRecorder-updateRotation(rotation: int): Promise<void>--><!--Device-AVRecorder-updateRotation(rotation: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rotation | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## state

```TypeScript
readonly state: AVRecorderState
```

AVRecorder state.

**Type:** [AVRecorderState](arkts-media-media-avrecorderstate-t.md)

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorder-readonly state: AVRecorderState--><!--Device-AVRecorder-readonly state: AVRecorderState-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder
