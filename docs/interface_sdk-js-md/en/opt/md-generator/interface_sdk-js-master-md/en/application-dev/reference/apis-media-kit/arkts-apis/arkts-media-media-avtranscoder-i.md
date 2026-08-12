# AVTranscoder

AVTranscoder is a transcoding management class. It provides APIs to transcode videos. Before calling any API in AVTranscoder, you must use [createAVTranscoder()](arkts-media-media-createavtranscoder-f.md#createAVTranscoder) to create an AVTranscoder instance.

For details about the AVTranscoder demo, see   
[Using AVTranscoder for Transcoding](../../../media/media/using-avtranscoder-for-transcodering.md).

**Since:** 12

<!--Device-media-interface AVTranscoder--><!--Device-media-interface AVTranscoder-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## addWatermark

```TypeScript
addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<number>
```

add a watermark for the AVTranscoder. This API uses a promise to return the result.App can add up to 5 watermarks.This API can be called only before the prepared state.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVTranscoder-addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<int>--><!--Device-AVTranscoder-addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

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
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-play-service-dead) |
| [5400108](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |

## cancel

```TypeScript
cancel(): Promise<void>
```

Cancels video transcoding. This API uses a promise to return the result.

This API can be called only after the [prepare()](#prepare),   
[start()](#start), [pause()](#pause), or   
[resume()](#resume) API is called.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-cancel(): Promise<void>--><!--Device-AVTranscoder-cancel(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## off('complete')

```TypeScript
off(type:'complete', callback?: Callback<void>):void
```

Unsubscribes from the event indicating that transcoding is complete.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-off(type:'complete', callback?: Callback<void>):void--><!--Device-AVTranscoder-off(type:'complete', callback?: Callback<void>):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'complete' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

## off('error')

```TypeScript
off(type:'error', callback?: ErrorCallback):void
```

Unsubscribes from AVTranscoder errors. After the unsubscription, your application can no longer receive AVTranscoder errors.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-off(type:'error', callback?: ErrorCallback):void--><!--Device-AVTranscoder-off(type:'error', callback?: ErrorCallback):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## off('progressUpdate')

```TypeScript
off(type:'progressUpdate', callback?: Callback<number>):void
```

Unsubscribes from transcoding progress updates.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-off(type:'progressUpdate', callback?: Callback<int>):void--><!--Device-AVTranscoder-off(type:'progressUpdate', callback?: Callback<int>):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'progressUpdate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

## on('complete')

```TypeScript
on(type:'complete', callback: Callback<void>):void
```

Subscribes to the event indicating that transcoding is complete. An application can subscribe to only one transcoding progress update event. When the application initiates multiple subscriptions to this event, the last subscription is applied. This API uses an asynchronous callback to return the result.

When this event is reported, the current transcoding operation is complete. You need to call   
[release()](#release) to exit the transcoding.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-on(type:'complete', callback: Callback<void>):void--><!--Device-AVTranscoder-on(type:'complete', callback: Callback<void>):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'complete' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## on('error')

```TypeScript
on(type:'error', callback: ErrorCallback):void
```

Subscribes to AVTranscoder errors. If this event is reported, call [release()](#release) to exit the transcoding. This API uses an asynchronous callback to return the result.

An application can subscribe to only one AVTranscoder error event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-on(type:'error', callback: ErrorCallback):void--><!--Device-AVTranscoder-on(type:'error', callback: ErrorCallback):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400101-memory-allocation-failed) |
| [5400106](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400106-format-not-supported) |
| [5400104](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400104-operation-timeout) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## on('progressUpdate')

```TypeScript
on(type:'progressUpdate', callback: Callback<number>):void
```

Subscribes to transcoding progress updates. An application can subscribe to only one transcoding progress update event. When the application initiates multiple subscriptions to this event, the last subscription is applied. This API uses an asynchronous callback to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-on(type:'progressUpdate', callback: Callback<int>):void--><!--Device-AVTranscoder-on(type:'progressUpdate', callback: Callback<int>):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'progressUpdate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

## pause

```TypeScript
pause(): Promise<void>
```

Pauses video transcoding. This API uses a promise to return the result.

This API can be called only after the [start()](#start) API is called. You can call   
[resume()](#resume) to resume transcoding.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-pause(): Promise<void>--><!--Device-AVTranscoder-pause(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## prepare

```TypeScript
prepare(config: AVTranscoderConfig): Promise<void>
```

Sets video transcoding parameters. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-prepare(config: AVTranscoderConfig): Promise<void>--><!--Device-AVTranscoder-prepare(config: AVTranscoderConfig): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [AVTranscoderConfig](arkts-media-media-avtranscoderconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400106](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400106-format-not-supported) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## release

```TypeScript
release(): Promise<void>
```

Releases video transcoding resources. This API uses a promise to return the result.

After the resources are released, you can no longer perform any operation on the AVTranscoder instance.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-release(): Promise<void>--><!--Device-AVTranscoder-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## resume

```TypeScript
resume(): Promise<void>
```

Resumes video transcoding. This API uses a promise to return the result.

This API can be called only after the [pause()](#pause) API is called.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-resume(): Promise<void>--><!--Device-AVTranscoder-resume(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## start

```TypeScript
start(): Promise<void>
```

Starts video transcoding. This API uses a promise to return the result.

This API can be called only after the [prepare()](#prepare) API is called.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-start(): Promise<void>--><!--Device-AVTranscoder-start(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400105](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## fdDst

```TypeScript
fdDst: number
```

Destination media file descriptor, which specifies the data source. After creating an AVTranscoder instance, you must set both **fdSrc** and **fdDst**.

**NOTE：**

- After the resource handle (FD) is transferred to an AVTranscoder instance, do not use the resource handle to   
perform other read and write operations, including but not limited to transferring this handle to other AVPlayer,AVMetadataExtractor, AVImageGenerator, or AVTranscoder instance.  
- Competition occurs when multiple AVTranscoders use the same resource handle to read and write files at the same  
time, resulting in errors in obtaining data.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-fdDst: int--><!--Device-AVTranscoder-fdDst: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

## fdSrc

```TypeScript
fdSrc: AVFileDescriptor
```

Source media file descriptor, which specifies the data source.

There is a media file that stores continuous assets, the address offset is 0, and the byte length is 100. Its file descriptor is **AVFileDescriptor { fd = resourceHandle; offset = 0; length = 100; }**.

**NOTE：**

- After the resource handle (FD) is transferred to an AVTranscoder instance, do not use the resource handle to   
perform other read and write operations, including but not limited to transferring this handle to other AVPlayer,AVMetadataExtractor, AVImageGenerator, or AVTranscoder instance.  
- Competition occurs when multiple AVTranscoders use the same resource handle to read and write files at the same  
time, resulting in errors in obtaining data.

**Type:** [AVFileDescriptor](arkts-media-media-avfiledescriptor-i.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-fdSrc: AVFileDescriptor--><!--Device-AVTranscoder-fdSrc: AVFileDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder
