# AVImageGenerator

AVImageGenerator is a class for video thumbnail retrieval. It provides APIs to obtain a thumbnail from a video. Before calling any API in AVImageGenerator, you must use   
[createAVImageGenerator()](arkts-media-media-createavimagegenerator-f.md#createAVImageGenerator)to create an AVImageGenerator instance.

For details about the demo for obtaining video thumbnails, see   
[Obtaining Video Thumbnails](../../../media/media/avimagegenerator.md).

**Since:** 12

<!--Device-media-interface AVImageGenerator--><!--Device-media-interface AVImageGenerator-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## fetchFrameByTime

```TypeScript
fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams,
      callback: AsyncCallback<image.PixelMap>): void
```

Obtains a video thumbnail. This API uses an asynchronous callback to return the result.

**Since:** 12

<!--Device-AVImageGenerator-fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams,      callback: AsyncCallback<image.PixelMap>): void--><!--Device-AVImageGenerator-fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams,      callback: AsyncCallback<image.PixelMap>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeUs | number | Yes |
| options | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | Yes |
| param | [PixelMapParams](arkts-media-media-pixelmapparams-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400106](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400106-format-not-supported) |

## fetchFrameByTime

```TypeScript
fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>
```

Obtains a video thumbnail. This API uses a promise to return the result.

**Since:** 12

<!--Device-AVImageGenerator-fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>--><!--Device-AVImageGenerator-fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeUs | number | Yes |
| options | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | Yes |
| param | [PixelMapParams](arkts-media-media-pixelmapparams-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400106](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400106-format-not-supported) |

## fetchScaledFrameByTime

```TypeScript
fetchScaledFrameByTime(timeUs: number, queryMode: AVImageQueryOptions, outputSize?: OutputSize):
      Promise<image.PixelMap>
```

Fetches a scaled thumbnail from the video at a particular timestamp. This API uses a promise to return the result.

**Since:** 20

<!--Device-AVImageGenerator-fetchScaledFrameByTime(timeUs: number, queryMode: AVImageQueryOptions, outputSize?: OutputSize):      Promise<image.PixelMap>--><!--Device-AVImageGenerator-fetchScaledFrameByTime(timeUs: number, queryMode: AVImageQueryOptions, outputSize?: OutputSize):      Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeUs | number | Yes |
| queryMode | [AVImageQueryOptions](arkts-media-media-avimagequeryoptions-e.md) | Yes |
| outputSize | [OutputSize](arkts-media-media-outputsize-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400106](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400106-format-not-supported) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this AVImageGenerator instance. This API uses an asynchronous callback to return the result.

**Since:** 12

<!--Device-AVImageGenerator-release(callback: AsyncCallback<void>): void--><!--Device-AVImageGenerator-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## release

```TypeScript
release(): Promise<void>
```

Releases this AVImageGenerator instance. This API uses a promise to return the result.

**Since:** 12

<!--Device-AVImageGenerator-release(): Promise<void>--><!--Device-AVImageGenerator-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |

## fdSrc

```TypeScript
fdSrc ?: AVFileDescriptor
```

Media file descriptor, which specifies the data source.

There is a media file that stores continuous assets, the address offset is 0, and the byte length is 100. Its file descriptor is **AVFileDescriptor { fd = resourceHandle; offset = 0; length = 100; }**.

**NOTE：**

After the resource handle (FD) is transferred to an AVImageGenerator instance, do not use the resource handle to perform other read and write operations, including but not limited to transferring this handle to other AVPlayer,AVMetadataExtractor, AVImageGenerator, or AVTranscoder instance. Competition occurs when multiple AVImageGenerator use the same resource handle to read and write files at the same time, resulting in errors in obtaining data.

**Type:** [AVFileDescriptor](arkts-media-media-avfiledescriptor-i.md)

**Since:** 12

<!--Device-AVImageGenerator-fdSrc ?: AVFileDescriptor--><!--Device-AVImageGenerator-fdSrc ?: AVFileDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator
